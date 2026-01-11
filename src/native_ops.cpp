#include "native_ops.h"

Tensor add_scalar(const Tensor &self, float other) {
  Tensor result = self;
  for (float &value : result.data) {
    value += other;
  }
  return result;
}

Tensor mul_scalar(const Tensor &self, float other) {
  Tensor result = self;
  for (float &value : result.data) {
    value *= other;
  }
  return result;
}
