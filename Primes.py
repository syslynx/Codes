# Importing datetime module so as to check how much time the algorithm takes
# I'd comment out the unimportant code
# from datetime import *
def lschk (ls,n):
    z=2
    for i in ls:
        if n%i==0:
            z+=1
            break
    return z
ur = int(input("Enter Upper Limit : "))
# t1=datetime.now()
nos,nums=0,[2]
for j in range (3,ur+1,1):
    if lschk (nums,j)==2:
        nums.append(j)
print(nums)
print("No. of Primes : ",len(nums))
# t2=datetime.now()
# print(t2-t1)
