#!/usr/bin/env python

import os

def create_file_list(directory):
    a = os.listdir(directory)
    a.sort()
    return a
    #returns sorted list of files
