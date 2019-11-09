import csv
import mlrose
import numpy as np
from math import sin, cos, sqrt, atan2, radians


_TRUCKS_FILE = 'trucks.csv'
_CARGOS_FILE = 'cargo.csv'


class Tsp:

    def calculateDistanceInKmFromLatsLongs(self, lat1, lon1, lat2, lon2):
        # approximate radius of earth in km
        R = 6356.0

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        return distance

    def getTrucks(self):
        trucks = {}
        with open(_TRUCKS_FILE, mode='r') as trucks_csv:

            reader = csv.reader(trucks_csv)
            count = 0
            for rows in reader:
                if(count>0):         
                    truck = {}
                    truck['truck'] = rows[0]
                    truck['city'] = rows[1]
                    truck['state'] = rows[2]
                    truck['lat'] = float(rows[3])
                    truck['long'] = float(rows[4])
                    truck['nearest_cargo'] = None
                    truck['nearest_dist'] = None
                    trucks[count-1] = truck
                    
                count+=1
        return trucks

    def getCargos(self):
        cargos = {}
        with open(_CARGOS_FILE, mode='r') as cargos_csv:

            reader = csv.reader(cargos_csv)
            count = 0
            for rows in reader:
                if(count>0): 
                    cargo = {}
                    cargo['product'] = rows[0]
                    cargo['origin_city'] = rows[1]
                    cargo['origin_state'] = rows[2]
                    cargo['origin_lat'] = float(rows[3])
                    cargo['origin_lng'] = float(rows[4])
                    cargo['destination_city'] = rows[5]
                    cargo['destination_state'] = rows[6]
                    cargo['destination_lat'] = float(rows[7])
                    cargo['destination_lng'] = float(rows[8])
                    cargos[count-1] = cargo
                count+=1
        return cargos
        
    def calculateBestPairTrucksCargos(self, trucks, cargos):
        return tsp.distanceList(trucks, cargos)
    
    def distanceList(self, trucks, cargos):
        dist_list = []
        final = {}
        for key, cargo in cargos.items():
            final[key] = {'truck': None, 'cargo': cargo['product'], 'distance': None}
            for key2, truck in trucks.items():
                distance = self.calculateDistanceInKmFromLatsLongs(truck['lat'], truck['long'], cargo['origin_lat'], cargo['origin_lng'])
                dist_list.append((key,key2,distance))

                if(final[key]['truck'] is None):
                    final[key]['truck'] = truck['truck']
                    final[key]['distance'] = distance
                elif(distance < final[key]['distance']):
                    final[key]['truck'] = truck['truck']
                    final[key]['distance'] = distance
            del final[key]['distance']
        return final
    
    def calculateFitnessDist(self, dist_list):
        return mlrose.TravellingSales(distances = dist_list)

                
               


tsp = Tsp()

trucks = tsp.getTrucks()
cargos = tsp.getCargos()
distance_list = tsp.distanceList(trucks, cargos)
print(distance_list)