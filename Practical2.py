fh = open('practical2.txt','w')
l = int(input("Enter a length: ")) 
b = int(input("Enter a breadth: "))  
area = l * b 
perimeter = 2 * ( l + b ) 
fh.write("Area of rectangle is: "+str(area)+'\n') 
fh.write("Perimeter of rectangle is:  " + str(perimeter)) 
fh.close()