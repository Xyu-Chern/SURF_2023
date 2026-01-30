#download the datasets from web
import requests
import json

url = "https://github.com/salesforce/CodeGen/blob/main/codegen1/benchmark/mtpb.jsonl"
filename = "mtpb.jsonl"

response = requests.get(url)
response.raise_for_status()

with open(filename, "wb") as file:
    file.write(response.content)

with open(filename, "r") as file:
    data = json.load(file)

# print(data)

data_cleared_str=data["payload"]["blob"]["rawLines"]

# print(len(data_cleared))
# print(type(data_cleared[114]))
# print(data_cleared[114])

data_list=[]

# data_cleared_dict= json.loads(data_cleared_str[114])
# print(data_cleared_dict.keys())

dict_keys=['prompts', 'inputs', 'outputs', 'max_gen_length', 'category', 'name', 'description', 'id']

for i in range(len(data_cleared_str)):
    data_cleared_dict= json.loads(data_cleared_str[i])
    data_list.append(data_cleared_dict)

# print(data_list[0])
# print(type(data_list[0]))


import os
import openai
from dotenv import load_dotenv, find_dotenv
import ast
import json
import codecs,yaml
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion_from_messages(messages,
                                 model="gpt-3.5-turbo",
                                 temperature=0,
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]

data=data_list[1]
print(data)

def summary_prompt(data):
    delimiter = "####"
    system_message = f"""
    You are now a smart languager who needs to summarize the contents according to user requirements\
    The customer service query will be delimited with \
    {delimiter} characters.\
    """

    user_message = f"""
    please understand the content :{data["prompts"]}\
    they are all steps to achieve a goal\
    tell me what the goal is
    """

    messages = [
        {'role': 'system',
         'content': system_message},
        {'role': 'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    response = get_completion_from_messages(messages)

    return response


response=summary_prompt(data)
print(response)

def generate_code(response,data):
    delimiter = "####"
    system_message = f"""
    You are now a smart programmer who needs to output the correct code in Python mode according to user requirements\
    The customer service query will be delimited with \
    {delimiter} characters.\
    """

    user_message = f"""
    I want you to write a python code \
    the task is to write a function\
    the function is named as {data['name']}
    the goal is {response}\
    You must output the code in JSON format \
    and generate with the key: code,explanation\
    please use less than 20 words about explanation\
    You must not give dimension of python in code\
    please confirm that the code has a return\
    in order to distinguish it from your interpretation of the code\
    You must use brace to combine the code and explannation
    """


    messages = [
        {'role': 'system',
         'content': system_message},
        {'role': 'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    code = get_completion_from_messages(messages)
    code = json.loads(code)
    code = code["code"]

    return code

code=generate_code(response,data)
print(code)


def get_functions(code):
    functions = []
    parsed = ast.parse(code)
    for node in parsed.body:
        if isinstance(node, ast.FunctionDef):
            name = node.name

    return name

# print(type(get_functions(code)))

name=get_functions(code)

print(name)




def test_code(code,data):
    input_data=data['inputs']
    output_data=data["outputs"]
    for i in range(len(input_data)):
        reward=1
        code_composed = code+"\n"+f"print({name}"+f"{tuple(list(input_data[i].values()))}=={output_data[i]})"
        exec(code_composed)
        rs=locals()
        print(rs)

    return reward

reward=test_code(code,data)
print(reward)





def mutiplestep_generatewiththought(response):
    delimiter = "####"
    system_message = f"""
    You are now a smart programmer who needs to think and answer  the contents according to user requirements\
    The customer service query will be delimited with \
    {delimiter} characters.\
    """

    user_message = f"""
    please understand the content :{response}\
    please teach me in a consistent style\
    each step followed by a thought\

    """

    messages = [
        {'role': 'system',
         'content': system_message},
        {'role': 'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    mutiple_response = get_completion_from_messages(messages)

    return mutiple_response   
print(response)

mutiple_response=mutiplestep_generatewiththought(response)
print(mutiple_response) 

code=generate_code(mutiple_response,data)
print(code) 










