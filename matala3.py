## This matala work for whatsup application for both ,operating systems, ios and android. 
##
### there are 3 times that i read the file by many reason, when you run the code do not forget change the file path 3 times
##
##
### in the first code line on *step 5* do not forget to change the path
##
import json
file = open(r'C:\Users\MyPC\Desktop\matalot\matala3\chat3.txt',encoding=('utf-8'))
#list of dict of messages
messages=list()
#dict of name - the key is the real name and the value is anonimous value start from 1
names=dict()
# list of dict incule the metadata of the conversation
metadata=list()
#list of lists of dictionary for the 4th step incule messages and metadata
chat = list()
# index that help understand if we are in the first or second or other sentences in the txt file
index = 0
#A variable that is responsible for counting the number of participants starts from 1  
count = 1

#Step 1 - creating anonymus dictionary for the members in the chat
for sentence in file:
    index = index + 1
    #for andorid
    if index == 2 and sentence[0]!="[":
        names[sentence[sentence.find("על ידי") + 7:].rstrip()]=count
        count = count + 1
    #for ios
    if index == 2 and sentence[0]=="[":
        names[sentence[sentence.find("] ")+4:sentence.find("יצר/ה")].rstrip().lstrip()]=count
        count = count + 1
    #for andorid
    if index >2 and sentence[sentence.find(" - "):].find(": ")>0 and sentence[0]!="[":
        if (sentence[sentence.find(" - ")+3:sentence.find(": ")]) not in names:
            names[sentence[sentence.find(" - ")+3:sentence.find(": ")]]=count
            count  = count + 1
    #for ios
    if index >2 and sentence[sentence.find("] "):].find(": ")>0 and sentence[0]=="[":
        if (sentence[sentence.find("] ")+2:sentence.find(": ")]) not in names:
            names[sentence[sentence.find("] ")+2:sentence.find(": ")]]=count
            count  = count + 1
        

#Step 2: create list of dictionary of messages {datetime,id,text} 
index = 0
file = open(r'C:\Users\MyPC\Desktop\matalot\matala3\chat3.txt',encoding=('utf-8'))
for sentence in file:
    index = index + 1
    #for andorid    
    if index>2 and sentence[sentence.find(" - "):].find(": ")>0 and sentence[0]!="[":
        messages.append({"datetime": sentence[:sentence.find(" - ")],
                         "id":names[sentence[sentence.find(" - ")+3:sentence.find(": ")]],
                         "text":sentence[sentence.find(": ")+2:].rstrip()})
    #for ios
    if index>2 and (sentence[0]=="["):
        if (sentence[sentence.find("] "):].find(": ")>0):
            messages.append({"datetime": sentence[1:sentence.find("] ")],
                              "id":names[sentence[sentence.find("]")+2:sentence.find(": ")]],
                              "text":sentence[sentence.find(": ")+2:].rstrip()})

#Step 3 - creationg dictionary for metadata {chat name, creation date, num of participants,creator}
index = 0
file = open(r'C:\Users\MyPC\Desktop\matalot\matala3\chat3.txt',encoding=('utf-8'))
for sentence in file:
    index = index + 1
    #for andorid
    if index == 2 and sentence[0]!="[":
        metadata.append({"chat_name":sentence[sentence.find("הקבוצה")+8:sentence.find("נוצרה")-2],
                     "creation_date":sentence[:sentence.find(" - ")],
                     "num_of_participants":len(names),
                     "creator":sentence[sentence.find("על ידי") + 7:].rstrip()})
    #for ios
    if index == 1 and sentence[0]=="[": 
        metadata.append({"chat_name":sentence[sentence.find("] ")+1:sentence.find(": ")],
                     "creation_date":sentence[1:sentence.find("] ")],
                     "num_of_participants":len(names)})
    if index == 2 and sentence[0]=="[":
        metadata[0]["creator"]=sentence[sentence.find("] ")+4:sentence.find("יצר/ה")].rstrip().lstrip()
    

#Step 4 - combine messages and metadata
chat.append({"messages":messages,
             "metadata":metadata})

#Step 5 - export json string into txt file
namefile = r"C:\Users\MyPC\Desktop\matalot\matala3\\" + metadata[0]['chat_name'] + ".txt"
jsonchat=json.dumps(chat, ensure_ascii=False, indent=5)
file2=open(namefile,"w",encoding="utf-8")
file2.write(jsonchat)
