#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Python script for google Test discover
#
# author:Atsushi Sakai
#
# license: MIT
#
import os
import sys
import logging as log
import subprocess
import importlib

# You can set top dir of the test file search
SearchPath = "../../../"


class Gtest:

    def __init__(self):
        # options for compiler
        self.options = []

        # Get gtest dir path
        self.gtestdir = os.environ.get("GTEST_DIR")
        if self.gtestdir is None:
            log.critical('Cannot find GTEST_DIR environment variable')
            sys.exit(1)

        testPaths = self.SearchTestFiles()

        for path in testPaths:
            self.ExeGTest(path)  # Execute test

    def search_opt_file(self, path):
        """
        Search optional file in the Test folder
        """
        optpath = path[:-4] + ".py"
        try:
            m = importlib.import_module(os.path.basename(optpath)[:-3])
            self.options += m.options
            print("found opt file:" + optpath)
        except ImportError:
            print("No opt file")

    def ExeGTest(self, path):
        """
            Execute gtest

            sample:g++ -lpthread test.cpp -I./gtest/include
                        -L./gtest/mybuild -lgtest_main -lgtest && ./a.out
        """
        print("\nDo test:" + path)

        # Search opt file
        self.search_opt_file(path)

        print("gtestdir:" + self.gtestdir)
        cmd = "g++ -pthread "
        cmd += path + " "
        cmd += "-I" + self.gtestdir + "/googletest/include "
        cmd += "-L" + self.gtestdir + "/googlemock/gtest "
        for option in self.options:
            cmd += option
        self.options = []

        cmd += " -lpthread -lgtest_main -lgtest -std=c++11 && ./a.out"
        print("compile command:\n" + cmd)
        try:
            output = subprocess.check_output(cmd, shell=True)
            #  returncode = 0
            Print(output, "green")
        except subprocess.CalledProcessError as e:
            output = e.output
            #  returncode = e.returncode
            Print(output, "red")
            sys.exit(1)

        os.remove("./a.out")

    def SearchTestFiles(self):
        """
        Search test file
        """
        testPaths = []
        for file in self.fild_all_files(SearchPath):
            if "Test.cpp" in file:
                testPaths.append(file)

        if len(testPaths) == 0:
            Print('Cannot find any test file.', "yellow")
            exit(0)

        print((str(len(testPaths)) + " test files are found"))
        #  print(testPaths)
        return testPaths

    def fild_all_files(self, directory):
        for root, dirs, files in os.walk(directory):
            yield root
            for file in files:
                yield os.path.join(root, file)


def Print(string, color, highlight=False):
    """
    Colored print

    colorlist:
        red,green

    """
    end = "\033[1;m"
    pstr = ""
    if color == "red":
        if highlight:
            pstr += '\033[1;41m'
        else:
            pstr += '\033[1;31m'
    elif color == "green":
        if highlight:
            pstr += '\033[1;42m'
        else:
            pstr += '\033[1;32m'
    elif color == "yellow":
        if highlight:
            pstr += '\033[1;43m'
        else:
            pstr += '\033[1;33m'

    else:
        print(("Error Unsupported color:" + color))

    if isinstance(string, str):
        print((pstr + string + end))
    else:
        print((pstr + string.decode('utf-8') + end))


if __name__ == '__main__':
    print(__file__ + " start!")
    argvs = sys.argv
    if len(argvs) >= 2:
        SearchPath = argvs[1]
    sys.path.append(os.path.abspath(SearchPath))
    #  print(sys.path)
    Gtest()
    print("All Test is OK!!!")
    sys.exit(0)
