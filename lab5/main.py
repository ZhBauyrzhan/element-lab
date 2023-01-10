import os.path
import sys
from contextlib import contextmanager
from os import getcwd, listdir, chdir
from typing import List
from os.path import isdir
from Exceptions import ArgumentError, NoDirError


@contextmanager
def _the_dir(command: List[str]) -> str:
    try:
        if len(command) == 1:
            yield getcwd()
        elif len(command) == 2:
            yield os.path.join('/home/zhnb', command[1])
        else:
            raise FileNotFoundError
    finally:
        ...


@contextmanager
def _ls(command: List[str]) -> list[str]:
    try:
        with _the_dir(command) as the_dir:
            yield listdir(the_dir)
    except FileNotFoundError as e:
        print(e)
        yield
    finally:
        ...
        # print('Finished')


@contextmanager
def _dir(command: List[str]) -> List[str]:
    try:
        with _the_dir(command) as the_dir:
            yield [n for n in listdir(the_dir) if isdir(os.path.join(the_dir, n))]
    except FileNotFoundError as e:
        print(e)
        yield
    finally:
        ...


@contextmanager
def _cd(command: List[str]) -> bool:
    try:
        if len(command) != 2:
            raise ArgumentError
        if command[1] == '..':
            the_dir = os.path.split(getcwd())
            os.chdir(the_dir[0])
            yield True
        else:
            os.chdir(os.path.join(command[1]))
            yield True
    except FileNotFoundError as e:
        print(e)
        yield False
    except NoDirError:
        print('No such dir')
        yield False
    except ArgumentError:
        print('Argument error')
        yield False
    finally:
        ...


@contextmanager
def _mkdir(command: List[str]) -> bool:
    try:
        if len(command) != 2:
            raise ArgumentError
        else:
            os.mkdir(os.path.join(getcwd(), command[1]))
            yield True
    except ArgumentError:
        print('Wrong argument')
        yield False
    except FileExistsError as e:
        print(e)
        yield False
    except FileNotFoundError as e:
        print(e)
        yield False
    finally:
        ...


def init():
    chdir('/home/zhnb/PycharmProjects')
    print(getcwd())
    # print(os.path.split(getcwd()))
    # print(listdir('/home/zhnb/PycharmProjects/element-lab/lab3'))
    # print(listdir('/home/zhnb/PycharmProjects/element-lab/lab3'))
    print("Print 'help' to see commands or print command")
    while True:
        command = input(getcwd() + '$').split()
        # print(_the_dir(command))
        match command[0]:
            case 'mkdir':
                with _mkdir(command) as mkdir:
                    if mkdir:
                        print('Created successfully')
            case 'help':
                print('Print ls to show all entities in folder')
                print('Print dir to show all dirs in folder')
                print('Print cd to change directory')
                print('Print exit to stop terminal')
            case 'ls':
                with _ls(command) as ls:
                    if ls is not None:
                        print(ls)
            case 'dir':
                with _dir(command) as dirs:
                    if dirs is not None:
                        print(dirs)
            case 'cd':
                with _cd(command) as cd:
                    if cd:
                        print('Changed successfully')
            case 'exit':
                sys.exit(0)


if __name__ == '__main__':
    init()
