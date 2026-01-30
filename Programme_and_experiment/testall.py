import ast
import json

with open('all_id_record_nopromptcopy.txt','r', encoding="utf-8") as f:
    file=f.readlines()


list0=[]
for i in file:
    if i != '\n':
        list0.append(i)
# print(list0)
dict0={}
list1=[]
mark_confirm_true="mark:True\n"
mark_confirm_false="mark:False\n"
test_code="test code\n"
method1='0 baseline\n'
method2="1 summary_prompt+decomposition\n"
method3="2 summary_prompt+mtbp_orignal\n"
method4="3 summary_promptdecomposition+chainofthought\n"
method5="4 summary_prompt+mtbp_orignal+chainofthought\n"

for i in range(115):
    id_confirm="id_number= id"+str(i+1)+"\n"
    for file_string in range(len(list0)):
        if id_confirm == list0[file_string]:
            list1.append(file_string)
list1.append(file_string+1)

def get_function_name(code):
    names = []

    tree = ast.parse(code)

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            names.append(node.name)
        elif isinstance(node, ast.ClassDef):
            names.append(node.name)

    return names[0]

def eval_reward(m_copy):
    try:
        exec(m_copy)
        reward = 1  
    except:
        reward = 0 
    return reward

for i in range(len(list1)-1):
    try:
        list3=[]
        list2=[]
        for file_string in range(list1[i]+1,list1[i+1]-2):
            if mark_confirm_true == list0[file_string]:
                list3.append("True")
            if mark_confirm_false == list0[file_string]:
                list3.append("False")
            if test_code == list0[file_string]:
                list2.append(file_string)
            if method1== list0[file_string]:
                list2.append(file_string)
            if method2== list0[file_string]:
                list2.append(file_string)
            if method3== list0[file_string]:
                list2.append(file_string)
            if method4== list0[file_string]:
                list2.append(file_string)
            if method5== list0[file_string]:
                list2.append(file_string)
        list2.append(file_string+1)
        # print(list2)
        test_string=""
        for m in range(list2[0]+1,list2[1]):
            test_string=test_string+list0[m]
        reward=[]
        for p in range(1,6):
            method0=""
            for m in range(list2[p]+1,list2[p+1]):
                method0=method0+list0[m]
            # print(method0)
            name=get_function_name(method0)
            q= test_string +method0+"check("+f"{name})"+"\n"
            print(q)
            reward.append(eval_reward(q))
        list3.append(reward)
        dict0["id"+str(i+1)]=list3
    except:
        pass

print(dict0)

json_data = json.dumps(dict0)
with open( "my_dict.json", "w") as file:
    file.write(json_data)
