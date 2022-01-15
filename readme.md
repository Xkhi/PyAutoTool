# PyAutoTool
<hr>
This tool aims to be a quick help to automate the process of creating generic key macros in any environment capable of running Python 3.

## Setup
This project is not supported out of the box, and requires some setup:

### (Optional) Create a virtual environment
If you don't want to mix the libraries required by this project with your current python environment, the best course of action is to create a virtual environment:
```bash
python3 -m venv <ENVIRONMENT_NAME>

# For POSIX users
source ./<ENVIRONMENT_NAME>/bin/activate

# For windows users
./<ENVIRONMENT_NAME>/bin/activate.bat
```

### Install all dependencies
Along this repo, the required dependencies for the project to run are listed in `requirements.txt`, you can run `pip` to install them
```bash
pip install -r requirements.txt
```

### Run the tool
Once the dependencies are installed, the tool should be ready to launch by using:
```bash
python3 gui.py
```
