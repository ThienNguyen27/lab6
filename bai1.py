s1 = [0,1,2,3,4,5,6,7,8,9]
s2 = [] #add 2
s3 = [] #multiple 2
s4 = [] #shift 2

for i in range(len(s1)): 
    a = int(s1[i]) + 2
    s2.append(a)
    
for i in range(len(s1)): 
    b = int(s1[i]) * 2
    s3.append(b)
for i in range(len(s1)):
    if i+2 not in s1:
        i=i-len(s1)
    s4.append(i+2)
    
print(f"Add 2: {s2}")
print(f"Multiply by 2: {s3}")
print(f"Shift 2: {s4}")

