#practice
#q1
i = 1
while i<=100: #stop condition
    print(i)
    i+=1

#2
i=100
while i>=1:
    print(i)
    i-=1

#3
i=1
while i<=10:
    print(3*i)
    i+=1

#4
nums =[1,4,9,16,25,36,49,64,81,100]
idx =0
while idx <len(nums):
   print(nums[idx]) #nums[0]
   idx +=1

#5 traverse
heroes = ["ironman", "thor", "superman", "batman"]
idx =0
while idx < len(heroes):
    print(heroes[idx])
    idx +=1


#tuple using loop 

nums = ( 1,4,9,16,25,36,49,64,81,100)

x =36

i=0
while i<len(nums):
    print(nums[i])
    i +=1

# next condition 

nums = ( 1,4,9,16,25,36,49,64,81,100)

x=36
i=0
while i< len(nums):
    if(nums[i]==x):
        print("Found at idx",i)
        break
    else:
        print("finding..")
    i+=1
print("end of loop")

#continue
i=1
while i <=5:
    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1

i=1
while i <=5:
    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1

i=1
while i <=5:
    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1

i=1
while i <=5:
    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1


i=1
while i <=5:
    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1

i=1
while i <=5:
    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1

i=1
while i <=5:
    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1

i=1
while i <=5:
    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1

i=1
while i <=5:
    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1

i=1
while i <=5:
    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1

i=1
while i<=10:
    if(i%2 !=0):
        i+=1
        continue
    print(i)
    i+=1
