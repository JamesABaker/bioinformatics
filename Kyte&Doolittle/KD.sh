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
echo Running KD calculations...
        #Complete KDcalc


echo
echo Preparing files for KD...
echo

    #Moving the script to the working dir
mv scripts/hydropathy.py hydropathy.py
mv scripts/KD_calc.pl KD_calc.pl

    #Preparing for calculation
cp input/$INPUT input.fasta

    #Running the script
python hydropathy.py

    #Moving everything to the correct place
echo
echo Tidying up files.
echo

    #moving scripts back
mv KD_calc.pl scripts/KD_calc.pl
mv hydropathy.py scripts/hydropathy.py
mv result.txt output/$DATE/KD.txt
mv KD_calc_in.txt output/$DATE/logs/KD_in.txt
mv KDcalc_out.txt output/$DATE/logs/KD_out.txt
mv input.fasta output/$DATE/logs/$INPUT
