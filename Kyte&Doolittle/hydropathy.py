#####
##### The list of lists holds the [[title1, seq1], [title2, seq2]]
#####

import subprocess
import re

print "Opening input.\n"

with open ("input.fasta", "rb") as fastafile:
    data=fastafile.read().replace("'\n", "':::") #this ::: acts as a marker for makign the list of lists
    stringA = data
    stringB = [] #Create an empty list
    for line in stringA.split('\n'): # Loop through each line in the original text.  Assumes these are newline line breaks which are represented by \n.
        splitLine = line.split(':::') #Split the pairs on the , into a 2 item list according to the marker
        stringB.append(splitLine) #Append that list to our empty list so thus it will end up with a list of lists.'''

seqs = stringB

for i in seqs:
    print i
    header = i[0]
    seq1 = i[1]
    print "Calculating KD of ", header, "..."
    with open('KD_calc_in.txt','wb') as temp_fasta:
        temp_fasta.write(header)
        temp_fasta.write("\n")
        temp_fasta.write(seq1)


    var = "/"
    pipe = subprocess.Popen(["perl", "KD_calc.pl", var])
    pipe.wait()


    with open('KDcalc_out.txt', 'rb') as totalKD:
        lines = totalKD.readlines()
        KD_line = lines[4]
        totalKD.close()

    KD_average = reduce(lambda x, y: x + y, KD_line) / len(KD_line)

    ID = str(header)
    KD = str(KD_line)
    Average = str(KD_average)

    ID = re.sub('[>]', '', ID)
    ID = re.sub("[']", '', ID)
    KD = re.sub("[KD=]", '', KD)
    result = ID+KD
    result = re.sub("  ", ', ', result)
    result = re.sub(", , , ,", '', result)
    result = re.sub(" , ", '', result)
    print result

    with open('result.csv', 'ab') as results_file:
        results_file.write(result)
