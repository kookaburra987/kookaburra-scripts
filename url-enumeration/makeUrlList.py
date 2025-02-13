#!/usr/bin/env python3
"""
Script to guess the URLs that might map to an HTTP-resource.

Arguments: <guess-file> <output-file> <mask>

guess-file is a file of words and numbers to add in the URLs

The mask tells the part of the URL that is always the same.
The part that is uncertain must be indicated with {$}.

Example: http://localhost:8080/my-app/{$}/{$}
"""
from sys import argv;

"""
Replaces the next {$} with a values of the guess-file.
The new masks are added to the mask_list.
"""


def add_urls(msk, wrds, url_list):
    if msk.find('{$}') != -1:
        for word in wrds:
            new_mask = msk.replace('{$}', word, 1)
            print(new_mask)
            add_urls(new_mask, wrds, url_list)
    else:
        url_list.append(msk)


"""
Makes a list of URLs based on the mask and a list of words and numbers.
"""


def make_urls(msk, wrds):
    url_list = []
    add_urls(msk, wrds, url_list)
    return url_list


def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


if __name__ == "__main__":
    arg1 = argv[1]
    if arg1 == "--help" or arg1 == "-h":
        print("Syntax: ./makeUrlList.py <guess-file> <output-file> <mask>")
        print("use {$} in mask for parts that are to be replaced")
        exit(0)
    output_file = argv[2]
    mask = argv[3]

    words = read_file(arg1).split("\n")
    words.remove("")
    urls = make_urls(mask, words)

    with open(output_file, "w") as file:
        for url in urls:
            file.write(url)
            file.write("\n")
