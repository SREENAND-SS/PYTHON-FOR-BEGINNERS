#program to shift names of science student from a given text file to other one
def shift_name():
    f=open('admission.txt','r')
    f1=open('science.txt','w')
    k=f.readlines()
    f1.write('ADMN_NO\t\tNAME\t\tSTREAM\n')
    for i in k:
        d=i.split()

        if 'science' in d or 'SCIENCE' in d:
            f1.write(i)

    f.close()
shift_name()
