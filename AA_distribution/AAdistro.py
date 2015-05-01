print "Opening input.\n"

with open ("input.fasta", "rb") as fastafile:
    data=fastafile.read().replace("'\n", "':::") #this ::: acts as a marker for makign the list of lists
    stringA = data
    stringB = [] #Create an empty list
    for line in stringA.split('\n'): # Loop through each line in the original text.  Assumes these are newline line breaks which are represented by \n.
        splitLine = line.split(':::') #Split the pairs on the , into a 2 item list according to the marker
        stringB.append(splitLine) #Append that list to our empty list so thus it will end up with a list of lists.'''

seqs = stringB

#This is for A, alanine. There is a seperate file generated for each amino acid.

for i in seqs:
    #Here we define the header, and the actual amino acid sequence held is i of seqs. i just means for each item do this.
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '1') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("A.csv", "ab")
    text_file.write("%s\n" % output)

#This is for R, arginine
for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '1') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("R.csv", "ab")
    text_file.write("%s\n" % output)


#This is for N
for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '1') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("N.csv", "ab")
    text_file.write("%s\n" % output)

#This is for D
for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '1') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("D.csv", "ab")
    text_file.write("%s\n" % output)


#And for B
for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '1') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("B.csv", "ab")
    text_file.write("%s\n" % output)

#This is for C
for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '1') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("C.csv", "ab")
    text_file.write("%s\n" % output)


for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '1') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("E.csv", "ab")
    text_file.write("%s\n" % output)


for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '1') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("Q.csv", "ab")
    text_file.write("%s\n" % output)


for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '1') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("Z.csv", "ab")
    text_file.write("%s\n" % output)





for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '1') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("G.csv", "ab")
    text_file.write("%s\n" % output)







for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '1') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("H.csv", "ab")
    text_file.write("%s\n" % output)





for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '1') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("I.csv", "ab")
    text_file.write("%s\n" % output)







for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '1') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("L.csv", "ab")
    text_file.write("%s\n" % output)







for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '1') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("K.csv", "ab")
    text_file.write("%s\n" % output)

for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '1') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("M.csv", "ab")
    text_file.write("%s\n" % output)

for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '1') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("F.csv", "ab")
    text_file.write("%s\n" % output)



for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '1') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("P.csv", "ab")
    text_file.write("%s\n" % output)



for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '1') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("S.csv", "ab")
    text_file.write("%s\n" % output)

for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '1') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("T.csv", "ab")
    text_file.write("%s\n" % output)







for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '1') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("W.csv", "ab")
    text_file.write("%s\n" % output)

for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '1') for w in AA_frequency]
    AA_frequency = [w.replace('V', '0') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("Y.csv", "ab")
    text_file.write("%s\n" % output)

for i in seqs:
    header = i[0]
    seq1 = i[1]

    AA_frequency = seq1
    AA_frequency = [w.replace('A', '0') for w in AA_frequency]
    AA_frequency = [w.replace('R', '0') for w in AA_frequency]
    AA_frequency = [w.replace('N', '0') for w in AA_frequency]
    AA_frequency = [w.replace('D', '0') for w in AA_frequency]
    AA_frequency = [w.replace('B', '0') for w in AA_frequency]
    AA_frequency = [w.replace('C', '0') for w in AA_frequency]
    AA_frequency = [w.replace('E', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Q', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Z', '0') for w in AA_frequency]
    AA_frequency = [w.replace('G', '0') for w in AA_frequency]
    AA_frequency = [w.replace('H', '0') for w in AA_frequency]
    AA_frequency = [w.replace('I', '0') for w in AA_frequency]
    AA_frequency = [w.replace('L', '0') for w in AA_frequency]
    AA_frequency = [w.replace('K', '0') for w in AA_frequency]
    AA_frequency = [w.replace('M', '0') for w in AA_frequency]
    AA_frequency = [w.replace('F', '0') for w in AA_frequency]
    AA_frequency = [w.replace('P', '0') for w in AA_frequency]
    AA_frequency = [w.replace('S', '0') for w in AA_frequency]
    AA_frequency = [w.replace('T', '0') for w in AA_frequency]
    AA_frequency = [w.replace('W', '0') for w in AA_frequency]
    AA_frequency = [w.replace('Y', '0') for w in AA_frequency]
    AA_frequency = [w.replace('V', '1') for w in AA_frequency]

    AA_frequency.insert(0,header)
    output = ', '.join(AA_frequency)
    text_file = open("V.csv", "ab")
    text_file.write("%s\n" % output)


#Now there are 22 files generated. Each contrains the realitive "hit or miss" for the corresponding amino acid through each of the sequences.





#Now we want to stitch all the seperate CSV files together in order.


with open ("A.csv", "r") as resultsfile:
    A=resultsfile.read()

with open ("R.csv", "r") as resultsfile:
    R=resultsfile.read()

with open ("N.csv", "r") as resultsfile:
    N=resultsfile.read()

with open ("D.csv", "r") as resultsfile:
    D=resultsfile.read()

with open ("B.csv", "r") as resultsfile:
    B=resultsfile.read()

with open ("C.csv", "r") as resultsfile:
    C=resultsfile.read()

with open ("E.csv", "r") as resultsfile:
    E=resultsfile.read()

with open ("Q.csv", "r") as resultsfile:
    Q=resultsfile.read()

with open ("Z.csv", "r") as resultsfile:
    Z=resultsfile.read()

with open ("G.csv", "r") as resultsfile:
    G=resultsfile.read()


with open ("H.csv", "r") as resultsfile:
    H=resultsfile.read()


with open ("I.csv", "r") as resultsfile:
    I=resultsfile.read()

with open ("L.csv", "r") as resultsfile:
    L=resultsfile.read()

with open ("K.csv", "r") as resultsfile:
    K=resultsfile.read()

with open ("M.csv", "r") as resultsfile:
    M=resultsfile.read()

with open ("F.csv", "r") as resultsfile:
    F=resultsfile.read()

with open ("P.csv", "r") as resultsfile:
    P=resultsfile.read()

with open ("S.csv", "r") as resultsfile:
    S=resultsfile.read()

with open ("T.csv", "r") as resultsfile:
    T=resultsfile.read()

with open ("W.csv", "r") as resultsfile:
    W=resultsfile.read()

with open ("Y.csv", "r") as resultsfile:
    Y=resultsfile.read()

with open ("V.csv", "r") as resultsfile:
    V=resultsfile.read()



#Now we can print all these files into one big file
master_table = open("master_AA_freq.csv", "wb")
master_table.write("A\n%s\n\n\nR\n%s\n\n\nN\n%s\n\n\nD\n%s\n\n\nB\n%s\n\n\nC\n%s\n\n\nE\n%s\n\n\nQ\n%s\n\n\nZ\n%s\n\n\nG\n%s\n\n\nH\n%s\n\n\nI\n%s\n\n\nL\n%s\n\n\nK\n%s\n\n\nM\n%s\n\n\nF\n%s\n\n\nP\n%s\n\n\nS\n%s\n\n\nT\n%s\n\n\nW\n%s\n\n\nY\n%s\n\n\nV\n%s\n\n\n" % (A, R, N, D, B, C, E, Q, Z, G, H, I, L, K, M, F, P, S, T, W, Y, V))
