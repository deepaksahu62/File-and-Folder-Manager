import os
from pathlib import Path

def createfolder():
    name=input("please tell yur folder name:-")
    p=Path(name)
    if not p.exists():
        p.mkdir()              #used for creating a folder
    else:
        print("folder name already exists.")
       
    
def listing():
    p=Path('')
    items=list(p.rglob('*'))          #used for recursive lob
    for i,v in enumerate(items):
        print(f"{i+1} : {v}")

def updatefolder():
    listing()
    O_name=input("wich folder you want to update :-")
    old_p= Path(O_name)
    if old_p.exists():
        n_name=input("tell folders new name :-")
        new_p=Path(n_name)
        if not new_p.exists():
            old_p.rename(new_p)      #used for over writing old_p
        else:
            prinnt("this name folder already exists.")
    else:
        print("no such folder name exists.")
           

def deletefolder():
    listing()
    name=input("which folder you want to delete :-")
    p=Path(name)
    if p.exists():
        p.rmdir()                  #used for deleting a folder
    else:
        print("no such folder exists.")

def createfile():
    name=input("tell your file name with extension :-")
    p=Path(name)
    if not p.exists():
        with open(p , "w") as file:
            data=input("what you want to write inside :-")
            file.write(data)
            print("created successfully.")
    else:
        print("this file already exists.")

def readfile():
    listing()
    name=input("tell the file name that you want to read with extension :-")
    p=Path(name)
    if p.exists() and p.is_file():
        with open(p , "r") as file:
            data=file.read()
            print(data)
            print("file read successfully.")
    else:
        print("no such file exists.")

def updatefile():
    listing()
    name=input("which file you want to update :-")
    p=Path(name)
    if p.exists() and p.is_file():
        print("press 1 for updating the file name.")
        print("press 2 for over writing the content.")
        print("press 3 for appending in file")
        check=int(input("tell your response:-"))
        if check==1:
            new_name=input("tell your new name :-")
            new_p=Path(new_name)
            if not new_p.exists():
                p.rename(new_p)
                print("name updated successfully.")
            else:
                print("this name already exists.")
        
        if check==2:
            with open(p , "w") as file:
                data=input("what you want to write in the file :-")
                file.write(data)
                print("updated successfully.")

        if check==3:
            with open(p , "a") as file:
                data=input("what you want to append in the file :-")
                file.write(" " + data)
                print("updated successfully.")

        else:
            print("invalid response.")

def deletefile():
    listing()
    name=input("which file you want to delete :-")
    p=Path(name)
    if p.exists() and p.is_file:
        os.remove(p)
        print("file deleted successfully")
    else:
        print("no such file exists.")


while True:
    print("press 1 for creating a folder")
    print("press 2 for listing files and folders")
    print("press 3 for updating a folder name")
    print("press 4 for deleting a folder")
    print("press 5 for creating a file")
    print("press 6 for reading a file")
    print("press 7 for updating a file")
    print("press 8 for deleting a file")
    print("press 0 to exit the application")
    res=int(input("tell your response :-"))
    if res==1:
            createfolder()

    if res==2:
            listing()

    if res==3:
            updatefolder()

    if res==4:
            deletefolder()

    if res==5:
            createfile()

    if res==6:
            readfile()

    if res==7:
            updatefile()

    if res==8:
        deletefile()

    if res==0:
        break

    else:
        print("invalid response , please enter valid response.")