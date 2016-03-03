# GoogleTestDiscover

A python script to discover google test code and run automatically

# How to use

## 1. Download the google test code.

> $ git clone https://github.com/google/googletest gtest


## 2. Compile the google test

> $ cd  gtest

> $ cmake .

> $ make


## 3. Set Environment variable of the google test path

> $ export GTEST_DIR='/Users/Hoge/gtest'

## 4. Run the GoogleTestDiscover.py

The script search test files which name is *Test.cpp and run:

![a](http://cdn-ak.f.st-hatena.com/images/fotolife/m/meison_amsl/20160302/20160302203251.png)

　

If you run the script without second arg,

The script search from the current dir.

If you runt the script with second arg,

The script search from the pointed dir:

> $ python GoogleTestDiscover.py ../../



# License

MIT
