from __future__ import division
from Bio import SeqIO
import sys
import matplotlib
#import matplotlib.pyplot as plt
import numpy as np


# These are the variables that are repeatedly used throughout the script.
# The only one that changes is the output_filename that is changed as the
# separate fasta sequences are generated.
filename = sys.argv[1]
input_format = "swiss"  # This SHOULD work with uniprot filetype
# For future modification, this can be used to look for any annotation in
# the .dat file.
feature_types = ["HELIX", "STRAND", "TRANSMEM"]

a_names = ["A", "C", "D", "E", "F", "G", "H", "I", "K",
           "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"]

# This list will be filled with empty lists that can be filled later, for
# example if we want to check more feature types.
absolute_propensity = []
feature_type_averaged_values = []
for n, i in enumerate(feature_types):
    absolute_propensity.append([])
    for number_of_residues in a_names:
        absolute_propensity[n].append(0)

for feature_type_index, feature_type in enumerate(feature_types):
    lengths = []
    total_structures = 0
    # Using SeqIO.parse will cope with multi-record files
    # A biopython module that can automatically parse uniprot .txt files
    for record in SeqIO.parse(filename, input_format):
        for f in record.features:
            # feature type refers to what secondary feature we are currently
            # querying.
            if f.type == feature_type:
                total_structures = total_structures + 1
                sequence_for_propensity_check = f.extract(record.seq)
                lengths.append(len(sequence_for_propensity_check))
                for residue_type_index, residue_type in enumerate(a_names):
                    for amino_acid_in_feature in sequence_for_propensity_check:
                        if str(amino_acid_in_feature) == residue_type:
                            absolute_propensity[feature_type_index][residue_type_index] = absolute_propensity[
                                feature_type_index][residue_type_index] + 1


    print "\n\n", feature_type, "\n", " ".join(map(str, a_names))
    print "Absolute values"
    print " ".join(map(str, absolute_propensity[feature_type_index]))
    print "Averaged values"
    averaged_values = []
    for i in absolute_propensity[feature_type_index]:
        # /total_structures)
        averaged_value = float(
            i / sum(absolute_propensity[feature_type_index]))
        averaged_values.append(averaged_value)
    print " ".join(map(str, averaged_values))
    feature_type_averaged_values.append(averaged_values)
    print "Mean length"
    print np.mean(lengths)

#plt.plot(feature_type_averaged_values) # Create a plot for sum_list
#plt.show() # Show the plot
