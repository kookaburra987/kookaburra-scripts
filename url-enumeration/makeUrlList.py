#!/usr/bin/env python3

import argparse

"""
Replaces the next {$} with a values of the dictionary_file.
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
    parser = argparse.ArgumentParser()
    parser.add_argument("dictionary_file", help="file with words and numbers to combine in URLs")
    parser.add_argument("output_file", help="file to write the URLs to")
    parser.add_argument("mask", help="baseUrl in which {$} will be replaced")
    args = parser.parse_args()

    words = read_file(args.dictionary_file).split("\n")
    words.remove("")
    urls = make_urls(args.mask, words)

    with open(args.output_file, "w") as file:
        for url in urls:
            file.write(url)
            file.write("\n")
