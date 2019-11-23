import unittest
from tsp.Tsp import Tsp


class TestTsp(unittest.TestCase):

    def test_simple_tsp(self):

        trucks = {
            0: {'truck': 'A', 'lat': 0.0, 'long': 0.0},
            1: {'truck': 'B', 'lat': -10.0, 'long': -10.0}
        }

        cargos = {
            0: {'product': 'Things', 'origin_lng': -10.0, 'origin_lat': -10.0, 'destination_lng': -20.0, 'destination_lat': -20.0},
            1: {'product': 'Phones', 'origin_lng': 0.0, 'origin_lat': 0.0, 'destination_lng': 80.0, 'destination_lat': 80.0},
        }

        result = {0: {'cargo': 'Things',
                      'destination_lat': -20.0,
                      'destination_lng': -20.0,
                      'distance': 0.0,
                      'origin_lat': -10.0,
                      'origin_lng': -10.0,
                      'truck': 'B'},
                  1: {'cargo': 'Phones',
                      'destination_lat': 80.0,
                      'destination_lng': 80.0,
                      'distance': 0.0,
                      'origin_lat': 0.0,
                      'origin_lng': 0.0,
                      'truck': 'A'}}
        tsp = Tsp()
        tsp.cargos = cargos
        tsp.trucks = trucks
        self.assertEqual(tsp.getNearesTrucksCargosPairs(), result)


if __name__ == '__main__':
    unittest.main()
