# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 09:37:15 2022

@author: Kyle
"""
import os, glob

os.chdir('C:/Users/Kyle/Documents/GA Tech - OMS Analytics/ISYE6414/Module4/Transcripts')

# get all txt files
read_files = glob.glob("*.txt")

# extract the number and create a tuple
read_files = [(int(s.split("_")[0]), s) for s in read_files]

# sort the tuple and create a new list with only the filename
read_files = [x[1] for x in sorted(read_files)]


with open("result_2.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write("\n\n".encode())
            outfile.write(f.encode())
            outfile.write("\n\n".encode())
            outfile.write(infile.read())