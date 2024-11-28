cmake_minimum_required(VERSION 3.15...3.30)
project(${SKBUILD_PROJECT_NAME} LANGUAGES C)
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)

find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(cmake_example src/main.cpp)

Python_add_library(_module MODULE src/module.c WITH_SOABI)
install(TARGETS _module DESTINATION ${SKBUILD_PROJECT_NAME})
