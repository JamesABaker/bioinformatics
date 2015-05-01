import os.path
import re
import fileinput
import sys
import shutil

with open ("input.txt", "r") as resultsfile:
    results=resultsfile.read().replace(' ', '')

'''
results = results.replace(':', '_')
results = results.replace('-', '_')
results = results.replace('|', '_')
results = results.replace("'", "_")

'''

results = results.replace('\n', ' ')
results = results.replace('_', '')
results = results.replace('>', '\n>')
print results

output= results
text_file = open("KD_calc_in_sed.txt", "w")
text_file.write("%s" % output)
text_file.close()
