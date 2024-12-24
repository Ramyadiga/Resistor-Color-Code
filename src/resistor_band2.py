import math
import serial
ser = serial.Serial('COM5')
x = ser.read(5).decode()
print(x)

def color_code(r):
    value = str (r)

    val1 = value[0]
    val2 = value[1]
    den = (int (value[0])*10 + int (value[1]))
    exp = math.log10(int (value)/den)
    val3=exp

    match = {0:"black",1:"brown",2:"red",3:"orange",4:"yellow",5:"green",6:"blue",7:"violet",8:"grey",9:"white"}
    print (match[int (val1)],match[int (val2)],match[int (val3)])
    return match[int (val1)],match[int (val2)],match[int (val3)]


v = (int (x)*5)/1024
print(v)
# r = int (v/(float (i)))
# print(r)
# color_code(r)
