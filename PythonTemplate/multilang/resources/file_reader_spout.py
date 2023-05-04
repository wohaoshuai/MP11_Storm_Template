# import os
# from os.path import join
from time import sleep

# from streamparse import Spout
import storm


class FileReaderSpout(storm.Spout):

    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        self._complete = False

        storm.logInfo("Spout instance starting...")

        # TODO:
        # Task: Initialize the file reader
        # hint: get the filename from conf argument 
        self.filename = conf["filename"]
        self.file = open(self.filename, "r")
        # End

    def nextTuple(self):
        # TODO:
        # Task 1: read the next line and emit a tuple for it
        # Task 2: don't forget to sleep for 1 second when the file is entirely read to prevent a busy-loop
        line = self.file.readline().strip()
        if line:
            storm.emit([line])
        else:
            if not self._complete:
                sleep(1)
                self._complete = True
                self.file.close()
        # End


# Start the spout when it's invoked
FileReaderSpout().run()
