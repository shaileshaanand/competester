from .compilers_common import java_compile_common
import subprocess


def java_compile(program_file):
    java_compile_common(program_file)
    subprocess.run(["javac", str(program_file)])
