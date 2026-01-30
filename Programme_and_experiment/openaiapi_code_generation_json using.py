import os
import openai
from datasets import load_dataset
from dotenv import load_dotenv, find_dotenv
import ast
import json
import codecs,yaml

_ = load_dotenv(find_dotenv())
openai.api_key =""


# def read_yaml(config_file):
#     with codecs.open(config_file, 'r',encoding='utf-8') as f:
#         config = yaml.load(f,Loader=yaml.FullLoader)
#     return config

# cfg = read_yaml('config_parameter_key.yaml')
# openai.api_key = cfg['key']

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

# You can choose the dataset in any of bellow

# dataset_org = load_dataset("openai_humaneval")
dataset_org = load_dataset("mxeval/mbxp","python")

dataset_renew = dataset_org["test"]
list = []
for sample in dataset_renew:
    list.append(sample)
key = ['prompt', 'canonical_solution', 'test', 'entry_point']


# print(list[0]['canonical_solution'])
# print(list[0]['test'])
# print(list[0]['entry_point'])
# print(list[0][ 'prompt'])

def generate_code(requirments):
    delimiter = "####"
    system_message = f"""
    You are now a smart programmer who needs to output the correct code in Python mode according to user requirements\
    The customer service query will be delimited with \
    {delimiter} characters.\
    """

    user_message = f"""
    I want you to generate my code \
    the privious code and meaning is {requirments[key[0]]}\
    You must output the missing code and output the complete code\
    You must output the code in JSON format \
    and generate like code:,explanation:\
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
    string_response = get_completion_from_messages(messages)
    json_response = json.loads(string_response)
    code_cleared = json_response["code"]
    return code_cleared

print(generate_code(list[4]))

def get_functions(code_str):
    functions = []
    parsed = ast.parse(code_str)
    for node in parsed.body:
        if isinstance(node, ast.FunctionDef):
            name = node.name
            args = [arg.arg for arg in node.args.args]
            body = ast.unparse(node.body)
            functions.append((name, args, body))
    return functions


def test_code(requirments):
    code_g = generate_code(requirments)
    code_t = requirments[key[2]]
    code_t_d = get_functions(requirments[key[2]])[0][0]
    code_composed = code_g + "\n" + code_t + "\n" + f"{code_t_d}({requirments[key[3]]})"
    try:
        exec(code_composed)
        reward = 1  # True
    except:
        reward = 0  # False
    return reward
