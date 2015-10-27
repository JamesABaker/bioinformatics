# WARNING
# Not secure against maliciously constructed data. If you need to parse
# untrusted or unauthenticated data see XML vulnerabilities.

#!/usr/bin/python


# ISSUES

# Super bored of this now. The other thing is that the last record
# doesn't seem to report as "ending" although the xml file looks fine to
# be honest!

import xml.sax
from sys import argv

# This OOP has a lot of oopsies, and alothough it LOOKs like the order is
# wrong, trust me, it won't work any other way without a lot of work...


class DataHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.CurrentData = ""

    # Call when an element starts
    def startElement(self, tag, attributes):

        global Chain_ID
        global sequence
        global Position_of_helix_coodinates

        self.CurrentData = tag
        if tag == "pdbtm":
            id = attributes["ID"]
            print("\n\n\n*******", "New ID:", id, "*******\n")


        elif tag == "CHAIN":
            TM_type = attributes["TYPE"]
            Chain_ID = attributes["CHAINID"]

        elif tag == "REGION":
            TM_region_type = attributes["type"]
            if "H" in TM_region_type:
                seq_beg = attributes["seq_beg"]
                seq_end = attributes["seq_end"]
                print("This is a sequence string", sequence)

            else:
                pass

    # Call when an elements ends
    def endElement(self, content):

        global sequence
        global Chain_ID
        global Position_of_helix_coodinates

        if self.CurrentData == "SEQ":
            print(Chain_ID)

        elif self.CurrentData == "pdbtm":
            print("Finished with that ID.")

        self.CurrentData = ""

    # Call when a character is read
    def characters(self, tag):

        global sequence
        global Chain_ID
        global Position_of_helix_coodinates

        if self.CurrentData == "SEQ":
            sequence = "No sequence held."
            self.SEQ = tag
            sequence = str(self.SEQ)
            sequence = sequence.replace(' ', '')
            # There is still a fecking annoying line break here.
            sequence = sequence.replace('\n', '')

            # This one prints for some reason. THe other one doesnt...
            print(sequence)


# Many of the sequence entries are empy, here we ignore the empty sequences.

if (__name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = DataHandler()
    parser.setContentHandler(Handler)

    parser.parse("PDBTM_15Oct2015original.xml")
