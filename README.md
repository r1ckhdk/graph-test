# graph-test

## Overview

This is a **work in progress** project for a test.

The test consists of creating a program that receives a rectangular grid as input and converts it to a graph.
Then through the graph, it outputs a rendered graph on `.png`format and a `.dot` file so you can check and edit, to generate it manually with **graphviz**, via the `dot` command.

> Unfortunately, I was not able to conclude the program yet.
 As for now, it is only capable of detecting nodes (buildings/warehouses correctly, intersections and dead ends partially, but no road width changes yet)
So, the output graph consists **only of nodes, and no edges**.

I still need to figure out how detect and generate edges properly (which is a crucial).


### Workflows

There is currently two workflows on this repo, one for formatting code with **Black** and other for linting with **Pylint**.

## Usage

**Requires Python 3.12+**

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

6. Run the main script to create a `graph.png` and `graph.dot` file on the directory

    ```bash
    python main.py

## Running with Docker

1. Build image

    ```bash
    docker build -t graph-test .
2. Run container with volume mapped to get output

    ```bash
    docker run --rm -v $(pwd)/output:/app/output graph-test