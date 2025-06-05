A CPU and Assembly compiler written in Python

## Overview

This project consists of a custom CPU, assembler, and runtime environment implemented in Python. The components include:

1. **Instruction Set Architecture (ISA)**:
   - Defined in `Drip.py` and `QuadShot.py`.
   - Instructions for arithmetic, jumps, data movement, comparison, stack operations, input/output, and subroutine calls.

2. **Assembler**:
   - Implemented in `Drip.py`.
   - Functions for tokenizing, parsing, and converting assembly code into machine code.

3. **CPU Runtime**:
   - Defined in `QuadShot.py`.
   - Includes the `CPU` class with methods for executing instructions, managing registers, and handling input/output.

4. **RAM**:
   - Defined in `ram.py`.
   - Provides a simple interface for memory storage and retrieval.

5. **Registers**:
   - Defined in `registers.py`.
   - Manages the CPU registers, supporting single, double, and adjacent register operations.

## Files

- `Drip.py`: Contains the ISA definition and assembler implementation.
- `QuadShot.py`: Contains the CPU runtime implementation.
- `ram.py`: Contains the RAM class for memory storage and retrieval.
- `registers.py`: Contains the Registers class for managing CPU registers.
- `Grind.py`: Contains the assembly pre-processor for Drip.
- `BUBBLE2.drip`: Example assembly code for a bubble sort algorithm.
- `echo.drip`: Example assembly code for an echo program.
- `print.bean`: Subroutine for printing strings.
- `input.bean`: Subroutine for reading input.

## Usage

To run the CPU with an assembly program, use the following command:

```sh
python QuadShot.py <program_name> <input_string>
```

- `<program_name>`: The name of the assembly program file (without the `.drip` extension).
- `<input_string>`: (Optional) Input string to be provided to the program.

Example:

```sh
python QuadShot.py BUBBLE2 "example input"
```

This command will run the `BUBBLE2.drip` program with the input "example input".
