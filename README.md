# FYP

Requires two files to run. One file in which the name and votes of a party are on separate lines.
  For example:
    Conservatives
    365
    Labour
    202
    etc...
The other file should contain the proababilities of each party siding with another, this can be calculated using the calc_probs.py file. For that you will need two files - one containing the % that each party
votes in a certain direction, the other containing 1 minus that %.

Upon first initalisation run ./setup.sh to install all libraries needed - setup.sh will also run the example scenario below to ensure that everything has been installed correctly.
To run the program:
python3 main.py <parties_and_votes.txt> <probabilities.txt> <num_parties> <target_needed>

	For example:
		python3 main.py UK2017_votes UK2017_probs 9 326
