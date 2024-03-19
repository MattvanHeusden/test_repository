# Algorand Tutorial Python Scripts

## Pre-requisite
To run the following scripts in this section, you will need to install the following tools:

### Python

- Before you can run the scripts in this directory, download Python from the followoing link: https://www.python.org/downloads/
- If you are new to programming and/or Python, please check out the following links for resourcres:
    1. https://cs50.harvard.edu/python/2022/ & [Harvard CS50 Python Youtube Playlist](https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V)
    2. https://wiki.python.org/moin/BeginnersGuide/NonProgrammers
    3. https://wiki.python.org/moin/BeginnersGuide/Programmers

To check if Python has been installed, run the following line in your terminal:
- On Windows OS: `python --version`. If this raises an error, try `py --version`.
- On MacOS & Linux: `python3 --version`

If you get an error similar to: `python not recognised`, python may not be added to your computer's environment PATH. To do so, please follow the recommendations from the following article: [How to Add Python to PATH](https://realpython.com/add-python-to-path/#how-to-add-python-to-path-on-windows)

### Pip
Pip (Preferred Installer Program) is the package installer for Python. You can use it to install packages from the Python Package Index and other indexes. Usually, when you install Python, pip is already installed. To check if pip is available, run the following commands (and get similar outputs):

- Linux
```
python --version
Python 3.N.N
python -m pip --version
pip X.Y.Z from ... (python 3.N.N)
```
- Mac OS
```
python --version
Python 3.N.N
python -m pip --version
pip X.Y.Z from ... (python 3.N.N)
```

- Windows
```
C:> py --version
Python 3.N.N
C:> py -m pip --version
pip X.Y.Z from ... (python 3.N.N)
```

If pip is not installed on your Operating System, navigate to [Pip's installation guide](https://pip.pypa.io/en/stable/installation/).
### Visual Studio Code

Visual Studio Code is a user-friendly tool designed to help beginners and experienced programmers write and edit Python code more efficiently. It provides a clean and intuitive interface where you can write your Python scripts, with features like syntax highlighting, auto-completion, and debugging tools to help you catch errors and understand your code better. Additionally, Visual Studio Code supports extensions that enhance its functionality, allowing you to customize your coding environment to suit your preferences and workflow. Overall, it's a valuable tool for anyone learning Python or working on Python projects. You can download Python from the following link: https://code.visualstudio.com/

There are many other Integrated development environment (IDEs) you can use to write code, however Visual Studio Code is arguably the most popular IDE.

### Python Virtual Environments

Python virtual environments are isolated environments that allow you to work on different Python projects without worrying about conflicts between dependencies (i.e. libraries). They help keep your project's dependencies separate from the system-wide Python installation, making it easier to manage and share your code with others. In simpler terms, virtual environments ensure that each of your Python projects has its own space to work in, keeping everything tidy and organized.

#### Creating Python Virtual Environment

Assuming you have Python Installed, to create a Python Virtual Environment:

1. Create Virtual environment:
    - On Windows OS: `python -m venv venv`
    - On MacOS & Linux: `python3 -m venv venv`

2. Activate it:
    - On Windows OS: `venv\Scripts\activate`
    - On MacOS & Linux: `source venv/bin/activate`

### Interact with Algorand blockchain using the Python SDK
Once you have activated your virtual environment, make sure you have installed py-algorand-sdk using th following command:
- `pip install py-algorand-sdk`

## generate_account.py

This script generates account key-pairs on the Algorand Blockchain. Assuming you have completed the pre-requisite steps, run the following command:

```
python generate_account.py
```

Output Example:
```
(.venv) @iscoruta % python generate_account.py                                                                                                                          Private key:  hnCunMBl7YVetswdUTlwWZuma/xWQ9mu8p9Or0vrBpGCj3cV8g0LvjkM+I4Prf9qmQDMgCRneLSxC8nW/YHmHg==
Address:  QKHXOFPSBUF34OIM7CHA7LP7NKMQBTEAERTXRNFRBPE5N7MB4YPJQULNCE
Mnemonic phrase:  awkward right exact foster suspect pause real smile casual torch retreat remain essay brain retire drive swamp skirt exit visual nuclear river market above stove
The address is valid!
```