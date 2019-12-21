import sys
import spacy
import logging
import re

#txt input file
if len(sys.argv) == 1:
    logging.error("No input file specified")
elif len(sys.argv) > 2:
    logging.error("More than one argument given. Please give me only one file path: ")
    filepath = input()
    if re.search(r'\s', filepath):
        logging.error("Stop trolling me, no whitespace allowed. I'm giving up on you now.")
else:
    filepath = sys.argv[1]
    if not path.exists(filepath):
		print("Input file \"{}\" does not exist! Please check that you specified the path correctly".format(filepath))
	else:
        with open(filepath, 'r') as input_file:
            parse_file()

def parse_file(input_file):
    

