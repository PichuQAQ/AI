cmake_minimum_required(VERSION 3.20)
project(aten_codegen_example LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Put the compiled extension into the Python package so imports work without extra steps.
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/python/aten_codegen_example)

include(FetchContent)
FetchContent_Declare(
  pybind11
  GIT_REPOSITORY https://github.com/pybind/pybind11.git
  GIT_TAG v2.13.6
)
FetchContent_MakeAvailable(pybind11)

pybind11_add_module(_ops
  src/generated_bindings.cpp
  src/native_ops.cpp
  src/tensor.cpp
)

target_include_directories(_ops PRIVATE src)
