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

   