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

dict_language = {"0": "all", "1": "arabic", "2": "german", "3": "english", "4": "spanish", "5": "french", "6": "hebrew", "7": "japanese", "8": "dutch", "9": "polish", "10": "portuguese", "11": "romanian", "12": "russian", "13": "turkish"}

original_language = sys.argv[1]
if original_language not in dict_language.values():
    print(f"Sorry, the program doesn't support {original_language}")

    sys.exit(0)

translation_language = sys.argv[2]
if translation_language not in dict_language.values():
    print(f"Sorry, the program doesn't support {translation_language}")

    sys.exit(0)

if translation_language == "all":
    translation_language = "0"

word = sys.argv[3]

headers = {'User-Agent': 'Mozilla/5.0'}
original_language = original_language

if translation_language != '0':
    r = requests.get(f"https://context.reverso.net/translation/{original_language}-{translation_language}/{word}", headers=headers)


    if not r:
        print("Something wrong with your internet connection")
        sys.exit(0)

    soup = BeautifulSoup(r.content, 'html.parser')

    if f"'{word}' not found in Context" in soup.select_one("#no-results").text:
        print(f"Sorry, unable to find {word}")

        sys.exit(0)

    translation(5, translation_language)

else:
    for number, language in dict_language.items():
        if number == '0':
            continue

        r = requests.get(f"https://context.reverso.net/translation/{original_language}-{language}/{word}", headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        if language == original_language:
            continue

        if f"'{word}' not found in Context" in soup.select_one("#no-results").text:
            print(f"Sorry, unable to find {word}")

            sys.exit(0)


        translation(2, language)