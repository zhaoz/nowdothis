# Super simple todos

import os

FILENAME="todos"
LOCKFILE="todos.lck"
CONFIGFILE="config"
DEFAULT_PATH="%s/nowdothis" % (os.path.expanduser("~"))

class NowDoThis(object):

    def __init__(self, editor, basepath=DEFAULT_PATH):
        """
        Given path, read in todos
        """
        self.todos = []

        self.basepath = basepath
        os.mkdir(basepath)
        self.todoPath = "%s/%s" % (basepath, FILENAME)
        self.lockFile = "%s/%s" % (basepath, LOCKFILE)
        self.configFile = "%s/%s" % (basepath, CONFIGFILE)

        self.editor = editor

        for path in (self.todoPath, self.configFile):
            if not os.path.exists(path):
                f = open(path, "a")
                f.close()

    def edit(self):
        os.spawnl(os.P_WAIT, "/usr/bin/cat", self.todoPath)

        ret = os.spawnl(os.P_WAIT, self.editor, self.todoPath)

        # test ret value, should be 0
        self.load()


    def save(self):
        """
        Save the todos to path
        """
        f = open(self.todoPath, "w")

        for todo in self.todos:
            f.write("%s\n" % (todo))

        f.close()

    def load(self):
        """
        Read in todo file in path
        """
        self.todos = []

        f = open(self.todoPath, "r")

        for line in f:
            self.todos.append(line.strip())

        f.close()

    def curTask(self):
        """
        Retrieve current task
        """

        if self.todos:
            return self.todos[0]

        return None

    def finishedTask(self):
        if self.todos:
            self.todos.pop(0)

    def addTask(self, task):
        """
        add task and write it out
        """
        self.todos.append(task)

    def numTasks(self):
        return len(self.todos)

    def insertTask(self, pos, task):
        """
        Insert task at given pos
        """
        if len(self.todos) < pos:
            pos = len(self.todos)

        self.todos.insert(pos, task)

    def isLocked(self):
        """
        Check to see if lock file exists
        """
        raise NotImplementedError("Locking not implemented yet")

