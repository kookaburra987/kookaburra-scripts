#!/usr/bin/env python3
"""
Script to encrypt and decrypt text using Caesar Cipher.
Supported characters: A-Z, a-z
Not supported characters will not be encrypted.

Arguments: <-e/-d> <in-file> <key> <output-file>
The key is a simple integer between 1 and 26.
-e for encryption
-d for decryption
"""
import string
from sys import argv


def rotate(text, rot):
    return text[-rot:] + text[:-rot]


def caesar_mapping(key):
    return rotate(string.ascii_lowercase, key)


def get_key():
    if mode == '-e':
        return int(argv[3])
    elif mode == '-d':
        return -int(argv[3])
    else:
        return 0


def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def map_char(char, mapping):
    if char in mapping:
        index = mapping.index(char)
        return string.ascii_lowercase[index]
    else:
        return char


def apply_caesar(text, key):
    mapping = caesar_mapping(key)
    new_text = ""
    for char in text:
        new_text += map_char(char, mapping)
    return new_text


if __name__ == '__main__':
    if argv[1] == "--help" or argv[1] == "-h":
        print("Syntax: ./caesar.py <-e/-d> <in-file> <key> <output-file>")
        exit(0)
    mode = argv[1]
    in_file = argv[2]
    key = get_key()
    out_file = argv[4]
    txt = read_file(in_file)
    out_txt = apply_caesar(txt, key)

    with open(out_file, "w") as file:
        file.write(out_txt)
