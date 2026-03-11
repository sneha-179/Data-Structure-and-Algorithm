class Hash(object):
    def __init__(self,bucket):
        self._buck=bucket
        self.table=[]
    
    def tableCreate(self):
        i=0
        for i in range(self._buck):
            self.table.append([])
            

    def HashFunction(self,key):
        return (key% self._buck)

    def insertH(self,key):
        index=self.HashFunction(key)
        self.table[index].append(key)

    def deleteH(self,key):
        index=self.HashFunction(key)
        if key not in self.table[index]:
            return
        self.table[index].remove(key)

    def display(self):
        for i in range(self._buck):
            print(i,end='->> ')
            for j in self.table[i]:
                print(j,end='-> ')
            print()

k=Hash(7)
print(k._buck)
k.tableCreate()
k.insertH(27)
k.insertH(11)
k.insertH(8)
k.insertH(15)
k.display()

