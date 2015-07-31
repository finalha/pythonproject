'''
Created on 2014-10-11

@author: 16101210-15
'''
# print("Hello World!")
import sys,urllib.request
url="http://www.putclub.com/html/radio/VOA/presidentspeech/index.html"
wp = urllib.request.urlopen(url)
print('start download...')
content = wp.read()
#center_box = content.count("center_box")
#print(content.count("center_box"))
print(type(content))
content = str(content)
center_box = content.count("center_box")
print(center_box)
index =  content.find("center_box")
content=content[content.find("center_box")+1:]
content=content[content.find("href=")+7:content.find("target")-2]
filename = content
url ="http://www.putclub.com/"+content
print(content)
print(url)
wp = urllib.request.urlopen(url)
print('start download...')
content = wp.read()
#print content
#print content.count(""):]
print(type(content))
content = str(content)
content = content[:content.find("<div class=\"dede_pages\"")-1]
filename = filename[filename.find("presidentspeech")+len("presidentspeech/"):]
filename = filename.replace('/',"-",filename.count("/"))
fp = open(filename,"w+")
fp.write(content)
fp.close()
print(content)
