from sys import stderr

from colorama import Fore, Style

from cocas.assembler import AssemblerException
from cocas.linker import LinkerException
from cocas.object_file import ObjectFileException


def log_error(tag: str, message: str):
    print(f'[{tag}] {Fore.RED}ERROR{Fore.RESET}', file=stderr)
    print(message, file=stderr)


def log_os_error(e: OSError):
    message = e.strerror
    if e.filename is not None:
        message += f': {Style.BRIGHT}{e.filename}{Style.NORMAL}'
    log_error("Main", message)
    exit(1)


def log_asm_exception(e: AssemblerException):
    print(f'[{e.tag.value}] {Fore.RED}ERROR{Fore.RESET} at {Style.BRIGHT}{e.file}{Style.RESET_ALL}, '
          f'line {Style.BRIGHT}{e.line}{Style.RESET_ALL}', file=stderr)
    print(f'{e.description}', file=stderr)


def log_object_file_exception(e: ObjectFileException):
    print(f'[Object file] {Fore.RED}ERROR{Fore.RESET} at {Style.BRIGHT}{e.file}{Style.RESET_ALL}, '
          f'line {Style.BRIGHT}{e.line}{Style.RESET_ALL}', file=stderr)
    print(f'{e.description}', file=stderr)


def log_link_exception(e: LinkerException):
    log_error("Linker", e.message)
