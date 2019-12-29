import sys
import os
from os import path
import spacy
from benepar.spacy_plugin import BeneparComponent
import logging
import re


def parse_file(file_path: str) -> list:
    def convert_bytes(num):
        """
        this function will convert bytes to MB.... GB... etc
        """
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0

    def get_file_size(file_path):
        """
        this function will return the file size
        """
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)

    file_size = get_file_size(file_path)
    if 'GB' or 'TB' in file_size:
        logging.error("File size is %s. This is too large!" % file_size)
        return []
    else:
        return ["Hello world!"]

    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe(BeneparComponent("benepar_en2"))
    with open(file_path, "r") as f:
        file_data = f.read()
        grammatical_sentences = []






if __name__ == "__main__":
    #txt input file
    if len(sys.argv) == 1:
        logging.error("No input file specified")
    elif len(sys.argv) > 2:
        logging.error("More than one argument given. Please give me only one file path: ")
        file_path = input()
        if re.search(r'\s', file_path):
            logging.error("Stop trolling me, no whitespace allowed. I'm giving up on you now.")
    else:
        file_path = sys.argv[1]
        if not path.exists(file_path):
            logging.error("Input file \"%s\" does not exist! Please check that you specified the path correctly" % file_path)
        else:
            sentence_array = parse_file(file_path)
            if sentence_array is None:
                quit()



