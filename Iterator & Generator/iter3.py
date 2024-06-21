class topten:
    def __init__(self):
        self.num=1
        return None
    def __iter__(self):
        return self
    def __next__(self):
        
        if self.num<=10:
            val=self.num
            self.num +=1
            return val
        else:
            raise StopIteration
        
values= topten()
print(values.__init__())
print(values.__iter__())
for i in values:
    print(i)