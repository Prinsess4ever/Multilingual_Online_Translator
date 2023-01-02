import sys
from pathlib import Path

import requests

from bs4 import BeautifulSoup

[x.unlink() for x in Path.cwd().glob('*.txt')]

def translation(how_many_times, full_word):
    write_en_print(word, f"\n\n{full_word.title()} Translations:")

    for i, text1 in enumerate(soup.select("span.display-term")):
        if i+1 == how_many_times:
            break

        write_en_print(word, text1.text)

    write_en_print(word, f"\n{full_word.title()} Examples:")

    text1 = soup.select("div.src")
    text2 = soup.select("div.trg")

    for i in range(how_many_times):
        zin1 = text1[i].text.strip()
        zin2 = text2[i].text.strip()

        if zin1 and zin2:
            write_en_print(word, zin1 + ":")
            write_en_print(word, zin2 + "\n")

def write_en_print(word, message):
    message += "\n"

    with open(f"{word}.txt", "a", encoding='utf8') as f:
        f.write(message)
    print(message, end='')

dict_language = {"1": "arabic", "2": "german", "3": "english", "4": "spanish", "5": "french", "6": "hebrew", "7": "japanese", "8": "dutch", "9": "polish", "10": "portuguese", "11": "romanian", "12": "russian", "13": "turkish"}

print("Hello, welcome to the translator. Translator supports:")
for number, language in dict_language.items():
    print(f"{number}. {language.title()}")


original_language = input("Type the number of your language: \n")
translation_language = input("Type the number of a language you want to translate to or '0' to translate to all languages:\n")
word = input("Type the word you want to translate:\n")

headers = {'User-Agent': 'Mozilla/5.0'}
original_language = dict_language[original_language]

if translation_language != '0':
    r = requests.get(f"https://context.reverso.net/translation/{original_language}-{dict_language[translation_language]}/{word}", headers=headers)
    if not r:
        sys.exit(0)
    soup = BeautifulSoup(r.content, 'html.parser')

    translation(5, dict_language[translation_language])

else:
    for number, language in dict_language.items():
        r = requests.get(f"https://context.reverso.net/translation/{original_language}-{language}/{word}", headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        if language == original_language:
            continue

        translation(2, language)