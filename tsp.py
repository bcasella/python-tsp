import csv

trucks = {}
with open('trucks.csv', mode='r') as trucks_csv:

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

print trucks