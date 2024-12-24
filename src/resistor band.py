band1=input("Enter 1st band color")
print(band1)
band2=input("Enter 2nd band color")
print(band2)
band3=input("Enter 3rd band color")
print(band3)
band4=input("Enter 4th band color")
print(band4)

colors = {"brown":1,"black":0,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}

print(colors [band1],
colors [band2],
colors [band3],
colors [band4],    
)

value = (colors[band1]*10+colors[band2])*10**colors[band3]
print(value)
