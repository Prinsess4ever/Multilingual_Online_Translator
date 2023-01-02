import sys

import requests

from bs4 import BeautifulSoup

dict_language = {"1": "arabic", "2": "german", "3": "english", "4": "spanish", "5": "french", "6": "hebrew", "7": "japanese", "8": "dutch", "9": "polish", "10": "portuguese", "11": "romanian", "12": "russian", "13": "turkish"}

print("Hello, welcome to the translator. Translator supports:")
for number, language in dict_language.items():
    print(f"{number}. {language.title()}")


original_language = input("Type the number of your language: \n")
translation_language = input("Type the number of language you want to translate to:\n")
word = input("Type the word you want to translate:\n")

headers = {'User-Agent': 'Mozilla/5.0'}

r = requests.get(f"https://context.reverso.net/translation/{dict_language[original_language]}-{dict_language[translation_language]}/{word}", headers=headers)
full_word = dict_language[translation_language]

if r:
    pass
else:
    sys.exit(0)

transleted_words = []
transleted_zinnen = []

soup = BeautifulSoup(r.content, 'html.parser')

print(f"\n{full_word.title()} Translations")

for i, text1 in enumerate(soup.select("span.display-term")):
    if i+1 == 6:
        break

    print(text1.text)
print(f"\n{full_word.title()} Examples")

text1 = soup.select("div.src.ltr")
text2 = soup.select("div.trg.ltr")

for i in range(5):
    print(text1[i].text.strip())
    print(text2[i].text.strip() + "\n")


