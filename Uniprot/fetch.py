#Not all of these are needed, but they are so quick to import it doesn't matter too much.
import os
import os.path
import re
import fileinput
import sys
import urllib,urllib2
import subprocess
import shutil


#This question allows the user to pick to query, or to use their own list.
own_list = raw_input('Do you have a list already that you want to use? Enter y/n. \n')


if 'n' in str(own_list):


    #Here is how the search term is defined. It is pasted exactly as is into a url query of uniprot so there is strict syntax. This needs to be addressed in the documentation.

    searchterm = raw_input('What is your search term. Do not use spaces or multiple queries unless you are comfortable with the uniprot query syntax. \n \n \n')

    print "\n \n \n", "Querying uniprot. This could take a long time..."

    url = 'http://www.uniprot.org/uniprot/?query=%s&format=tab&compress=no&columns=id' % (searchterm)
    print 'Fetching from ', url
    urllib.urlretrieve(url, filename='uniprot_list.txt')
    #A list now exists of a bunch of uniprot IDs each on a new line.

    #This reads the list just to show the user some hits exist.
    f = open('uniprot_list.txt','r')
    print "The search revealed the following IDs:\n", (f.read(300)), "... \n", "et cetera... \n"
    with open('uniprot_list.txt') as file1list:
        interaction = file1list.readlines()
        interaction = list(interaction)
        if interaction[0] == "Entry":
            print "The first ID was 'Entry' which is going to cause problems. Tidying up..."
            interaction.pop(0) #The first line always reads "entry". This causes problems later on so its simpler to just remove this.

        else:
            print "Check first entry of list..."

#Here the user has there own list and we want to save this as interaction too.
elif 'y' in str(own_list):
    print "Please make sure that the list is saved in the input folder."
    list_name = raw_input("What is the name of your list?\nInclude the file extension.\n\n")
    with open('input/%s' % list_name) as custom_list:
        custom_list = custom_list.readlines()
        interaction = list(custom_list)

interaction = interaction

#In the next part of the script, each line of the script is iteratively read and the url is requested from uniprot to download as a text file. The text file recieved is then appended to a local file.

for i in interaction: #Begins the iteration
    i = i.translate(None, '\n') #Removes the spaces between lines. This was causing some really weird bugs and cutting the url below in half.
    urllib.urlretrieve('http://www.uniprot.org/uniprot/%s.txt' % i, filename='uniget.dat') #This uses the ID (saved as i) in a file called uniget.dat.
    #this_number = interaction.index(i)
    #print this_number, " out of ", that_number
    print "Getting %s..." % i
    print "Appending uniprot_list.dat.\n"

    #The individual result held in uniget.dat is saved as lildat, and then added to bigdat.
    with open ("uniget.dat", "r") as lildatfile:
        lildat=lildatfile.read()
    with open('uniprot_list.dat','ab') as bigdat:
        bigdat.write(lildat)
