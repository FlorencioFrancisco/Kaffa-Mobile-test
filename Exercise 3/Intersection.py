def RetangleIntersect (retangleA, retangleB):
    retangleA = FormatRetangle(retangleA) # format retangles
    retangleB = FormatRetangle(retangleB)
    b1 = retangleB[0]                         # define the 4 vertices of the second retangle
    b2 = retangleB[1]
    b3 = [retangleB[0][0], retangleB[1][1]]
    b4 = [retangleB[1][0], retangleB[0][1]]
                                              
    if (PointInsideRetangle(b1, retangleA)):# verify if any of the vertices are inside the first retangle
        return True
    if (PointInsideRetangle(b2, retangleA)):
        return True
    if (PointInsideRetangle(b3, retangleA)):
        return True
    if (PointInsideRetangle(b4, retangleA)):
        return True
    return False

def PointInsideRetangle(point, retangle): # verify if a given point is inside a retangle
    a1 = retangle[0]
    a2 = retangle[1]
    if ((point[0]>=a1[0]) & (point[0]<=a2[0])):
        if ((point[1]>=a1[1]) & (point[1]<=a2[1])):
            return True
    return False

def FormatRetangle(retangle): # formats the string in the format (x,y;x,y) into a 2d array
    retangle = retangle.replace('(','')
    retangle = retangle.replace(')','')
    retangle = retangle.replace(' ','')
    formatted = retangle.split(';')
    formatted[0] = formatted[0].split(',')
    formatted[1] = formatted[1].split(',')
    formatted[0] = list(map(int,formatted[0]))
    formatted[1] = list(map(int,formatted[1]))
    return formatted

retangleA = input('Type the coordinates of retangle A:\nEx: (x,y;x,y)\n ')
retangleB = input('Type the coordinates of retangle B:\nEx: (x,y;x,y)\n ')

if (RetangleIntersect(retangleA, retangleB)):
    print("A anb B Intersect")
else:
    print("A and B don't intersect")

# A = (3 ,5;11,11) B = (7,2; 13,7) C = (11,11;15,13) 
