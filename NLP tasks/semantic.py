import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp('cat')
word2 = nlp('monkey')
word3 = nlp('banana')

print(f'Similarity between {word1} and {word2} is {word1.similarity(word2)}')
print(f'Similarity between {word2} and {word3} is {word2.similarity(word3)}')
print(f'Similarity between {word3} and {word1} is {word3.similarity(word1)}')

# similarity between a series of words in vectors
tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print (token1.text, token2.text, token1.similarity(token2))

# similarity between sentences/texts 
sentence_to_compare = 'why is my cat on the car'

sentences = ['where did my dog go',
            'Hello, there is my car',
            'I\'ve left keys in my car',
            'I\,d like my boat back',
            'I will name my dog Diana']
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + ' - ', similarity)          

# Similarity between movies
movies = ['Movie A :When Hiccup discovers Toothless isn\'t the only Night Fury, he must seek "The Hidden World" a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.',
        'Movie B :After the death of Superman, several new people present themselves as possible successors.',
        'Movie C :A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.',
        'Movie D :A humorous take on Sir Arthur Conan Doyle\'s classic mysteries featuring Sherlock Holmes and Doctor Watson.',
        'Movie E :A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed.']     
for movie1 in movies:
    movie1_name = movie1.split(':')[0]
    for movie2 in movies:
        movie2_name = movie2.split(':')[0]
        similarity = nlp(movie1).similarity(nlp(movie2))
        print(f'similarity between {movie1_name} and {movie2_name} is {similarity}')    


print('''-------My observation ------
    'en_core_web_sm' - 1. Similarity value a bit higher than result from 'en_core_web_mb'
                        2. The model you're using has no word vectors loaded, 
                        so the result of the Doc.similarity method will be based on the tagger,
                        parser and NER, which may not give useful similarity judgments.
                        This may happen if you're using one of the small models, e.g. `en_core_web_sm`,
                        which don't ship with word vectors and only use context-sensitive tensors.
                        You can always add your own word vectors, or use one of the larger models instead if available.
    'en_core_web_mb' - 1. Similarity value a bit lower than result from 'en_core_web_mb'
                        2.You can get the results of similarity, with no warning signs. running smoothly for longer texts.
    ''')             