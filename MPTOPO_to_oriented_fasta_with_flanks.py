from xml.dom.minidom import parse, parseString
import itertools

dom = parse('MPTOPO.xml')

proteins_in_xml = dom.getElementsByTagName('mptopoProtein')

singlepass = 0
multipass = 0

long_tmh = 0
short_tmh = 0
total_tmhs = 0

list_of_singlepass_sequences = []
list_of_multipass_sequences = []

for proteins in proteins_in_xml:  # visit every node <bar />
    #Get Name
    print"\n"


    names=proteins.getElementsByTagName('proteinName')
    for name in names:
        this_name = name.childNodes[0].nodeValue
        print this_name

    #Parse sequence
    sequences=proteins.getElementsByTagName('sequence')
    for sequence in sequences:
        N_to_C_sequence = sequence.childNodes[0].nodeValue
        #print N_to_C_sequence


    #N to C or C to N?
    insideoroutside=proteins.getElementsByTagName('nTerminal')
    for ioro in insideoroutside:
        io = ioro.childNodes[0].nodeValue
        print"N terminal starts", io ,"side."

    #TMH counter
    TMH_number = 0 #This number counts how many TMHs there have been in the protein. If the number is odd or even, and if the io is N->C or not determines if the final sequence is reversed.



    #Parse start and stop
    start_locations=proteins.getElementsByTagName('beginIndex')
    start_location_list = []
    for start in start_locations:
        start_location = start.childNodes[0].nodeValue
        start_location_list.append(start_location)
        TMH_number=TMH_number + 1
    print"There are", TMH_number,"transmembrane regions in this protein."

    end_locations=proteins.getElementsByTagName('endIndex')
    end_location_list=[]
    for end in end_locations:
        end_location = end.childNodes[0].nodeValue
        end_location_list.append(end_location)

    start_and_end_locations = []

    for number, location in enumerate(start_location_list):
        start_and_stop_of_this_TMH=[]
        start_and_stop_of_this_TMH.append(start_location_list[int(number)])
        start_and_stop_of_this_TMH.append(end_location_list[int(number)])
        start_and_end_locations.append(start_and_stop_of_this_TMH)


    # Slicing the sequence of each TMH
    TMHs_counted_so_far=0

    tmh_in_this_protein=[]

    for i in start_and_end_locations:
        print"start:", i[0]
        print"end:", i[1]

        tmh_correct_length = True


        if len(N_to_C_sequence[int(i[0])+1:int(i[1])+1]) > 38:
            long_tmh = long_tmh + 1
            tmh_correct_length = False



        if len(N_to_C_sequence[int(i[0])+1:int(i[1])+1]) < 17:
            short_tmh = short_tmh +1
            tmh_correct_length = False


        #Currently TMH_number is only holding the final total, not the running total.

        if tmh_correct_length == True:
            if"out" in io:
                if (TMHs_counted_so_far % 2 == 0): #even
                    oriented_tmh_sequence = N_to_C_sequence[int(i[0])+1:int(i[1])+1]
                else: #odd
                    oriented_tmh_sequence = N_to_C_sequence[int(i[0])+1:int(i[1])+1][::-1] #+1 because python counts from 0 not 1. Flank length should be taken into account here.
            elif"in" in io:
                if (TMHs_counted_so_far % 2 == 0): #even
                    oriented_tmh_sequence = N_to_C_sequence[int(i[0])+1:int(i[1])+1][::-1] #+1 because python counts from 0 not 1. Flank length should be taken into account here.
                else: #odd
                    oriented_tmh_sequence = N_to_C_sequence[int(i[0])+1:int(i[1])+1]

            print "Oriented TMH sequence:", oriented_tmh_sequence

            tmh_in_this_protein.append(oriented_tmh_sequence)

        elif tmh_correct_length == False:
            print"This transmembrane helix is outside the length parameters."
            print"Sequence N to C:", N_to_C_sequence[int(i[0])+1:int(i[1])+1]

        TMHs_counted_so_far = TMHs_counted_so_far + 1
        total_tmhs = total_tmhs + 1


    print"Complete Sequence:", N_to_C_sequence

    #Counting multi vs single pass
    if TMH_number == 1:
        singlepass = singlepass + 1
        list_of_singlepass_sequences.append(tmh_in_this_protein)

    if TMH_number > 1:
        multipass = multipass + 1
        list_of_multipass_sequences.append(tmh_in_this_protein)

#Flattens the multipass list of lists
list_of_multipass_sequences = list(itertools.chain(*list_of_multipass_sequences))
list_of_singlepass_sequences = list(itertools.chain(*list_of_singlepass_sequences))


print "\nMulti-pass sequences:\n"
for i in list_of_multipass_sequences:
    print "Sequence:", i
print "\nSingle-pass sequences:\n"
for i in list_of_singlepass_sequences:
    print "Sequence:", i


#Log
print"\n\nAt the time of download there are 165 proteins in the MPTOPO database. In this alpha transmembrane file there are",len(proteins_in_xml)," proteins."
print"Of those proteins there are", multipass,"multi-pass proteins and", singlepass,"single-pass proteins."
print"There are", total_tmhs,"transmembrane helices in those proteins."
print"There are", long_tmh,"transmembrane helices greater than 38 residues and", short_tmh,"transmembrane helices shorter than 17 residues."
print "After removing these from the dataset there are ",  int(len(list_of_multipass_sequences)+len(list_of_singlepass_sequences)) , ".", len(list_of_multipass_sequences), "helices are from multipass proteins and", len(list_of_singlepass_sequences), " helices are from singlepass proteins."
