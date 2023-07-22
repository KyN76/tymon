from tymon.parser import *

class EnglishEtymologyParser(EtymologyParser):

    def get_wiki_base_url(self):
        return "https://en.wiktionary.org/wiki/"
    

    def is_etymological_descendant(self, desc)->bool:
        if desc.has_attr("id"):
            return "Etymology" in desc["id"]
        else:
            return False
        
    
    def get_etymological_sections(self, h3_etym):
        etym_sections = []
        for ns in h3_etym.next_siblings:
            if ns.name in ["h3", "h4"]:
                break
            elif ns.name == "p" and ns.text.strip() != "":
                etym_sections.append(ns)
        return etym_sections
    

    def print_not_found(self, word:str):
        print(f"\nNo etymological section for the word {word}.\n")