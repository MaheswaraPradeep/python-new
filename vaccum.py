import numpy as np
def display(room):
    for i in range(len(room)):
        print(room[i])
room=np.random.choice([0,1],size=(4,4))
display(room)
x=y=z=0
while(x<4):
    while(y<4):
        if(room[x][y]==1):
            print("the room",x,y,"is dirty here")
            room[x][y]=0
            print("the room is cleaned")
            z=z+1
        y+=1
    x+=1
    y=0
print("the room is all cleaned now")
print("the cost is",z)
display(room)
