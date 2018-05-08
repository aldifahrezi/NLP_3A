import json
import pickle
import re
from gensim.models import Word2Vec

def main():
    with open('../scrapper/reviews.json', 'r') as fp:
        reviews = json.load(fp)['reviews']
    
    sentences_tokens = []

    for i in range(0, 5):
        review = reviews[i]
        try :
            tokens =  re.sub(r"[^a-z0-9]+", " ", review.lower()).split()
            sentences_tokens.append(tokens)
        except:
            continue
        
    
    # print(sentences_tokens)
    
    model = Word2Vec(
        sentences=sentences_tokens,
        size=100,
        window=5,
        min_count=5,
        workers=4,
    )

    # with open('wordmodel', 'w') as fp:
    #     pickle.dump(model, fp)

    sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]

if __name__=='__main__':
    main()
    