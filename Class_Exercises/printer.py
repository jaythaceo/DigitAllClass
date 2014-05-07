#!/usr/bin

grab = open("random.txt", "r")
text = grab.read()

print(text)
grab.close()