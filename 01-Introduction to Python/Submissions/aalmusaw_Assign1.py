# Student Name: Ali Al-Musawi
# Username: aalmusaw
# This program receives user input and computes the area of a square/triangle minus the area of an inscribed circle.
from math import *
SquareOrTriangle = input("Is your circle inscribed in a square or a triangle? ")  # Prompts User Input
if SquareOrTriangle.lower() == "s" or SquareOrTriangle.lower() == "square":
    # Compute Square Algorithm
    SqSideLength = input("The square's side length: ")
    if SqSideLength.isnumeric():  # Check for a numeric input
        while int(SqSideLength) <= 0:  # Check for a positive input
            SqSideLength = input("The side length must be a positive integer. The square's side length: ")
        else:
            Circle1Radius = (1/2)*int(SqSideLength)  # The square side length = circle diameter = 2*radius.
            Circle1Area = round(pi*Circle1Radius**2, 3)  # Computes the area of the inscribed circle to 3 decimal places.
            print('The area of the inscribed circle is', Circle1Area, 'units squared')
            SquareArea = int(SqSideLength)**2  # Computes the area of the square inscribing the circle.
            Algorithm1Area = round(SquareArea - Circle1Area, 3)  # Computes the desired area to 3 decimal places.
            print('The area of the square minus the area of the inscribed circle is', '%.3f' % Algorithm1Area,'units squared')
    else:
        print('Only positive integers are allowed as input. Please restart the program.')
elif SquareOrTriangle.lower() == "t" or SquareOrTriangle.lower() == "triangle":
    # Compute Triangle Algorithm
    # Create empty lists to contain the coordinates of the vertices.
    Vertex1 = []
    Vertex2 = []
    Vertex3 = []
    Vertices = [Vertex1, Vertex2, Vertex3]

    # This loop repeats for each vertex of the triangle; after 3 valid iterations, the 4th iteration will not occur.
    counter = 1
    while counter < 4:
        print("Enter the following values for Vertex ", counter,": ")
        UserInputx = input("Enter the x-coordinate: ")
        UserInputy = input("Enter the y-coordinate: ")
        #  This validates the input to ensure it is numeric and non-negative for both x, y.
        if (not(UserInputx.isnumeric()) or int(UserInputx) < 0) or (not(UserInputy.isnumeric()) or int(UserInputy) < 0):
            print("Only Non-negative integers are allowed!")
        else:
            Vertices[counter-1].append(int(UserInputx))
            Vertices[counter-1].append(int(UserInputy))
            counter = counter+1


    def geolength(x1, x2, y1, y2):  # Define a function that computes the distance between two points
        return sqrt((x1 - x2)**2 + (y1 - y2)**2)  # This is the Euclidean distance formula for two points on a plane.
    # Compute the length of the triangle's first, second, and third side respectively.
    TrSideLength1 = geolength(Vertex2[0], Vertex3[0], Vertex2[1], Vertex3[1])
    TrSideLength2 = geolength(Vertex1[0], Vertex3[0], Vertex1[1], Vertex3[1])
    TrSideLength3 = geolength(Vertex1[0], Vertex2[0], Vertex1[1], Vertex2[1])
    TrianglePerimeter = TrSideLength1+TrSideLength2+TrSideLength3

    # Compute the x-coordinate of the circle's centre.
    Circle2Centrex = ((TrSideLength1*Vertex1[0] + TrSideLength2*Vertex2[0]\
                                 + TrSideLength3*Vertex3[0])/TrianglePerimeter)
    # Compute the y-coordinate of the circle's centre.
    Circle2Centrey = ((TrSideLength1*Vertex1[1] + TrSideLength2*Vertex2[1]\
                                 + TrSideLength3*Vertex3[1])/TrianglePerimeter)

    print('The circle is centred at (', '%.2f' % Circle2Centrex, ',', '%.2f' % Circle2Centrey, ')')

    # Compute the Area of the circle using Heron's formula.
    HalfTrPerimeter = TrianglePerimeter*0.5
    Circle2Radius = sqrt((HalfTrPerimeter)*(HalfTrPerimeter-TrSideLength1)*(HalfTrPerimeter-TrSideLength2)\
                             *(HalfTrPerimeter-TrSideLength3))/HalfTrPerimeter
    Circle2Area = pi*Circle2Radius**2
    print('The area of the inscribed circle is', '%.4f' % Circle2Area, 'units squared')

    # Compute the Area of the triangle rounded to 4 decimal places.
    TriangleArea = Circle2Radius*HalfTrPerimeter
    print('The area of the triangle is', '%.4f' % TriangleArea, 'units squared')

    # Compute the desired area rounded to 3 decimal places.
    Algorithm2Area = round(TriangleArea - Circle2Area, 3)
    print('The area of the triangle minus the inscribed circle is', '%.3f' % Algorithm2Area, 'units squared')
else:
    print('Sorry, your input was:', SquareOrTriangle, '. This program accepts one of "square" or "triangle"')
