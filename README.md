# ZPR
Larger than Life 

# How to install and run

## using pip (preferred)
    git clone https://github.com/pybind/pybind11.git
    pip install -r requirements.txt
    mkdir build
    cd build
    cmake ..
    make
    cd ..
    python main.py `or` python3 main.py

## using conda
    git clone https://github.com/pybind/pybind11.git
    conda env create -f zpr_ltl_conda_env.yml -n ltl
    conda activate ltl
    mkdir build
    cd build
    cmake ..
    make
    cd ..
    python main.py `or` python3 main.py
