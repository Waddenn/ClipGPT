import openai


def ask_gpt(question, config):
    response = openai.ChatCompletion.create(
        model=config["model_name"],
        messages=[
            {"role": "system", "content": config["prompt"]},
            {"role": "user", "content": question},
        ],
        max_tokens=config["max_tokens"],
        temperature=config["temperature"],
    )
    return response.choices[0].message["content"]
