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

 echo "Preparing to sort proteins into seperate fastas by number of TMDs."

echo "Type the name and extension of your input file for example whales.dat or input.fasta, followed by [ENTER]:"
echo
read INPUT
echo

cp input/$INPUT input.fasta

    #Runs FETCH script
mv scripts/TMDcounter.py TMDcounter.py
echo
python TMDcounter.py
echo
mv TMDcounter.py scripts/TMDcounter.py

    #Logs and results put away neatly...
echo
echo Putting the results neatly away. Your uniprot.dat file is in output/$DATE
echo


mv input.fasta logs/$DATE/$INPUT_used.fasta
mv single.fasta output/$DATE/single_pass.fasta
mv multi.fasta output/$DATE/mutli_pass.fasta
