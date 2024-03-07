# -*- coding: utf-8 -*-
"""

LLM Demo
model.py

"""



!pip install ctransformers>=0.2.24

from ctransformers import AutoModelForCausalLM

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = AutoModelForCausalLM.from_pretrained("TheBloke/CodeLlama-13B-Instruct-GGUF", model_file="codellama-13b-instruct.Q4_K_M.gguf", model_type="llama", gpu_layers=0)

prompt = """ [INST] Write code to solve the following coding problem that obeys the constraints and passes the example test cases. Please wrap your code answer using ```:
{Given a string, write a python function to check if it is palindrome or not. A string is said to be a palindrome if the reverse of the string is the same as the string. For example, “radar” is a palindrome, but “radix” is not a palindrome. }
[/INST]"""
print(llm(prompt))

!pip install langchain

from langchain.llms import CTransformers
llm = CTransformers(model="TheBloke/CodeLlama-13B-Instruct-GGUF", model_file="codellama-13b-instruct.Q4_K_M.gguf", model_type="llama")

from langchain import PromptTemplate,  LLMChain

template = """
              [INST] Write code to solve the following coding problem that obeys the constraints and passes the example test cases. Please wrap your code answer using ```:
              {text}
              [/INST]
           """

prompt = PromptTemplate(template=template, input_variables=["text"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

text1 = """
Given a string, write a python function to check if it is palindrome or not. A string is said to be a palindrome if the reverse of the string is the same as the string. For example, “radar” is a palindrome, but “radix” is not a palindrome.
"""

print(llm_chain.run(text1))

text2 ="""
Given a string str, find the length of the longest substring without repeating characters.
For “ABDEFGABEF”, the longest substring are “BDEFGA” and “DEFGAB”, with length 6.
For “BBBB” the longest substring is “B”, with length 1.
For “GEEKSFORGEEKS”, there are two longest substrings shown in the below diagrams, with length 7
"""
print(llm_chain.run(text2))

##################################################
## helper function (nicer printing)
##################################################

def pretty_print(s):
    print("Output:\n" + 80 * '-')
    print(textwrap.fill(tokenizer.decode(s, skip_special_tokens=True),80))
