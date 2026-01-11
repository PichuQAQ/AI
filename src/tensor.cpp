#include "tensor.h"

Tensor make_tensor(std::vector<float> data, std::vector<int64_t> shape) {
  return Tensor{std::move(data), std::move(shape)};
}
