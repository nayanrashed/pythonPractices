place_visited = ['Thailand', 'Nepal', 'Malaysia', 'Bhutan', 'USA']
# index() method
print(place_visited.index('Thailand'))

# append()
place_visited.append('UK')
print(place_visited)

# insert()
place_visited.insert(2, 'Maldives')
print(place_visited)

# remove()
place_visited.remove('Nepal')
print(place_visited)

# sort()
# place_visited.sort()
place_visited.sort(key=str.lower)
place_visited.sort(key=str.lower, reverse=True)

print(place_visited)


