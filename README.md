[![Run Tests](https://github.com/urfuMagDS2022SFgroup/urfu_ml_backend/actions/workflows/run_tests_.yml/badge.svg?branch=main)](https://github.com/urfuMagDS2022SFgroup/urfu_ml_backend/actions/workflows/run_tests_.yml)
[![Run Linters](https://github.com/urfuMagDS2022SFgroup/urfu_ml_backend/actions/workflows/run_linters.yml/badge.svg)](https://github.com/urfuMagDS2022SFgroup/urfu_ml_backend/actions/workflows/run_linters.yml)

# Welcome to our small repository(20 group)

## Setup

### Prerequisites

- We use python 3.10 please install it

### Using poetry and Linux and Windows 10+:

1. `pip install poetry` (1.2+)

#### Install dependencies

1. `poetry install --with backend,torch`

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

- Streamlit lives [here](https://github.com/urfuMagDS2022SFgroup/streamlit_frontend) and should be run with this backend
##### Practice 3
1. Run `uvicorn backend:app` to use web API
2. Use HTTP request to know sentence sentiment as result of your sentence processing
###### Using Docker
1. [Install docker](https://docs.docker.com/get-docker/) on your system
2. From the project dir run `docker build -t api .` where `api` - tag for image and `.` is where project Dockerfile is
3. After build the project run `docker run -d --name ml_urfu -p 80:80 api` where `-d` detached launch
`--name` name for the app `-p 80:80` mapping outside:inside ports `api` built image

Server will be available on `your_ip_address:80` e.g. `192.168.1.1:80` or `127.0.0.1:80`

You can check the server availability using `http://your_ip_here:80/info`
Answer should be like:

```json
{
  "root": "/",
  "get_info": "/info",
  "create_prediction": "/predict",
  "docs": "/docs"
}
```

#### Practice 4

1. Install project using Poetry `poetry install --with backend,torch,tests`
2. Run tests `poetry run pytest` (you must be in the project folder)
