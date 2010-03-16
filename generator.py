from collections import namedtuple

def generate_madlibs(input_filepath):
    "Takes in a file of madlibs (delimited by an empty line). Assumes '_blank_' fields are designated by curly braces ('{' and '}'), with the field subject contained inside. Example: I feel {Adjictive} today."
    
    input_file = open(input_filepath,"rb")
    
    Madlib = namedtuple("Madlib","madlib, words")
    
    # List of All the madlibs in the file, in the form of 'Madlib' namedtuples
    madlibs = []
    
    madlib = ""
    words = []
    
    for line in input_file.readlines():
        if line.isspace():
            madlibs.append(Madlib(madlib,words))
            madlib = ""
            words = []
        else:
            temp_madlib = line
            for i in xrange(temp_madlib.count("{")):
                left_text = temp_madlib.split("{",1)
                subject, right_text = left_text[1].split("}",1)
                left_text = left_text[0]
                words.append(subject)
                temp_madlib = left_text + "<word>" + right_text
            
            madlib += temp_madlib
    
    input_file.close()
    return madlibs
