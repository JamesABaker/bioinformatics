# This script aims at analysing the relationship between the
# hydrophobicity of the flanking regions and the hydropbobicity of the
# TMH.

# PYTHON3

# This requires a working version of Biopython.
from Bio import SeqIO
import numpy

### BIOPYTHON STANDARD VARIABLES FOR SEQ-IO ###


# These are the variables that are repeatedly used throughout the script.
# The only one that changes is the output_filename that is changed as the
# separate fasta sequences are generated.
filenames = ["helixnottransmembraneandhuman.txt"]
input_format = "swiss"  # This SHOULD work with uniprot filetype
# For future modification, this can be used to look for any annotation in
# the .dat file.
feature_type = "HELIX"
# Simply the output name, can be anything as it is written in binary (not
# file-type specific language).
output_filename = "Helix.fasta"


with open("output/flank1.fasta", "wb") as myfile:
    myfile.write("")


with open("output/TMD.fasta", "wb") as myfile:
    myfile.write("")


with open("output/flank2.fasta", "ab") as myfile:
    myfile.write("")


# This list will hold the IDs and the average KD


total_average_KD = []

### PULLING EACH TMD FROM THE .DAT FILE. ###

###We are just parsing to the correcting bit to loop here###
output = open(output_filename, "w")
for filename in filenames:
    # Using SeqIO.parse will cope with multi-record files
    # A biopython module that can automatically parse uniprot .txt files
    for record in SeqIO.parse(filename, input_format):

        total_average_KD = []
        TMD_counter = 0
        for x, f in enumerate(record.features):

            # feature type refers to TRANSMEM
            if f.type == feature_type:
                TMD_counter = TMD_counter + 1

                TMD = f.extract(record.seq)
                flank1 = record.seq[(f.location.start - 5):(f.location.start)]
                flank2 = record.seq[(f.location.end):(f.location.end + 5)]

                header = str(">" + record.id +
                             record.description + record.name)
                print header
                print flank1, TMD, flank2
                flank1 = str(flank1)
                flank2 = str(flank2)
                TMD = str(TMD)
                with open("output/flank1.fasta", "ab") as myfile:
                    myfile.write(header)
                    myfile.write("\n")
                    myfile.write(flank1)
                    myfile.write("\n")

                with open("output/TMD.fasta", "ab") as myfile:
                    myfile.write(header)
                    myfile.write("\n")
                    myfile.write(TMD)
                    myfile.write("\n")

                with open("output/flank2.fasta", "ab") as myfile:
                    myfile.write(header)
                    myfile.write("\n")
                    myfile.write(flank2)
                    myfile.write("\n")
