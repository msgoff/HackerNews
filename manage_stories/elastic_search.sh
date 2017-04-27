wget "https://hacker-news.firebaseio.com/v0/item/"$1".json?print=pretty" -O - > test
curl -XPOST 'localhost:9200/hn/story/?routing=$1&pretty' -d @test
