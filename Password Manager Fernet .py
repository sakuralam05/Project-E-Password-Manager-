from cryptography.fernet import Fernet

'''
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
    key_file.write(key)'''

def load_key():
 file= open("key.key","rb")
 key=file.read()
 filoe.close()
 
return key

master_pwd=input("What is the master password?")
key=load_key()+master_pwd
fer=fernet(key)

def view():
    with open('Password.txt','r') as f:
    for line in f.readlines():
    data=line.rstrip()
    user,passw=data.split("|")
    print("user:",user,"|password:",str(fer.dencrypt(pw.encode()).decode())
        
def add():
    name=input('account name: ')
    pwd=input("password:")

with open('Password.txt','a') as f:
    f.write(name+"|"+str(fer.encrypt(passw.encode())))
    

While True
mode=input("Would you like to add a new password or add a new one(view, add),press q to quit ?").lower()
if mode=="q":
    break


if mode=="view":
    view()
elif mode=="add":
    add()
else:
    print("Invalid mode")
    continue


