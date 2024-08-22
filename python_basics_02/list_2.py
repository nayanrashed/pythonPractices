fav_movie=[]
while True:
    print('Movie No '+ str(len(fav_movie)+1) +'or press enter to stop adding the list.')
    movie=input()
    if movie =='':
        break
    fav_movie=fav_movie+[movie]
    
if len(fav_movie)!=0:
    print('The Favorite Movies are:')
    for i in range(len(fav_movie)):
        print(fav_movie[i])