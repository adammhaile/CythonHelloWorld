#include <iostream>
#include <string>
class Test {
public:
    int _x;
    Test();
    ~Test();
    std::string str = R"(A\nB\nC\n)";
    int calc(int x);
};

Test::Test() {}

Test::~Test() { }

int Test::calc(int x) {
    auto q = nullptr;
    std::string test;
    std::cout << str << std::endl;
    int ar[5] = {1, 2, 3, 4, 5};
    for(auto &i: ar){
        x += i;
    }

    if (x>1 and x>2 or x>3)
    {
        std::cout << "testing";
    }

    std::string hel = "hello";
    decltype(hel) wor = "world";
    return x;
}
