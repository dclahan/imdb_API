# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:08:33 2021

@author: clahad

program that, given two movies, finds connections between movies by actors in similar movies, 
eg. toy story to magic mike
toy story -> tom hanks -> catch me if you can -> leo dicap -> wolf of wall st -> jonah hill -> 21 jmp st -> channing tatum -> magic mike
"""

#import imdb and others
from imdb import IMDb #, IMDbError
from time import time

#function to find degrees of separazation using hashing for actors and movies
def find_movies(filmog,act): #want to parse so that only movies, no shows or commercials or upcoming movies
    for credit in filmog[act]:
        print(credit)

# create an instance of the IMDb class
ia = IMDb()

# get a movie
mov_name = input("enter a movie: ")
movies = ia.search_movie(mov_name)
is_mov = False
i = 0
while is_mov==False:
    if len(movies) == 0 :
        print("No movies found")
        break
    print("Is", movies[i]['title'], movies[i]['year'],  "your movie? (y/n)")
    y_n = input()
    if y_n == "y":
        movie = movies[i]
        is_mov = True
    else:
        i+=1
    
tik = time() #start the clock

#make dictionary with genres as keys and values a set of the movies of each actor
watchable_movies = dict()
actors = set()

ia.update(movie, info=['main'])

ten = 0
for actor in movie['actors']:
    if ten == 5:
        break
    print('retreiving %s\'s filmography...'%actor)
    ia.update(actor,info=['filmography'])
    actors.add(actor)
    ten +=1
    
    man = 'actor'
    fem = 'actress'
    
for actor in actors:
    print("%s:"%actor)
    filmog = actor['filmography']
    if man in filmog:
        find_movies(filmog,man)
    if fem in filmog:
        find_movies(filmog,fem)
    print()
tok = time()
print("it took:", tok-tik)
