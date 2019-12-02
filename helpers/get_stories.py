

def get_stories(start_id,count):
    from main.models import Stories
    import re
    import requests
    for ix in range(start_id,count):
        X = Stories()
        data=requests.get('https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(ix)).json()
        try:
            if 'article' in data.keys():
                X.article = data['article']
            if 'author' in data.keys():
                X.author = data['author']
            if 'comments' in data.keys():
                X.comments = data['comments']
            if 'domain' in data.keys():
                X.domain = data['domain']
            if 'points' in data.keys():
                X.points = data['points']
            if 'time_stamp' in data.keys():
                X.time_stamp = data['time_stamp']
            if 'by' in data.keys():
                X.by = data['by']
            if 'descendants' in data.keys():
                X.descendants = data['descendants']
            if 'id' in data.keys():
                X.id = data['id']
            if 'kids' in data.keys():
                X.kids = data['kids']
            if 'score' in data.keys():
                X.score = data['score']
            if 'time' in data.keys():
                X.time = data['time']
            if 'title' in data.keys():
                X.title = data['title']
            if 'type' in data.keys():
                X.type = data['type']
            if 'url' in data.keys():
                X.url = data['url']
            X.save()
        except Exception as e:
            print(e)