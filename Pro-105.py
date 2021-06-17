import math
import csv
location = input("Enter file location :- ")
with open(location,newline="") as f :
  reader = csv.reader(f)
  fileData = list(reader)

data = fileData[0]

def mean(data):
  n = len(data)
  total = 0
  for x in data :
    total += int(x)
  mean = total/n
  return(mean)

squaredList=[]

for number in data :
  a = int(number) - mean(data)
  a = a**2
  squaredList.append(a) 

sum = 0

for i in squaredList :
  sum += i


n1 = sum/(len(data)-1)

standardDev = math.sqrt(n1)
print(standardDev)
