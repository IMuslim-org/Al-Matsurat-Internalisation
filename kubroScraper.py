from bs4 import BeautifulSoup
import requests
import os 
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
kubro_bahasa = open(f"{dir_path}/bahasa/kubro.json", "w")

response = requests.get("https://almatsurat.net/kubro")
soup = BeautifulSoup(response.text)

zikirChilds = soup.findAll(attrs={'class': 'zikir-child'})
translatedTextContents = []

for elementIndex in range(len(zikirChilds)):
    element = zikirChilds[elementIndex]

    content = {'id':elementIndex}
    translatedTextContent = {'id':elementIndex}

    # the translation text
    
    title = element.find('span', attrs={'class': 'title'}).text
    translatedTexts = []

    textTranslatesDivs = element.findAll('div', attrs={'class': ['text-translate']})
    textTranslatesPs = element.findAll('p', attrs={'class': ['text-justify']})

    introTranslatedText = element.find('div', attrs={'class': 'text-translate'})

    if introTranslatedText is not None:
        translatedTextContent['intro'] = introTranslatedText.text


    if len(textTranslatesDivs) > 0:
        for text in textTranslatesDivs:
            translatedTexts.append(text.text)
    else:
        translatedTexts.append(textTranslatesPs[1].text)
        
    translatedTextContent['contents'] = translatedTexts
    translatedTextContents.append(translatedTextContent)
    


kubro_bahasa.write(json.dumps(translatedTextContents))
