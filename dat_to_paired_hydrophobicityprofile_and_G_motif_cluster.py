#This script aims at analysing the relationship between the G zip motif and pairwise hydrophobicity. This calculates the average hydrophobicity of the pairs alongside the number of G motifs in that pair.

#This requires a working version of Biopython.
from Bio import SeqIO
import numpy
import re

### Function to find G zippers.
number_of_zip_motifs = 0

def Find(pat, text):
    global number_of_zip_motifs
    match = re.search(pat, text)
    if match:
        number_of_zip_motifs = number_of_zip_motifs + 1
    else:
        pass
        #print 'No G zippers found in this TMD.'



### Dictionary for Kyte and Doolittle hydrophobicity index.

kd = {'A': 1.8, 'R':-4.5, 'N':-3.5, 'D':-3.5, 'C': 2.5, 'Q':-3.5, 'E':-3.5, 'G':-0.4, 'H':-3.2, 'I': 4.5, 'L': 3.8, 'K':-3.9, 'M':1.9, 'F': 2.8, 'P':-1.6,'S':-0.8, 'T':-0.7, 'W':-0.9, 'Y':-1.3, 'V': 4.2,}


#These are the variables that are repeatedly used throughout the script. The only one that changes is the output_filename that is changed as the separate fasta sequences are generated.
filenames = ["human_transmem.txt"]
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
        for f in record.features:
            #feature type refers to TRANSMEM
            if f.type == feature_type:


                TMD = f.extract(record.seq)
                TMD = str(TMD)



                #print "Searching for G zipper motif in the TMD from ", record.id, ": ", TMD
                Find('G...G...G', TMD) #Should the significant complete zippers be used here instead? (G,A,S)XXXGXXXG and GXXXGXXX(G,S,T).
                #print number_of_zip_motifs
                Find('A...G...G', TMD)
                Find('S...G...G', TMD)
                Find('G...G...S', TMD)
                Find('G...G...T', TMD)


                #Hydrophobicity of TMD
                TMD = list(TMD)

                TMD_KD_complete = []
                #print record.id, TMD
                for i in TMD:
                    if i == 'X':
                        pass
                    else:
                        hydrophobicity = kd[i]
                        TMD_KD_complete.append(hydrophobicity)

                TMD_KD_avg = numpy.mean(TMD_KD_complete)

                #print TMD_KD_avg

                protein_name = record.description
                start_name = protein_name.find("Full=")
                end_name = protein_name.find(";")
                protein_name = protein_name[start_name+5:end_name]
                protein_name = protein_name.replace(',','-')

                this_total_average_output = [record.id, f.location.start, f.location.end, TMD_KD_avg, protein_name, number_of_zip_motifs]
                total_average_KD.append(this_total_average_output)

        #G zipper counter reset per protein ID
        number_of_zip_motifs = 0

#total_average_KD now holds each TMD as an [ID, header line, start position, end position, average KD]

print " ID, Name and details, Distance between pair, Average hydrophobicity of pair, The difference in hydrophobicity between the pair, The number of gzip motifs in the pair."

for i, item in enumerate(total_average_KD):
    this_protein = total_average_KD[i]
    that_protein = total_average_KD[i+1]
    #Check that they are in the same protein
    if this_protein[0] == that_protein[0]:
        #calculate the distance between the end of this helix and the begining of the next helix.
        distance = int(that_protein[1] - this_protein[2])
        this_that_pair = [this_protein[3], that_protein[3]]
        this_TMD_pair_KD = numpy.mean(this_that_pair)
        this_difference = abs(this_protein[3]-that_protein[3])

        pairwise_gzippers = this_protein[5] = that_protein[5]




        print this_protein[0], ",", this_protein[4], ",",distance,",", this_TMD_pair_KD, ",", this_difference, ",", pairwise_gzippers


    else:
        pass

output.close()
