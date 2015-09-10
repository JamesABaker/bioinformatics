#!/bin/bash

#
# -- SGE options :
#

#$ -S /bin/bash
#$ -cwd
#$ -q


################################################
##########       Version 0.1       #############
##########       James Baker       #############
################################################

#
# -- the commands to be executed (programs to be run) :
#
# remember to run `qrsh -l inter -l short` before running on the cluster!!!! Running on the cluster is not advised since this is a somewhat interactive sript and pulls information from different modules and applications.

DATE=$(date +"date:%Y.%m.%d_time:%H:%M:%S")

echo
echo "This script was developed by James A Baker under the supervision of Dr Jim Warwicker."
echo
echo "It requires an active internet connection and an up to date version of biopython."
echo
echo "See readme.md for more information on installation and visit www.github.com/jbkr/TA_predict to report any errors."
sleep 2

echo
echo
echo
echo "What is the name of your input file? (include extension i.e file.dat or file.txt). Do not run this script using a file named 'input.dat'"
echo
echo

read filename

cp $filename input.dat
echo
