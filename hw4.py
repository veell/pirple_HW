
myUniqueList = []
#Function that adds only unique elements to myUniqueList
def addUniq(thing):
    if myUniqueList.count(thing) == 0: #if occurences of parameter is in List
        myUniqueList.append(thing)
        return True
    else:
        return False
#Extra
myLeftovers = []
def addUniqWithRejects(thing):
    if myUniqueList.count(thing) == 0: #if occurences of parameter is in List
        myUniqueList.append(thing)
        return True
    else:
        myLeftovers.append(thing)
        return False

#Testing addUniq function
print(addUniq(1))
print(myUniqueList)
print(addUniq(7))
print(myUniqueList)
print(addUniq(1))
print(myUniqueList)
print(addUniq(78))
print(myUniqueList)
print(addUniq("word"))
print(myUniqueList)
print(addUniq("word"))
print(myUniqueList)

#Testing addUniqWithRejects function
#Initializing myUniqueList with empty list
print("test#2")
myUniqueList = []
print(addUniqWithRejects(1))
print(myUniqueList)
print(myLeftovers)
print(addUniqWithRejects(7))
print(myUniqueList)
print(myLeftovers)
print(addUniqWithRejects(1))
print(myUniqueList)
print(myLeftovers)
print(addUniqWithRejects(78))
print(myUniqueList)
print(myLeftovers)
print(addUniqWithRejects("word"))
print(myUniqueList)
print(myLeftovers)
print(addUniqWithRejects("word"))
print(myUniqueList)
print(myLeftovers)