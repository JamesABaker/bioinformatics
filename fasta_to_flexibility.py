
###############################################################
########################## BioTM ##############################
################## Kyte&Doolittle calculator ##################
###############################################################
###############################################################

# Getting all the system stuff

import sys
import os
import fileinput
import sys
import urllib,urllib2
import Bio
from Bio.SeqUtils import ProtParam
from Bio.SeqUtils.ProtParam import ProteinAnalysis




from Bio import SeqIO
handle = open("mutants.fasta", "r")
for record in SeqIO.parse(handle, "fasta") :
    print record.id
    print record.seq
    my_seq = str(record.seq)
    analysed_seq = ProteinAnalysis(my_seq)

    #Disorder
    print analysed_seq.flexibility()
