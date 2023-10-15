PROMPTS_DEFAULT = [
    "You are ChatGPT, a large language model trained by OpenAI. Carefully heed the user's instructions. Respond using Markdown.",
    'You are a code expert. Provide only the code when asked, no explanations. \n Example:\nUser: "How do you declare a variable in Python?"\nResponse: "x = 10"',
]

AVAILABLE_MODELS = ["gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4", "gpt-4-32k"]
MODEL_TOKEN_RANGES = {
    "gpt-3.5-turbo": (0, 4096),
    "gpt-3.5-turbo-16k": (0, 16384),
    "gpt-4": (0, 8192),
    "gpt-4-32k": (0, 32768),
}


DEFAULT_CONFIG = {
    "api_key": "api-key",
    "model_name": "gpt-3.5-turbo",
    "max_tokens": 3500,
    "temperature": 1,
    "prompts": {"Default": PROMPTS_DEFAULT[0], "Code Expert": PROMPTS_DEFAULT[1]},
    "save_logs_to_file": True,
}

SHORTCUT_KEYS = ["ctrl", "c", "c"]
SHORTCUT_DELAY = 0.5
