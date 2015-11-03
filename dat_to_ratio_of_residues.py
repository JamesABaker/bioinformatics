from Bio import SeqIO
import numpy

### BIOPYTHON STANDARD VARIABLES FOR SEQ-IO ###


# These are the variables that are repeatedly used throughout the script.
# The only one that changes is the output_filename that is changed as the
# separate fasta sequences are generated.
filenames = ["human.txt"]
input_format = "swiss"  # This SHOULD work with uniprot filetype
# For future modification, this can be used to look for any annotation in
# the .dat file.
feature_type = "TRANSMEM"
# Simply the output name, can be anything as it is written in binary (not
# file-type specific language).
output_filename = "Helix.fasta"

negative_residues_in_total = 0
positive_residues_in_total = 0
total_residues_in_total = 0

negative_residues_in_helix = 0
positive_residues_in_helix = 0
total_residues_in_helix = 0

negative_residues_in_flank = 0
positive_residues_in_flank = 0
total_residues_in_flank = 0


for filename in filenames:
    # Using SeqIO.parse will cope with multi-record files
    # A biopython module that can automatically parse uniprot .txt files
    for record in SeqIO.parse(filename, input_format):

        total_average_KD = []

        for x, f in enumerate(record.features):

            # Now we add each count of charge residues to any protein.
            sequence = str(record.seq)
            negative_residues_in_total = negative_residues_in_total + \
                sequence.count('E') + sequence.count('D')
            positive_residues_in_total = positive_residues_in_total + \
                sequence.count('K') + sequence.count('R')
            total_residues_in_total = total_residues_in_total + len(sequence)

            # feature type refers to TRANSMEM
            if f.type == feature_type:

                TMD = f.extract(record.seq)
                flank1 = record.seq[(f.location.start - 5):(f.location.start)]
                flank2 = record.seq[(f.location.end):(f.location.end + 5)]

                # print sequence
                # print flank1, TMD, flank2

                # Now we add each count of charge residues to the respective
                # counter that matches the feature type
                negative_residues_in_helix = negative_residues_in_helix + \
                    TMD.count('E') + TMD.count('D')
                positive_residues_in_helix = positive_residues_in_helix + \
                    TMD.count('K') + TMD.count('R')
                total_residues_in_helix = total_residues_in_helix + len(TMD)

                flanks = flank1 + flank2
                negative_residues_in_flank = negative_residues_in_flank + \
                    flanks.count('E') + flanks.count('D')
                positive_residues_in_flank = positive_residues_in_flank + \
                    flanks.count('K') + flanks.count('R')
                total_residues_in_flank = total_residues_in_flank + len(flanks)


print "Input file:", filenames

percentage = (1. * positive_residues_in_total / total_residues_in_total) * 100
print "Positive resiudues in the total population:", positive_residues_in_total, " Total", total_residues_in_total, " Percentage:", percentage, "%"

percentage = (1. * negative_residues_in_total / total_residues_in_total) * 100
print "Negative resiudues in the total population:", negative_residues_in_total, " Total:", total_residues_in_total, " Percentage:", percentage, "%"


percentage = (1. * positive_residues_in_helix / total_residues_in_helix) * 100
print "Positive resiudues in the helix:", positive_residues_in_helix, " Total", total_residues_in_helix, " Percentage:", percentage, "%"

percentage = (1. * negative_residues_in_helix / total_residues_in_helix) * 100
print "Negative resiudues in the helix:", negative_residues_in_helix, " Total:", total_residues_in_helix, " Percentage:", percentage, "%"


percentage = (1. * positive_residues_in_flank / total_residues_in_flank) * 100
print "Positive resiudues in the flanks:", positive_residues_in_flank, " Total", total_residues_in_flank, " Percentage:", percentage, "%"

percentage = (1. * negative_residues_in_flank / total_residues_in_flank) * 100
print "Negative resiudues in the flanks:", negative_residues_in_flank, " Total:", total_residues_in_flank, " Percentage:", percentage, "%"
