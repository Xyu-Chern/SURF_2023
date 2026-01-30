import openai
import os

# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv())
openai.api_key =""
os.environ["OPEANAI_API_KEY"]=""
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.chains import ConversationChain

from langchain.agents.agent_toolkits import create_python_agent
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0.9,OPENAI_API_KEY=openai.api_key)
model="gpt-3.5-turbo-0613"

prompt = 'from typing import List\ndef has_close_elements(numbers: List[float], threshold: float) -> bool:\n    """ Check if in the given list of numbers, there are any two numbers closer to each other than the given threshold.\n\n    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)\n    False\n    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)\n    True\n    """\n'
canonical_solution=" for idx, elem in enumerate(numbers): for idx2, elem2 in enumerate(numbers): if idx != idx2: distance = abs(elem - elem2) if distance < threshold: return True return False "
test = " METADATA = { 'author': 'jt', 'dataset': 'test' } def check(candidate): assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False "


# prompt template 1
first_prompt = ChatPromptTemplate.from_template(
    "I want you to act as a python Expert.\
     I will provide you with all the information needed about my technical problems,\
     and your role is to solve my problem by writing code. \
     You should use your computer science and algorithm knowledge to solve my problem.\
     Try to avoid any explanation, only use them by noting when necessary. \
     Your answer should only contain code\
     I will provide problem information by following format:\
     {prompt}: input for the model containing function header and docstrings."
)

# chain 1
chain_one = LLMChain(llm=llm, prompt=first_prompt,
                     output_key="raw_code"
                    )

# prompt template 2
second_prompt = ChatPromptTemplate.from_template(
    "I want you to act as a python Expert.\
     I will provide you with technical problems and corresponding solution codes.\
     Your task is to optimize the code. You should use your computer science and algorithm knowledge to complete this task.\
     If there is an error in the code, please correct the error\
     Try to avoid any explanation, only use them by noting when necessary. \
     Your answer should only contain code\
     I will provide problem and solution code by following format:\
     \n{prompt}: input for the model containing function header and docstrings.\
     \n{raw_code}:code that needs to be optimized"
)
# chain 2
chain_two = LLMChain(llm=llm, prompt=second_prompt,
                     output_key="optimized_code"
                    )
# prompt template 3
third_prompt = ChatPromptTemplate.from_template(
    "I want you to act as a python Expert.\
     I will provide you the canonical code and my own optimized code\
     Your task is to judge whether both can solve the same problem.\
     You should use your computer science and algorithm knowledge to complete this task.\
     Your task is to judge whether both can solve the same problem then generate final code\
     Try to avoid any explanation, only use them by noting when necessary. \
     Your answer should only contain code\
     I will provide the canonical code and my own optimized code by following format:\
    \n{optimized_code}:my own optimized code\
    canonical_solution:for idx, elem in enumerate(numbers): for idx2, elem2 in enumerate(numbers): if idx != idx2: distance = abs(elem - elem2) if distance < threshold: return True return False"
)
# chain 3
chain_three = LLMChain(llm=llm, prompt=third_prompt,
                       output_key="final_code"
                      )

overall_chain = SequentialChain(
    chains=[chain_one, chain_two, chain_three],
    input_variables=["prompt"], #会跟着一起输出，而且输入变量必须要有，没有会报错
    output_variables=["raw_code","optimized_code","final_code"],
    verbose=True
)#verbose是调试用来显示进程的，一般改成False
print(overall_chain(prompt))#输出语句

final_code = overall_chain(prompt)["final_code"]

# prompt 4
agent = create_python_agent(
    llm,
    tool=PythonREPLTool(),
    verbose=True
)

agent.run(f"""I will provide you the final code and the test fuction\
     Run the final code to get the result,\
     and use the test function in test to verify whether the result satisfies the problem.\
     Output true if satisfied, false if not satisfied: {final_code},{test}""")
