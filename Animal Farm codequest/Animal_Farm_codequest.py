import sys #needed for readline function


cases = (int(sys.stdin.readline().rstrip())) #get the first number of cases

for i in range(cases): #go through the other lines
    line = sys.stdin.readline().rstrip()#strips off extra spaces at the end of the line
    
    line = line.split(" ") #split up the line by spaces
    num = int(line[0]) * 2 + int(line[1]) * 4 + int(line[2]) * 4

    print(num)
   
   
        



        