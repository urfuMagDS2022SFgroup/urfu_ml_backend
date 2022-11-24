# Welcome to our small repository

## Setup
### Prerequisites
- We use python 3.10 please install it
### Using poetry and Linux:

1. `pip install poetry` (1.2+)

#### Install dependencies

1. `poetry install --with torch,tensorflow,streamlit`


### Using pip and Windows or Mac:

- for Mac, Linux and CPU
  - use env_setup.sh
- for Windows and CPU
  - read [this](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3) first
  - use evn_setup.ps1

### Manually all OS

1. Install virtualenv
   - python3 -m pip install --user virtualenv
2. Create venv
   - python3 -m venv ./venv
3. Activate venv
   - On Linux and Mac
     - source ./venv/bin/activate
   - On Windows 7+
     - venv/bin/Activate.ps1
4. Install requirements
   - pip3 install -r requirments.txt

## Run the demo app
#### Demo application try to understand entered sentence sentiment
##### Practice 2: Web app text sentiment recognition using [Streamlit](https://streamlit.io/)
1. Run `streamlit demo_web.py`
2. Go to  [localhost:8501](http://localhost:8501)
3. Enter a sentence in Russian
