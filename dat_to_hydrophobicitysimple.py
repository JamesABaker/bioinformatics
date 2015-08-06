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


#These are the variables that are repeatedly used throughout the script. The only one that changes is the output_filename that is changed as the separate fasta sequences are generated.
filenames = ["human/human_PM.txt"]
input_format = "swiss" #This SHOULD work with uniprot filetype
feature_type = "TRANSMEM" #For future modification, this can be used to look for any annotation in the .dat file.
output_filename = "human_ER.txt" #Simply the output name, can be anything as it is written in binary (not file-type specific language).



#This list will hold a list of lists
total_list = []

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


                ### HYDROphobicity average CALCULATOR ###
                #Now we are going to get the average hydrophobicity of each region and save it to a string. It goes through the fasta sequence and replaces adds a number to the list depending on the amino acid. Then the average of those numbers is taken.

                # Kyte & Doolittle index of hydrophobicity
                kd = {'A': 1.8, 'R':-4.5, 'N':-3.5, 'D':-3.5, 'C': 2.5, 'Q':-3.5, 'E':-3.5, 'G':-0.4, 'H':-3.2, 'I': 4.5, 'L': 3.8,'K':-3.9, 'M':1.9, 'F': 2.8, 'P':-1.6,'S':-0.8, 'T':-0.7, 'W':-0.9, 'Y':-1.3, 'V': 4.2}

                TMD = list(TMD)

                TMD_KD_complete = []

                for i in TMD:
                    hydrophobicity = kd[i]
                    TMD_KD_complete.append(hydrophobicity)


                TMD_KD_avg = numpy.mean(TMD_KD_complete)


                #Check this line for ID start/end
                title_line = ">'%s','%s', '%s' | TMH: '%i-%i'" % (record.id, record.name, TMD_KD_avg, f.location.start, f.location.end)

                #Now for the hydropathy windowed profile
                for i in TMD:
                    with open('KD_calc_in.txt','w') as temp_fasta:
                        temp_fasta.write(title_line)
                        temp_fasta.write("\n")
                        temp_fasta.write(str(f.extract(record.seq)))

                #Change this to the scale you want from the available perl scripts
                var = "/"
                pipe = subprocess.Popen(["perl", "KyteDoolittle.pl", var])
                pipe.wait()


                with open('KDcalc_out.txt', 'r') as totalKD:
                    lines = totalKD.readlines()
                    KD_line = lines[4]
                    totalKD.close()
                print(title_line, KD_line)
                os.remove("KDcalc_out.txt")
                os.remove("KD_calc_in.txt")
print("End.")
