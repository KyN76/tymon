import pycurl
import certifi
import urllib.parse
from bs4 import BeautifulSoup
from io import BytesIO
from abc import abstractmethod


class EtymologyParser:

    def get_parsed_html(self, word:str):
        word = self.html_format_word(word)
        url = self.get_wiki_base_url() + word

        # Creating a buffer as the cURL is not allocating a buffer for the network response
        buffer = BytesIO()
        c = pycurl.Curl()
        #initializing the request URL
        c.setopt(c.URL, url.encode('iso-8859-1'))
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
    

    @abstractmethod
    def get_wiki_base_url(self):
        pass


    def html_format_word(self, word:str):
        res = urllib.parse.quote(word.encode('utf-8'))
        return res

    
    def get_etymology_h3(self, parsed_html):
        h3s = parsed_html.find_all("h3")
        for h3 in h3s:
            if self.is_etymological_h3(h3):
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

    @abstractmethod
    def is_etymological_descendant(self, desc)->bool:
        pass


    @abstractmethod
    def get_etymological_sections(self, h3_etym):
        pass