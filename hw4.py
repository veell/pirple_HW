
myUniqueList = []
#Function that adds only unique elements to myUniqueList
def addUniq(thing):
    if myUniqueList.count(thing) == 0: #if occurences of parameter is 
        myUniqueList.append(thing)
        return True
    else:
        return False


#Testing this function
print(addUniq(1))
print(myUniqueList)
print(addUniq(7))
print(myUniqueList)
print(addUniq(1))
print(myUniqueList)
print(addUniq(78))
print(myUniqueList)
print(addUniq("hello"))
print(myUniqueList)
print(addUniq("hello"))
print(myUniqueList)