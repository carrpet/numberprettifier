# Number Prettifier

A number prettifier class for Python.

## Getting Started

Clone the repo from Github into your local directory.

### Prerequisities

You need Python3 installed on your machine.  The code was developed and tested with Python 3.8.0. 

### Installation

Installation instructions for python depend on your platform.  See here: https://www.python.org/downloads/.  
After you have cloned the repo to your local directory, you can import the module into your Python project or play around with it in the Python REPL.  For example, in your terminal, fire up the REPL in the directory that you cloned, by typing ```python```.  Then you can import the module by typing ```import numberprettifier```.

### Running the Tests

Navigate to the directory that was cloned from the repo. On the command line type:

```python test_numberprettifier.py```

This will run the test suite.  The tests should all pass.

### Usage

The module exposes a Python class ```PrettyNumber```.  
Instantiate a new object of the class by passing an int into its constructor, ie.

```
import numberprettifier as np
myPrettyNumber = np.PrettyNumber(1000000)
print(myPrettyNumber)  ##prints 1M
```

Note that it truncates numbers in the millions, billions, and trillions.


