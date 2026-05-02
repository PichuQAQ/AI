"""Python entrypoint for the generated ATen-style bindings."""

from __future__ import annotations

try:
    from ._ops import Tensor, add_scalar, mul_scalar  # type: ignore
except ImportError as exc:  # pragma: no cover - import only when built
    raise ImportError(
        "The native extension is not built. Run the CMake build to compile _ops."
    ) from exc

__all__ = ["Tensor", "add_scalar", "mul_scalar"]
