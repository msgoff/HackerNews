import requests
import re
import json
import sys
import pandas as pd 
pd.options.display.max_colwidth = 1000


ID=sys.argv[1]
print ID
def get(ID):
    url="https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty".format(ID)
    data=requests.get(url)
    return json.loads(data.text)

def make_df(lst):
    return pd.DataFrame([get(ID) for ID in lst])

def df_kids(df):
    test=set()
    if 'kids' in df.columns.tolist():
        for lst in df.kids.tolist():
            if str(lst)!='nan':
                for ix in lst:
                    test.add(ix)
        return list(test)
    else:
        return ""

def get_new_ids(df):
    kids=df_kids(df)
    return list(set(kids)-set(df.id.tolist()))





df= make_df(get(ID)['kids'])
for ix in range(7):
    tf=make_df(get_new_ids(df))
    df=pd.concat([df,tf])
    df=df.drop_duplicates('id')
if 'deleted' in df.keys():
	del df['deleted']
if 'type' in df.keys():
	del df['type']

df.to_csv('{}.csv'.format(ID),encoding='utf-8')
