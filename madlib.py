#! /usr/bin/python

# Program: Madlib Generator
# Author: Enrique Gavidia
# E-mail: enrique@enriquegavidia.com
# License: TBD
# Date: 2009-2010

from generator import generate_madlibs
from optparse import OptionParser
from os.path import abspath
import textwrap
#import random

parser = OptionParser()
__opts, input_file = parser.parse_args() 

# Randomly select a madlib
#madlib = random.choice(madlibs)

madlibs = generate_madlibs(abspath(input_file[0]))

num_of_madlibs = str(len(madlibs))
print "There are "+num_of_madlibs+" madlibs in this file."

if not num_of_madlibs is "0":
    choice = raw_input("Please select which one you would like to do (1-"+num_of_madlibs+"): ")
    print
    
    madlib = madlibs[int(choice)]
    words = madlib.words
    madlib = madlib.madlib
    
    word = 0
    # For every blank in the given madlib...
    for i in words:
        # Enter a word for it...
        words[word] = raw_input("Please enter a(n) "+words[word]+": ")
        # And fill it in.
        madlib = madlib.replace('<word>', words[word], 1)
        # Then move on to the next blank.
        word += 1
    
    print
    print "Your Madlib:"
    print textwrap.fill(madlib, width=79)
    print
    
    
