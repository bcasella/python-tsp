import unittest
from tsp_panda import Tsp


class TestTsp(unittest.TestCase):

    def test_simple_tsp(self):

        trucks = {
            0:{'truck': 'A', 'lat': 0.0, 'long': 0.0},
            1:{'truck': 'B', 'lat': -10.0, 'long': -10.0}
        }

        cargos = {
            0:{'product': 'Things', 'origin_lng': -10.0, 'origin_lat': -10.0, 'destination_lng': -20.0, 'destination_lat': -20.0},
            1:{'product': 'Phones', 'origin_lng': 0.0, 'origin_lat': 0.0, 'destination_lng': 80.0, 'destination_lat': 80.0},
        }

        result = {
            0:{'truck': 'B', 'cargo': 'Things'},
            1:{'truck': 'A', 'cargo': 'Phones'},
        }
        tsp = Tsp()
        self.assertEqual(tsp.calculateBestPairTrucksCargos(trucks, cargos), result)

if __name__ == '__main__':
    unittest.main()