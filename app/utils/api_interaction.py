from openai import OpenAI
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


def handle_api_response(model_name, api_key, clipboard_content, config):
    if "mistral" in model_name:
        answer = ask_mistral(api_key, clipboard_content, config)
    else:
        answer = ask_gpt(api_key, clipboard_content, config)
    return answer


def ask_gpt(api_key, question, config):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=config["model_name"],
        messages=[
            {"role": "system", "content": config["prompt"]},
            {"role": "user", "content": question},
        ],
        max_tokens=config["max_tokens"],
        temperature=config["temperature"],
    )
    return response.choices[0].message.content


def ask_mistral(api_key, question, config):
    client = MistralClient(api_key=api_key)

    messages = [
        ChatMessage(role="system", content=config["prompt"]),
        ChatMessage(role="user", content=question),
    ]

    chat_response = client.chat(
        model=config["model_name"],
        messages=messages,
        max_tokens=config["max_tokens"],
        temperature=config["temperature"],
    )

    return chat_response.choices[0].message.content
