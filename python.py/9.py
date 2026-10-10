dict= {
    "cat":"a small animal",
    "table" : ["a piece of furniture","list of facts& figures"]
}

print(dict)

marks = {}

x= int(input("enter the no.of phy: "))
marks.update({"phy": x})

y=int(input("enter the no.chem"))
marks.update({"chem": y})

z=int(input("enter the no.Maths"))
marks.update({"Maths": z})

print(marks)