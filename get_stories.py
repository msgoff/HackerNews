from tqdm import tqdm
import pandas as pd
import re
import requests
from sys import argv

start_id = int(argv[1])
stop = int(argv[2])


def get_stories(start_id, stop):
    output = []
    for ix in tqdm(range(start_id, stop)):
        data = requests.get(
            "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty".format(ix)
        ).json()
        output.append(data)
    df = pd.DataFrame(output)
    df.to_csv(f"{start_id}_{stop}.csv", index=False)
    return df


df = get_stories(start_id, stop)
print(df.head())
