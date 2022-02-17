# FYP

Requires two files to run. One file in which the name and votes of a party are on separate lines.
  For example:
    Conservatives
    365
    Labour
    202
    etc...
The other file should contain the proababilities of each party siding with another. This can be calculated using the calc_probs.py file.

To run the program, run the main.py file and enter the appropriate information
The number of parties inputted will determine the number of parties used from the party file provided.
  For example:
    If using the United States, and the number of parties enetered is 17, the program will use the first 17 parties it encounters in the file in which party names and votes were given rather than using all 51.
