import os
import yaml
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAI
from langchain_anthropic import Anthropic

# def load_config():
#     config_file = os.path.join(os.path.dirname(__file__), 'config.yaml')
#     with open(config_file, 'r') as f:
#         config = yaml.safe_load(f)
#     return config

def load_config(config_file=None):
    if config_file is None:
        config_file = os.getenv('NSHELL_CONFIG', 'config.yaml')

    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Config file '{config_file}' not found.")

    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config

def get_language_model():
    config = load_config()
    model_name = config.get('model', 'google-genai')
    api_key = config.get('api_key')
    base_url = config.get('base_url')

    if model_name == "google-genai":
        return ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key, temperature=1)
    elif model_name == "openai":
        return OpenAI(api_key=api_key, temperature=1, base_url=base_url)
    elif model_name == "anthropic":
        return Anthropic(api_key=api_key, temperature=1)
    else:
        raise ValueError(f"Invalid model name: {model_name}")

llm = get_language_model()
