from lxml import html
import requests

class Scraper(object):
	tree = ''
	path = '//table/tbody/tr'
	"""docstring for Scraper"""
	def __init__(self, url):
		page = requests.get(url)
		self.tree = html.fromstring(page.content)
		
	def setTableXPath(self, path):
		self.path = path

	def extract(self):
		data = []
		index = 1
		for row in self.tree.xpath(self.path):
			dataRow = []
			for td in row.xpath('td'):
				dataRow.append(td.xpath('text()')[0].strip())
			data.append(dataRow)
		return data
	


