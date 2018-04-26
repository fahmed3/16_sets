def union(a,b):
    return [x for x in a if x not in b] + [y for y in b]

def intersect(a,b):
    return [x for x in a if x in b]

def setDifference(a,b):
    return [x for x in a if x not in b]

def symmetricDif(a,b):
    return [x for x in a if x not in b] + [y for y in b if y not in a]

def cartesian(a,b):
    return [[x,y] for x in a for y in b]

a = [1,2,3]
b = [2,3,4]
print "list A: "+str(a)
print "list B: "+str(b)
print "union:"
print union(a,b)
print "intersection:"
print intersect(a,b)
print "set difference:"
print setDifference(a,b)
print "symmetric difference:"
print symmetricDif(a,b)
print "cartesian product:"
print cartesian(a,b)


a = ['red','yellow','blue']
b = ['red', 'green', 'blue']
print "list A: "+str(a)
print "list B: "+str(b)
print "union:"
print union(a,b)
print "intersection:"
print intersect(a,b)
print "set difference:"
print setDifference(a,b)
print "symmetric difference:"
print symmetricDif(a,b)
print "cartesian product:"
print cartesian(a,b)
