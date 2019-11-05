import csv

_TRUCKS_FILE = 'trucks.csv'
_CARGOS_FILE = 'cargo.csv'



def getTrucks():
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
                trucks[count] = truck
            count+=1
    return trucks

def getCargos():
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
                cargos[count] = cargo
            count+=1
    return cargos    

trucks = getTrucks()
cargos = getCargos()

print trucks