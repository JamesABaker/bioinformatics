# WARNING
# Not secure against maliciously constructed data. If you need to parse
# untrusted or unauthenticated data see XML vulnerabilities.

#!/usr/bin/python

import xml.sax

#This OOP has a lot of oopsies, and alothough it LOOKs like the order is wrong, trust me, it won't work any other way without a lot of work...


class DataHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.CurrentData = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "pdbtm":
            id = attributes["ID"]
            print "\n\n\n*******", "New ID:", id, "*******\n"

        elif tag == "CHAIN":
            TM_type = attributes["TYPE"]
            if "alpha" in TM_type:
                print "TM alpha helix recorded in chain"
            elif "beta" in TM_type:
                print "B barrel TM structure recorded in chain"

        elif tag == "REGION":
            TM_region_type = attributes["type"]
            if "H" in TM_region_type:
                print "TM alpha helix recorded in chain"
                seq_beg=attributes["seq_beg"]
                seq_end=attributes["seq_end"]
                print seq_beg
                print seq_end
            else:
                pass


    # Call when an elements ends
    def endElement(self, content):
        if self.CurrentData == "SEQ":
            print "End of chain.\n"

        self.CurrentData = ""

    # Call when a character is read
    def characters(self, tag):
        if self.CurrentData == "SEQ":
            self.SEQ = tag
            sequence = str(self.SEQ)
            sequence = sequence.translate(None, ' ')
            sequence = sequence.translate(None, '\n')

#Many of the sequence entries are empy, here we ignore the empty sequences.
            if not sequence:
                pass
            else:
                print "Chain sequence:",sequence
            # print self.SEQ
       #  elif self.CurrentData == "REGION":
       #     self.REGION = content


if (__name__ == "__main__"):

    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = DataHandler()
    parser.setContentHandler(Handler)

    parser.parse("PDBTM_15Oct2015.xml")
