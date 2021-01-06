from imdb import IMDb, IMDbError

# or import imdb
# ia = imdb.IMDb()

ia = IMDb()

# Simple movie search
movies = ia.search_movie('matrix')

# Simple people search
people = ia.search_person('angelina')

# Simple keyword search
keywords = ia.search_keyword('dystopia')

try:
    people = ia.search_person('Mel Gibsons')
    for each in people:
        print(each)
except IMDbError as e:
    print(e)