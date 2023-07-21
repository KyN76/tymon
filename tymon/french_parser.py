from tymon.parser import *

class FrenchEtymologyParser(EtymologyParser):

    def get_wiki_base_url(self):
        return "https://fr.wiktionary.org/wiki/"
    

    def is_etymological_descendant(self, desc)->bool:
        if desc.has_attr("class"):
            return "titreetym" in desc["class"]
        else:
            return False
        
    
    def get_etymological_sections(self, h3_etym):
        etym_sections = []
        for ns in h3_etym.next_siblings:
            if ns.name == "h3":
                break
            elif ns.text.strip() != "":
                etym_sections.append(ns)
        return etym_sections