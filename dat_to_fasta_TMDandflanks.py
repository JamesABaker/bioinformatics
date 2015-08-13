#Converts a .dat or uniprot text file to TMH_and_flanking.fasta


#This requires a working version of Biopython.
from Bio import SeqIO





#These are the variables that are repeatedly used throughout the script. The only one that changes is the output_filename that is changed as the separate fasta sequences are generated.
filenames = ["tail_anchors.dat"]
input_format = "swiss" #This SHOULD work with uniprot filetype
feature_type = "TRANSMEM" #For future modification, this can be used to look for any annotation in the .dat file.
output_filename = "TMH_and_flanking.fasta" #Simply the output name, can be anything as it is written in binary (not file-type specific language).


output = open(output_filename, "w")
for filename in filenames:
    # Using SeqIO.parse will cope with multi-record files
    for record in SeqIO.parse(filename, input_format): #A biopython module that can automatically parse uniprot .txt files
        for f in record.features:
            #feature type refers to TRANSMEM
            if f.type == feature_type:
                #These are the flanking regions and the TMD using record.seq. They are identified by simply counting 5 spaces before and after the TMD is annotated as being.
                print(record.id)
                flank1 = record.seq[(f.location.start-5):(f.location.start)]
                flank2 = record.seq[(f.location.end):(f.location.end+5)]
                TMD = f.extract(record.seq)
                flank1length = len(flank1)
                flank2length = len(flank2)
                #Here we define the ID code and then the start and end positions.
                title_line = "'%s' | TMH: '%i-%i'| N-terminal flank: '%i-%i'| C-terminal flank: '%i-%i'" % (record.id, f.location.start+1, f.location.end, f.location.start-flank1length, f.location.start, f.location.end+1, f.location.end+flank2length+1)

                #This prints the title and then any TRANSMEM regions associated with that entry along with flanking regions.
                output.write(">%s\n%s%s%s\n" % (title_line, flank1, TMD, flank2))

                #if there are any TRANSMEM entries, it prints them. Note that if there is no transmem domain then the ID is skipped, you won't get flanking regions without an identified TMD.
                #Prints the output in the terminal
                print("ID: ", title_line)
                print("N flank: " , flank1)
                print("Trans Membrane Domain: ", f.extract(record.seq))
                print("C flank: " , flank2)
                print("fasta output to file: \n>%s\n%s%s%s\n" % (title_line, flank1, TMD, flank2))


output.close()
