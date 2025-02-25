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
import argparse
import time
import requests

from requests import RequestException

def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def fire_to_url(target_url, method, hits):
    if method != "GET":
        print("HTTP method " + method + " not supported")

    print("Cannons ready to fire " + method + " request to " + target_url)
    if method == "GET":
        try:
            resp = requests.get(target_url)
            is_hit = analyse_response(resp)
            if is_hit:
                hits.append(target_url + " " + str(resp.status_code))
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
        return True
    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url_list_file", help="file with list of URLs to call")
    parser.add_argument("output_file", help="file to write the URLs that were hit to")
    parser.add_argument("-m", "--method", help="HTTP-method to use", default="GET")
    parser.add_argument("-d", "--delay", help="delay between calls in milliseconds", default=200, type=int)
    args = parser.parse_args()

    urls = read_file(args.url_list_file).split("\n")
    hit_urls = []
    delay_seconds = float(args.delay) / 1000.0
    for url in urls:
        if url != "":
            fire_to_url(url, args.method, hit_urls)
            time.sleep(delay_seconds)
    with open(args.output_file, "w") as output_file:
        for hit_url in hit_urls:
            output_file.write(hit_url + "\n")
