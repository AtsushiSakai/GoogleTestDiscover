# GoogleTestDiscover

A python script to discover google test code and run automatically.

It's like the unittest discover on python.

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

If you run the script with second arg,

The script search from the specified dir:

> $ python GoogleTestDiscover.py ../../


# How to add compile option 

If you want to do a test which is based on other libraries, 
   
you can add some compile options with a config file.

The config file is a python script,

and it has to have a same name of the test cpp code.

For example, if the test code name is "sampleTest.cpp",

The config file needs to be "sampleTest.py".

  

config_sample.py is a sample of the config file.

you can set options like:


    opt_include = "src/include/ " #include dir
    opt_lib = "src/ -lsample" #library dit



# License

MIT
