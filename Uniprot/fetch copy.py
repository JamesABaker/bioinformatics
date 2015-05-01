#Not all of these are needed, but they are so quick to import it doesn't matter too much.
import fileinput
import urllib,urllib2

print "\n \n \n", "Querying uniprot. This could take a long time..."

url = 'http://www.uniprot.org/uniprot/?query=transmem&format=tab&compress=no&columns=id'
print 'Fetching from ', url
urllib.urlretrieve(url, filename='uniprot_list.txt')
    #A list now exists of a bunch of uniprot IDs each on a new line.

    #This reads the list just to show the user some hits exist.
f = open('uniprot_list.txt','r')
print "The search revealed the following IDs:\n", (f.read()), "... \n"
with open('uniprot_list.txt') as file1list:
    interaction = file1list.readlines()
    interaction = list(interaction)
    if interaction[0] == "Entry":
        print "The first ID was 'Entry' which is going to cause problems. Tidying up..."
        interaction.pop(0) #The first line always reads "entry". This causes problems later on so its simpler to just remove this.
            
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