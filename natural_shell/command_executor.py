import platform
from langchain.prompts import PromptTemplate
from natural_shell.language_model import llm
from natural_shell.parser import parser

# Define the prompt template
prompt_template = """
You are an AI assistant that converts natural language input into a real command.
The output should be a valid JSON with a key "command" containing the real command.
The command should be compatible with the {platform} platform.
{format_instructions}
Input: {query}
"""

def fetch_command(user_input, language_model=None):
    if language_model is None:
        language_model = llm.get_language_model()

    # Create the chain
    prompt = PromptTemplate(template=prompt_template, input_variables=["query"], partial_variables={"format_instructions": parser.get_format_instructions(), "platform": platform.system()})
    chain = prompt | language_model | parser

    retry = 0
    while retry <= 5:
        try:
            output = chain.invoke({"query": user_input})
            cmd = output['command']
            return cmd
        except Exception as e:
            print(f"Error: {e}")
            retry += 1
    if retry <= 5:
        return f"Error: {e}"

def execute_command(user_input, language_model=None):
    cmd = fetch_command(user_input, language_model)
    import os
    output = os.popen(cmd).read()
    return cmd, output

__all__ = ["fetch_command", "execute_command"]

