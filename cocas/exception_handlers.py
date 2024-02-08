from colorama import Fore, Style

from cocas.assembler import CdmAssemblerException
from cocas.linker import CdmLinkException
from cocas.object_file import CdmObjectFileException


def log_exception(tag: str, message: str):
    print(f'[{tag}] {Fore.RED}ERROR{Fore.RESET}')
    print(message)


def log_os_error(e: OSError):
    message = e.strerror
    if e.filename is not None:
        message += f': {Style.BRIGHT}{e.filename}{Style.NORMAL}'
    log_exception("Main", message)
    exit(1)


def log_asm_exception(e: CdmAssemblerException):
    print(f'[{e.tag.value}] {Fore.RED}ERROR{Fore.RESET} at line {Style.BRIGHT}{e.line}{Style.RESET_ALL} of '
          f'{Style.BRIGHT}{e.file}{Style.RESET_ALL}')
    print(f'{e.description}')


def log_object_file_exception(e: CdmObjectFileException):
    print(f'[Object file] {Fore.RED}ERROR{Fore.RESET} at line {Style.BRIGHT}{e.line}{Style.RESET_ALL} of '
          f'{Style.BRIGHT}{e.file}{Style.RESET_ALL}')
    print(f'{e.description}')


def log_link_exception(_: CdmLinkException):
    # todo: find this code from previous revisions
    pass
