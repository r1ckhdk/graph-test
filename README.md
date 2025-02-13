# graph-test

## Overview

This is a **work in progress** project for a test.

The test consists of creating a program that receives a rectangular grid as input and converts it to a graph.
Then through the graph, it should output a `.dot` file so **graphviz** can generate an image visualization of the created graph.

Unfortunately, I was not able to conclude the program yet.

Other things to do besides the ones marked on code itself:
- Generate Dockerfile to conteinarize application
- Create new workflows to format, lint and test code (for now there is only a format check with Black)

## Usage

Well, since it is not completed yet, you can not use it right away.

But when it is finished, you can run the project with the following steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/r1ckhdk/graph-test.git
   cd graph-test
2. Start a virtual environment (optional, but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate
3. For the program be able to generate the output with graphviz, you need to have the binary on the machine. You can install it with:

    ```bash
    apt install graphviz
4. Install dependencies:

    The only dependency now is the `graphviz` package, which can be installed with:

    ```bash
    pip install graphviz
    ```

    Or you can install through the `requirements.txt` file with:

    ```bash
    pip install -r requirements.txt
5. Edit `input_grid` and `warehouses` variables accordingly on main.py (appropriate way should be reading an external file or getting it through an API request, for example)

6. Run the main script to create a `graph.png` file on the directory

    ```bash
    python main.py