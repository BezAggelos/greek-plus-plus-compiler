# 🚀 greek++ Compiler

A complete, multi-pass compiler developed from scratch for a custom procedural programming language named "greek++". Written entirely in Python, this compiler translates high-level `greek++` source code into executable RISC-V assembly language. 

The project demonstrates a deep understanding of language processing, memory management, and computer architecture by implementing all standard compiler phases without relying on external parser generators.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Target Architecture:** RISC-V Assembly
* **Core Concepts:** Automata Theory, Recursive Descent Parsing, Symbol Tables, Backpatching, Assembly Code Generation.

## ✨ Key Features
* **Lexical Analysis:** Custom scanner built using a Finite State Automaton (FSA) to tokenize the source code and handle early error detection.
* **Syntax Analysis:** Implemented a Top-Down Recursive Descent Parser to validate the language's grammar and structure.
* **Intermediate Representation:** Generates Three-Address Code (Quads) and handles complex control flow using Backpatching techniques.
* **Symbol Table Management:** Dynamic symbol table utilizing object-oriented principles to track scopes, nesting levels, variable offsets, and subprogram parameters (pass-by-value and pass-by-reference).
* **Code Generation:** Translates intermediate quads into valid RISC-V assembly instructions, handling memory allocation and register management.

## ⚙️ How to Run

### Prerequisites
* Python 3.x installed on your machine.
* A `greek++` source code file.

### Execution
Run the compiler from the command line by passing the source file as an argument:

```bash
python greek_4092_4432.py <source_file_name>
