import os.path
import sys
from os import getcwd, listdir, chdir
from typing import List
from os.path import isdir
from Exceptions import PathError, NoDirError


def _the_dir(command: List[str]) -> str:
    if len(command) == 1:
        return getcwd()
    elif len(command) == 2:
        return os.path.join('/home/zhnb', command[1])
    else:
        raise PathError


def _ls(command: List[str]) -> List[str]:
    return listdir(_the_dir(command))


def _dir(command: List[str]) -> List[str]:
    the_dir = _the_dir(command)
    return [n for n in _ls(command) if isdir(os.path.join(the_dir, n))]


def _cd(command: List[str]) -> None:
    if len(command) != 2:
        raise NoDirError
    if command[1] == '..':
        the_dir = os.path.split(getcwd())
        os.chdir(the_dir[0])
    else:
        os.chdir(os.path.join(command[1]))


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
            case 'help':
                print('Print ls to show all entities in folder')
                print('Print dir to show all dirs in folder')
                print('Print cd to change directory')
                print('Print exit to stop terminal')
            case 'ls':
                try:
                    print(_ls(command))
                except FileNotFoundError:
                    print('There is no such directory')
                except PathError:
                    print('Wrong path attributes')
            case 'dir':
                try:
                    print(_dir(command))
                except FileNotFoundError:
                    print('There is no such directory')
                except PathError:
                    print('Wrong path attributes')
            case 'cd':
                try:
                    _cd(command)
                except FileNotFoundError:
                    print('There is no such directory')
                except NoDirError:
                    print('Write directory name or .. to move to previous dir')
            case 'exit':
                sys.exit(0)


if __name__ == '__main__':
    init()
