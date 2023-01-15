# ZPR
Larger than Life 

# How to install and run

## general instructions
1. clone pybind11 repository from github (`git clone https://github.com/pybind/pybind11.git`)
2. install requirements (`pip install -r requirements.txt`)
3. configure and build cmake
4. run main.py (`python main.py`)
NOTE: In case there is a problem with import, try adding `__init__.py` file to build folder (`touch build/__init__.py`)

## example using pip (preferred)
    git clone https://github.com/pybind/pybind11.git
    pip install -r requirements.txt
    mkdir build
    cd build
    cmake ..
    make
    cd ..
    touch build/__init__.py
    python main.py `or` python3 main.py `or` python3.9 main.py

## example using conda
    git clone https://github.com/pybind/pybind11.git
    conda env create -f zpr_ltl_conda_env.yml -n ltl
    conda activate ltl
    mkdir build
    cd build
    cmake ..
    make
    cd ..
    touch build/__init__.py
    python main.py `or` python3 main.py `or` python3.9 main.py

# How to give your own starting board as an argument
If you want, you can give your own starting board as a txt file.
- the file's name must be `starting_board.txt`
- `example_starting_board.txt` is a good example (if you want to use it, just change it's name to `starting_board.txt`)
- the file must have 50 lines with 50 integers seperated by spaces
- the integers can't be below 0 and can't be bigger than `count_of_states - 1`
- if the `starting_board.txt` file is invalid, or if there is no such file, the program will just run with a randomized board

# Run tests

## example using pip (preferred)
    git clone https://github.com/pybind/pybind11.git
    pip install -r requirements.txt
    mkdir build
    cd build
    cmake ..
    make
    cd ..
    touch build/__init__.py
    pytest tests/

## example using conda
    git clone https://github.com/pybind/pybind11.git
    conda env create -f zpr_ltl_conda_env.yml -n ltl
    conda activate ltl
    mkdir build
    cd build
    cmake ..
    make
    cd ..
    touch build/__init__.py
    pytest tests/

# Generate documentation
    doxygen config_doxygen


for Ubuntu runs, ```sudo apt-get install python3-tk``` is required

Python code formatter - Black:
```black .```

TODO: pylint command
Python linter - Pylint:
```pylint ./GUI```
```pylint ```