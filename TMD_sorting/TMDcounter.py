
#####
##### The list of lists holds the [[title1, seq1], [title2, seq2]]
#####


with open ("input.fasta", "rb") as fastafile:
    data=fastafile.read().replace("'\n", "':::") #this ::: acts as a marker for makign the list of lists
stringA = data
print stringA
stringB = [] #Create an empty list
for line in stringA.split('\n'): # Loop through each line in the original text.  Assumes these are newline line breaks which are represented by \n.
    splitLine = line.split(':::') #Split the pairs on the , into a 2 item list according to the marker
    stringB.append(splitLine) #Append that list to our empty list so thus it will end up with a list of lists.'''
print stringB
seqs = stringB

#Now we have our list in a lit, we can replace the sequence with whatever values we want.

#However we want to create some more lists based on how many duplicates there are.

#Here we add a new entry to each list so it contains the header, the fasta, and a number of how many TMDs are in that protein.
for i, item in enumerate(seqs): #This is disgusting code.
    this_list = seqs[i]
    last_list = seqs[i - 1]
    #next_list = seqs[i + 1]

    this_header = this_list[0]
    last_header = last_list[0]
    #next_header = next_list[0]

    length_of_list = len(this_list)

    if length_of_list == 2:
        this_list.extend([1])
        print "\nThis entry of ", this_header, "does not have a TMD count. Adding now... \n"


    if this_header[:10] == last_header[:10]: #if the IDs match (the first 10 characters), then we presume a multipass protein.
        print "Huzzah! ", this_header, " matches the previous entry ", last_header, ". Amending the TMD count.\n"
        #This isn't a great way of counting since it maxes out at 2. Perhaps looping the script 10 times.
        this_list[2] += 1
        TMDcount = this_list[2]
        last_list[2] = TMDcount
    else:
        print this_header, "looks like a single pass transmembrane protein. The TMD count will be left at one."

print seqs

#Now that each fasta entry is tagged with a TMD count we can sort them into different lists.


for i in seqs:
    #This goes through the list and splits the items into different text files based on their TMD count.

    if i[2] == 1:
        print i[0][:10], " looks like a single pass protein."
        with open ("single.fasta", "ab") as single_fasta_file:
            single_fasta_file.write(i[0])
            single_fasta_file.write("\n")
            single_fasta_file.write(i[1])
            single_fasta_file.write("\n")
    elif i[2] == 2:
        print i[0][:10], " looks like a multi pass protein."
        with open ("multi.fasta", "ab") as single_fasta_file:
            single_fasta_file.write(i[0])
            single_fasta_file.write("\n")
            single_fasta_file.write(i[1])
            single_fasta_file.write("\n")

    else:
        "Something went wrong, no IDs could be counted."

print "DONE"

