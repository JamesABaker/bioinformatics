#Having a new crack at counting the fasta domains.

#DEPENDENCIES
from Bio import SeqIO
import subprocess
import numpy
from Bio.SeqUtils.ProtParamData import kd
from Bio.SeqUtils import ProtParam


#INPUT
records = list(SeqIO.parse("input.fasta", "fasta"))
print("\nThere are", len(records), "entries.\n")

with open('input.fasta') as f:
    all_fasta = str(f.read().splitlines())

ID_with_count = []

for i, item in enumerate(records):

    #this_fasta is the entire information on a specific sequence
    this_fasta = records[i]

    #this_fasta_ID holds the ID and checks how many times this ID comes up. Note that duplicate entries are presumed to be different TRANSMEM domains, however duplicate entries will not arise if using a pipeline from the TMDigger project.
    this_fasta_ID = this_fasta.id
    this_fasta_ID = this_fasta_ID.replace("'", "")
    occurance = all_fasta.count(this_fasta_ID)

    this_fasta_sequence = this_fasta.seq

    this_fasta_description = this_fasta.description
#    print(this_fasta_ID, "contains", occurance, "transmembrane domains.\n")
#    print(this_fasta_description,"\n",this_fasta_sequence,"\n\n\n\n")



    fasta_output = ">" + this_fasta_description + "Contains_" + str(occurance) + "_TMDs'\n" + this_fasta_sequence + "\n"
    fasta_output = str(fasta_output)
    print(fasta_output)

#ID_with_count now contains a list of IDs and how many TMDs that ID has.


    #This adds the current fasta sequence to a text file. Each text file only contains fasta sequences with the same number of TMDs. For example 7_TMDs.fasta only contains sequences that the protien has 7 TMDs
    output_file = str(occurance) + "_TMDs.fasta"
    with open(output_file, 'a') as out:
        out.write(fasta_output)

    #Now we are going to perform a KD calculation on the
    output_working_file = "KD_calc_in.txt"
    with open(output_working_file, 'w') as out:
        out.write(fasta_output)



#JIM WARWICKER FLAVOUR OF HYDROPHOBICITY
    var = "/"
    pipe = subprocess.Popen(["perl", "KD_calc.pl", var])
    pipe.wait()


    with open('KDcalc_out.txt', 'r') as totalKD:
        lines = totalKD.readlines()
        KD_line = lines[4]
        KD_line = KD_line.replace(" KD= ", "")
        KD_line = KD_line.replace(" ", ", ")
        KD_line = KD_line.replace(", ,", ",")
        totalKD.close()





    #Calculating the average KD count from the windowed data.
#    KD_average = numpy.mean(KD_list)
    print(KD_line)




    KD_output = ">" + this_fasta_description + "Contains_" + str(occurance) + "_TMDs'" + KD_line


    KD_output_file = str(occurance) + "_TMDs_KD_plot.csv"

    list_of_IDs = str(occurance) + "_ID_list.txt"

    with open(KD_output_file, 'a') as out:
        out.write(KD_output)

    with open(list_of_IDs, 'a') as out:
        out.write(this_fasta_ID)
        out.write(" ")
