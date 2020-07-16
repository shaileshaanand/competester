import subprocess


def python(program_file, input_data):
    return subprocess.run(["python3", program_file],
                          input=input_data,
                          capture_output=True)


def pypy(program_file, input_data):
    return subprocess.run(["pypy3", program_file],
                          input=input_data,
                          capture_output=True)


def java(program_file, input_data):
    classname = program_file.stem
    program_path = program_file.parent
    return subprocess.run(["java", "-classpath", program_path, classname],
                          input=input_data,
                          capture_output=True)


def exe(program_file, input_data):
    return subprocess.run([program_file],
                          input=input_data,
                          capture_output=True)


def c(program_file, input_data):
    return subprocess.run([program_file],
                          input=input_data,
                          capture_output=True)


def cpp(program_file, input_data):
    return subprocess.run([program_file],
                          input=input_data,
                          capture_output=True)
