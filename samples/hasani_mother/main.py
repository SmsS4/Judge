import datetime
import json
import os
from zipfile import ZipFile

NAME = "problem"
SOL = ["dij.cpp"]
VAL = ["val.py"]
GEN = ["random.cpp"]
CONF = [
    (0, 3, GEN[0], VAL[0], 100, 100, 100, 0),
    (0, 3, GEN[0], VAL[0], 100, 100, 1_000_000_000, 0),

    (0, 3, GEN[0], VAL[0], 100, 100_000, 100, 0),
    (0, 3, GEN[0], VAL[0], 100, 100_000, 1_000_000_000, 0),

    (0, 3, GEN[0], VAL[0], 100_000, 100, 100, 0),
    (0, 3, GEN[0], VAL[0], 100_000, 100, 1_000_000_000, 0),

    (0, 3, GEN[0], VAL[0], 100, 100, 100, 1),
    (0, 3, GEN[0], VAL[0], 100, 100, 1_000_000_000, 1),

    (0, 3, GEN[0], VAL[0], 100, 100_000, 100, 1),
    (0, 3, GEN[0], VAL[0], 100, 100_000, 1_000_000_000, 1),

    (0, 3, GEN[0], VAL[0], 100_000, 100, 100, 1),
    (0, 3, GEN[0], VAL[0], 100_000, 100, 1_000_000_000, 1),

    (0, 1, GEN[0], VAL[0], 100_000, 100_000, 1_000_000_000, -1),
    (0, 1, GEN[0], VAL[0], 100, 100_000, 1_000_000_000, -1),

]
SUBTASKS = [100]
SHUTDOWN_ON_FAILURE = True
CREATE_CONFIG_JSON = False

tests = [[] for _ in range(len(SUBTASKS))]
os.makedirs(f"{NAME}/out", exist_ok=True)
os.makedirs(f"{NAME}/in", exist_ok=True)
os.makedirs("temp", exist_ok=True)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def shutdown(reason: str) -> None:
    os.system('rm -rf temp')
    print(bcolors.FAIL + '*' * 50 + bcolors.ENDC)
    print('Shutting Down... :(')
    print('Reason:')
    print(reason)
    print(bcolors.FAIL + '*' * 50 + bcolors.ENDC)
    if SHUTDOWN_ON_FAILURE:
        exit(0)


def get_no_format(name: str) -> str:
    return name.split(".")[0]


def compile_code(name) -> None:
    if name.endswith(".cpp"):
        print(bcolors.OKBLUE + 'Compiling ' + name + bcolors.ENDC)
        if os.system(f"g++ -std=c++11 {name} -o temp/{get_no_format(name)}"):
            shutdown(f'compile {name} failed')


def pre_compile() -> None:
    print('PreCompile...')
    for sol in SOL:
        compile_code(sol)
    for val in VAL:
        compile_code(val)
    for gen in GEN:
        compile_code(gen)
    print(bcolors.OKGREEN + 'PreCompile Finished' + bcolors.ENDC)


def run(name: str, argv: tuple = None, inp: str = None, out: str = None) -> bool:
    print('running', name, argv)
    if name.endswith(".cpp"):
        runner = f"./temp/{get_no_format(name)}"
    else:
        runner = f"python3 {name}"

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


def diff(file1, file2) -> bool:
    with open(file1, "r") as f:
        lines = f.readlines()
    with open(file2, "r") as f:
        lines2 = f.readlines()
    lines = [line.strip() for line in lines if line.strip()]
    lines2 = [line.strip() for line in lines2 if line.strip()]
    return lines2 != lines


if __name__ == '__main__':
    pre_compile()
    print('Generating tests')
    num = 1
    time_limit = 0
    for conf in CONF:
        sub = conf[0]
        cnt = conf[1]
        gen = conf[2]
        val = conf[3]
        sol = SOL[0]
        args = conf[4:]
        print(sub, cnt, gen, val, sol, args)
        for i in range(cnt):
            print(f'Test {num}')
            if run(gen, args + (num,), out=f"{NAME}/in/input{num}.txt"):
                shutdown(f'Generator FAILED\nGen: {gen}\nargs: {args}\nTestNum: {num}')
            elif val and run(val, inp=f"{NAME}/in/input{num}.txt"):
                shutdown(f'Validator FAILED\nVal: {val}\nGen: {gen}\nargs: {args}\nTestNum: {num}')
            else:
                o = datetime.datetime.now()
                if run(sol, inp=f"{NAME}/in/input{num}.txt", out=f"{NAME}/out/output{num}.txt"):
                    shutdown(f'Solution FAILED\nSol: {sol}\nGen: {gen}\nargs: {args}\nTestNum: {num}')
                else:
                    time_limit = max(time_limit, (datetime.datetime.now() - o).total_seconds())
                    print(bcolors.OKGREEN + "Successful" + bcolors.ENDC)
            for s in range(sub, len(SUBTASKS)):
                tests[s].append(num)
            num += 1
    json_config = {
        "packages": [
            {
                "score": SUBTASKS[sub],
                "tests": tests[sub]
            } for sub in range(len(SUBTASKS))
        ]
    }
    if CREATE_CONFIG_JSON:
        json.dump(json_config, open(f'{NAME}/config.json', 'w'))
    print('Timelimit =', time_limit)
    if len(SOL) > 1:
        print('Check other soultions')
        os.system(f"rm -rf temp/val_out")
        os.makedirs(f"temp/val_out")
        suc = True
        for sol in SOL[1:]:
            print(sol)
            for test in range(1, num):
                run(sol, inp=f"{NAME}/in/input{test}.txt", out=f"temp/val_out/output{test}.txt")
                if diff(f"temp/val_out/output{test}.txt", f"{NAME}/out/output{test}.txt"):
                    print(bcolors.FAIL + f'Sol failed at test {test}' + bcolors.ENDC)
                    suc = False
        if suc:
            print(bcolors.OKGREEN + "Successful" + bcolors.ENDC)
    os.system(f"rm -rf temp")
    with ZipFile(f'{NAME}/{NAME}.zip', 'w') as zf:
        for folderName, subfolders, filenames in os.walk(NAME):
            for filename in filenames:
                if filename.endswith('txt') or filename.endswith('json'):
                    filePath = os.path.join(folderName, filename)
                    zf.write(filePath, filePath[filePath.find('/'):])
