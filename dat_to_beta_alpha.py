from Bio import SeqIO
import sys

# These are the variables that are repeatedly used throughout the script.
# The only one that changes is the output_filename that is changed as the
# separate fasta sequences are generated.
filename = sys.argv[1]
input_format = "swiss"  # This SHOULD work with uniprot filetype
# For future modification, this can be used to look for any annotation in
# the .dat file.
feature_types = ["HELIX", "STRAND"]

a_names = ["A", "C", "D", "E", "F", "G", "H", "I", "K",
    "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"]

absolute_propensity = []

for n, i in enumerate(feature_types):
    absolute_propensity.append([])
    for number_of_residues in a_names:
        absolute_propensity[n].append(0)

for feature_type_index, feature_type in enumerate(feature_types):
    # Using SeqIO.parse will cope with multi-record files
    # A biopython module that can automatically parse uniprot .txt files
    for record in SeqIO.parse(filename, input_format):
        for f in record.features:
            # feature type refers to what secondary feature we are currently
            # querying.
            if f.type == feature_type:
                sequence_for_propensity_check = f.extract(record.seq)
                for residue_type_index, residue_type in enumerate(a_names)):
                    for amino_acid_in_feature in sequence_for_propensity_check:
                        if str(amino_acid_in_feature) == residue_type:
                            absolute_propensity[feature_type_index][residue_type_index]=absolute_propensity[
                                feature_type_index][residue_type_index] + 1
    print a_names
    print absolute_propensity[feature_type_index]
