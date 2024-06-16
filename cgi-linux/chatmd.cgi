#!/home/dcj/miniconda3/bin/python
import os
from openai import OpenAI
import httpx
import cgi
import json
import time

os.environ["http_proxy"] = "http://node1:3128"
os.environ["https_proxy"] = "http://node1:3128"

form = cgi.FieldStorage()
question = str(form.getvalue('question'))
conversation_history = str(form.getvalue('conversation_history'))

client = OpenAI(
    base_url="https://api.xty.app/v1",
    api_key="sk-62SnoJMqaJW9DJtaEd405500Dd7b4b3bB3Ed162cAfE89aA7",
    http_client=httpx.Client(
        base_url="https://api.xty.app/v1",
        follow_redirects=True,
    ),
)


def chat_with_gpt(message, max_history=10):
    global conversation_history
    conversation_history += f"User: {message}\nChatGPT:"
	
    try:
        messages = [
            {"role": "system", "content": "You are an AI language model specialized in providing Gromacs command lines to simulate molecular dynamics. Generate clear and effective command lines in a continuous manner. Do not generate any comments,but only Gromacs command lines."}
        ]

        # Keep only the max_history latest exchanges to avoid making the conversation too long
        message_parts = conversation_history.strip().split("\n")[-2 * max_history:]
        
        for i, part in enumerate(message_parts):
            role = "user" if i % 2 == 0 else "assistant"
            messages.append({"role": role, "content": part})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=256,
            n=1,
            temperature=0,
        )
        answer = response.choices[0].message.content.strip()

        conversation_history += f"{answer}\n"

        return answer
    except Exception as e:
        print(f"Error: {e}")
        return ""

response_data = {'answer': chat_with_gpt(question)}
print("Content-Type: application/json\n")
print(json.dumps(response_data))

