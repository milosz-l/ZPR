cmake_minimum_required(VERSION 3.4)
project(LargerThanLife)
add_subdirectory(pybind11)
pybind11_add_module(BoardEngine engine/BoardEngine.cpp)