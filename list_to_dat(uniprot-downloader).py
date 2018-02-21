# Not all of these are needed, but they are so quick to import it doesn't matter too much.
import os
import os.path
import re
import fileinput
import sys
import urllib
import urllib2
import subprocess
import shutil


# This question allows the user to pick to query, or to use their own list.
own_list = raw_input(
    'Do you have a list already that you want to use? Enter y/n. \n')


if 'n' in str(own_list):

    # Here is how the search term is defined. It is pasted exactly as is into a url query of uniprot so there is strict syntax. This needs to be addressed in the documentation.

    searchterm = raw_input(
        'What is your search term. Do not use spaces or multiple queries unless you are comfortable with the uniprot query syntax. \n \n \n')

    print "\n \n \n", "Querying uniprot. This could take a long time..."

    url = 'http://www.uniprot.org/uniprot/?query=%s&format=tab&compress=no&columns=id' % (
        searchterm)
    print 'Fetching from ', url
    urllib.urlretrieve(url, filename='uniprot_list.txt')
    # A list now exists of a bunch of uniprot IDs each on a new line.

    # This reads the list just to show the user some hits exist.
    f = open('uniprot_list.txt', 'r')
    print "The search revealed the following IDs:\n", (f.read(300)), "... \n", "et cetera... \n"
    with open('uniprot_list.txt') as file1list:
        interaction = file1list.readlines()
        interaction = list(interaction)
        if interaction[0] == "Entry":
            print "The first ID was 'Entry' which is going to cause problems. Tidying up..."
            # The first line always reads "entry". This causes problems later on so its simpler to just remove this.
            interaction.pop(0)

        else:
            print "Check first entry of list..."

# Here the user has there own list and we want to save this as interaction too.
elif 'y' in str(own_list):
    print "Please make sure that the list is saved in the input folder."
    list_name = raw_input(
        "What is the name of your list?\nInclude the file extension.\n\n")
    with open('input/%s' % list_name) as custom_list:
        custom_list = custom_list.readlines()
        interaction = list(custom_list)


# In the next part of the script, each line of the script is iteratively read and the url is requested from uniprot to download as a text file. The text file recieved is then appended to a local file.
failed_download_ids = []

filename='uniget.dat'
f=open(filename, "w")
for n, i in enumerate(interaction):
    # Removes the spaces between lines. This was causing some really weird bugs and cutting the url below in half.
    i = i.translate(None, '\n')
    print "\nGetting %s..., record %s of %s" % (i, str(n+1), str(len(interaction)))
    try:
        # This uses the ID (saved as i) in a file called uniget.dat.
        download = urllib2.urlopen('http://www.uniprot.org/uniprot/%s.txt' % i,  timeout=3)
        content = download.read()
        f.write(content)
        #f.close()
        #this_number = interaction.index(i)
        # print this_number, " out of ", that_number

        print "Appending uniprot_list.dat...\n"

        # The individual result held in uniget.dat is saved as lildat, and then added to bigdat.
        with open("uniget.dat", "r") as lildatfile:
            lildat = lildatfile.read()
        with open('uniprot_list.dat', 'ab') as bigdat:
            bigdat.write(lildat)
        print "%s fetch complete." % i
    except urllib2.URLError, e:
        print "Timeout on record %s\nRetrying download of %s" % (i, i)
        try:
            download = urllib2.urlopen('http://www.uniprot.org/uniprot/%s.txt' % i, timeout=3)

            content = download.read()
            f.write(content)
            #f.close()
            #this_number = interaction.index(i)
            # print this_number, " out of ", that_number

            print "Appending uniprot_list.dat...\n"

            # The individual result held in uniget.dat is saved as lildat, and then added to bigdat.
            with open("uniget.dat", "r") as lildatfile:
                lildat = lildatfile.read()
            with open('uniprot_list.dat', 'ab') as bigdat:
                bigdat.write(lildat)
            print "%s fetch complete." % i
        except urllib2.URLError, e:
            print "Redownload failed. Adding entry to catch-up list that will be downloaded after other entries."
            failed_download_ids.append(str(i))


print "There were %s failed downloads." % len(failed_download_ids)

permanent_failed_records = []
if len(failed_download_ids) > 0:
    print "Retrying downloading failed downloads."
    for i in failed_download_ids:
        try:
            # This uses the ID (saved as i) in a file called uniget.dat.
            download = urllib2.urlopen('http://www.uniprot.org/uniprot/%s.txt' % i,  timeout=3)
            content = download.read()
            f.write(content)
            #f.close()
            #this_number = interaction.index(i)
            # print this_number, " out of ", that_number

            print "Appending uniprot_list.dat...\n"

            # The individual result held in uniget.dat is saved as lildat, and then added to bigdat.
            with open("uniget.dat", "r") as lildatfile:
                lildat = lildatfile.read()
            with open('uniprot_list.dat', 'ab') as bigdat:
                bigdat.write(lildat)
            print "%s fetch complete." % i

        except urllib2.URLError, e:
            print "Timeout on record %s. Abandoning record." % (i)
            permanent_failed_records.append(i)
    if len(permanent_failed_records) > 0:
        print "%s permanently failed:"
        for i in permanent_failed_records:
            print "%s\n" % i
