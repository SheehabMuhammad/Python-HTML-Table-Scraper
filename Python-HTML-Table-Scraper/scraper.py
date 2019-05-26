from lxml import html
import requests



page = requests.get('https://rds2.northsouth.edu/index.php/common/showofferedcourses')
tree = html.fromstring(page.content)

course_array = []
num = 1

for i in tree.xpath('//table/tbody/tr'):
	no = i.xpath('td[1]/text()')[0].strip()
	course = i.xpath('td[2]/text()')[0].strip()
	section = i.xpath('td[3]/text()')[0].strip()
	faculty = i.xpath('td[4]/text()')[0].strip()
	time = i.xpath('td[5]/text()')[0].strip()
	room = i.xpath('td[6]/text()')[0].strip()
	seats = i.xpath('td[7]/text()')[0].strip()
	course_array.append([num, course, section, faculty, time, room, seats])
	num = num + 1