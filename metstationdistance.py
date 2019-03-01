import geopy.distance
import csv

with open('sd_metstations.csv', 'r') as csv_file:
	metstations = csv.reader(csv_file)
	metstationlist = list(metstations)


print(metstationlist)

	def calculate_distance(coords_1,coords_2):
		coords_1 = metstationlist[ : ,1:2]
		coords_2 = metstationlist[1,1:2]
		return geopy.distance.distance(coords_1, coords_2).miles




		# TODO: find the distance between one row and each of the rest of the rows
		# TODO: identify the one that is closest to that row
		# TODO: Insert that value into a new array
		# TODO: Repeat the distance analysis for the next row
		# TODO: Write the shortest distance values to new file with name of site and distance value
