import unittest
from homework_2_1_server import preparing_data
class TestPreparing_data(unittest.TestCase):
    def test_changing_values(self):
        r = preparing_data(b'{"something": "wants", "to": "be", "bigger": "now"}')
        self.assertEqual(r, {'something': 'WANTS', 'to': 'BE', 'bigger': 'NOW'})