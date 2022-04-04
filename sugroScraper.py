
   
from bs4 import BeautifulSoup
import requests
import os 
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
arabic_file = open(f"{dir_path}/data/sugro.json", "w")
sugro_bahasa = open(f"{dir_path}/bahasa/sugro.json", "w")

response = requests.get("https://almatsurat.net/sugro")
soup = BeautifulSoup(response.text)

zikirChilds = soup.findAll(attrs={'class': 'zikir-child'})
contents = []
translatedTextContents = []

for elementIndex in range(len(zikirChilds)):
    element = zikirChilds[elementIndex]

    content = {'id':elementIndex}
    translatedTextContent = {'id':elementIndex}
   
    textQurans = element.findAll(['p', 'div'], attrs={'class': 'text-quran text-justify'})
    intro = element.find('div',attrs={'class': 'text-center'})
    dzkirContents = []
    
    for textQuran in textQurans:
        dzkirContents.append(textQuran.text)

    if intro == None:
        pass
    else:
        content['intro'] = intro.text

    content['contents'] = dzkirContents
    contents.append(content)

    # the translation text
    
    title = element.find('span', attrs={'class': 'title'}).text
    translatedTexts = []
    
    textTranslatesDivs = element.select('div.text-translate.text-justify') 
    # print(textTranslatesDivs)

    # remove quranText, being removed because to get the translation text
    for textQuran in element.select('p.text-quran'):
        print(textQuran.decompose())

    textTranslatesPs = element.findAll('p', attrs={'class': ['text-justify']})
    textTranslatesAyat = element.findAll('span', attrs={'class': ['ayat']})

    introTranslatedText = element.select('div.text-translate.text-center') 
    # translatedTexts.append(introTranslatedText.text)
    # print(introTranslatedText)


    if introTranslatedText is not None and isinstance(introTranslatedText, list):
        try:
            translatedTextContent['intro'] = introTranslatedText[0].text
        except:
            pass

    if len(textTranslatesDivs) > 0:
        for textIndex in range(len(textTranslatesDivs)):
            text = textTranslatesDivs[textIndex]
            translatedText = {'ayat': textTranslatesAyat[textIndex].text, 'text': text.text}
            translatedTexts.append(translatedText)
    else:
        translatedText = {'ayat': textTranslatesAyat[0].text, 'text':textTranslatesPs[0].text}
        translatedTexts.append(translatedText)
        
    translatedTextContent['contents'] = translatedTexts
    translatedTextContent['title'] = title

    translatedTextContents.append(translatedTextContent)
    

arabic_file.write(str(contents).replace('\'', '"'))
sugro_bahasa.write(json.dumps(translatedTextContents))