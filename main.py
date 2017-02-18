__author__ = 'ANKIT VERMA'
import requests
import operator
from bs4 import BeautifulSoup

keywords = {}

# ADD THE WORDS WHOSE COUNT IS NOT REQUIRED IN THE LIST BELOW

not_require_keywords = ['how', 'and', 'when', 'why', 'which', 'who', 'a', 'all', 'or', 'an', 'the', 'aboard', 'about',
                        'above',
                        'across', 'after', 'against', 'ahead of', 'along', 'amid', 'amidst', 'among', 'around', 'as',
                        'as far as', 'as of', 'aside from', 'at', 'athwart', 'atop ', 'barring', 'because of', 'before',
                        'behind', 'below', 'beneath', 'beside', 'besides', 'between', 'beyond', 'but', 'by',
                        'by means of ', 'circa', 'concerning ', 'despite', 'down', 'during ', 'except', 'except for',
                        'excluding ', 'far from', 'following', 'for', 'from ', 'in', 'in accordance with',
                        'in addition to', 'in case of', 'in front of', 'in lieu of', 'in place of', 'in spite of',
                        'including', 'inside', 'instead of', 'into ', 'like ', 'minus ', 'near', 'next to',
                        'notwithstanding ', 'of', 'off', 'on', 'on account of', 'on behalf of', 'on top of', 'onto',
                        'opposite', 'out', 'out of', 'outside', 'over ', 'past', 'plus', 'prior to ', 'regarding',
                        'regardless of ', 'save', 'since ', 'than', 'through', 'till', 'to', 'toward', 'towards ',
                        'under', 'underneath', 'unlike', 'until', 'up', 'upon ', 'versus', 'via ', 'with',
                        'with regard to', 'within', 'without']


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for post_text in soup.findAll('a'):
        content = post_text.string
        if content:
            words = content.lower().split()
            for each_word in words:
                word_list.append(each_word)
    clean_word(word_list)


def clean_word(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = ",./;\'-!@#$%^&*()\"_+=|`[]>>:{}?><:1234567890"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    get_count(clean_word_list)


def get_count(clean_word_list):
    for word in clean_word_list:
        if word in keywords and word not in not_require_keywords:
            keywords[word] += 1
        elif word not in not_require_keywords:
            keywords[word] = 1


url = input("ENTER URL TO GET WORD FREQUENCY IN HYPERLINKS:\n")
start(url)
for key, value in sorted(keywords.items(), key=operator.itemgetter(1), reverse=True):
    print(key + ':', value)
