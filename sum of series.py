input_data = open('input.txt' , 'r')
data = input_data.read()
data = data.split()

L = int(data[0])
E = int(data[1])
S = int(data[2])
sum = 0
a = 0
c = float(round(1.6449, E))
b  = 1
if a  > 0 :
    for i in range (1, 2) :
        sum += i
while sum >= c :
    b += 1 

output = open('output.txt', 'w')
output.write(str(b))

input_data.close()
output.close()