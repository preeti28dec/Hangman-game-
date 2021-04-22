# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
import json
filename = 'Text_file.txt'
dict1 = {}
# hum file ko open kar kar read and write karne ke liye with open file ka use karte hai .
with open(filename) as fh: 
    for line in fh:
        command,description = line.strip().split(None, 1)
        #yhan kuch split nhi huaa hai bs key and value  ko split karne ke liye  humne splite use kiya hai none ka matlab hai kuch nhi hai 
        dict1[command] = description.strip()
out_file = open("Hello.json", "w")
json.dump(dict1, out_file, indent = 4)
out_file.close()
