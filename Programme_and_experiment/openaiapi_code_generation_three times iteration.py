import os
import openai
import json
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

def gpt_student(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

def gpt_teacher(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

def collect_messages(message1, message2):
    global messages
    messages.append({'role': 'student', 'content': message1})
    messages.append({'role': 'teacher', 'content': message2})
    return messages



with open('openai_humaneval', 'r') as file:
    dataset = json.load(file)


correct_number = 0
total_number = 0

for item in dataset:
    total_number += 1
    messages = []
    req = ""
    ans = ""
    correct_ans = ""

    task_id = item['task_id']
    req = item['prompt']
    correct_ans = item['canonical_solution']


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

            Your previous code and feedback:"{messages}" \
            Requirement:"{req}" \
            """



        ans = gpt_teacher(actor_prompt)


        evaluator_prompt = f"""
                    You are now a teacher of Python. \
                    Your purpose is to coach students, point out their problems, and provide suggestions for correction. \
                    Now that a student has completed the assignment you assigned, \
                    you need to check whether the student's answer is correct based on the standard answer. \

                    If the student's answer is correct, please let him know. \
                    If the student's answer is incorrect, \
                    please indicate that the answer is incorrect and provide feedback to help the student better correct his mistake. \

                    Remenber: The standard answer and his answer may not be completely consistent in character, \
                    but his answer may still be correct. Please compare carefully. \
                    If the student's answer is actually consistent with the standard answer, then the student's answer is correct. \

                    The student answer:{ans}
                    Standard answer:{correct_ans}

                    """


        feedback = gpt_teacher(evaluator_prompt)
        messages = collect_messages(ans, feedback)

    final_prompt = f"""
    You are currently a teacher assistant, please read the interaction between student and teacher first. \
    Based on the interaction, determine if the student answered the question correctly in the end? \
    Note that the teacher should clearly state at the end of the interaction whether the student's answer is correct. Please judge based on this. \
    Remember, you can only output 0 or 1. 0 represents wrong and 1 represents correct.
    
    The interaction between student and teacher:{messages}
    
    """

    final_result = gpt_teacher(final_prompt)

    if int(final_result) == 1:
        correct_number += 1



acc = correct_number / total_number
print(acc)


