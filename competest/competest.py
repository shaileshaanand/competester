import click
import sys
import json
import pathlib
from time import time

if sys.platform == "linux":
    from .linux import (
        python,
        java,
        pypy,
        exe
    )
elif sys.platform == "win32":
    from .windows import (
        python,
        java,
        pypy,
        exe
    )
else:
    raise Exception


@click.command("competest",
               context_settings={
                   "help_option_names": ['-h', '--help']
               })
@click.argument("language", type=click.Choice(["python", "java", "pypy", "exe"]), required=True)
@click.argument("program_file", type=click.Path(exists=True), required=True)
@click.option("--test-cases", "-t", type=click.File("r"), help="File containing test cases.", required=True)
def competest(language, program_file, test_cases):
    """Run PROGRAM_FILE with test cases from the file specified in --test-cases (or -t) option and check them against the correct output specified in the same file.

       Supported Languages: java, python, pypy and exe(i.e. compiled executables)"""
    test_cases = json.loads(test_cases.read())
    total_cases = len(test_cases)
    failed_cases = 0
    languages = {
        "python": python,
        "java": java,
        "pypy": pypy,
        "exe": exe
    }
    for i, test_case in enumerate(test_cases, 1):
        input_data = "\n".join(test_case["input"]).encode()
        required_output = "\n".join(test_case["output"])
        program_file = pathlib.Path(program_file).resolve()
        start_time = time()
        process = languages[language](program_file, input_data)
        time_taken = time()-start_time
        actual_output = process.stdout.decode().strip().replace('\r', '')
        if process.returncode == 0 and required_output == actual_output:
            print(f"Test Case {i} Passed and took {time_taken:.3f} seconds  ✅")
        else:
            failed_cases += 1
            print(f"Test Case {i} Failed ❎")
            if process.returncode == 0:
                print(f"Required Output:\n{required_output}\n---------------")
                print(
                    f"Actual Output:\n{actual_output}\n---------------\n(took {time_taken:.3f} seconds)\n")
            else:
                print("---------------")
                print(f"Runtime Error: (took {time_taken:.3f} seconds)")
                print(process.stderr.decode().strip())
                print("---------------\n")

    if failed_cases == 0:
        print("All tests passed successfully. ✅")
    else:
        print(f"{failed_cases}/{total_cases} Test Cases Failed ❎")
