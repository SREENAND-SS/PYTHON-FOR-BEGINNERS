#menu driven program in python to add ,search ,update and delete details of a student in  a binary file

import pickle
def add_rec():
    f=open('student.dat','ab')
    n=input('enter name of the student:')
    r=int(input('enter rollno:'))
    m=int(input('enter marks:'))
    d={'name':n,'roll no':r,'marks':m}
    pickle.dump(d,f)
    f.close()
def read():
    f=open('student.dat','rb')
    try:
        while True:
            k = pickle.load(f)
            print(k['name'],k['roll no'],k['marks'])
    except:
        f.close()
def search():
    f = open('student.dat', 'rb')
    c=False
    while True:
        try:
            k = pickle.load(f)
            n=int(input('enter data for search(name,roll no,marks):'))
            if k['roll no']==n or k['marks']==n or k['name']==n:
                print(k['name'], k['roll no'], k['marks'])
            else:
                print('not found')
        except:
            f.close()
def update():
    f=open('student.dat','rb')
    n=[]
    x=int(input('enter the roll no of the student whose data is to be updated:'))
    y=int(input('enter new mark:'))
    while True:
        try:
            data=pickle.load(f)
            n.append(data)
        except:
            break
    f.close()
    for i in n:
        if i['roll no']== x:
            i['marks']=y
    f=open('student.dat','wb')
    for k in n:
        pickle.dump(k,f)
    f.close()
def del_rec(r):
    f=open('student.dat','rb')
    k=[]
    while True:
        try:
           data = pickle.load(f)
           k.append(data)
        except:
            f.close()
    f=open('student.dat','wb')
    for i in k:
        if i['roll no']==r:
     f.close()
# menu
while True:
    print('''1.insert record
    2.read record
    3.search record
    4.update record
    5.delete record''')
    ch=int(input('enter your choice:'))
    if ch==1:
        add_rec()
    elif ch==2:
        read()
    elif ch==3:
        search()
    elif ch==4:
        update()
    elif ch==5:
        r=int(input('enter roll no of the student whose record is to be deleted'))
        del_rec(r)
    else:
        quit()



# add_rec()
# read()
# search()
# update()
