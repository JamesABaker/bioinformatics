#This script aims at analysing the relationship between the hydrophobicity of the flanking regions and the hydropbobicity of the TMH.

#PYTHON3

#This requires a working version of Biopython.
from Bio import SeqIO
import numpy

### BIOPYTHON STANDARD VARIABLES FOR SEQ-IO ###


#These are the variables that are repeatedly used throughout the script. The only one that changes is the output_filename that is changed as the separate fasta sequences are generated.
filenames = ["input/human_transmem.txt"]
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
                print("\nfeature number:", x)

                TMD = f.extract(record.seq)

                title_line = "'%s' | TMH: '%i-%i'" % (record.id, f.location.start, f.location.end)



                ### HYDROPATHY CALCULATOR ###
                #Now we are going to get the average hydrophobicity of each region and save it to a string.
                # Kyte & Doolittle index of hydrophobicity
                kd = {'A': 1.8, 'R':-4.5, 'N':-3.5, 'D':-3.5, 'C': 2.5, 'Q':-3.5, 'E':-3.5, 'G':-0.4, 'H':-3.2, 'I': 4.5, 'L': 3.8,'K':-3.9, 'M':1.9, 'F': 2.8, 'P':-1.6,'S':-0.8, 'T':-0.7, 'W':-0.9, 'Y':-1.3, 'V': 4.2}

                TMD = list(TMD)

                TMD_KD_complete = []

                for i in TMD:
                    hydrophobicity = kd[i]
                    TMD_KD_complete.append(hydrophobicity)


                TMD_KD_avg = numpy.mean(TMD_KD_complete)


                this_total_average_output = [record.id, title_line, TMD_KD_avg]

                total_average_KD.append(this_total_average_output)

                #total_average_KD holds a list of lists ([ID, header line, average KD],[ID, header line, average KD])


                this_protein = total_average_KD[TMD_counter-1] #-1 needed because we are counting from 0 here.
                print("TMD", TMD_counter,":", this_protein)

        print(record.id)
        print("Final count:", TMD_counter, "containing:", total_average_KD, "\n")

        print("there were", len(total_average_KD), "helices in",record.id,".\n")
