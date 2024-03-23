from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="natural-shell",
    version="0.1.0",
    author="Sourabh Singh",
    # author_email="email@example.com",
    description="A tool for converting natural language to shell commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/your_username/natural-shell",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "langchain",
        "langchain-google-genai",
        "langchain-openai",
        "langchain-anthropic",
        "pyyaml",
    ],
    entry_points={
        'console_scripts': [
            'nshell=natural_shell.cli:main',
        ],
    },
)
