import datetime
import json
import os

SOL = ["sol.py"]
VAL = []
GEN = ["random.cpp", "fix_time.cpp", "same_diff.cpp", "stack_queue.cpp"]
CONF = [
    (3, 1, GEN[2], None, 5, 4, 3),
    (3, 1, GEN[0], None, 3, 4, 3),

    ((0, 2), 3, GEN[0], None, 100, 100, 2),
    ((0, 2), 1, GEN[0], None, 10, 100, 2),
    ((0, 2), 1, GEN[1], None, 100, 100, 2),
    ((0, 2), 1, GEN[2], None, 100, 100, 2),

    ((1, 2), 3, GEN[0], None, 100, 100, 1),
    ((1, 2), 1, GEN[0], None, 10, 100, 1),
    ((1, 2), 1, GEN[1], None, 100, 100, 1),
    ((1, 2), 1, GEN[2], None, 100, 100, 1),

    (3, 5, GEN[0], None, 100, 100, 3),
    (3, 5, GEN[0], None, 10, 100, 3),
    (3, 1, GEN[1], None, 10, 100, 3),
    (3, 1, GEN[1], None, 100, 100, 3),
    (3, 1, GEN[2], None, 10, 100, 3),
    (3, 1, GEN[2], None, 100, 100, 3),
    (3, 1, GEN[3], None, 10, 100, 3),
    (3, 1, GEN[3], None, 100, 100, 3),

]
SUBTASKS = [20, 20, 20, 60]
tests = [[] for _ in range(len(SUBTASKS))]

os.makedirs("out", exist_ok=True)
os.makedirs("in", exist_ok=True)
os.makedirs("val_out", exist_ok=True)


def get_no_format(name: str) -> str:
    return name.split(".")[0]


def compile_code(name):
    if name.endswith(".cpp"):
        print('Compiling', name)
        os.system(f"g++ -std=c++11 {name} -o {get_no_format(name)}")


def pre_compile():
    for sol in SOL:
        compile_code(sol)
    for val in VAL:
        compile_code(val)
    for gen in GEN:
        compile_code(gen)


def run(name: str, argv: tuple = None, inp: str = None, out: str = None) -> bool:
    if name.endswith(".cpp"):
        runner = f"./{get_no_format(name)}"
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
            if run(gen, args + (num,), out=f"in/input{num}.txt"):
                print('Generator FAILED')
            elif val and run(val, inp=f"in/input{num}.txt"):
                print('Validator FAILED')
            else:
                o = datetime.datetime.now()
                if run(sol, inp=f"in/input{num}.txt", out=f"out/output{num}.txt"):
                    print("Solution Failed")
                else:
                    time_limit = max(time_limit, (datetime.datetime.now() - o).total_seconds())
                    print("Successful")
            if isinstance(sub, tuple):
                for s in sub:
                    tests[s].append(num)
            else:
                tests[sub].append(num)
            num += 1
    json_config = {
        "packages": [
            {
                "score": SUBTASKS[sub],
                "tests": tests[sub]
            }for sub in range(len(SUBTASKS))
        ]
    }
    json.dump(json_config, open('config.json', 'w'))
    print('Timelimit =', time_limit)
    if len(SOL) > 1:
        print('Check other soultions')
        os.system("rm -rf val_out")
        os.makedirs("val_out")
        for sol in SOL[1:]:
            print(sol)
            for test in range(1, num):
                run(sol, inp=f"in/input{test}.txt", out=f"val_out/output{test}.txt")
                if diff(f"val_out/output{test}.txt", f"out/output{test}.txt"):
                    print(f'Sol failed at test {test}')
