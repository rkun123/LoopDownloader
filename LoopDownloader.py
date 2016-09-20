#LoopDownloader v0.1
import requests
import os
import re
import sys
from PIL import Image
from io import StringIO

print("Hi")

count = 1

pat = r"num"
urlData = sys.argv[1]

kakuchoshi = sys.argv[2]
loop = True

if os.path.isdir("data") != True:
    os.mkdir("data")
else:
    print("directory has already existed.")

while loop:
    url = re.sub(pat,str(count),urlData)
    data = requests.get(url)

    if data.status_code == 200:
        print (str(count)+"th image is Downloading...")
        fn = "data/data"+str(count)+"."+kakuchoshi
        #print(fn)

        f = open(fn,'wb+')
        f.write(data.content)
        count+=1

    else:
        loop = False
print("All finished!!")
