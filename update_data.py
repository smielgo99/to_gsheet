import gspread
import sys

def get_data():
	# Login with your Google account
	gc = gspread.login(sys.argv[1], sys.argv[2])

	# Open a worksheet from spreadsheet with one shot
	wks = gc.open("Prueba").sheet1
	
	lista= wks.get_all_values()
	print lista
	print lista[0]
	print len(lista)
	update_data(wks)

def update_data(worksheet):
	# Select a range
	print "update_data"

	worksheet.update_cell(1, 2, 'Bingo!')
	
	cell_list = worksheet.range('A2:G2')
	cell_values = [1,2,3,4,5,6,7]

	for i, val in enumerate(cell_values):  #gives us a tuple of an index and value
		cell_list[i].value = val    #use the index on cell_list and the val from cell_values

	# Update in batch
	worksheet.update_cells(cell_list)

if __name__ == "__main__":
	get_data()