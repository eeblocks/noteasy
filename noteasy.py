#!/usr/bin/python3
# notEasy v1.0
# Coded by @esiquiel

# Dependencies
import argparse
import string
import random
import os

from time import sleep

try:
    import clipboard as c
except:
    print('\n----------------------------')
    print('Installing clipboard module')
    print('----------------------------\n')
    os.system('pip3 install clipboard')

parser = argparse.ArgumentParser(description='Generate a strong password not easy to hack')
parser.add_argument('-s', '--save', action='store_true', help='Save the password to a file')

args = parser.parse_args()

class Colors:
    MAGENTA = '\033[35m'
    WHITE = '\033[37m'
    RED = '\033[31m'

# Clear the terminal
def refresh():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = open('banner.txt', 'r').read()
    print(Colors.MAGENTA, banner, Colors.WHITE)

# Generate the password
def generate(length):

    characters = list(string.ascii_letters + string.digits + "!@#$%&()")

    if length < 15:
        characters = list(string.ascii_letters + string.digits + "@@0123456789@@")

    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)
    passwd = "".join(password)

    return passwd

# Copy to the clipboard
def clipboard(passwd):
    try:
        c.copy(passwd)
        print('\n(Copied to the clipboard)')
    except Exception as e:
        print(f'\n{Colors.RED}-----------------------------------')
        print(f' Error copying to the clipboard...')
        print(f'-----------------------------------')
        print(Colors.WHITE, e)


# Save the password to a file
def save(passwd):
    try:
        open('generated.txt', 'w').write(passwd)
    except Exception as e:
        print(f'\n{Colors.RED}-----------------------------------')
        print(f' Error saving to a file...')
        print(f'-----------------------------------')
        print(Colors.WHITE, e)



if __name__ == '__main__':
    refresh()

    length = input("Enter password length (Default 45): ")
    if length == "":
        length = 45
    elif int(length) < 8:
        print(f'\nAre you sure of a {length} character password?')
        print('(Recommended to have more than 8 characters)\n')

        sure = input('Y/n: ').lower()
        if sure == 'no' or sure == 'n':
            exit()
        
    refresh()


    output = generate(int(length))
    print(f'\n{output}')

    clipboard(output)

    if args.save:
        save(output)