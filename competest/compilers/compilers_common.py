from click import BadParameter
import subprocess


def java_compile_common(program_file):
    if program_file.suffix != ".java":
        raise BadParameter(
            f"for java PROGRAM_FILE extention should be .java not {program_file.suffix}")
