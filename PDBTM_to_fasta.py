# WARNING
# Not secure against maliciously constructed data. If you need to parse
# untrusted or unauthenticated data see XML vulnerabilities.

#!/usr/bin/python

import xml.sax


class DataHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.CurrentData = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "pdbtm":
            id = attributes["ID"]
            print "\n\n\n*******", "New ID:", id, "*******\n"

    # Call when an elements ends
    def endElement(self, content):
        if self.CurrentData == "SEQ":
            print "End of sequence:"

        self.CurrentData = ""

    # Call when a character is read
    def characters(self, tag):
        if self.CurrentData == "SEQ":
            self.SEQ = tag
            sequence = str(self.SEQ)
            sequence = sequence.translate(None, ' ')
            sequence = sequence.translate(None, '\n')
            print "Sequence:"
            print sequence
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
