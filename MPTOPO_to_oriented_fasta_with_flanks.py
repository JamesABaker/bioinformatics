from xml.dom.minidom import parse, parseString

dom = parse('MPTOPO.xml')

proteins_in_xml = dom.getElementsByTagName('mptopoProtein')

print "There are ", len(proteins_in_xml), " proteins in the dataset."

for proteins in proteins_in_xml:  # visit every node <bar />
    #Get Name
    print "\n"


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
        print "N terminal starts ", io ,"side."

    #TMH counter
    TMH_number = 0 #This number counts how many TMHs there have been in the protein. If the number is odd or even, and if the io is N->C or not determines if the final sequence is reversed.



    #Parse start and stop
    start_locations=proteins.getElementsByTagName('beginIndex')
    start_location_list = []
    for start in start_locations:
        start_location = start.childNodes[0].nodeValue
        start_location_list.append(start_location)
        TMH_number=TMH_number + 1
    print "TMH count:", TMH_number

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
    for i in start_and_end_locations:
        print "start:", i[0]
        print "end:", i[1]
        if "out" in io:
            if (TMH_number % 2 == 0): #even
                print "Reversed TMH", N_to_C_sequence[int(i[0])+1:int(i[1])+1][::-1]
            else: #odd
                print N_to_C_sequence[int(i[0])+1:int(i[1])+1] #+1 because python counts from 0 not 1. Flank length should be taken into account here.
        if "in" in io:
            if (TMH_number % 2 == 0): #even
                print N_to_C_sequence[int(i[0])+1:int(i[1])+1] #+1 because python counts from 0 not 1. Flank length should be taken into account here.
            else: #odd
                print "Reversed TMH", N_to_C_sequence[int(i[0])+1:int(i[1])+1][::-1]
    print N_to_C_sequence
