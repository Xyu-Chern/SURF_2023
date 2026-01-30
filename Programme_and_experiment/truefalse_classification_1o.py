import json
import pandas as pd

with open("my_dict.json","r") as file:
    data=json.load(file)
# print(data)

data_t={}
data_f={}

data_copy={}
for i in range(115):
    data_copy["id"+str(i+1)]=i+1



for id in data.keys():
    for m in range(1,116):
        i="id"+str(m)
        if i==id:
            del data_copy[id]

# print(data_copy)

for id in data.keys():
    if data[id][0]=="True":
        data_t[id]=data[id][1]
        data_t["id4"]=[0,0,0,0,0]
        data_t["id38"]=[0,0,0,0,0]
        data_t["id105"]=[0,0,0,0,0]
    else:
        data_f[id]=data[id][1]

import torch
sum_t=torch.tensor([0,0,0,0,0])

for i in data_t.values():
    sum_t=sum_t+torch.tensor(i)
acc_t=sum_t/len(data_t.values())
print(acc_t)

sum=torch.tensor([0,0,0,0,0])
for i in data_f.values():
    sum=sum+torch.tensor(i)
acc_f=sum/len(data_f.values())
print(acc_f)

acc_all=(sum+sum_t)/115
print(acc_all)

for id in data.keys():
    print(f"{id}",data[id])
