# NaturalShell 🐚✨

NaturalShell, an innovative command-line tool, seamlessly bridges the gap between natural language and shell commands. With NaturalShell, executing complex terminal operations becomes as simple as conversing in everyday language. Bid farewell to memorizing cryptic commands and welcome a more intuitive approach to interacting with your system!

![Demo](https://user-images.githubusercontent.com/your_username/natural-shell/assets/demo.gif)

## Features ✨

- **Natural Language Processing**: NaturalShell employs cutting-edge language models to comprehend your natural language input and translate it into executable shell commands.
- **Multi-Model Support**: Choose from Google GenerativeAI, OpenAI, or Anthropic language models to align with your requirements.
- **Flexible Execution**: Effortlessly print or execute commands directly from your terminal using intuitive subcommands.
- **Customizable Configuration**: Tailor your API keys and language model preferences conveniently within a centralized `config.yaml` file.
- **Easy Installation**: Install NaturalShell swiftly with a few commands and kickstart your journey immediately.

## Installation 🚀
To install NaturalShell directly from its GitHub repository using pip, you can use the following command:

```bash
pip install git+https://github.com/theghostrat/NaturalShell.git
```

This command will clone the repository and install the package along with its dependencies.

Alternatively, if you want to install it in editable mode, allowing you to make changes to the code and see the changes reflected immediately without reinstalling, you can use:

```bash
pip install -e git+https://github.com/theghostrat/NaturalShell.git
```

This will install NaturalShell in editable mode, and any changes you make to the code will be reflected without needing to reinstall the package.

Both of these commands will fetch the latest version of NaturalShell from its GitHub repository and install it on your system.

##Manual Installation

NaturalShell isn't available on PyPI yet, but fret not, you can install it directly from the GitHub repository:

1. Clone the repository:

```bash
git clone https://github.com/theghostrat/NaturalShell.git
```

2. Navigate to the project directory:

```bash
cd natural-shell
```

3. Install the package and its dependencies:

```bash
pip install .
```

## Usage 🤖

Post-installation, commence your NaturalShell experience right from your terminal or command prompt:

```bash
# Print the shell command
nshell "list all files in the current directory" print

# Execute the shell command
nshell "list all files in the current directory" exec
```


## Contributing 🤝

Community contributions are highly valued! If you're inclined to enhance NaturalShell, follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request


## License 📄

NaturalShell operates under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments 🙏

NaturalShell flourishes thanks to the remarkable contributions of the following open-source projects:

- [LangChain](https://github.com/hwchase17/langchain)
- [langchain-google-genai](https://github.com/hwchase17/langchain/tree/main/langchain/chains/llm)
- [langchain-openai](https://github.com/hwchase17/langchain/tree/main/langchain/llms/openai)
- [langchain-anthropic](https://github.com/hwchase17/langchain/tree/main/langchain/llms/anthropic)

We extend our gratitude to our phenomenal contributors and the vibrant open-source community for their invaluable support and contributions.
