import unittest
import os
from pyqoptionapi.stable_api import IQ_Option

class TestOpCodes(unittest.TestCase):
  
    def test_opcodes(self):
        I_want_money=IQ_Option(os.getenv("email"),os.getenv("password"))
        I_want_money.change_balance("PRACTICE")
        I_want_money.reset_practice_balance()
        self.assertEqual(I_want_money.check_connect(), True)

        actives = I_want_money.get_all_open_time()
        print(I_want_money.get_all_ACTIVES_OPCODE())
         