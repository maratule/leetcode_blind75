import os

os.chdir('/Users/marattulegenov/Desktop/work/')

with open('AL_5G.txt') as file:
    content = file.readlines()
for i in content:
    print(i.strip())