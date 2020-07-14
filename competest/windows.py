import subprocess
import pathlib
from click import BadParameter


def python(program_file, input_data):
    return subprocess.run(["python", program_file],
                          input=input_data,
                          capture_output=True,
                          shell=True)


def pypy(program_file, input_data):
    return subprocess.run(["pypy", program_file],
                          input=input_data,
                          capture_output=True,
                          shell=True)


def java(program_file, input_data):
    program_file = pathlib.Path(program_file).resolve()
    if program_file.suffix != ".java":
        raise BadParameter(
            f"for java PROGRAM_FILE extention should be .java not {program_file.suffix}")
    classname = program_file.stem
    program_path = program_file.parent
    subprocess.run(["javac", program_file])
    return subprocess.run(["java", "-classpath", program_path, classname],
                          input=input_data,
                          capture_output=True,
                          shell=True)


def exe(program_file, input_data):
    return subprocess.run([program_file],
                          input=input_data,
                          capture_output=True,
                          shell=True)
