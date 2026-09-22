# movie_rating

def movie_rating(rating):
    if(rating > 9 and rating <=10):
        print("excellent")

    elif(rating > 7 and rating <=8):
        print("good")

    elif(rating > 5 and rating <= 6):
        print("average")

    else:
        print("poor")

movie_rating(10)
movie_rating(8)
movie_rating(6)