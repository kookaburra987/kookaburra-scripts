#!/usr/bin/env python3
"""
Script to encrypt text using Caesar Cipher.
Supported characters: A-Z, a-z, and 0-9.
Not supported characters will not be encrypted.

Arguments: <file-to-encrypt> <caesar-key-file> <output-file>

Format of the key: every character represents the replacement of the following characters (in order):
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
"""
import sys
from sys import argv;

key_format = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def encrypt_char(char, key):
    if char in key_format:
        index = key_format.index(char)
        return key[index]
    else:
        return char


def encrypt_str(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_text += encrypt_char(char, key)
    return encrypted_text


def encrypt_file(filename, key):
    with open(filename, "r") as file:
        text = file.read()
        return encrypt_str(text, key)


if __name__ == "__main__":
    arg1 = ""
    if len(sys.argv) < 3 or argv[1] == "--help" or argv[1] == "-h":
        arg1 = argv[1]
        print("Syntax: ./caesarEncrypt.py <file-to-encrypt> <caesar-key-file> <output-file>")
    arg2 = argv[2]
    encrypted_txt = encrypt_file(arg1, arg2)

    with open(argv[3], "w") as out_file:
        out_file.write(encrypted_txt)
