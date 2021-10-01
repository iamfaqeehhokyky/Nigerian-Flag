from turtle import *

screen = Turtle()
bgcolor("green")
speed()

hideturtle()
penup()
backward(240)
left(90)
backward(220)
right(90)
pendown()

pensize(2)
pencolor("#ff6b21")

#First Chamber
begin_fill()
for i in range(2):
    forward(300)
    left(90)
    forward(20)
    left(90)
fillcolor("#934a05")
end_fill()

left(90)
forward(20)
right(90)
forward(50)

#Second Chamber
begin_fill()
for i in range(2):
    forward(200)
    left(90)
    forward(20)
    left(90)
fillcolor("#934a05")
end_fill()

left(90)
forward(20)
right(90)
forward(50)

#Third Chamber
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(20)
    left(90)
fillcolor("#934a05")
end_fill()

#Designing Pole
left(90)
forward(20)
right(90)
forward(40)

pencolor("#ff6b21")
left(90)

begin_fill()
for i in range(2):
    forward(400)
    right(90)
    forward(20)
    right(90)
fillcolor("#808080")
end_fill()

forward(400)
right(90)
forward(20)
right(90)
forward(10)
left(90)

pencolor("#ffffff")
#Green Part
begin_fill()
for i in range(2):
    forward(100)
    right(90)
    forward(180)
    right(90)
fillcolor("#0cff00")
end_fill()

forward(200)
right(90)

#White Part
begin_fill()
for i in range(2):
    forward(180)
    right(90)
    forward(100)
    right(90)

fillcolor("#ffffff")
end_fill()

left(90)


#Green Part
begin_fill()
for i in range(2):
    forward(100)
    right(90)
    forward(180)
    right(90)
fillcolor("#0cff00")
end_fill()

penup()
backward(183)
right(90)
forward(125)
right(180)

pendown()
#Draw Letter N
pencolor("#ffffff")
forward(90)
right(150)
forward(103)
left(150)
forward(90)

penup()
hideturtle()
right(90)
forward(105)
right(90)
forward(25)
left(90)

#Draw Letter G
pencolor("#0cff00")
pendown()
backward(40)
left(190)
forward(7)
for i in range(7):
    left(5)
    forward(3)
left(45)
forward(70)
for i in range(7):
    left(10)
    forward(3)
left(20)
forward(40)
for i in range(7):
    left(10)
    forward(3)
left(20)
forward(30)
left(90)
forward(35)
penup()
hideturtle()
backward(85)
pendown()
right(90)
backward(10)

#Draw Letter N
pencolor("#ffffff")
forward(90)
right(150)
forward(103)
left(150)
forward(90)







done()
