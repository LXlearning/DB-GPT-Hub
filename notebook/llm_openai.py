import json
import sys
import time

MODEL_NAME = 'gpt-3.5-turbo-0125' #
total_prompt_tokens = 0
total_response_tokens = 0

import os

from openai import OpenAI

with open('/Users/luoxin/Desktop/项目/github/MAC-SQL/data/chatgpt_api.txt', 'r') as f:
    OPENAI_API_KEY = f.read()
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
client = OpenAI()


def api_func(prompt:str):
    global MODEL_NAME
    print(f"\nUse OpenAI model: {MODEL_NAME}\n")
    if 'Llama' in MODEL_NAME:
        openai.api_version = None
        openai.api_type = "open_ai"
        openai.api_key = "EMPTY"
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )
    else:
        # response = openai.ChatCompletion.create(
        #     engine=MODEL_NAME,
        #     messages=[{"role": "user", "content": prompt}],
        #     temperature=0.1
        # )
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )
    text = response.choices[0].message.content.strip()
    prompt_token = response.usage.prompt_tokens
    response_token = response.usage.completion_tokens
    return text, prompt_token, response_token


def safe_call_llm(input_prompt, MAX_TRY = 5) -> str:
    """
    函数功能描述：输入 input_prompt ，返回 模型生成的内容（内部自动错误重试5次，5次错误抛异常）
    """
    global MODEL_NAME

    for i in range(MAX_TRY):
        try:
            print(f'input_prompt:\n', input_prompt)
            sys_response, prompt_token, response_token = api_func(input_prompt)
            print(f"\nsys_response: \n{sys_response}")
            print(f'\n prompt_token,response_token: {prompt_token} {response_token}\n')
            return sys_response
        except Exception as ex:
            print(ex)
            print(f'Request {MODEL_NAME} failed. try {i} times. Sleep 20 secs.')
            time.sleep(20)

    raise ValueError('safe_call_llm error!')


if __name__ == "__main__":
    res = safe_call_llm('我爸妈结婚为什么不邀请我？')
    print(res)
