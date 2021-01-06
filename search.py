import argparse
from imdb import IMDb, IMDbError

# or import imdb
# ia = imdb.IMDb()

ia = IMDb()

# Simple movie search
def getMovies(movie):
    myMovie = ia.search_movie(movie)
    try:
        for film in myMovie:
            return film
    except IMDbError as e:
        print(e)

# Simple people search
def getPeople(folks):
    stars = ia.search_person(folks)
    try:
        for star in stars:
            return star
    except IMDbError as e:
        print(e)

# Simple keyword search
def findKeywords(word):
    _find = ia.search_keyword(word)
    try:
        for words in _find:
            return words
    except IMDbError as e:
        print(e)


parser = argparse.ArgumentParser(description='Search imdb for movies, people, or keywords')

parser.add_argument('-m', '--movie', help='search for a movie or movies', type=str, metavar='film')
parser.add_argument('-p', '--people', help='search for a people', type=str, metavar='folks')
parser.add_argument('-k', '--keyword', help='search using keywords', type=str, metavar='word')
# parser.add_argument('yourMovie', help='Search for a movie or movies', type=str)

# yourMovie = input('What movie are you looking for?\n ')

args = parser.parse_args()
if args.movie:
    print()
    print(getMovies(args.movie))
elif  args.people:
    print()
    print(getPeople(args.people))
elif args.keyword:
    print()
    print(findKeywords(args.keyword))
else:
    print('Search IMDB for Movies, People, or Keywords')
    print()
    print('USAGE: Use "-m MOVIE" to search for a movie or movies')
    print('       Use "-p PEOPLE" to search for a person')
    print('       Or use "-k KEYWORD" to search by keyword')
