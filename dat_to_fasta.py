#This script aims at analysing the relationship between the hydrophobicity of the flanking regions and the hydropbobicity of the TMH.

#PYTHON3

#This requires a working version of Biopython.
from Bio import SeqIO
import numpy

### BIOPYTHON STANDARD VARIABLES FOR SEQ-IO ###


#These are the variables that are repeatedly used throughout the script. The only one that changes is the output_filename that is changed as the separate fasta sequences are generated.
filenames = ["O14AG.txt"]
input_format = "swiss" #This SHOULD work with uniprot filetype
feature_type = "TRANSMEM" #For future modification, this can be used to look for any annotation in the .dat file.
output_filename = "TMH.fasta" #Simply the output name, can be anything as it is written in binary (not file-type specific language).



#This list will hold the IDs and the average KD


total_average_KD = []

### PULLING EACH TMD FROM THE .DAT FILE. ###

###We are just parsing to the correcting bit to loop here###
output = open(output_filename, "w")
for filename in filenames:
    # Using SeqIO.parse will cope with multi-record files
    for record in SeqIO.parse(filename, input_format): #A biopython module that can automatically parse uniprot .txt files

        total_average_KD = []
        TMD_counter=0
        for x, f in enumerate(record.features):

            #feature type refers to TRANSMEM
            if f.type == feature_type:
                TMD_counter = TMD_counter+1


                TMD = f.extract(record.seq)
                print(">", record.id, record.description, record.name)
                print(TMD)
