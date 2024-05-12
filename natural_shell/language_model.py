import os
import sys
import yaml
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAI
from langchain_anthropic import Anthropic

class LanguageModel:
    def __init__(self, config_file=None):
        self.load_config(config_file)

    def load_config(self, config_file=None):
        if config_file is None:
            # If no config file is provided, use default values
            self.api_key = None
            self.model = 'google-genai'
            self.base_url = None
            return

        if not os.path.exists(config_file):
            raise FileNotFoundError(f"Config file '{config_file}' not found.")

        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)

        self.api_key = config.get('api_key')
        self.model = config.get('model', 'google-genai')
        self.base_url = config.get('base_url')
        self.temperature = config.get('temperature', 1)

    def get_language_model(self):
        if self.model == "google-genai":
            return ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=self.api_key, temperature=self.temperature)
        elif self.model == "openai":
            return OpenAI(api_key=self.api_key, temperature=self.temperature, base_url=self.base_url)
        elif self.model == "anthropic":
            return Anthropic(api_key=self.api_key, temperature=self.temperature)
        else:
            raise ValueError(f"Invalid model name: {self.model}")

nshell_config_filename = os.getenv('NSHELL_CONFIG')

if nshell_config_filename is None:
    print("NSHELL_CONFIG environment variable is not set. (Should contain path to config.yaml). Exiting...")
    sys.exit(1)  # Exiting with a non-zero status code to indicate an error

# Create a default instance
llm = LanguageModel(nshell_config_filename)

# def get_language_model(llm_instance):
#     if llm_instance.model == "google-genai":
#         return ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=llm_instance.api_key, temperature=1)
#     elif llm_instance.model == "openai":
#         return OpenAI(api_key=llm_instance.api_key, temperature=1, base_url=llm_instance.base_url)
#     elif llm_instance.model == "anthropic":
#         return Anthropic(api_key=llm_instance.api_key, temperature=1)
#     else:
#         raise ValueError(f"Invalid model name: {llm_instance.model}")

# __all__ = ["llm", "get_language_model","load_config"]
