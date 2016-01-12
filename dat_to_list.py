#This script aims at analysing the relationship between the hydrophobicity of the flanking regions and the hydropbobicity of the TMH.

#PYTHON3

#This requires a working version of Biopython.
from Bio import SeqIO
import numpy

### BIOPYTHON STANDARD VARIABLES FOR SEQ-IO ###


#These are the variables that are repeatedly used throughout the script. The only one that changes is the output_filename that is changed as the separate fasta sequences are generated

filenames = ["Human_clustered.txt"]
input_format = "swiss" #This SHOULD work with uniprot filetype
feature_type = "TRANSMEM" #For future modification, this can be used to look for any annotation in the .dat file.
output_filename = "TMH.fasta" #Simply the output name, can be anything as it is written in binary (not file-type specific language).
#This list will hold the IDs and the average KD
list_of_ID = []
### PULLING EACH TMD FROM THE .DAT FILE. ###
###We are just parsing to the correcting bit to loop here###
output = open(output_filename, "w")
for filename in filenames:
    # Using SeqIO.parse will cope with multi-record files
    for record in SeqIO.parse(filename, input_format): #A biopython module that can automatically parse uniprot .txt files
        for f in record.features:
            #feature type refers to TRANSMEM
            if f.type == feature_type:
                #These are the flanking regions and the TMD using record.seq. They are identified by simply counting 5 spaces before and after the TMD is annotated as being.
                list_of_ID.append(record.id)
#print(list_of_ID)
multi=[]
single=[]
#total_average_KD now holds a list of lists TMD as a list with: [ID, header line, average KD]
for i, item in enumerate(list_of_ID):
    how_many=list_of_ID.count(item)
    #print(item,"occured", how_many,"times.")
    if how_many == 1:
        single.append(item)
    elif how_many != 1:
        multi.append(item)

print("MULTI STARTS HERE")
for i in multi:
    print(i)
print("\n\n\n\n\n\n\n\n\n")
print("SINGLE STARTS HERE")
for i in single:
    print(i)

output.close()
