# PyMultiPointer
It's a way to create multidimensional pointers

## Installation
Installation is easy.
Just do
```bash
pip install multipointer
```
Alternatively you can download the repository and start `setup.py` with the parameter `install` as with every other module

## How to use it
Import it:
```python
from multipointer import *
```
Convert a variable into one you can use the `index` method:
```python
# for dict
converted = dict({"key": "value"})
# for list
converted = list([foo, bar])
# etc.
```
### Use the multidimensional `index` method:
```python
d = {
  "list": [
    "Hi", "Hey"
  ]
}
d.index("list", 0)
# Returns -> "Hey"
```
### The `index` function:
To use the `index` function you don't have to convert the object:
```python
d = {
  "list": [
    "Hi", "Hey"
  ]
}
index(d, "list", 0)
```
