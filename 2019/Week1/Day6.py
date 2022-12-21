lst = [(el.split(')')) for el in open('../input.txt').read().splitlines()]

class Tree:

    def __init__(self):
        self.data = []
        self.names = []
        self.children = []

    def Addleaf(self, leaf):
        self.data.append(leaf)
        self.names.append(leaf.name, leaf.child)


    def FindLeaf(self, name):
        leaf = self.data[name]
        return(Leaf)
    
    def FindFather(self, name):
        father = ''
        for leaf in self.data:
            for child in leaf.children:
                if child = name:
                    father = leaf
                    break
        return(father)
    
    def IsChild(self, child, father):
        father.children.append


    def __str__(self):
        s = ''
        for el in self.data:
            s += str(el)
        return(s)

        
class Leaf:

    def __init__(self, name, child):
        self.count = 0
        self.name = name
        self.children = [child]
    
    def AddChild(self, child):
        self.count += 1
        self.children.append(child)
    
    def __str__(self):
        return(self.name)


T = Tree()
leaf = Leaf(lst[0][0], lst[0][1])
T.Addleaf(leaf)
newleaf = Leaf(lst[1][0], lst[1][1])
if newleaf.name in T.names:
    father = T.FindFather(newleaf.name)
    T.IsChild(newleaf, father)


# for l in lst:
#     leaf = Leaf(l[0], l[1])
#     if leaf.name not in T.names:
#         pass
        
#     T.Addleaf(leaf)
s = str(T)
