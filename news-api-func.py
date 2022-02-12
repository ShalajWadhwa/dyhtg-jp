from newsapi import NewsApiClient
import datetime

#pip install newsapi

today = datetime.date.today()
def get_news(region, date):
    newsapi = NewsApiClient(api_key='b6fb94a5a7c54883b63495d3f38b3c03')
    all_articles = newsapi.get_everything(q=region,
                                        sources='bbc-news, independent, financial-times',
                                        domains='bbc.co.uk,',
                                        from_param=str(date),
                                        to=str(date),
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)
                        
    #base case: the list is not empty, return the result
    if all_articles['articles'] != []:
        #print(date)
        title = all_articles['articles'][0]['title']
        #print(title)
        descr = all_articles['articles'][0]['description']
        link = all_articles['articles'][0]['url']
        #return get_news(region, date)
        return title, descr, link

    #recursive case: the list is empty, add one more day to check
    else:
        new_date = date - datetime.timedelta(days=1)
        return get_news(region, new_date)

title, description, link = get_news("Glasgow", today)
print(title)
print()
print(description)
print()
print(link)