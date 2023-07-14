import EtymologyParser

class FrenchEtymologyParser(EtymologyParser):

    def get_etymology_h3(self, parsed_html, lang:str):
        h3s = parsed_html.find_all("h3")
        for h3 in h3s:
            if self.is_etymological_h3(h3, lang):
                return h3
        raise(AssertionError("Pas de section étymologique"))


    def is_etymological_h3(self, h3)->bool:
        for desc in h3.descendants:
            try:
                if self.is_etymological_descendant(desc):
                    return h3
            except:
                continue
        return False

    def is_etymological_descendant(self, desc)->bool:
        if desc.has_attr("class"):
            return "titreetym" in desc["class"]


    def get_etymological_sections(self, h3_etym):
        etym_sections = []
        for ns in h3_etym.next_siblings:
            if ns.name == "h3":
                break
            elif ns.text.strip() != "":
                etym_sections.append(ns)
        return etym_sections