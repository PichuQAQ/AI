# ATen-Style Codegen + Pybind11 Demo

This repository is a small, self-contained project that mirrors the **idea** behind
`aten/src/ATen/native/native_functions.yaml`: a YAML file defines native operator
signatures, a codegen script turns them into C++ bindings + Python stubs, and
`pybind11` exposes the C++ ops to Python.

## Layout

- `native_functions.yaml`: minimal operator registry (input to codegen).
- `tools/codegen.py`: reads the YAML and generates:
  - `src/generated_bindings.cpp` (pybind11 bindings)
  - `python/aten_codegen_example/_ops.pyi` (type stubs)
- `src/native_ops.cpp`: hand-written C++ implementations.
- `python/aten_codegen_example`: Python package that imports the compiled module.

## Regenerating code

```bash
pip install -r requirements.txt
python3 tools/codegen.py
```

## Building the extension

```bash
cmake -S . -B build
cmake --build build
```

The CMake build drops the compiled `_ops` module directly into
`python/aten_codegen_example`, so Python can import it without additional steps.

## Running the demo

```bash
export PYTHONPATH="$(pwd)/python"
python3 examples/demo.py
```

## Example output

```
input [1.0, 2.0, 3.0]
add_scalar [3.0, 4.0, 5.0]
mul_scalar [3.0, 6.0, 9.0]
```
