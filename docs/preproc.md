# Preprocessor Documentation

## Overview

The preprocessor is responsible for processing assembly code before it is passed to the assembler. It handles tasks such as macro substitution, conditional assembly, and file inclusion. The preprocessor is implemented in the `Grind.py` file.

## Grind Class

The `Grind` class is the main class for the preprocessor. It provides methods for loading and processing assembly code.

### Methods

- `__init__(self, **args)`: Initializes the `Grind` object with the specified arguments.
  - `file`: The assembly file to be processed.
  - `config`: The configuration file for the preprocessor.

- `sub(self)`: Processes the assembly code for macro substitution.
  - If the `subs` attribute is not empty, it iterates through the list of macros and substitutes them in the assembly code.

- `out(self)`: Returns the processed assembly code.

## Examples

### Example 1: Basic Usage

```python
from Grind import Grind

# Initialize the preprocessor with the assembly file and configuration file
preprocessor = Grind(file='example.drip', config='example.dripc')

# Perform macro substitution
preprocessor.sub()

# Get the processed assembly code
processed_code = preprocessor.out()
```

### Example 2: Configuration File

The configuration file is a JSON file that specifies the macros and switches for the preprocessor. Here is an example configuration file:

```json
{
  "subs": [
    "print",
    "input"
  ],
  "switches": {
    "mode": "save"
  }
}
```

### Example 3: Assembly File

The assembly file contains the assembly code to be processed. Here is an example assembly file:

```assembly
.data_
  string>text="Hello, World!"
  literal>len=0010
.exec_
  %print%
  MOV   AX, text
  CALL  PRINT
  END
```

## Purpose and Benefits

The preprocessor simplifies the assembly code by handling repetitive tasks and providing a way to include external files and macros. This makes the assembly code more readable and maintainable. The preprocessor also allows for conditional assembly, which enables the inclusion or exclusion of code based on certain conditions.
