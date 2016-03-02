#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Atsushi Sakai
import os
import logging as log
import subprocess 

def Print(string, color, highlight=False):
    u"""
    Colored print

    colorlist:
        red,green,yellow,blue,magenta,cyan,white,crimson

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
    elif color == "blue":
        if highlight:
            pstr+='\033[1;44m'
        else:
            pstr+='\033[1;34m'
    elif color == "magenta":
        if highlight:
            pstr+='\033[1;45m'
        else:
            pstr+='\033[1;35m'
    elif color == "cyan":
        if highlight:
            pstr+='\033[1;46m'
        else:
            pstr+='\033[1;36m'
    elif color == "white":
        if highlight:
            pstr+='\033[1;47m'
        else:
            pstr+='\033[1;37m'
    elif color == "crimson":
        if highlight:
            pstr+='\033[1;48m'
        else:
            pstr+='\033[1;38m'
    else:
        print("Error Unsupported color:"+color)

    print(pstr+string+end)



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
        u"""
            Execute gtest

            sample:g++ test.cpp -I./gtest/include  -L./gtest/mybuild -lpthread -lgtest_main -lgtest && ./a.out 
        """
        print self.gtestdir
        cmd="g++ "
        cmd+=path
        cmd+=" -I"
        cmd+=self.gtestdir+"/googletest/include -L"
        cmd+=self.gtestdir+"/googlemock/gtest "
        cmd+="-lpthread -lgtest_main -lgtest && ./a.out"
        print cmd
        try:
            output = subprocess.check_output(cmd,shell=True)
            returncode = 0
            print(output)
        except subprocess.CalledProcessError as e:
            output = e.output
            returncode = e.returncode
            Print(output,"red")

    def SearchTestFiles(self):
        u""" 
        Search test file
        """
        testPaths=[]
        for file in self.fild_all_files('.'):
            if "Test.cpp" in file:
                testPaths.append(file)

        if len(testPaths)==0:
            log.warning('Cannot find any test file.')
            exit(0)

        print(str(len(testPaths))+" test files are found")
        print testPaths
        return testPaths

    def fild_all_files(self,directory):
        for root, dirs, files in os.walk(directory):
            yield root
            for file in files:
                yield os.path.join(root, file)


if __name__ == '__main__':
    print __file__+" start!!"
    Gtest()


