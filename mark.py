# python program to add the marks details of a student in a text file

def result():
    f=open('mark.txt','w+')
    c=0
    f.write('name\tcomputer\tmaths\tenglish')
    while c<2:
        k=input('enter student name :')
        cs=int(input('enter computer mark:'))
        ma=int(input('enter maths mark :'))
        en=int(input('enter english mark :'))
        n='\n'+k+'\t\t'+str(cs)+'\t\t'+str(ma)+'\t\t'+str(en)
        f.write(n)
        print('record added ')
        c+=1
    f.seek(0)
    g=f.readlines()
    for i in g:
        print(i)
    f.close()
result()
