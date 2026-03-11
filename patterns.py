class Patterns(object):
 
    def pattern1(self,a,b):
        for i in range(0,a):
            for j in range(0,b):
                print('*',end='')
            print()

    def pattern2(self,a):
        for i in range(1,a+1):
            for j in range(0,i):
                print('*',end='')
            print()    

    def pattern3(self,a):
        for i in range(1,a+1):
            l=1
            for j in range(0,i):
                print(l,end=' ')
                l+=1
            print()   

    def pattern4(self,a):
        for i in range(a,0,-1):
            for j in range(0,i):
                print('*',end='')
            print()             
        



#a=No. of row, b=No. of columm
k=Patterns()
k.pattern4(5)              