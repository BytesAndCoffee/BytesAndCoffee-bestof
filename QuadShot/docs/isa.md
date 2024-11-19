# Instruction Set Architecture (ISA)

## Overview

The instruction set architecture (ISA) defines the set of instructions that the CPU can execute. These instructions are used to perform various operations such as arithmetic, data movement, comparison, and control flow. The ISA is implemented in the `Drip.py` and `QuadShot.py` files.

## Instruction Formats

Each instruction consists of an opcode and operands. The opcode specifies the operation to be performed, and the operands specify the data to be operated on. The format of an instruction is as follows:

```
[opcode] [operand1], [operand2]
```

### Arithmetic Instructions

- **ADD**: Adds two operands.
  - Format: `ADD [destination], [source]`
  - Example: `ADD AX, BX`

- **SUB**: Subtracts the second operand from the first operand.
  - Format: `SUB [destination], [source]`
  - Example: `SUB AX, BX`

- **MUL**: Multiplies two operands.
  - Format: `MUL [destination], [source]`
  - Example: `MUL AX, BX`

- **DIV**: Divides the first operand by the second operand.
  - Format: `DIV [destination], [source]`
  - Example: `DIV AX, BX`

- **MOD**: Computes the remainder of the division of the first operand by the second operand.
  - Format: `MOD [destination], [source]`
  - Example: `MOD AX, BX`

- **XOR**: Performs a bitwise XOR operation on two operands.
  - Format: `XOR [destination], [source]`
  - Example: `XOR AX, BX`

- **INC**: Increments the operand by 1.
  - Format: `INC [operand]`
  - Example: `INC AX`

- **DEC**: Decrements the operand by 1.
  - Format: `DEC [operand]`
  - Example: `DEC AX`

### Data Movement Instructions

- **MOV**: Moves data from the source operand to the destination operand.
  - Format: `MOV [destination], [source]`
  - Example: `MOV AX, BX`

- **PUSH**: Pushes the operand onto the stack.
  - Format: `PUSH [operand]`
  - Example: `PUSH AX`

- **POP**: Pops the top value from the stack into the operand.
  - Format: `POP [operand]`
  - Example: `POP AX`

- **PUSHG**: Pushes the operand onto the global stack.
  - Format: `PUSHG [operand]`
  - Example: `PUSHG AX`

- **POPG**: Pops the top value from the global stack into the operand.
  - Format: `POPG [operand]`
  - Example: `POPG AX`

- **SWP**: Swaps the two halves of a register.
  - Format: `SWP [operand]`
  - Example: `SWP AX`

### Comparison Instructions

- **CMP**: Compares two operands and sets the status register based on the result.
  - Format: `CMP [operand1], [operand2]`
  - Example: `CMP AX, BX`

### Control Flow Instructions

- **JMP**: Jumps to the specified address.
  - Format: `JMP [address]`
  - Example: `JMP 0x1000`

- **JZ**: Jumps to the specified address if the zero flag is set.
  - Format: `JZ [address]`
  - Example: `JZ 0x1000`

- **JNZ**: Jumps to the specified address if the zero flag is not set.
  - Format: `JNZ [address]`
  - Example: `JNZ 0x1000`

- **JS**: Jumps to the specified address if the sign flag is set.
  - Format: `JS [address]`
  - Example: `JS 0x1000`

- **JNS**: Jumps to the specified address if the sign flag is not set.
  - Format: `JNS [address]`
  - Example: `JNS 0x1000`

- **JO**: Jumps to the specified address if the overflow flag is set.
  - Format: `JO [address]`
  - Example: `JO 0x1000`

- **JNO**: Jumps to the specified address if the overflow flag is not set.
  - Format: `JNO [address]`
  - Example: `JNO 0x1000`

- **CALL**: Calls a subroutine at the specified address.
  - Format: `CALL [address]`
  - Example: `CALL 0x1000`

- **RET**: Returns from a subroutine.
  - Format: `RET`
  - Example: `RET`

### Input/Output Instructions

- **OUT**: Outputs the value of the operand.
  - Format: `OUT [operand]`
  - Example: `OUT AX`

- **IN**: Inputs a value into the operand.
  - Format: `IN [operand]`
  - Example: `IN AX`

## Examples

### Example 1: Addition

```
MOV AX, 5
MOV BX, 10
ADD AX, BX
```

This example moves the value 5 into the AX register, the value 10 into the BX register, and then adds the values in AX and BX, storing the result in AX.

### Example 2: Loop

```
MOV CX, 10
LOOP_START:
DEC CX
JNZ LOOP_START
```

This example initializes the CX register to 10, then enters a loop that decrements CX and jumps back to the start of the loop if CX is not zero.

### Example 3: Subroutine Call

```
CALL SUBROUTINE
...
SUBROUTINE:
MOV AX, 1
RET
```

This example calls a subroutine that moves the value 1 into the AX register and then returns to the caller.
