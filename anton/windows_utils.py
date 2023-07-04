"""Module for making Window's requests or system calls

This module contains various helper/util functions for messing with
Window's OS

Features:
    fn execute_cmd_command (str) -> str: Executes `str` command in Window's cmd
    and returns the output of it

"""

import subprocess
import re
import win32gui, win32process


def execute_cmd_command(command: str) -> str:
    """Execute command in cmd

    Returns:
        str: command output
    """
    assert isinstance(command, str)

    try:
        output = subprocess.check_output(
            command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True
        )
        return output
    except subprocess.CalledProcessError as e:
        # Handle command execution error
        print(f"Command execution failed with error code {e.returncode}: {e.output}")
        return "Command execution failed."


def search_hndw_by_name(target: str) -> int:
    """Searches window hndw's with windows32 api

    Returns:
        int: Window HNDW, 0 if cant find
    """
    return win32gui.FindWindow(None, target)


def get_thread_id_process_id(target_hndw: int) -> tuple[int, int]:
    """Gets (thread_id, process_id) from `target_hndw`

    Returns:
        int, int: thread_id, process_id
    """
    return win32process.GetWindowThreadProcessId(target_hndw)


if __name__ == "__main__":
    print(execute_cmd_command("pwd"))
