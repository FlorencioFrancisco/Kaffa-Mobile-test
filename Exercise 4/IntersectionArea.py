from Intersection import FormatRetangle, PointInsideRetangle, RetangleIntersect

def RetangleIntersectArea (retangleA, retangleB):
    retangleA = FormatRetangle(retangleA) # format retangles
    retangleB = FormatRetangle(retangleB)
    intersection_retangle = FindIntersectionVertices(retangleA, retangleB)
    side = intersection_retangle[0][0] - intersection_retangle[1][0] +1
    if (side < 0):
        side = intersection_retangle[1][0] - intersection_retangle[0][0] +1
    high = intersection_retangle[1][1] - intersection_retangle[0][1] +1
    if (high <0):
        high = intersection_retangle[0][1] - intersection_retangle[1][1] +1
    print(intersection_retangle)
    print(f'side: {side} - high: {high}')
    return side * high

def FindIntersectionVertices (retangleA, retangleB):
    verticesA=[]
    verticesB=[]
    verticesB.append(retangleB[0])                         # define the 4 vertices of the second retangle
    verticesB.append(retangleB[1])
    verticesB.append([retangleB[0][0], retangleB[1][1]])
    verticesB.append([retangleB[1][0], retangleB[0][1]])
    verticesA.append(retangleA[0])                         # define the 4 vertices of the first retangle)
    verticesA.append(retangleA[1])
    verticesA.append([retangleA[0][0], retangleA[1][1]])
    verticesA.append([retangleA[1][0], retangleA[0][1]])

    intersection_retangle = []
    for vertice in verticesA:
        if (PointInsideRetangle(vertice, retangleB)):
            intersection_retangle.append(vertice)
            break
    
    for vertice in verticesB:
        if (PointInsideRetangle(vertice, retangleA)):
            intersection_retangle.append(vertice)
            break
    
    return intersection_retangle
    
retangleA = input('Type the coordinates of retangle A:\nEx: (x,y;x,y)\n ')
retangleB = input('Type the coordinates of retangle B:\nEx: (x,y;x,y)\n ')

if (RetangleIntersect(retangleA, retangleB)):
    print("the area of intersection between A and B is: ",RetangleIntersectArea(retangleA, retangleB))
else:
    print("A and B don't intersect")

# A = (3 ,5;11,11) B = (7,2; 13,7) C = (11,11;15,13)

# areaOfIntersection(A, B) = 15
# areaOfIntersection(A, C) = 1
