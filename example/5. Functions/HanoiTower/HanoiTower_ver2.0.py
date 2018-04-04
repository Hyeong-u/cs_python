#Declare variables
a = []
b = []
c = []
m = [0] # Number of moves
v = [0, 0, 0, 0]


#Input number of rings
print("Type number of rings.", end=' ')
rings = int(input())


#Make List
for i in range(rings):
    a.append(rings-i)
v[0] = rings


#Define function
def HanoiTower(n, g1, g2, g3):    
    if n == 1:
        g3.append(g1.pop())
        m[0] += 1
    else:
        if n%2 == 0:
            v[1] = g1
            v[2] = g3
            v[3] = g2
            HanoiTower(n-1, v[1], v[2], v[3])
            g3.append(g1.pop())
            m[0] += 1
            if n == 2:
                HanoiTower(n-1, v[3], v[1], v[2])
            else:
                HanoiTower(n-1, v[2], v[3], v[1])
        else:
            v[1] = g1
            v[2] = g3
            v[3] = g2
            HanoiTower(n-1, v[1], v[2], v[3])
            g3.append(g1.pop())
            m[0] += 1
            HanoiTower(n-1, v[2], v[1], v[3])
            

        
#Main program
HanoiTower(rings, a, b, c)
print("a = ",a)
print("b = ",b)
print("c = ",c)
print("Number of moves : ", m[0])

