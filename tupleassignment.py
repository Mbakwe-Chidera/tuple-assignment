#indexing
tupleProject = ('list', 'tuple', 'set', 'dictionary')
print(tupleProject[1])

#negative_indexing
tupleProject = ('list', 'tuple', 'set', 'dictionary')
print(tupleProject[-2])

#convert-tuple-values
x = ('list', 'tuple', 'set', 'dictionary')
y = list(x)
y[1] = 'index'
x = tuple(y)
print(x)

#unpacking tuple
tupleProject = ('list', 'tuple', 'set', 'dictionary')
(indexing, unpacking, clear, pop) = tupleProject
print(indexing)
print(unpacking)
print(clear)
print(pop)

#add item converting to list first
tupleProject = ('list', 'tuple', 'set', 'dictionary')
y.append('index')
tupleProject = tuple(y)
print(tupleProject)

#add using tuple to tuple
tupleProject = ('list', 'tuple', 'set', 'dictionary')
y = ('index' ,)
tupleProject +=y
print(tupleProject)

#remove item by converting to list first, remove and convert back to tuple
tupleProject = ('list', 'tuple', 'set', 'dictionary')
y = list(tupleProject)
y.remove('list')
tupleProject = tuple(y)
print(tupleProject)

 #join tuple
tupleProject = ('list', 'tuple', 'set', 'dictionary')
tupleProject2 = ('accessing', 'count', 'join')
tupleProject3 = tupleProject + tupleProject2
print(tupleProject3)

