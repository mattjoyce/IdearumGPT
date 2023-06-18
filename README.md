# IdearumGPT

## Description

IdearumGPT is a Python-based program designed to generate natural language text based on combinations or permutations of tokens specified in multiple files. It utilizes the power of OpenAI's GPT models via an OpenAI wrapper to generate context-relevant text. It can be used for various applications like generating dialogues, narratives, and other creative or simulation purposes.

## Prerequisites

- Python 3.x
- Required Python Libraries: 
  - `pyyaml`
  - `requests`
  - `json`
  - `itertools`
- OpenAI API key
- OpenAI's GPT model (specified in the configuration)

## Getting Started

1. Clone the repository.
2. Install the necessary libraries using pip:

    ```
    pip install -r requirements.txt
    ```

3. Place the OpenAI API key in the environment variables or as specified by the OpenAI wrapper.

4. Ensure the relevant token files, system file, user template file, and function file are available and paths are set appropriately in the config YAML file.

5. Run the program with the config file as a parameter:

    ```
    python IdearumGPT.py config.yaml
    ```

## Usage

At its core, IdearumGPT uses a configuration file to get necessary parameters, including the paths to token files, system role file, user template file, GPT model, and function files.

It generates all possible combinations of tokens from the provided files, and then constructs messages using a given template, with the system role and the tokens as inputs. The resulting message is then processed by the OpenAI GPT model to generate a text output, which is saved to an output file.

## Contributing

Contributions to IdearumGPT are welcome! Please feel free to submit a pull request or open an issue for any enhancements, bug fixes, or suggestions.

## License

This project is open-source, under the [MIT License](https://choosealicense.com/licenses/mit/).

