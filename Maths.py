
class Maths_for_prakash:
    def __init__(self, lst):
        self.list = lst
        self.count = len(lst)
        self.max= max(lst)
    
    def append(self, x):
        self.list.append(x)
        self.count += 1
        if x> self.max:
            self.max = x


mat = Maths_for_prakash([3,5,7,9,2,3])
print(mat.count)
print(mat.list)
print(mat.max)
print(mat.append(11))
print(mat.count)
print(mat.list)
print(mat.max)



