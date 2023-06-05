This is a simple reproducer to show different setuptools behavior when doing a
single threaded build versus when doing a parallel build.

Non-parallel build:

1) ./setup.py build -j1
2) objdump -d build/lib*/mod1*.so | grep -A5 myfunction
   0000000000001135 <myfunction>:
    1135:       55                      push   %rbp
    1136:       48 89 e5                mov    %rsp,%rbp
    1139:       b8 0c 00 00 00          mov    $0xc,%eax
    113e:       5d                      pop    %rbp
    113f:       c3                      ret

3) objdump -d build/lib*/mod2*.so | grep -A5 myfunction
   0000000000001135 <myfunction>:
    1135:       55                      push   %rbp
    1136:       48 89 e5                mov    %rsp,%rbp
    1139:       b8 2a 00 00 00          mov    $0x2a,%eax
    113e:       5d                      pop    %rbp
    113f:       c3                      ret

As expected, myfunction() returns value 12 for mod1 and value 42 for mod2.

Now, do a parallel build and check again.

1) ./setup.py build -j2
2) objdump -d build/lib*/mod1*.so | grep -A5 myfunction
   0000000000001135 <myfunction>:
    1135:       55                      push   %rbp
    1136:       48 89 e5                mov    %rsp,%rbp
    1139:       b8 2a 00 00 00          mov    $0x2a,%eax
    113e:       5d                      pop    %rbp
    113f:       c3                      ret

3) objdump -d build/lib*/mod2*.so | grep -A5 myfunction
   0000000000001135 <myfunction>:
    1135:       55                      push   %rbp
    1136:       48 89 e5                mov    %rsp,%rbp
    1139:       b8 2a 00 00 00          mov    $0x2a,%eax
    113e:       5d                      pop    %rbp
    113f:       c3                      ret

In both cases value 42 (0x2a) is returned.
