import csv
import time
import pandas as pd
df = pd.read_csv('french_dictionary.csv')
start = time.time()
f = open('french_dictionary.csv','r')
reader = csv.reader(f)
french_dictionary ={}
frequency = {}
for i in reader:
  french_dictionary[i[0]] = i[1]

input = open('t8.shakespeare.txt','rt')
output = open('output.txt','wt')
count = 0
for line in input:
  temp = line.split()
  res = []
  for wrd in temp:
    if wrd in french_dictionary:
      res.append(french_dictionary[wrd])
      if wrd in frequency:
        frequency[wrd] += 1
      else:
        frequency[wrd] = 1
      if wrd not in frequency:
        frequency[wrd] = 0
    else:
      res.append(wrd)
  res = ' '.join(res)
  output.write(str(res))
  output.write("\n")



s = df["abide"].unique()
res = []
for i in s:
  if i in frequency:
    res.append(frequency[i])
  else:
    res.append(0)

df["values"] = res
df.to_csv("french_dictionary2.csv")
end = time.time()
print(frequency)
print("The time of execution of above program is :", end-start)
input.close()
output.close()