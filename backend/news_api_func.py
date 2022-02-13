from newsapi import NewsApiClient
import datetime

# pip install newsapi

def get_news(region, date, news_api_key):
    newsapi = NewsApiClient(api_key=news_api_key)
    all_articles = newsapi.get_everything(q=region,
                                        sources='bbc-news, independent, financial-times',
                                        domains='bbc.co.uk,',
                                        from_param=str(date),
                                        to=str(date),
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)
                        
    # base case: the list is not empty, return the result
    if all_articles['articles'] != []:
        title = all_articles['articles'][0]['title']
        descr = all_articles['articles'][0]['description']
        link = all_articles['articles'][0]['url']
        return title, descr, link

    # recursive case: the list is empty, add one more day to check
    else:
        new_date = date - datetime.timedelta(days=1)
        if new_date - datetime.date.today() < datetime.timedelta(-7):
            return None
        else:    
            return get_news(region, new_date, news_api_key)