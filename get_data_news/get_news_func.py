import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt


async def get_news_ixbt():

    url = "https://www.ixbt.com/news/?show=tape"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    all_data = soup.find_all("div", class_='item no-padding')

    all_pretty_data = []

    for news in all_data:

        title = news.find('h2', class_='no-margin').text
        url = 'https://www.ixbt.com' + news.find('h2', class_='no-margin').a['href']
        time = news.find('span', class_='time_iteration_icon').text.strip()
        tags = news.find('p', class_='b-article__tags__list')
        tags = [x.strip() for x in tags.text[6:].split(',')] if tags else []

        all_pretty_data.append({

            'title': title,
            'url': url,
            'date': time,
            'tags': tags

        })

    with open('secret_data/last_news_time.txt', 'r+', encoding='utf-8') as f:
        date_last_news = f.read()

    date_last_news = dt.strptime(date_last_news, '%H:%M')

    def need_format_data(date):

        date_news = dt.strptime(date, '%H:%M')

        return date_news

    result_data = list(filter(lambda x: need_format_data(x['date']) > date_last_news, all_pretty_data))

    date_last_news = max([dt.strptime(time, '%H:%M') for time in
                          [x['date'] for x in all_pretty_data]
                          ]).strftime('%H:%M')

    with open('secret_data/last_news_time.txt', 'w', encoding='utf-8') as f:
        f.write(date_last_news)

    return result_data
