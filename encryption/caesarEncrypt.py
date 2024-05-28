#!/usr/bin/env python3
"""
UNDER CONSTRUCTION !

Script to encrypt text using Caesar Cipher.
Supported characters: A-Z, a-z, and 0-9.
Not supported characters will not be encrypted.

Arguments: <file-to-encrypt> <caesar-key-file> <output-file>

Format of the key: every character represents the replacement of the following characters (in order):
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
"""
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


if __name__ == "__main__":
    arg1 = argv[1]
    if argv[1] == "--help" or argv[1] == "-h":
        print("Syntax: ./caesarEncrypt.py <file-to-encrypt> <caesar-key-file> <output-file>")
