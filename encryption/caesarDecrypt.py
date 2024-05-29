#!/usr/bin/env python3
"""
Script to decrypt cyper text using Caesar Cipher.
Supported characters: A-Z, a-z, and 0-9.
Not supported characters will not be decrypted.

Arguments: <file-to-decrypt> <caesar-key-file> <output-file>

Format of the key: every character represents the replacement of the following characters (in order):
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
"""
from sys import argv;

key_format = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def decrypt_char(char, key):
    if char in key_format:
        index = key.index(char)
        return key_format[index]
    else:
        return char


def decrypt_str(cipher_text, key):
    decrypted_text = ""
    for char in cipher_text:
        decrypted_text += decrypt_char(char, key)
    return decrypted_text


def decrypt_file(filename, key):
    with open(filename, "r") as file:
        cipher_text = file.read()
        return decrypt_str(cipher_text, key)


def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


if __name__ == "__main__":
    arg1 = argv[1]
    if arg1 == "--help" or arg1 == "-h":
        print("Syntax: ./caesarDecrypt.py <file-to-decrypt> <caesar-key-file> <output-file>")
        exit(0)
    key_file = argv[2]
    key_file_content = read_file(key_file)
    decrypted_txt = decrypt_file(arg1, key_file_content)

    with open(argv[3], "w") as out_file:
        out_file.write(decrypted_txt)
