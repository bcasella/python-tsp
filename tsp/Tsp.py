import os
import csv
import numpy as np
from math import sin, cos, sqrt, atan2, radians
""""
To run this program, use python version >3.7
"""


class Tsp:

    __usedTrucks = []
    cargos = {}
    trucks = {}
    TRUCKS_FILE = os.path.join(os.path.dirname(__file__), './trucks.csv')
    CARGOS_FILE = os.path.join(os.path.dirname(__file__), './cargo.csv')

    def __init__(self):
        self.cargos = self.__getCargos()
        self.trucks = self.__getTrucks()

    def __calculateDistanceInKmFromLatsLongs(self, lat1, lon1, lat2, lon2):
        # approximate radius of earth in km
        R = 6356.0

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        return distance

    def __getTrucks(self):
        trucks = {}
        with open(self.TRUCKS_FILE, mode='r') as trucks_csv:

            reader = csv.reader(trucks_csv)
            count = 0
            for rows in reader:
                if(count > 0):
                    truck = {}
                    truck['truck'] = rows[0]
                    truck['city'] = rows[1]
                    truck['state'] = rows[2]
                    truck['lat'] = float(rows[3])
                    truck['long'] = float(rows[4])
                    truck['final_destination'] = False
                    truck['used'] = False
                    trucks[count-1] = truck

                count += 1
        return trucks

    def __getCargos(self):
        cargos = {}
        with open(self.CARGOS_FILE, mode='r') as cargos_csv:

            reader = csv.reader(cargos_csv)
            count = 0
            for rows in reader:
                if(count > 0):
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
                count += 1
        return cargos

    def __makeDestinations(self):
        destinations = self.trucks
        destination = {}
        for key, cargo in self.cargos.items():
            destination['truck'] = None
            destination['city'] = None
            destination['state'] = None
            destination['lat'] = cargo['destination_lat']
            destination['long'] = cargo['destination_lng']
            destination['final_destination'] = True
            destinations[len(destinations.keys())] = destination
        return destinations

    def getNearesTrucksCargosPairs(self):
        dist_list = []
        final = {}
        for key, cargo in self.cargos.items():
            final[key] = {
                'truck': None,
                'cargo': cargo['product'],
                'distance': None,
                'origin_lat': cargo['origin_lat'],
                'origin_lng': cargo['origin_lng'],
                'destination_lat': cargo['destination_lat'],
                'destination_lng': cargo['destination_lng'],
            }
            for key2, truck in self.trucks.items():
                distance = self.__calculateDistanceInKmFromLatsLongs(
                    truck['lat'], truck['long'], cargo['origin_lat'], cargo['origin_lng'])
                dist_list.append((key, key2, distance))

                if(final[key]['truck'] is None):
                    final[key]['truck'] = truck['truck']
                    final[key]['truck_key'] = key2
                    final[key]['distance'] = distance
                elif(distance < final[key]['distance'] and not self.trucks[key2]['used']):
                    final[key]['truck'] = truck['truck']
                    final[key]['truck_key'] = key2
                    final[key]['distance'] = distance
            self.__usedTrucks.append(final[key]['truck'])
            self.trucks[final[key]['truck_key']]['used'] = True
            del final[key]['truck_key']
        return final

    def __calculatePath(self, point):
        currentLocation = {
            'lat': point['origin_lat'], 'long': point['origin_lng'], 'totalDist': point['distance'], 'truck': point['truck']}
        path = {0: point}
        count = 1
        while((currentLocation['lat'] is not point['destination_lat']) and (currentLocation['long'] is not point['destination_lng'])):
            minDist = float('inf')
            tempPath = {'lat': None, 'long': None}
            usedKey = None
            currentLocationToFinalDist = self.__calculateDistanceInKmFromLatsLongs(
                    currentLocation['lat'], currentLocation['long'], point['destination_lat'], point['destination_lng'])
            
            for key, truck in self.trucks.items():      
                if not truck['used']:
                    currentLocationToTruckDist = self.__calculateDistanceInKmFromLatsLongs(
                        currentLocation['lat'], currentLocation['long'], truck['lat'], truck['long'])
                    truckToFinalDist = self.__calculateDistanceInKmFromLatsLongs(
                        point['destination_lat'], point['destination_lng'], truck['lat'], truck['long'])
                    totalDist = currentLocationToTruckDist + truckToFinalDist
                    if (totalDist < minDist and currentLocationToTruckDist < currentLocationToFinalDist):
                        tempPath['lat'] = truck['lat']
                        tempPath['totalDist'] = currentLocation['totalDist'] + \
                            currentLocationToTruckDist
                        tempPath['long'] = truck['long']
                        tempPath['deltaDist'] = currentLocationToTruckDist
                        tempPath['truck'] = truck['truck']
                        usedKey = key
            if usedKey is None:
                tempPath['lat'] = point['destination_lat']
                tempPath['long'] = point['destination_lng']
                tempPath['truck'] = currentLocation['truck']
                tempPath['totalDist'] = currentLocation['totalDist'] + \
                    currentLocationToFinalDist
            else:
                self.trucks[usedKey]['used'] = True
            path[count] = tempPath
            currentLocation = tempPath
            count = count+1

        return path

    def calculateAllPaths(self):
        initialList = self.getNearesTrucksCargosPairs()
        paths = {}
        for key, point in initialList.items():
            paths[key] = self.__calculatePath(point)
        return paths

    def run(self):

        print(self.calculateAllPaths())


if __name__ == '__main__':
    tsp = Tsp()
    tsp.run()
