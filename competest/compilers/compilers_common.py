from click import BadParameter
import subprocess


def java_compile_common(program_file):
    if program_file.suffix != ".java":
        raise BadParameter(
            f"for java PROGRAM_FILE extention should be .java not `\
                 {program_file.suffix}")


def c_compile_common(program_file, output_file):
    subprocess.run(["gcc", "-O2", "-lm", "-o", output_file, program_file])


def cpp_compile_common(program_file, output_file):
    subprocess.run(["g++", "-O2", "-lm", "-o", output_file, program_file])
