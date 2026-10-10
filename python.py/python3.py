questions = [
  [ 
      "which languages was used to create facebook?", 
      "python", "french","javascript","php", "none", 4
  ]
  [ "how many state are in india ?",[ 28,29,27,34]]
]
      

levels=[100,2000,3000,5000,10000,20000,40000,80000,160000,320000]

for i in range(0,len(questions)):
  question = question(i)
  print(f"questions for Rs.{levels[i]}")
  print(f"a.{question[1]} b.{question[2]}")
  print(f"c.{question[3]}  d.{questions[4]}") 
reply=int(input("enter your answer (1-4)"))
if (reply == questions[-1]):
    print(f"correct answer ,you have won Rs.{levels [i]}")
    if(i ==4):
       money = 10000
    elif(i==9):
       money= 320000
    elif(i==14):
       money=10000000   
else:
  print("wrong answer!")
  breakpoint

     
       
