from os.path import dirname
from time import strftime
from string import ascii_lowercase
from random import randint, choice
from bargparser.core import parse_args

def test_case():
    argv = "<program_name> "
    n = randint(2, 5)

    for i in range(n):
        corkey = randint(0, 3)
        shared_content = "".join([choice(ascii_lowercase) for _ in range(4)])

        if corkey == 0: # command
            argv += shared_content
        elif corkey == 1: # keyword 1
            argv += "-" + shared_content
        elif corkey == 2: # keyword 2
            argv += "--" + shared_content
        else: # keyword 3
            argv += "--" + shared_content + "="
            continue
    
        if i != n - 1:
            argv += " "
    try:
        return "Test case: \"%s\"" %argv, "result: %s" %parse_args(argv.split(' '))
    except:
        return argv

def unit_test(n):
    global test_file_name
    test_file_name = f"{dirname(__file__)}/test-result-{strftime('%y%m%d%H%M%S')}.txt"

    with open(test_file_name, 'w') as f:
        for _ in range(n):
            tc = test_case()
            try:
                tc, res = tc
            except ValueError:
                f.write("WARNING: There is an invalid input: \"%s\"" %tc + '\n\n')
                continue

            f.write(tc + "\n")
            f.write(" " * 4 + res + "\n\n")

unit_test(10)
print("Test finished !")
print(f"Take a look at: './test/{test_file_name.split('/')[-1]}'")
