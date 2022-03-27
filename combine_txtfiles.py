# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 09:37:15 2022

@author: Kyle
"""

# import packages
import os, glob

# set directory for where your txt files are
os.chdir('C:/Users/Kyle/Documents/GA Tech - OMS Analytics/ISYE6414/Module4/Transcripts')

# get all txt files
read_files = glob.glob("*.txt")

# iterate and add all files back into a single file path
with open("result_2.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write("\n\n".encode())
            outfile.write(f.encode())
            outfile.write("\n\n".encode())
            outfile.write(infile.read())
