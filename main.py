#!/usr/bin/python3

import sys
import pycurl
import certifi
import urllib.parse
from bs4 import BeautifulSoup
from io import BytesIO

def get_parsed_html(word:str, lang:str):
    word = html_format_word(word)
    request = "https://" + lang + ".wiktionary.org/wiki/" + word

    # Creating a buffer as the cURL is not allocating a buffer for the network response
    buffer = BytesIO()
    c = pycurl.Curl()
    #initializing the request URL
    c.setopt(c.URL, request.encode('iso-8859-1'))
    #setting options for cURL transfer  
    c.setopt(c.WRITEDATA, buffer)
    #setting the file name holding the certificates
    c.setopt(c.CAINFO, certifi.where())
    # perform file transfer
    c.perform()
    #Ending the session and freeing the resources
    c.close()
    body = buffer.getvalue()
    #decoding the buffer 
    html = body.decode('utf-8')
    return BeautifulSoup(html, 'html.parser')

def html_format_word(word:str):
    res = urllib.parse.quote(word.encode('utf-8'))
    return res

def get_etymology_h3(parsed_html, lang:str):
    h3s = parsed_html.find_all("h3")
    for h3 in h3s:
        if is_etymological_h3(h3, lang):
            return h3
    raise(AssertionError("Pas de section étymologique"))


def is_etymological_h3(h3, lang)->bool:
    for desc in h3.descendants:
        try:
            if is_etymological_descendant(desc, lang):
                return h3
        except:
            continue
    return False

def is_etymological_descendant(desc, lang)->bool:
    if lang == "fr":
        if desc.has_attr("class"):
            return "titreetym" in desc["class"]
    elif lang == "en":
        if desc.has_attr("id"):
            return "Etymology" in desc["id"]


def get_etymological_sections(h3_etym):
    etym_sections = []
    for ns in h3_etym.next_siblings:
        if ns.name == "h3":
            break
        elif ns.text.strip() != "":
            etym_sections.append(ns)
    return etym_sections


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

def extract_word(argv):
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

    word, lang = extract_word(sys.argv)
    
    try :
        parsed_html = get_parsed_html(word, lang)
        h3_etym = get_etymology_h3(parsed_html, lang)
        etym_sections = get_etymological_sections(h3_etym)
        pretty_print(etym_sections)
    except AssertionError as e:
        print(f"\nPas de section étymologique pour le mot {word}.\n")

if __name__ == "__main__":
    main()
