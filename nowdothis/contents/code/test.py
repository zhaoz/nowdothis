#!/usr/bin/python

import os
import unittest
from nowdothis import NowDoThis

TESTDIR="%s/ndt_test" % (os.getcwd())

def cleanTodo():
    if os.path.exists("%s/%s" % (TESTDIR, "todos")):
        os.remove("%s/%s" % (TESTDIR, "todos"))

    if os.path.exists("%s/%s" % (TESTDIR, "todos.lck")):
        os.remove("%s/%s" % (TESTDIR, "todos.lck"))

    if os.path.exists(TESTDIR):
        os.rmdir(TESTDIR)

class TestBlank(unittest.TestCase):

    def setUp(self):
        self.ndt = NowDoThis("/usr/bin/vim", TESTDIR)

    def tearDown(self):
        cleanTodo()

    def testRead(self):
        self.ndt.load()
        self.assertEqual(0, len(self.ndt.todos), "There should be no todos")

    def testWrite(self):
        self.ndt.save()
        self.testRead()

    def testFinishedTask(self):
        self.ndt.finishedTask()

    def testCurTask(self):
        self.assertEqual(None, self.ndt.curTask(), "Should be no cur task")

class TestNDT(unittest.TestCase):

    def setUp(self):
        self.ndt = NowDoThis("/usr/bin/vim", TESTDIR)

    def tearDown(self):
        cleanTodo()

    def testWrite(self):
        self.ndt.addTask("TEST1")
        self.assertEqual(1, self.ndt.numTasks())

    def testMultipleRW(self):
        num = 4

        self.assertEqual(0, self.ndt.numTasks())

        for ii in range(0,4):
            self.ndt.addTask("%d" % (ii+1))

        self.assertEqual(num, self.ndt.numTasks())

        self.ndt.save()

        f = open(self.ndt.todoPath, "r")
        ii = 0
        for line in f:
            self.assertEqual(self.ndt.todos[ii], line.strip())
            ii += 1

        f.close()

        self.ndt.save()
        self.assertEqual(num, self.ndt.numTasks())
        for ii in range(0,4):
            self.assertEqual(str(ii+1), self.ndt.todos[ii])


if __name__ == "__main__":
    ts = unittest.TestSuite((
            unittest.makeSuite(TestBlank, "test"),
            unittest.makeSuite(TestNDT, "test")
        ))

    runner = unittest.TextTestRunner()
    runner.run(ts)
    cleanTodo()
