# Welcome to our small repository

## Setup

### Using poetry and PyTorch:

1. install python 3.10 +
2. `pip install poetry` (1.2+)

#### Install PyTorch

1. `poetry install --with torch`


### Using pip3

- for Linux and CPU
  - ```pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu```
- for Windows and CPU
  - ```pip3 install torch torchvision torchaudio```

[official setup manual](https://pytorch.org/get-started/locally/)

### Using poetry and Tensorflow:

1. install python 3.10 +
2. `pip install poetry` (1.2+)
3. `poetry install --with tensorflow`

## Run the demo app
#### Demo application try to understand entered sentence sentiment

1. Run `python3 demo.py`
2. Enter a sentence in Russian
