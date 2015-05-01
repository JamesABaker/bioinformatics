import os.path
import re
import fileinput
import sys
import shutil

with open ("KDcalc_out.txt", "r") as resultsfile:
    results=resultsfile.read().replace(' KD', 'KD')
    #results=results.replace(' KD', '')

output= results
text_file = open("KDcalc_out.txt", "w")
text_file.write("%s" % output)
text_file.close()
