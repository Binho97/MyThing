print("Pattern A")
def pattern(A):
     for i in range(1, A):
         for j in range(1, i + 1):
             print(j, end= " ")
         print("\r")
pattern(7)
print("\r")

print("Pattern B")

def pattern(B):
    for i in range(B, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
 
        print("\r")
 
pattern(6)


