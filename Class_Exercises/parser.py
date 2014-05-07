#!/usr/bin

grab = open("random.txt", "r")
text = grab.read()

search = "IRobot"
index = text.find(search)
print(search, "found at index", index)
grab.close()
