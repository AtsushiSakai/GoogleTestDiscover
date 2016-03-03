#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Atsushi Sakai
import os
import sys
import logging as log
import subprocess 

#You can set top dir of the test file search
SearchPath="."

def Print(string, color, highlight=False):
    """
    Colored print

    colorlist:
        red,green

    """
    end="\033[1;m"
    pstr=""
    if color == "red":
        if highlight:
            pstr+='\033[1;41m'
        else:
            pstr+='\033[1;31m'
    elif color == "green":
        if highlight:
            pstr+='\033[1;42m'
        else:
            pstr+='\033[1;32m'
    elif color == "yellow":
        if highlight:
            pstr+='\033[1;43m'
        else:
            pstr+='\033[1;33m'

    else:
        print(("Error Unsupported color:"+color))

    print((pstr+string+end))

class Gtest:
    def __init__(self):
           # Get gtest dir path
        self.gtestdir=os.environ.get("GTEST_DIR")
        if self.gtestdir==None:
            log.critical('Cannot find GTEST_DIR environment variable')
            exit(0)

        testPaths=self.SearchTestFiles()

        for path in testPaths:
            self.ExeGTest(path)

    def ExeGTest(self,path):
        """
            Execute gtest

            sample:g++ -lpthread test.cpp -I./gtest/include  -L./gtest/mybuild -lgtest_main -lgtest && ./a.out 
        """
        print(self.gtestdir)
        cmd="g++ -lpthread "
        cmd+=path
        cmd+=" -I"
        cmd+=self.gtestdir+"/googletest/include -L"
        cmd+=self.gtestdir+"/googlemock/gtest "
        cmd+=" -lgtest_main -lgtest && ./a.out"
        print(cmd)
        try:
            output = subprocess.check_output(cmd,shell=True)
            returncode = 0
            Print(output,"green")
        except subprocess.CalledProcessError as e:
            output = e.output
            returncode = e.returncode
            Print(output,"red")

    def SearchTestFiles(self):
        """ 
        Search test file
        """
        testPaths=[]
        for file in self.fild_all_files(SearchPath):
            if "Test.cpp" in file:
                testPaths.append(file)

        if len(testPaths)==0:
            Print('Cannot find any test file.',"yellow")
            exit(0)

        print((str(len(testPaths))+" test files are found"))
        print(testPaths)
        return testPaths

    def fild_all_files(self,directory):
        for root, dirs, files in os.walk(directory):
            yield root
            for file in files:
                yield os.path.join(root, file)


if __name__ == '__main__':
    print(__file__+" start!!")
    argvs = sys.argv 
    if len(argvs)>=2:
        SearchPath=argvs[1]
    Gtest()


