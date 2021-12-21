from django.shortcuts import render
import bs4
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):

    word = request.GET['word']

    res = requests.get('https://www.dictionary.com/browse/'+word)
    res2 = requests.get('https://www.thesaurus.com/browse/'+word)
    

    if res:
        soup = bs4.BeautifulSoup(res.text, features='html.parser')  

    
        meaning = soup.find_all('div', {'value': '1'})
        meaning1 = meaning[0].getText()
    else:
        word = 'Sorry, '+ word + ' Is Not Found In Our Database'
        meaning = ''
        meaning1 = ''

    if res2:
        soup2 = bs4.BeautifulSoup(res2.text, features='html.parser')

        synonyms = soup2.find_all('a', {'class': 'css-1kg1yv8 eh475bn0'})
        ss = []
        for i in synonyms[:8]:
            synonym = i.text.strip()
            ss.append(synonym)
        synonym = ss
        


        antonyms = soup2.find_all('a', {'class': 'css-15bafsg eh475bn0'})
        aa = []
        for i in antonyms[:8]:
            antonym = i.text.strip()
            aa.append(antonym)
        antonym = aa
    else:
        synonym = ''
        antonym = ''


    results = {
        'word' : word,
        'meaning' : meaning1,
    }


    return render(request, 'search.html', {'synonym': synonym, 'antonym': antonym, 'results': results})