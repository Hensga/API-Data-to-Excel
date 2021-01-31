import requests
import xlsxwriter


outWorkbook = xlsxwriter.Workbook("out.xlsx")
outSheet = outWorkbook.add_worksheet()


r = requests.get('https://randomfox.ca/floof')

imageJson = r.json()

imagePath = imageJson['image']

outSheet.write("A1", f"{imagePath}")

outWorkbook.close()
