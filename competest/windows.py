import subprocess


def python(program_file, input_data):
    return subprocess.run(["python", str(program_file)],
                          input=input_data,
                          capture_output=True,
                          shell=True)


def pypy(program_file, input_data):
    return subprocess.run(["pypy", str(program_file)],
                          input=input_data,
                          capture_output=True,
                          shell=True)


def java(program_file, input_data):
    classname = program_file.stem
    program_path = program_file.parent
    return subprocess.run(["java", "-classpath", str(program_path), classname],
                          input=input_data,
                          capture_output=True,
                          shell=True)


def exe(program_file, input_data):
    return subprocess.run([str(program_file)],
                          input=input_data,
                          capture_output=True,
                          shell=True)


def c(program_file, input_data):
    return subprocess.run([str(program_file)],
                          input=input_data,
                          capture_output=True,
                          shell=True)


def cpp(program_file, input_data):
    return subprocess.run([str(program_file)],
                          input=input_data,
                          capture_output=True,
                          shell=True)
