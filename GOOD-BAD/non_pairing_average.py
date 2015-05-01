#This script aims at analysing the relationship between the hydrophobicity of the flanking regions and the hydropbobicity of the TMH.

#PYTHON3

#This requires a working version of Biopython.
from Bio import SeqIO
import numpy

### BIOPYTHON STANDARD VARIABLES FOR SEQ-IO ###


#These are the variables that are repeatedly used throughout the script. The only one that changes is the output_filename that is changed as the separate fasta sequences are generated.
filenames = ["ER_human_multi.dat"]
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
                #These are the flanking regions and the TMD using record.seq. They are identified by simply counting 5 spaces before and after the TMD is annotated as being.
                #print(record.id)
                #flank1 = record.seq[(f.location.start-5):(f.location.start)]
                #flank2 = record.seq[(f.location.end):(f.location.end+5)]
                TMD = f.extract(record.seq)
                #flank1length = len(flank1)
                #flank2length = len(flank2)
                #Here we define the ID code and then the start and end positions.
                #title_line = "'%s' | TMH: '%i-%i'| N-terminal flank: '%i-%i'| C-terminal flank: '%i-%i'" % (record.id, f.location.start+1, f.location.end, f.location.start-flank1length, f.location.start, f.location.end+1, f.location.end+flank2length+1)
                title_line = "'%s' | TMH: '%i-%i'" % (record.id, f.location.start+1, f.location.end)

                #This prints the title and then any TRANSMEM regions associated with that entry along with flanking regions.
                #output.write(">%s\n%s%s%s\n" % (title_line, flank1, TMD, flank2))
                output.write(">%s\n%s\n" % (title_line, TMD))
                #if there are any TRANSMEM entries, it prints them. Note that if there is no transmem domain then the ID is skipped, you won't get flanking regions without an identified TMD.
                #Prints the output in the terminal
                #print("ID:", record.id)
                #print("Header:", title_line)
                #print("N flank: " , flank1)
                #print("Trans Membrane Domain:", TMD)
                #print("C flank: " , flank2)
                #print("fasta output to file: \n>%s\n%s%s%s\n" % (title_line, flank1, TMD, flank2))
                #print("fasta output to file: \n>%s\n%s\n" % (title_line, TMD))

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
                print(record.id, TMD_KD_avg)


#total_average_KD now holds a list of lists TMD as a list with: [ID, header line, average KD]



output.close()
