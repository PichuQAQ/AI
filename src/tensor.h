#pragma once

#include <cstdint>
#include <vector>

struct Tensor {
  std::vector<float> data;
  std::vector<int64_t> shape;
};

Tensor make_tensor(std::vector<float> data, std::vector<int64_t> shape);
