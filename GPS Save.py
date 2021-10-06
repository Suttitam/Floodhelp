import os
os.chdir('C:\\Python Project')
import shelve
shelfFile = shelve.open('mydata')
x = shelfFile['cats']
print(x)
