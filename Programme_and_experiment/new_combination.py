import os
import openai
from datasets import load_dataset
from dotenv import load_dotenv, find_dotenv
import ast

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')


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


dataset_org = load_dataset("openai_humaneval")
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
    feedback=""
    for i in range(3):
        student_system_message = f"""
        You are now a smart programmer who needs to output the correct code in Python mode according to user requirements\
        Now you need to write a Python code according to the requirement\
        
        Please follow these steps\
        Step 1 - Please read the code you previously wrote and the feedback from the teacher first\
        and learn from the mistakes you made before \
        ensuring that you will not make the same mistakes again \
        If the teacher told you that you were right, skip this step \
        Step 2 - Based on the knowledge you have learned, write a Python code\
        that meets the requirements according to the code requirements again\
        If the teacher told you that you were right, skip this step \
        Step 3 - Just output the code part answer as a string \
        Do not print the examples in the requirement \
        If the teacher told you that you were right, just output your latest answer in your previous code \

        You must not do following things\
        You must not generate any explanations\
        Do not appear any word like "Here's the code you requested:"\
        Explanations are forbidden before ```\
        if you want to generate something which is not coding\
        please add the signal#\
        please add # before the word,python\
        
        after you genenrate the code\
        you will be given feedback \
        carefully study the feedback and generate the new code
        
        The customer service query will be delimited with \
        {delimiter} characters.\
        """

        student_user_message = f"""
        a profesoor have give some feedback\
        the content is {feedback}\
        Please generate the code\
        the code meaning is {requirments[key[0]]}\
        you shuold just give the code without any explanation or hint so that i can directly use\
        
        
        """

        messages_student = [{'role': 'system','content': student_system_message},
                            {'role': 'user','content': f"{delimiter}{student_user_message}{delimiter}"},]
        response = get_completion_from_messages(messages_student)
        
        evaluator_system_message = f"""
        You are now a experinced professor in  Python. \
        Your purpose is to coach students, point out their problems, and provide suggestions for correction. \
        Now that a student has completed the assignment you assigned, \
        you have been told whether the student's answer is correct or not. \

        If the student's answer is correct, please let him know. \
        If the student's answer is incorrect, \
        please indicate that the answer is incorrect and provide feedback to help the student better correct his mistake. \

        Remenber: Do not judge whether the student's code is correct or incorrect on your own. \
        Please strictly follow the information provided to you \
        whether the student's answer is correct or not to make the judgment. \
        """
        
        evaluator_user_message = f"""
        the code meaning is {requirments[key[0]]}\
        previous code is {response}\
        please anaylsize whether the code is correct\
        give the feedback to help me learn and output the corrct code
        
        """
        messages_evaluator = [{'role': 'system','content': evaluator_system_message},
                            {'role': 'user','content': f"{delimiter}{evaluator_user_message}{delimiter}"},]
        feedback = get_completion_from_messages(messages_evaluator)
    response = get_completion_from_messages(messages_student)
    return response


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


s = 0
l=len(list)
for i in range(l):
    m = test_code(list[i])
    print("m=",m)
    s = s + m
    print("s=",s)
    acc = s/(i+1)
    print("acc=",acc)
