import collections
import datetime
import os
import platform
import shutil
from pathlib import Path
from pprint import pprint
from typing import Optional
from zipfile import ZipFile

from models import Config, Test, Colors
import json


def task_log(func):
    def wrapper(self, *argg, **kwargs):
        self.task(func.__name__)
        try:
            result = func(self, *argg, **kwargs)
        except Exception as e:
            raise e
            self.shutdown(exception=e, exit_after=True)
        self.finished()
        return result

    return wrapper


class Judge:
    OUT = "out"
    IN = "in"
    TEMP = "temp"

    def __init__(self, config_path: str):
        self.config = self.get_config(config_path)
        self.time_limit = 0
        self.tests = [[] for _ in range(len(self.config.sub_tasks_score))]
        self.input = self.config.name + "\\" + self.IN
        self.output = self.config.name + "\\" + self.OUT
        self.temp = self.config.name + "\\" + self.TEMP
        self.makedires()
        self.compile_codes()
        self.gen()
        self.exit()

    # TODO(SmsS): use logger
    def log(self, log: str, color: str, *args) -> None:
        print(color, end="")
        if len(args):
            print(log % args, end="")
        else:
            print(log, end="")
        print(Colors.END)

    def diff(self, file1, file2) -> bool:
        with open(file1, "r") as f:
            lines = f.readlines()
        with open(file2, "r") as f:
            lines2 = f.readlines()
        lines = [line.strip() for line in lines if line.strip()]
        lines2 = [line.strip() for line in lines2 if line.strip()]
        return lines2 != lines

    @task_log
    def gen(self) -> None:
        cnt = 1
        for test in self.config.tests:
            self.info("\tNumber of tests: %s\n\tGeneratorr: %s\n\tArgs: %s\n\tValidators: %s\n\tTest sub tasks: %s",
                      test.number_of_tests, test.generator, str(test.args), test.validator, str(test.sub_tasks))
            for i in range(test.number_of_tests):
                self.info("Test %s from %s", i+1, test.number_of_tests)
                if self.run(test.generator, test.args + [cnt], out=f"{self.input}\\input{cnt}.txt"):
                    self.shutdown(f'Generator FAILED\nGen: {test.generator}\nargs: {test.args}\nTestNum: {cnt}', exit_after=self.config.shutdown_on_failure)
                elif test.validator and self.run(test.validator, inp=f"{self.input}\\input{cnt}.txt"):
                    self.shutdown(f'Validator FAILED\nVal: {test.validator}\nGen: {test.generator}\nargs: {test.args}\nTestNum: {cnt}', exit_after=self.config.shutdown_on_failure)
                else:
                    o = datetime.datetime.now()
                    if self.run(self.config.solutions[0], inp=f"{self.input}\\input{cnt}.txt", out=f"{self.output}\\output{cnt}.txt"):
                        self.shutdown(f'Solution FAILED\nSol: {self.config.solutions[0]}\nGen: {test.generator}\nargs: {test.args}\nTestNum: {cnt}', exit_after=self.config.shutdown_on_failure)
                    else:
                        self.time_limit = max(self.time_limit, (datetime.datetime.now() - o).total_seconds())
                        print(Colors.SUCCESSFUL+ "Successful" + Colors.END)
                for s in test.sub_tasks:
                    self.tests[s].append(cnt)
                cnt += 1
        if len(self.config.sub_tasks_score):
            json_config = {
                "packages": [
                    {
                        "score": self.config.sub_tasks_score[sub],
                        "tests": self.tests[sub]
                    } for sub in range(len(self.config.sub_tasks_score))
                ]
            }
            json.dump(json_config, open(f'{self.config.name}\\config.json', 'w'))
        print('Timelimit: %s', self.time_limit)
        if len(self.config.solutions) > 1:
            print('Check other solutions')
            try:
                shutil.rmtree(f"{self.temp}\\val_out")
            except FileNotFoundError:
                pass
            os.makedirs(f"{self.temp}\\val_out")
            suc = True
            for sol in self.config.solutions[1:]:
                print(sol)
                for test in range(1, cnt):
                    self.run(sol, inp=f"{self.input}/input{test}.txt", out=f"{self.temp}/val_out/output{test}.txt")
                    if self.diff(f"{self.temp}/val_out/output{test}.txt", f"{self.output}/output{test}.txt"):
                        print(Colors.FAIL + f'Sol failed at test {test}' + Colors.END)
                        suc = False
            if suc:
                print(Colors.SUCCESSFUL + "Successful" + Colors.END)
        with ZipFile(f'{self.config.name}\\{self.config.name}.zip', 'w') as zf:
            for folderName, subfolders, filenames in os.walk(self.config.name):
                for filename in filenames:
                    if filename.endswith('txt') or filename.endswith('json'):
                        filePath = os.path.join(folderName, filename)
                        zf.write(filePath, filePath[filePath.find('/'):])
    def task(self, log: str, *args) -> None:
        self.log(log, Colors.TASK, *args)

    def info(self, log: str, *args) -> None:
        self.log(log, Colors.INFO, *args)

    def finished(self):
        self.log("Finished :)", Colors.SUCCESSFUL)

    @task_log
    def makedires(self):
        os.makedirs(self.input, exist_ok=True)
        os.makedirs(self.output, exist_ok=True)
        os.makedirs(self.temp, exist_ok=True)

    @task_log
    def exit(self):
        shutil.rmtree(self.temp)
        pass

    def get_path(self, name) -> str:
        return f"{self.config.resource}\\{name}"

    @task_log
    def compile_codes(self):
        compiled = set()
        codes = [test.validator for test in self.config.tests if test.validator] + [test.generator for test in
                                                                                    self.config.tests if
                                                                                    test.generator] + self.config.solutions
        for code in codes:
            if code in compiled:
                continue
            if code.endswith(".cpp"):
                compiled.add(code)
                self.info("\tCompiling %s", code)
                if os.system(f"g++ -std=c++11 {self.get_path(code)} -o {self.temp}\\{code.split('.')[0]}"):
                    self.shutdown(f"Compiled failed `{code}`", exit_after=True)

    def shutdown(self, reason: Optional[str] = None, hint: Optional[str] = None, exception: Optional[Exception] = None,
                 exit_after: bool = True) -> None:
        self.exit()
        print(Colors.FAIL + f'{"*" * 23}ERROR{"*" * 23}')
        print('Shutting Down... :(' + Colors.END)
        if reason:
            print(Colors.FAIL + 'Reason:' + Colors.END)
            print(reason)
        if exception:
            print(Colors.FAIL + 'Exception:' + Colors.END)
            print(str(exception))
        if hint:
            print(Colors.FAIL + 'Hint:' + Colors.END)
            print(hint)
        print(Colors.FAIL + '*' * 51 + Colors.END)
        if exit_after:
            exit(0)

    @task_log
    def get_config(self, config_path: str) -> Config:
        try:
            json_data = json.load(open(config_path))
            json_data['tests'] = [Test(**test) for test in json_data['tests']]
            return Config(**json_data)
        except FileNotFoundError as e:
            self.shutdown("config file not found", exception=e, exit_after=True)
        except (json.decoder.JSONDecodeError, TypeError) as e:
            self.shutdown("Deserialize error", hint="Check config json file", exception=e, exit_after=True)

    def get_name(self, name_with_format: str) -> str:
        return name_with_format.split(".")[0]

    def run(self, name: str, argv: list = None, inp: str = None, out: str = None) -> bool:
        self.info("\t\tRunning %s", name)
        if name.endswith(".cpp"):
            runner = f"{self.temp}\\{self.get_name(name)}"
            if 'Windows' in platform.platform():
                runner += ".exe"
        else:
            runner = f"python {self.config.resource}\\{name}"

        if argv:
            argv = " ".join(map(str, argv))
        else:
            argv = ""

        if inp:
            inp = f"< {inp}"
        else:
            inp = ""

        if out:
            out = f"> {out}"
        else:
            out = ""
        return bool(os.system(" ".join([runner, argv, inp, out])))


if __name__ == '__main__':
    judge = Judge('settings2.json')
