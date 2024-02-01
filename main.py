#!/usr/bin/python3

from tymon.parser import *
from tymon.french_parser import *
from tymon.english_parser import *
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Wiktionary etymology extractor for French and English words.',
    )
    parser.add_argument("word", help="Word to extract etymology")
    parser.add_argument("--fr", dest="language", action="store_const", const="fr", help="Extract French etymology")
    parser.add_argument("--en", dest="language", action="store_const", const="en", help="Extract English etymology")
    args = parser.parse_args()

    if args.language == "fr" or args.language is None:
        etymology_parser = FrenchEtymologyParser()
    elif args.language == "en":
        etymology_parser = EnglishEtymologyParser()

    try :
        parsed_html = etymology_parser.get_parsed_html(args.word)
        h3_etym = etymology_parser.get_etymology_h3(parsed_html)
        etym_sections = etymology_parser.get_etymological_sections(h3_etym)
        etymology_parser.pretty_print(etym_sections)
    except AssertionError as e:
        etymology_parser.print_not_found(args.word)


if __name__ == "__main__":
    main()
