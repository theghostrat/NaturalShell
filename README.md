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

For a deeper dive into options and examples, refer to the [documentation](#documentation).

## Documentation 📚

NaturalShell boasts extensive documentation to facilitate your journey and maximize the utility of this robust tool:

- [Installation Guide](https://github.com/theghostrat/NaturalShell/wiki/Installation)
- [Usage Examples](https://github.com/theghostrat/NaturalShell/wiki/Usage-Examples)
- [Language Model Configuration](https://github.com/theghostrat/NaturalShell/wiki/Language-Model-Configuration)
- [Advanced Options](https://github.com/theghostrat/NaturalShell/wiki/Advanced-Options)

## Contributing 🤝

Community contributions are highly valued! If you're inclined to enhance NaturalShell, follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request

For detailed instructions, peruse our [Contributing Guidelines](https://github.com/theghostrat/NaturalShell/blob/main/CONTRIBUTING.md).

## License 📄

NaturalShell operates under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments 🙏

NaturalShell flourishes thanks to the remarkable contributions of the following open-source projects:

- [LangChain](https://github.com/hwchase17/langchain)
- [langchain-google-genai](https://github.com/hwchase17/langchain/tree/main/langchain/chains/llm)
- [langchain-openai](https://github.com/hwchase17/langchain/tree/main/langchain/llms/openai)
- [langchain-anthropic](https://github.com/hwchase17/langchain/tree/main/langchain/llms/anthropic)

We extend our gratitude to our phenomenal contributors and the vibrant open-source community for their invaluable support and contributions.

## Join the Community! 🌎

Stay updated on the latest news, updates, and discussions surrounding NaturalShell by joining our community:

- [Twitter](https://twitter.com/your_username)
- [Discord](https://discord.gg/your_invite_link)

Share your thoughts, feedback, and ideas with us! Together, let's shape the future of natural language command execution and make shell computing more intuitive and accessible for all! 🚀
