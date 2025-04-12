from ollama import chat
from ollama import ChatResponse
from typing import List, Dict
import os
from dotenv import load_dotenv
import requests

load_dotenv()
WEATHERAPI_KEY = os.getenv('WEATHERAPI_KEY')

system_prompt = {
    "role": "system", 
    "content": "You are a helpful assistant. You can get the weather for any city by calling a function called 'fetch_weather'."
}
user_prompt = {
  'role': 'user',
  'content': '',
}

def fetch_weather(city: str) -> str:
    api_url = f"http://api.weatherapi.com/v1/current.json?key={WEATHERAPI_KEY}&q={city}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return f"In {city} it is currently {data['current']['condition']['text']}. The temperature is {data['current']['temp_f']} degrees Fahrenheit. The temperature feels like {data['current']['feelslike_f']} degrees Fahrenheit. Wind Speed is {data['current']['wind_mph']} miles per hour."
    else:
        return "Error fetching weather data."

def LLamaChatTools(messages: List[Dict[str,str]], isStream: bool = False) -> ChatResponse:
    return chat(model='llama3.1:8b', messages=messages,
        tools=[{'name':'fetch_weather'}],
        stream=isStream)

def LLamaChat(messages: List[Dict[str,str]]) -> ChatResponse:
    return chat(model='llama3.1:8b', messages=messages,
        stream=True)

user_prompt['content'] = "What is the weather in New York?"
messages = [system_prompt, user_prompt]

response: ChatResponse = LLamaChatTools(messages)

if response['message']['tool_calls']:
    for tool in response['message']['tool_calls']:
        func_name = tool['function']['name']
        args = tool['function']['arguments']
        if func_name == "fetch_weather":
            result = fetch_weather(**args)
            assistant_prompt = {"role": "assistant", "content": f"{result}."}
            messages_result = [system_prompt, user_prompt, assistant_prompt]
            response = LLamaChat(messages_result)
            for chunk in response:
                print(chunk['message']['content'], end='', flush=True)