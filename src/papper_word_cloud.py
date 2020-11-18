from wordcloud import WordCloud

wordcloud = WordCloud()

wordcloud.generate("hello world")
wordcloud.to_file("w.jpg")


