PROMPTS_DEFAULT = [
    "You are ChatGPT, a large language model trained by OpenAI. Carefully heed the user's instructions. Respond using Markdown.",
    'You are a code expert. Provide only the code when asked, no explanations. \n Example:\nUser: "How do you declare a variable in Python?"\nResponse: "x = 10"',
]

AVAILABLE_MODELS = [
    "mistral-tiny",
    "mistral-small",
    "mistral-medium",
    "gpt-3.5-turbo-1106",
    "gpt-4-1106-preview",
    "gpt-4-32k-0314",
]

MODEL_TOKEN_RANGES = {
    "mistral-tiny": (0, 16344),
    "mistral-small": (0, 16344),
    "mistral-medium": (0, 16344),
    "gpt-3.5-turbo-1106": (0, 4096),
    "gpt-4-1106-preview": (0, 4096),
    "gpt-4-32k-0314": (0, 32768),
}


DEFAULT_CONFIG = {
    "gpt_api_key": "gpt-api-key",
    "mistral_api_key": "mistral-api-key",
    "model_name": "gpt-3.5-turbo-1106",
    "max_tokens": 4096,
    "temperature": 1,
    "prompts": {"Default": PROMPTS_DEFAULT[0], "Code Expert": PROMPTS_DEFAULT[1]},
    "save_logs_to_file": True,
}


SHORTCUT_KEYS = ["ctrl", "c", "c"]
SHORTCUT_DELAY = 0.5