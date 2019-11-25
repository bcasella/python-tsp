import unittest
from tsp.Tsp import Tsp


class testTsp(unittest.TestCase):
    tsp = None

    def __init__(self, *args, **kwargs):
        super(testTsp, self).__init__(*args, **kwargs)
        trucks = {
            0: {'truck': 'A', 'lat': 0.0, 'long': 0.0, 'used' : False},
            1: {'truck': 'B', 'lat': -10.0, 'long': -10.0, 'used' : False}
        }

        cargos = {
            0: {'product': 'Things', 'origin_lng': -10.0, 'origin_lat': -10.0, 'destination_lng': -20.0, 'destination_lat': -20.0},
            1: {'product': 'Phones', 'origin_lng': 0.0, 'origin_lat': 0.0, 'destination_lng': 80.0, 'destination_lat': 80.0},
        }
        self.tsp = Tsp()
        self.tsp.cargos = cargos
        self.tsp.trucks = trucks

    def testFullTsp(self):
        
        result = {0: {
            0: {'truck': 'B', 'cargo': 'Things', 'distance': 0.0, 'origin_lat': -10.0, 'origin_lng': -10.0, 'destination_lat': -20.0, 'destination_lng': -20.0}, 
            1: {'lat': -20.0, 'long': -20.0, 'truck': 'B', 'totalDist': 11324.55890420625}}, 
        1: {0: {'truck': 'A', 'cargo': 'Phones', 'distance': 0.0, 'origin_lat': 0.0, 'origin_lng': 0.0, 'destination_lat': 80.0, 'destination_lng': 80.0}, 1: {'lat': 80.0, 'long': 80.0, 'truck': 'A', 'totalDist': 9906.529492379585}}}

        self.assertEqual(self.tsp.calculateAllPaths(), result)

if __name__ == '__main__':
    unittest.main()
