# MyPyconf

MyPyconf is a Python library to read configuration files from .yaml, .cfg and .conf and write python dict to .json, .env or write directly to the os environments.   

## Requirements
python 3.6


## Build and Installation

Get
```bash
git clone https://github.com/09hirenpatel/pyconf.git
cd pyconf 
```

Build
```bash 
python3 setup.py bdist_wheel
```
  
Install

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyconf.

```bash
pip install /path/to/wheelfile.whl
```

## Usage

To read the configurations files.
```python
from mypyconf.loader import load

# read '.yaml' or '.yml' to python dict
yaml_configs = load("sample/test.yaml")

# read '.cfg' to python dict
cfg_configs = load("sample/test.cfg")

# read '.conf' to python dict
conf_configs = load("sample/test.conf")
```

To write python dict to the .json or to .env file.

```python
from mypyconf.loader import store_to_file

# to write python dict to json file
data = {
    "UserName": "UserName",
    "Email": "UserName@Email.com"
}
store_to_file(data, "sample/test1.json")

# to write python dict to env file
data = {
    "UserName": "UserName",
    "Email": "UserName@Email.com"
}
store_to_file(data, "sample/test1.env")


# to write python dict to env file even if file exist
data = {
    "UserName": "UserName",
    "Email": "UserName@Email.com"
}
store_to_file(data, "sample/test1.env", if_exist_ok = True)

```  


To write python dict to the os environment .

```python
from mypyconf.loader import set_to_environment

data = {
    "UserName": "UserName",
    "Email": "UserName@Email.com"
}
set_to_environment(data)
```