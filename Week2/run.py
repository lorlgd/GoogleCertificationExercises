#! /usr/bin/env python3
import os, sys
import json
import requests


def get_files(folder):
    try:
        if os.path.isdir(folder):
            return os.listdir(folder)
        raise OSError
    except OSError as e:
        print("{} does not exist or is not a folder. Make sure the path specified is a path to a valid folder.")
        sys.exit(1)


def convert_to_json(files, folder):
    keys = ["title", "name", "date", "feedback"]
    feedbacks = []
    url = "http://35.224.251.203/feedback/"
    for file in files:
        abs_file = os.path.join(folder, file)
        if file.endswith(".txt"):
            data = {}
            with open(abs_file, 'r') as feedback:
                for line, key in zip(feedback, keys):
                    data[key] = line.rstrip("\n")
            feedbacks.append(json.dumps(data))
    return feedbacks


def post_data(feedbacks):
    url = "http://myexample.com/feedback/"
    for feedback in feedbacks:
        response = requests.post(url, data=feedback)
        if response.status_code != 201:
            print("Couldn't post data. Status code: {}".format(response.status_code))
        else:
            print("Data posted successfully")


feedback_folder = "/data/feedback"
files = get_files(feedback_folder)
feedbacks = convert_to_json(files, feedback_folder)
post_data(feedbacks)
