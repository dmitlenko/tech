r = "сонячна погода"
class StringWorker:
    def __init__(self,s):
        self.s = s
    def list(self):
        return self.s.split()
class sub_StringWorker(StringWorker):
    def list(self):
        return list(self.s)
    def sort(self):
        return sorted(self.list())
    
obj1 = StringWorker(r)
obj2 = sub_StringWorker(r)
print('слова:',obj1.list())
print('список:',obj2.list())
print('сортований список:',obj2.sort())
