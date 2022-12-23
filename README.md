# Tymon
Wiktionary etymology extractor for French and English words.

## Introduction
Tymon is a language tool which make HTTP request to Wiktionary and extract the etymology of a specified word. Every word with an etymology section in a Wiktionary page can be requested through Tymon.  

The name Tymon comes from 'etymon' which refers to a morpheme (linguistic unit) from which a  word is derived.

## Usage
As a French tool, the default behavior is searching inside the French Wiktionary (Wikitionnaire).  

Command to get the etymology of the word \<word\>,  
- in French :  
`tymon <word>`  
or  
`tymon --fr <word>`  

- in English :  
`tymon --en <word>`  
