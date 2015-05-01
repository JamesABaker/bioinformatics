#####
##### Converts .dat files to [ID, NAME, AVERAGE KD, KD profile]
#####

#PYTHON3
import os
import subprocess
import re
#This requires a working version of Biopython.
from Bio import SeqIO
import numpy

### BIOPYTHON STANDARD VARIABLES FOR SEQ-IO ###


#These are the variables that are repeatedly used throughout the script.

filenames = ["human/human_PM.txt"]
input_format = "swiss" #This SHOULD work with uniprot filetype
other_feature_type = "TOPO_DOM" #For future modification, this can be used to look for any annotation in the .dat file.
output_filename = "human_ER.txt" #Simply the output name, can be anything as it is written in binary (not file-type specific language).

for filename in filenames:
    # Using SeqIO.parse will cope with multi-record files
    for record in SeqIO.parse(filename, input_format): #A biopython module that can automatically parse uniprot .txt files
        for q in record.features:
            #feature type refers to TRANSMEM
            if q.type == other_feature_type:
                print(q.qualifiers)
                if "Cytoplasmic" in str(q.qualifiers):
                    print("Cytoplasmic")
                elif "Extracellular" in str(q.qualifiers):
                    print("Extracellular")
                else:
                    pass
