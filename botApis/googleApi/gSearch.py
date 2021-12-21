from DiscordBot.botApis.googleApi import _googleApiClient
import click
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def FilterStopWords(data):
    stop_words = set(stopwords.words('english'))

    punc = '''!-{};:'"\\,<>./?@#$%^&*~'''
    for ele in data:
        if ele in punc:
            data = data.replace(ele, "")

    word_tokens = word_tokenize(data)

    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    return filtered_sentence


@click.group()
def cli():
    pass


@cli.command(help='Run a search on google')
@click.option('-s', is_flag='True', help='Runs using a stop words define search')
def Single_Search(s):
    search_term = input("Enter the term you want to search: ")
    if s:
        search_term = FilterStopWords(search_term)
    resp = _googleApiClient.google_search(search_term)
    for title, link, snippet in resp:
        print("Title: {}\nLink: {}\nSum: {}\n".format(title, link, snippet))


if __name__ == '__main__':
    cli()
