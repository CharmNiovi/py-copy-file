"""
I thought that such decisions might not be fair

import subprocess
def copy_file(command: str):
    subprocess.run(command, shell=True)

import os
def copy_file(command: str):
    os.system(command)
"""


def get_files_with_double_quotes(command):
    return [i for i in command.split("\"") if i and i != " "]


def get_files_with_shielding(command):
    source_destination = command.replace("\ ", " ")  # NOQA
    source_parts = source_destination.split(".")

    source_file = source_parts[0] + "." + source_parts[1].split()[0]
    destination_file = source_destination[len(source_file) + 1:]
    return source_file, destination_file


def copy_file(command: str) -> None:
    if command[:3] == "cp":
        raise ValueError(
            "Expected 'cp' as the first argument"
        )
    command = command[3:]

    if "\"" in command:
        source_file, destination_file = get_files_with_double_quotes(command)
    else:
        source_file, destination_file = get_files_with_shielding(command)

    if not destination_file or len(destination_file.split(".")) > 2:
        raise ValueError(
            "Expected 3 arguements"
        )

    if source_file != destination_file:
        with (
            open(source_file, "r") as source,
            open(destination_file, "w") as destination
        ):
            destination.write(source.read())
