word = 'hippo'
print(word)
print(len(word))
print(word[0:3])
print(word[1])
print(word[-1])

print(word.upper())
print(word.capitalize())

print(word.find('i'))
print(word.find('z'))

country = "Bangladesh"
print(country.startswith("Ban")) 
print(country.endswith("shk")) 

country1 = "Bangladesh, Japan, Italy"
print(country1.split(","))

list = ['a','b','c']
joined = ", ".join(list)
print(joined)