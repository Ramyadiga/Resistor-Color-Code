import math
import serial
ser = serial.Serial('COM5')

#while true:
read1 = ser.read_until(",",size=5).decode('utf-8')
read2 = ser.read_until(",",size=5).decode('utf-8')
read = read1 + read2
# print(read.split(",")[0])

# x = ser.read(10).decode()
# print(x)  

def color_code(r):
    value = str (r)

    val1 = value[0]
    val2 = value[1]
    den = (int (value[0])*10 + int (value[1]))
    exp = math.log10(int (float(value))/den)
    val3=exp

    match = {0:"\033[37mblack",1:"brown",2:"\033[31mred",3:"orange",4:"\033[33myellow",5:"green",6:"blue",7:"\033[35mviolet",8:"grey",9:"white"}
    print (match[int (val1)],match[int (val2)],match[int (val3)])
    return match[int (val1)],match[int (val2)],match[int (val3)]

x = (read.split(",")[0])
 
v = (int (float(x))*5)/1024
# Given resistance 
r = 150 
i = (5 - v)/r
# print(v)
# print(i)
res = v/i
# print("calculated resistance =",res)
std_r = [10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91]
comb_res = int(str(res)[0] + str(res)[1])

# print(comb_res)
subt = []
for i in std_r:
    subt.append(i-comb_res)
    
# print(subt)
subt_new = []
for i in subt:
    subt_new.append(abs(i))
# print(subt_new)
m=subt_new[0]
for i in subt_new:
    if(i < m):
        m = i
# print(m)

#index of minimum
x = 0
for i in subt_new:
    if i == m:
        # print("x=",x)
        min_index = x
        # print("Index of minimum = ", min_index)
    x = x + 1
    
x1 = 0

for i in std_r:
    if x1 == min_index:
        # print("i=",i)
        c = i
    x1 = x1 + 1

temp = str(res)
den_res = 10 * int(temp[0]) + int(temp[1])
# print(den_res)
mul = res//den_res
# print(mul)
print("Unknown value of resistor is = ", mul*c)
color_code((mul*c))
