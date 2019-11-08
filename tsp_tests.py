import unittest
from tsp import Tsp


class TestTsp(unittest.TestCase):

    def test_simple_tsp(self):

        trucks = {
            0:{'truck': 'A', 'lat': 1.0, 'long': 1.0},
            1:{'truck': 'B', 'lat': 35.0, 'long': 35.0}
        }

        cargos = {
            0:{'product': 'Things', 'origin_lng': -10.0, 'origin_lat': -10.0, 'destination_lng': -20.0, 'destination_lat': -20.0},
            0:{'product': 'Phones', 'origin_lng': 40.0, 'origin_lat': 40.0, 'destination_lng': 60.0, 'destination_lat': 60.0},
        }

        result = {
            0:{'truck': 'A', 'cargo': 'Things'},
            1:{'truck': 'B', 'cargo': 'Phones'},
        }
        tsp = Tsp()
        self.assertEqual(tsp.calculateBestPairTrucksCargos(trucks, cargos), result)

if __name__ == '__main__':
    unittest.main()