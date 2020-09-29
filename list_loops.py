songs = ["ROCKSTAR", "Do It", "For The Night"]

#print out first element on the list
print(songs[0])

#print out the last element on the list
print(songs[2])

#print out Do It and For The Night
print(songs[1:])

# update the first element
songs[0] = "Malibu"

# print the list
print(songs)

# adds an element to the end of the list
songs.append("Save Room For Us")

# adds a list to end of a list
songs.extend(["The Light is Coming", "Cherry"])

# adds element at specific index followed by item
songs.insert(0, "Experience")

#removes an element
songs.pop(0)

#new list 
animals = ["cat", "tiger", "lion"]

animals.append("panther")

print(animals[2])

animals.pop(0)

for animal in animals:
    print(animal)