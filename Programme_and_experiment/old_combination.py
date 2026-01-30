import os
import openai
from datasets import load_dataset
import ast
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')



def gpt(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

dataset_org = load_dataset("openai_humaneval")
dataset_renew=dataset_org["test"]
list=[]
for sample in dataset_renew:
    list.append(sample)


key=[ 'prompt', 'canonical_solution', 'test', 'entry_point']


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


def test_code(requirments,answer):
    code_generate=answer
    code_try=requirments[key[2]]
    code_exe=get_functions(requirments[key[2]])[0][0]
    code_composed=code_generate+ "\n" +code_try+ "\n" + f"{code_exe}({requirments[key[3]]})"
    try:
        exec(code_composed)
        reward = 1 #True
    except:
        reward = 0 #False
    return reward

def collect_messages(message1, message2, mem):
    mem.append({'role': 'student', 'content': message1})
    mem.append({'role': 'teacher', 'content': message2})
    return mem



def generate_code(requirments):
    delimiter = "####"
    mem = []
    req = requirments[key[0]]
    correct_ans = requirments[key[1]]

    for i in range(3):
        actor_prompt = f"""
            You are now a smart student studying Python. \
            Now you need to write a Python code according to the requirement. \
            Please follow these steps: \

            Step 1 - Please read the code you previously wrote and the feedback from the teacher first, and learn from the mistakes you made before, \
            ensuring that you will not make the same mistakes again. \
            If the teacher told you that you were right, skip this step. \
            Step 2 - Based on the knowledge you have learned, write a Python code that meets the requirements according to the code requirements again. \
            If the teacher told you that you were right, skip this step. \
            Step 3 - Just output the code part answer as a string. \
            Do not print the examples in the requirement. \
            If the teacher told you that you were right, just output your latest answer in your previous code. \

            Your previous code and feedback:"{mem}" \
            Requirement:"{req}" \
            """

        ans_from_student = gpt(actor_prompt)
        result_number = test_code(requirments, ans_from_student)
        if result_number == 1:
            result = "Correct"
        else:
            result = "Wrong"

        evaluator_prompt = f"""
                                    You are now a teacher of Python. \
                                    Your purpose is to coach students, point out their problems, and provide suggestions for correction. \
                                    Now that a student has completed the assignment you assigned, \
                                    you have been told whether the student's answer is correct or not. \

                                    If the student's answer is correct, please let him know. \
                                    If the student's answer is incorrect, \
                                    please indicate that the answer is incorrect and provide feedback to help the student better correct his mistake. \

                                    Remenber: Do not judge whether the student's code is correct or incorrect on your own. \
                                    Please strictly follow the information provided to you (whether the student's answer is correct or not) to make the judgment. \
                                    
                                    The original requirement:{req}
                                    The student answer:{ans_from_student}
                                    Standard answer:{correct_ans}
                                    Whether the answer from student is correct or not:{result}

                                    """

        feedback = gpt(evaluator_prompt)
        mem = collect_messages(ans_from_student, feedback, mem)

    final_result = mem[4]["content"]
    return final_result



def test_code_final(requirments):
    code_g=generate_code(requirments)
    code_t=requirments[key[2]]
    code_t_d=get_functions(requirments[key[2]])[0][0]
    code_composed=code_g+ "\n" +code_t+ "\n" + f"{code_t_d}({requirments[key[3]]})"
    try:
        exec(code_composed)
        reward = 1#True
    except:
        reward = 0#False
    return reward

s = 0
for i in range(len(list)):
    m = test_code_final(list[i])
    s = s + m
acc = s/len(list)

print(acc)














