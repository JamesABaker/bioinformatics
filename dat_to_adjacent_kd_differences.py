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
import os
from Bio import SeqIO
import numpy

# Here the user has there own list and we want to save this as interaction too.
filename = str(sys.argv[1])
