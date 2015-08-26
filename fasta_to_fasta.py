#Fixes fastas into more manageable fastas (header line, sequence line rather than header line, several sequence lines)
import os

print "Opening input.\n"

input = "cytb5_alignment_uniprot.fasta"
fasta_results = "fasta_results.fasta"

if os.path.isfile(fasta_results):
    os.remove(fasta_results)
else:
    pass

results = open(fasta_results, "a")

broken_fasta_list = []
with open (input, "rb") as fastafile:
    data=fastafile.read()
    for line in data.split('\n'):
        broken_fasta_list.append(line)

for i in enumerate(broken_fasta_list):
    this_text = i[1]
    this_order = i[0]
    previous_text = broken_fasta_list[this_order-1]
    next_text = broken_fasta_list[this_order+1]

    if ">" in this_text:
        header = this_text
        sequence = ''
    elif ">" not in this_text:
        sequence = sequence + this_text
        if ">" in next_text:
            print header
            print sequence
        else:
            pass
    else:
        pass
