#TMD bioinformatic scripts

This project is made up of a bundle of scripts that aims to study transmembrane sequence data. There are several pipelines that can be easily used.


###Getting started | Requirements.

The scripts require `python`, `python3`, `perl`, and `Biopython` to work fully.

Do not try and run simultaneous instances of these scripts as this will probably cause files to be lost and mishmashed together.

Hopefully you have a copy of python installed already. If not, head [here](https://www.python.org/downloads/) to download python. Currently the Python of the project is written in Python2 which is still the most supported and widely used version. There is a stub of a branch in GitHub that has the same scripts written in python3 however they are too buggy to currently be used.

####Installing Biopython:

Whilst python and perl are readily available witha  quick google, Biopython is a bit less common. After you have installed python,

 - Open a terminal.
 - Run the following commands:

 	`sudo easy_install pip`

 	`sudo pip install numpy`

	`sudo pip install Biopython`

  `sudo python3 -m pip install Biopython`

If you come across any errors it is probably because python is not installed in the default locations, or a package has already been installed before you did these commands. Type in the above commands one after the other regardless and then try running the TMD function.
