#!/usr/bin/env python3
"""
Script to fire a way a bunch of HTTP calls to a list of provided URLs
with the intention of discovering resources available on that URL.

Arguments: <url-list-file> <output-file> <httpMethod> <delay>

Be careful with the httpMethod parameter.
GET calls are safe, but POST, PUT, PATCH and DELETE calls can do damage on the server.

Be careful with the delay in milliseconds.
Some targets will not allow a high rate of calls.
"""
import sys
import time
import requests
from sys import argv

from requests import RequestException

def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def fire_to_url(target_url, method):
    if method != "GET":
        print("HTTP method " + method + " not supported")

    print("Cannons ready to fire " + method + " request to " + target_url)
    if method == "GET":
        try:
            resp = requests.get(target_url)
            analyse_response(resp)
        except requests.exceptions.ConnectionError:
            print("Connection error")
        except requests.exceptions.Timeout:
            print("Timeout error")
        except RequestException as e:
            print("Request error " + str(type(e)))


def analyse_response(resp):
    resp_status_code = resp.status_code
    print(resp_status_code)
    if resp_status_code != 404:
        print("HIT!")


if __name__ == "__main__":
    arg1 = argv[1]
    if arg1 == "--help" or arg1 == "-h":
        print("Syntax: ./fireAway.py <url-list-file> <output-file> <httpMethod> <delay>")
        exit(0)
    output_file = argv[2]
    http_method = "GET"
    if len(sys.argv) > 3:
        http_method = sys.argv[3]

    urls = read_file(arg1).split("\n")
    delay_seconds = float(sys.argv[4]) / 1000.0
    for url in urls:
        if url != "":
            fire_to_url(url, http_method)
            time.sleep(delay_seconds)