# graph-test

## Overview

This is a **work in progress** project for a test.

The test consists of creating a program that receives a rectangular grid as input and converts it to a graph.
Then through the graph, it should output a `.dot` file so **graphviz** can generate an image visualization of the created graph.

Unfortunately, I was not able to conclude the program yet.

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
3. Install dependencies:

    ```bash
    # As for now, there is no external libraries being used so actually there is no requirements

    pip install -r requirements
4. Edit `input_grid` and `warehouses` variables accordingly on main.py (appropriate way should be reading an external file or getting it through an API request, for example)

5. Run the main script

    ```bash
    python main.py
6. When the function to generate the dot file is done, you should run something like this

    ```bash
    dot -Tpng output_graph.dot -o graph.png
