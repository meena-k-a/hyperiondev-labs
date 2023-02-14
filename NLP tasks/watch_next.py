# This program reads movies details from a text file 'movies.txt' and returns user which movies he has to watch next .

movie_dict = {}

# Read contents of file Movies.txt
with open("movies.txt") as file_movies:
    file_movies_txt = file_movies.readlines()

# store the contents of text file into a dictionary {key:value}  
for line in file_movies_txt:
    split_line = line.strip('\n').split(':') # strip new line and split where : presents 
    movie_dict[split_line[0]] = split_line[1]
    
print(movie_dict)    