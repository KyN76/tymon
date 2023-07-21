#!/usr/bin/python3

import sys
from tymon.parser import *
from tymon.french_parser import *


def pretty_print(etym_sections):
    assert len(etym_sections) > 0, "Pas de section étymologique"
    if len(etym_sections) == 1:
        text = etym_sections[0].text
        print("\n" + text)
    
    else:
        for i,section in enumerate(etym_sections):
            print(f"\n== {i+1} ==")
            text = etym_sections[i].text
            print(text)
    print("")


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
    
    try :
        parser = FrenchEtymologyParser()
        parsed_html = parser.get_parsed_html(word)
        h3_etym = parser.get_etymology_h3(parsed_html)
        etym_sections = parser.get_etymological_sections(h3_etym)
        pretty_print(etym_sections)
    except AssertionError as e:
        print(f"\nPas de section étymologique pour le mot {word}.\n")

if __name__ == "__main__":
    main()
