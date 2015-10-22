# WARNING
# Not secure against maliciously constructed data. If you need to parse
# untrusted or unauthenticated data see XML vulnerabilities.

#!/usr/bin/python




######ISSUES

#Super bored of this ow. There are issues though, output generates several times more recordsfor the sequence positions than it should. GOOD LUCK WITH THAT ONE FUTURE ME. Probably an indentation error somewhere. The other thing is that the last record doesn't seem to report as "ending" although the xml file looks fine to be honest!







import xml.sax
from sys import argv

#This OOP has a lot of oopsies, and alothough it LOOKs like the order is wrong, trust me, it won't work any other way without a lot of work...

File = open('Header.txt', 'a+')

Header = []
Sequence = []


class DataHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.CurrentData = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        global Header
        global Sequence

        self.CurrentData = tag
        if tag == "pdbtm":
            print Header
            #EMPTY OLD Variables
            Header = []
            Sequence = []

            id = attributes["ID"]
            print "\n\n\n*******", "New ID:", id, "*******\n"
            id_for_header = str(id)
            Header.append(">%s: " %id_for_header)
            #print Header

        elif tag == "CHAIN":
            TM_type = attributes["TYPE"]
            if "alpha" in TM_type:
                print "\nTM alpha helix recorded in chain"
            #elif "beta" in TM_type:
                #print "B barrel TM structure recorded in chain"
            else:
                pass

        elif tag == "REGION":
            TM_region_type = attributes["type"]
            if "H" in TM_region_type:
                seq_beg=attributes["seq_beg"]
                seq_end=attributes["seq_end"]
                print "Helix begins at position", seq_beg, "and ends at position", seq_end
                seq_beg_number = str(seq_beg)
                seq_end_number = str(seq_end)
                sequence_list_for_numbers_in_this_helix = []
                sequence_list_for_numbers_in_this_helix.append(seq_beg_number)
                sequence_list_for_numbers_in_this_helix.append(seq_end_number)
                Header.append(sequence_list_for_numbers_in_this_helix)
            else:
                pass


    # Call when an elements ends
    def endElement(self, content):
        global Header
        global Sequence
        if self.CurrentData == "SEQ":
            print "End of chain.\n"
        elif self.CurrentData == "pdbtm":
            print Header


        self.CurrentData = ""

    # Call when a character is read
    def characters(self, tag):
        global Header
        global Sequence
        if self.CurrentData == "SEQ":
            self.SEQ = tag
            sequence = str(self.SEQ)
            sequence = sequence.translate(None, ' ')
            sequence = sequence.translate(None, '\n')


#Many of the sequence entries are empy, here we ignore the empty sequences.
            if not sequence:
                pass
            else:
                print sequence
            # print self.SEQ
       #  elif self.CurrentData == "REGION":
       #     self.REGION = content


if (__name__ == "__main__"):
    Header =[]
    Sequence = []
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = DataHandler()
    parser.setContentHandler(Handler)

    parser.parse("PDBTM_15Oct2015original.xml")
