
#Converts a .dat or uniprot into two text files. One text file is a list of IDs that only have one tmd, the other text file is a list with more than one.


#This requires a working version of Biopython.
from Bio import SeqIO


#These are the variables that are repeatedly used throughout the script. The only one that changes is the output_filename that is changed as the separate fasta sequences are generated.
filenames = ["human_ER.txt"]
input_format = "swiss" #This SHOULD work with uniprot filetype
feature_type = "TRANSMEM" #For future modification, this can be used to look for any annotation in the .dat file.
output_filename = "single_list.txt" #Simply the output name, can be anything as it is written in binary (not file-type specific language).
output2_filename = "multi_list.txt"


output_single = open(output_filename, "w")
output_multi = open(output2_filename, "w")
for filename in filenames:
    # Using SeqIO.parse will cope with multi-record files
    for record in SeqIO.parse(filename, input_format): #A biopython module that can automatically parse uniprot .txt files
        transmembrane_counter=0
        for f in record.features:
            #feature type refers to TRANSMEM
            if f.type == feature_type:
                transmembrane_counter=transmembrane_counter+1
        if transmembrane_counter==1:
            output_single.write(record.id)
            output_single.write("\n")
        elif transmembrane_counter>1:
            output_multi.write(record.id)
            output_multi.write("\n")
