import random
from nltk.corpus import wordnet as wn
import json

def get_synonyms(word):
    synonyms = []
    synsets = wn.synsets(word)
    for synset in synsets:
        for lemma in synset.lemmas():
            synonym = lemma.name()
            if synonym != word and synonym not in synonyms:
                synonyms.append(synonym)
                if len(synonyms) >= 3:
                    return synonyms[:3]  # Return the first 3 unique synonyms
    return synonyms  # Return whatever synonyms were found

output = []
unique_words = set()

while len(output) < 4:
    synset = random.choice(list(wn.all_synsets()))
    word = random.choice(synset.lemma_names())  # Get a random word from a random synset
    if word not in unique_words:
        unique_words.add(word)
        synonyms = get_synonyms(word)
        
        # If there aren't 3 synonyms, find a different starting word 
        while len(synonyms) < 3:
            synset = random.choice(list(wn.all_synsets()))
            word = random.choice(synset.lemma_names())
            synonyms = get_synonyms(word)
        
        output.append([word] + synonyms)

while len(output) < 4:
    synset = random.choice(list(wn.all_synsets()))
    word = random.choice(synset.lemma_names())
    synonyms = get_synonyms(word)
    
    # If there aren't 3 synonyms, find a different starting word 
    while len(synonyms) < 3:
        synset = random.choice(list(wn.all_synsets()))
        word = random.choice(synset.lemma_names())
        synonyms = get_synonyms(word)
    
    output.append([word] + synonyms)

with open('public/word_list.json', 'w') as file:
    json.dump(output, file, indent=4)
