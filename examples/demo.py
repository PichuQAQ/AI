from __future__ import annotations

from aten_codegen_example import Tensor, add_scalar, mul_scalar


def main() -> None:
    tensor = Tensor([1.0, 2.0, 3.0], [3])
    print("input", tensor.data)

    out = add_scalar(tensor, 2.0)
    print("add_scalar", out.data)

    out = mul_scalar(tensor, 3.0)
    print("mul_scalar", out.data)


if __name__ == "__main__":
    main()
