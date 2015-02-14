from unittest import TestCase
import time
from PeriodicTimer import PeriodicTimer
__author__ = 'DRIA'


class TestPeriodicTimer(TestCase):
    def test_start(self):

        timer = PeriodicTimer(3, self.foo)

        timer.start()
        try:
            while time < 11:
                time.sleep(1)

        finally:
            timer.cancel()

    def foo(self):
        print "Boom!"