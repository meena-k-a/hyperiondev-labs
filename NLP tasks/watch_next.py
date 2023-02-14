# This program reads movies details from a text file 'movies.txt' and returns user which movies he has to watch next .

import spacy

def get_most_similar_movie(movie_description) :
    nlp = spacy.load('en_core_web_md')
    high_similarity_value = 0
    for key in movie_dict:
        similarity_value = nlp(movie_dict[key]).similarity(nlp(movie_description))        
        if (similarity_value > high_similarity_value):
            high_similarity_value = similarity_value
            most_match_movie = key
    #print(most_match_movie,high_similarity_value, movie_dict[most_match_movie])    
    return most_match_movie

# Global variable
movie_dict = {}

# -----------Main program---------
# Read contents of file Movies.txt
with open("movies.txt") as file_movies:
    file_movies_txt = file_movies.readlines()

# store the contents of text file into a dictionary {key:value}  
for line in file_movies_txt:
    split_line = line.strip('\n').split(':') # strip new line and split where : presents 
    movie_dict[split_line[0]] = split_line[1]

watched_movie_description =''''Will he save the world or destroy it? when the world become too dangerous for the earth,
                         the illuminati trick hulk into a shuttle and launch into space to a planet where the hulk can live in peace.
                         unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

movie_to_watch = get_most_similar_movie(watched_movie_description)  

print(f"\n\t Next movie to watch is {movie_to_watch}\n")