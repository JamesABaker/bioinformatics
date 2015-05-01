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
# remember to run `qrsh -l inter -l short` before running on the cluster!!!!




################################################
################ Version 0.3 ###################
################################################

#The date is used to identify different runs. It is in a bit of a weird format... But it'll do!
DATE=$(date +"date:%Y.%m.%d_time:%H:%M:%S")

echo
echo "TMproject v0.3. Making a new directory for this run..."
echo


#Here the new directories are made regardless of if any hits are recieved or any succesful runs are made. This ensures log files are caught, helps with debugging and any cases where no hits are found.
mkdir ./output/$DATE
mkdir ./output/$DATE/logs

echo "Type the name and extension of your input file for example whales.dat or input.fasta, followed by [ENTER]:"
echo
read INPUT
echo
  #Copies the input file into the working directory.
    #User is prompted to provide $INPUT and this can be anything.
    #All processing scripts should open working_files/input.fasta as binary file.
    #Binary files are imported as is without any format specific packaging meaning a .fasta file could contain anything from an actual fasta to the complete works of shakespeare.

cp input/$INPUT input.fasta

echo
echo Running scripts...
echo

#Functions to carry out
    #Moves the script into the working dir
echo moving scripts...
mv scripts/TMDcatcher.py TMDcatcher.py

    #Calls the script that processes the input file.
echo letting the script to its thing...
python TMDcatcher.py

    #Puts the script back
echo putting the script back...
mv TMDcatcher.py scripts/TMDcatcher.py
    #Any grep etc. should be done now. Logs can be saved in /logs/$DATE.

echo
echo Calculation complete. Tidying files...
echo

#Log handling
    #Logs the results.
mv TMH_only.fasta output/$DATE/TMH_$DATE.fasta
mv TMH_and_flanking.fasta output/$DATE/TMHwithflanks_$DATE.fasta
mv N_flanking.fasta output/$DATE/Nflank_$DATE.fasta
mv C_flanking.fasta output/$DATE/Cflank_$DATE.fasta
mv input.fasta output/$DATE/logs/input.txt

echo
echo Outputs saved in output/$DATE/...
echo
echo Complete TMH and flanking saved at output/$DATE/TMHwithflanks_$DATE.fasta
echo