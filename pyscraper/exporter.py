import json
import csv


class Exporter(data):
	data = []

	"""docstring for Exporter"""
	def __init__(self, data):
		self.data = data
		
	def exportJSON(self, filename = 'data.json'):
		with open(filename, 'w') as outfile:  
    		json.dump(self.data, outfile)
    	print("Succesfully Exported to ", name)

    def exportCSV(self, filename = 'data.csv'):
		with open(filename, mode='w') as csv_file:
     		csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
     		for item in self.data:
     			csv_writer.writerow(item)
    	print("Succesfully Exported to ", name)


