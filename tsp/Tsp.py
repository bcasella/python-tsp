import os
import csv
import numpy as np
from math import sin, cos, sqrt, atan2, radians

class Tsp:

    __usedTrucks = []
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

    def __getCargos(self):
        cargos = {}
        with open(self.CARGOS_FILE, mode='r') as cargos_csv:

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
        
    def getNearesTrucksCargosPairs(self):
        dist_list = []
        final = {}
        for key, cargo in self.cargos.items():
            final[key] = {'truck': None, 'cargo': cargo['product'], 'distance': None}
            for key2, truck in self.trucks.items():
                distance = self.__calculateDistanceInKmFromLatsLongs(truck['lat'], truck['long'], cargo['origin_lat'], cargo['origin_lng'])
                dist_list.append((key,key2,distance))

                if(final[key]['truck'] is None):
                    final[key]['truck'] = truck['truck']
                    final[key]['distance'] = distance
                elif(distance < final[key]['distance'] and (truck['truck'] not in self.__usedTrucks)):
                    final[key]['truck'] = truck['truck']
                    final[key]['distance'] = distance
            del final[key]['distance']
            self.__usedTrucks.append(final[key]['truck'])
        return final
    
    
    # com a funcao acima temos o ponto e caminhoes de inicio
    # tenho que marcar os caminhoes ja usados
    # tenho que criar uma lista com todos os pontos possiveis, incluindo destino de entrega
    # a partir daí, é nearest neabors
    # e com isso temos a solucao

