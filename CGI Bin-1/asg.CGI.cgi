#!C:\Python\Python38-32\python.exe

# print("Content-type:text/html\r\n\r\n")

import cgi
import hashlib
import os

status = "Ready for command"

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<link rel="stylesheet" href="index.css">')
print('<title>Hello World - First CGI Program</title>')
print('</head>')
print('<body>')

def insert(name, value):
    flag = 0
    data = []
    with open('C:\\xampp\\htdocs\\cgia\\db.txt', 'r+') as file:
        data = file.readlines()
        i = 0
        index = 0
        for item in data:
            old_name = item.split(":")
            if name == old_name[0]:
                index = i
                flag = 1
                break
            i += 1
    if flag == 0:
        data.append(name + ":" + value+"\n")
        with open('C:\\xampp\\htdocs\\cgia\\db.txt', 'a') as file:
            line = "".join(data)
            file.write(line)
            status = "<div class = 'green' >Successfully inserted " + name + " = " + value + "</div>"
            print(status)
    else:
        data[index] = name + ":" + value+"\n"
        with open('C:\\xampp\\htdocs\\cgia\\db.txt', 'w+') as file:
            line = "".join(data)
            file.write(line)
            status = "<div class = 'green' >Successfully inserted " + name + " = " + value + "</div>"
            print(status)


    
def retrieve(retrieve_name):
    flag = 0
    with open('C:\\xampp\\htdocs\\cgia\\db.txt', 'r') as file:
        data = file.readlines()
        for item in data:
            name = item.split(":")
            # print(name)
            if retrieve_name == name[0]:
                # print("inner")
                flag = 1
                break
    if flag == 1:
        status = "<div class = 'green' >" + name[0] + " = " + name[1] + "</div>"
    else:
        status = "<div class = 'red'> The name " + name[0] +" is not in the database</div>"
    print(status)

def clear(password):
    if password == "really!":
        with open('C:\\xampp\\htdocs\\cgia\\db.txt', 'w') as file:
            file.write("")
            status = "<div class = 'green' >database cleared</div>"
    else:
        status = "<div class = 'red'> wrong password </div>"
    print(status)

def digest(file_name):
    try:
        with open('C:\\xampp\\htdocs\\cgia\\' + file_name + '.txt',"r") as f:
            bytes = f.read().encode('utf-8') # read entire file as bytes
            readable_hash = hashlib.sha256(bytes).hexdigest()
        
        status = '<div class = "green" >Digest  is ' + file_name + " : " + readable_hash +"</div>"
    except:
        status = "<div class = 'red'>Cannot read " + file_name + "</div>"
    print(status)



# # __________________________________BONUS________________________________________

def inspect(fileitem):
    if fileitem.filename:
        fn = os.path.basename(fileitem.filename)
        open('C:\\xampp\\htdocs\\cgia\\' + fn, 'wb').write(fileitem.file.read())
        # message = '<div class = "green" > The file "' + fn + '" was uploaded successfully</div>'
        try:
            with open('C:\\xampp\\htdocs\\cgia\\' + fn ,"r") as f:
                bytes = f.read().encode('utf-8') # read entire file as bytes
                readable_hash = hashlib.sha256(bytes).hexdigest()
            
                status = '<div class = "green" >Digest  is ' + fn + " : " + readable_hash +"</div>"
        except:
            status = "<div class = 'red'>Cannot read " + fn + "</div>"
        print(status)
    else:
        message = '<div class = "red">No file Presented</div>'
        print(message)
    
    
    

form = cgi.FieldStorage()
command = form.getvalue("command")
if(command == "insert"):
    insert(form.getvalue('name'), form.getvalue('value'))
if(command == "retrieve"):
    retrieve(form.getvalue('retrieve-name'))
    # print(form.getvalue('retrieve-name'))
if(command == "clear"):
    clear(form.getvalue('password'))
if(command == "digest"):
    digest(form.getvalue('filename'))
if(command == "inspect"):
    inspect(form['file'])



print('</body>')
print('</html>')
