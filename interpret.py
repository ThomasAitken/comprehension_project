#!/home/crastollgorton/ai-env/bin/python



import sys
sys.path.insert(0, '/home/crastollgorton/comprehension_project')
# sys.path.append('/home/crastollgorton/comprehension_project')
import os
from os import path
import spacy
from benepar.spacy_plugin import BeneparComponent
import logging
import re
from parsing.text_compute import parse_sentences
import pdb
logger = logging.getLogger(__name__)
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
    if re.search(r'[GT]B', file_size):
        logger.error("File size is %s. This is too large!" % file_size)
        return []
    else:
        nlp = spacy.load("en_core_web_lg")
        nlp.add_pipe(BeneparComponent("benepar_en2"))
        f = open(file_path, "r")
        for idx,paragraph in enumerate(filter(lambda line: line != "", map(lambda line: line.strip('\n'), f.readlines()))):
            if idx == 0:
                title = paragraph
                print(title)
                continue
            else:
                doc = nlp(paragraph)
            # grammatical_sentences = list(doc.sents)
            parse_paragraph(doc)


            # print(list(grammatical_sentences[0]))
            # pdb.set_trace()
        f.close()






if __name__ == "__main__":
    #txt input file
    if len(sys.argv) == 1:
        logger.error("No input file specified")
    elif len(sys.argv) > 2:
        logger.error("More than one argument given. Please give me only one file path: ")
        file_path = input()
        if re.search(r'\s', file_path):
            logger.error("Stop trolling me, no whitespace allowed. I'm giving up on you now.")
    else:
        file_path = sys.argv[1]
        if not path.exists(file_path):
            logger.error("Input file \"%s\" does not exist! Please check that you specified the path correctly" % file_path)
        else:
            sentence_array = parse_file(file_path)
            if sentence_array is None:
                quit()



