# ZPR
Larger than Life 

# How to install and run

## general instructions
1. clone pybind11 repository from github (`git clone https://github.com/pybind/pybind11.git`)
2. install requirements (`pip install -r requirements.txt`)
3. configure and build cmake
4. create __init__.py file in build folder (`touch build/__init__.py`)
5. run main.py (`python main.py`)

## example using pip (preferred)
    git clone https://github.com/pybind/pybind11.git
    pip install -r requirements.txt
    mkdir build
    cd build
    cmake ..
    make
    cd ..
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