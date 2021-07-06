# MyPyconf

MyPyconf is a Python library to read configuration files from .yaml, .cfg anf .conf 

## Requirements


## Installation

```bash
git clone https://github.com/09hirenpatel/pyconf.git
cd pyconf 
python3 setup.

```
  
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install dist/mypyconf-0.1.0-py3-none-any.whl
```

## Usage

```python
from mypyconf.loader import load

# read '.yaml' or '.yml'
yaml_configs = load("sample/test.yaml")

# read '.cfg'
cfg_configs = load("sample/test.cfg")

# read '.conf'
conf_configs = load("sample/test.conf")
```

## License
[MIT](https://choosealicense.com/licenses/mit/)