#!/usr/bin/python3

import sys
from tymon.parser import *
from tymon.french_parser import *
from tymon.english_parser import *


def parse_word(argv):
    options = ["--fr", "--en"]
    
    if argv[1] in options:
        try:
            if argv[1] == "--fr":
                lang = "fr"
            elif argv[1] == "--en":
                lang = "en"
            word = argv[2]
        except:
            print(usage)
    else:
        word = argv[1]
        lang = "fr"
    return (word, lang)


def usage():
    print("usage : tymon [--en|--fr] <word>\n")
    exit(1)


def main():
    if len(sys.argv) < 2:
        usage()

    word, lang = parse_word(sys.argv)
    if lang == "fr":
        parser = FrenchEtymologyParser()
    elif lang == "en":
        parser = EnglishEtymologyParser()
    else:
        print("Unknown language")
        usage()
    try :
        parsed_html = parser.get_parsed_html(word)
        h3_etym = parser.get_etymology_h3(parsed_html)
        etym_sections = parser.get_etymological_sections(h3_etym)
        parser.pretty_print(etym_sections)
    except AssertionError as e:
        parser.print_not_found(word)


if __name__ == "__main__":
    main()
