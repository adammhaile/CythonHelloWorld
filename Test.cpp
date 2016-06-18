#include "Test.h"

Test::Test() {}

Test::~Test() { }

int Test::calc(int x) {
    x = x * 2;
    return x;
}
