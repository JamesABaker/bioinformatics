####################################################
#####         Converts .dat files to           #####
#####       TMDs as different entries          #####
#####            in a FASTA file.              #####
#####     The rightmost number of the profile  #####
#####     is at the cytosolic edge of the TMD. #####
#####          Script by James Baker           #####
#####         University of Manchester         #####
####################################################

#requires PYTHON3
#requires KD_calc.pl in the working directory

import os
import subprocess
import re

#This requires a working version of Biopython and numpy.
#SeqIO is a biopython module that can automatically parse uniprot .txt files
from Bio import SeqIO
import numpy

### BIOPYTHON STANDARD VARIABLES FOR SEQ-IO ###

#These are the variables that are repeatedly used throughout the script.

FILE = "human_singlepass" ##########CHANGE THIS TO "YOUR FILE".txt without the .dat or .txt extension############
filenames = ["input/%s.txt" %FILE]



input_format = "swiss" #This works with uniprot filetype
feature_type = "TRANSMEM" #This is the TM helix. http://www.uniprot.org/help/transmem
other_feature_type = "TOPO_DOM" #This is a domain that has topology.http://www.uniprot.org/help/topo_dom

### PULLING EACH ENTRY FROM THE .DAT FILE. ###

big_list_of_direction_helices = []
for filename in filenames:
    for record in SeqIO.parse(filename, input_format):
        this_id_record = []




        ### TOPOLOGY CHECKER ###
        #We are only interested in finding helices with annotated cytoplasmic regions.



        #This opens the loop within the record (ie loops through the features in a single id)
        for i, f in enumerate(record.features): #i holds the number of the feature in 0,1,2,3,4 etc. f is the feature record.

            #if the feature is a TRANSMEM region then...
            if f.type == feature_type:

                #this checks that the helix actually has a TM with a flanking region.
                if f.location.end != "":

                    flank1 = record.seq[(f.location.start-5):(f.location.start)]

                    #There was a weird bug where one flank had "Unknown" annotation. This error handler reports any similar ids.
                    if "UnknownPosition" in str(f.location):
                        print(record.id, "contained a TMD without sequence number information.")

                    else:
                        flank2 = record.seq[(f.location.end):(f.location.end+5)]
                        TMD = f.extract(record.seq)
                        flanks_and_TMD = record.seq[(f.location.start-5):(f.location.end+5)]
                        flanks_and_TMD_reversed = flanks_and_TMD[::-1]



                        if i+1 < len(record.features):
                            next_feature = record.features[i+1]
                            previous_feature = record.features[i-1]


                            #This checks that the record has topological domain annotation.
                            if next_feature.type == other_feature_type:





                                ###Cytoplasmic facing###
                                #Checks that the next feature is a cytoplasmic region
                                if "Cytoplasmic" in str(next_feature.qualifiers):
                                    #print("Helix faces the cytoplasm.")
                                    #This checks that the cytoplasmic region starts where the transmembrane sequence ends.Be wary that location uses python slicing and zero-base counting rather than human friendly counting. https://www.biostars.org/p/139981/#140157
                                    if f.location.end == next_feature.location.start:

                                        #This fetches the sequence from the record according to the transmem annotation. This corrects for the zero-base counting and python slicing of the location.
                                        cyt_facing_TMD = flanks_and_TMD


                                        #Extract human readable name of ID
                                        protein_name = record.description
                                        start_name = protein_name.find("Full=")
                                        end_name = protein_name.find(";")
                                        protein_name = protein_name[start_name+5:end_name]
                                        protein_name = protein_name.replace(',','-')


                                        print(">", record.id, protein_name,"\n", cyt_facing_TMD, sep="")





                                ### not cytoplasmic facing, these TRANSMEM sequences should be reversed - still unsure of what to do for Plasma membrane... ###

                                elif "Cytoplasmic" in str(previous_feature.qualifiers):
                                    #print("Helix faces away from the cytoplasm.")
                                    #This checks that the next topological domain starts where the transmembrane sequence ends.
                                    if f.location.start == previous_feature.location.end:
                                        non_cyt_facing_TMD = flanks_and_TMD_reversed

                                        protein_name = record.description
                                        start_name = protein_name.find("Full=")
                                        end_name = protein_name.find(";")
                                        protein_name = protein_name[start_name+5:end_name]
                                        protein_name = protein_name.replace(',','-')
                                        print(">", record.id, protein_name, "\n", non_cyt_facing_TMD, sep="")



print("End.")
