# Tymon
Wiktionary etymology extractor for French and English words.

## Introduction
Tymon is a language tool which make HTTP request to Wiktionary and extract the etymology of a specified word. Every word with an etymology section in a Wiktionary page can be requested through Tymon.  

The name Tymon comes from 'etymon' which refers to a morpheme (linguistic unit) from which a  word is derived.

## Installation
- Clone / download this repository
- Set a line like this in your .bashrc / .zshrc or other :
```
alias tymon='python3 <path_to_the_cloned_repository>/tymon/main.py'
```
- Reexecute the content of your .bashr / .zshrc / ... file, by opening another terminal or the command `source <file>`.

## Usage
As it was written for French words in the first place, the default behavior (without option) is searching inside the French Wiktionary (Wikitionnaire).  
Command line options allow to search in the specified available languages.  

To get the etymology of the word \<word\>,  
- in French :  
`tymon <word>`  
or  
`tymon --fr <word>`  

- in English :  
`tymon --en <word>`  
