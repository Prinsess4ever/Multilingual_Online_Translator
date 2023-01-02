import sys

import requests

from bs4 import BeautifulSoup

dict_language = {"1": "Arabic", "2": "German", "3": "English", "4": "Spanish", "5": "French", "6": "Hebrew", "7": "Japanese", "8": "Dutch", "9": "Polish", "10": "Portuguese", "11": "Romanian", "12": "Russian", "13": "Turkish"}

print("Hello, welcome to the translator. Translator supports:")
for number, language in dict_language.items():
    print(f"{number}. {language}")


original_language = input("Type the number of your language: \n")
translation_language = input("Type the number of language you want to translate to:")
word = input("Type the word you want to translate:\n")

headers = {'User-Agent': 'Mozilla/5.0'}

r = requests.get(f"https://context.reverso.net/translation/{dict_language[original_language]}-{dict_language[translation_language]}/{word}", headers=headers)
full_word = dict_language[translation_language]

if r:
    print("200 OK")
else:
    sys.exit(0)

transleted_words = []
transleted_zinnen = []

soup = BeautifulSoup(r.content, 'html.parser')

print(f"\n{full_word} Translations")

for i, text1 in enumerate(soup.select("span.display-term")):
    if i+1 == 6:
        break

    print(text1.text)
print(f"\n{full_word} Example")

text1 = soup.select("div.src.ltr")
text2 = soup.select("div.trg.ltr")

for i in range(5):
    print(text1[i].text.strip())
    print(text2[i].text.strip() + "\n")


