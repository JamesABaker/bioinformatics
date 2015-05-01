#!/bin/bash

#
# -- SGE options :
#

#$ -S /bin/bash
#$ -cwd
#$ -q

#
# -- the commands to be executed (programs to be run) :
#
# remember to run `qrsh -l inter -l short twoday` before running on the cluster!!!! And this will only last for two days.

export HTTP_PROXY=http://webproxy.its.manchester.ac.uk:3128

export http_proxy=http://webproxy.its.manchester.ac.uk:3128

python fetch.py