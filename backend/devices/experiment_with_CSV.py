import csv
import os

from devices.models import Device

# go to the correct directory in order to get CSV report
open_dir = os.open( '..', os.O_RDONLY )
os.fchdir(open_dir)
pwd = os.getcwd()

# read the data from CSV file and save them into the database
with open('{}/report.csv'.format(pwd), 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    if Device.objects.first() != None:
        Device.objects.all().delete()
    for row in enumerate(csv_reader):
        if row[0] > 0:
            Device.objects.create(id=row[0], device_id=row[1][1], timestamp=row[1][0], device_type=row[1][2], status=row[1][3])
