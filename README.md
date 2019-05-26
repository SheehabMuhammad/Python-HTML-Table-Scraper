# HTML Table Scraper

A python package that can extract data from any HTML table and extract to CSV or JSON files


## Usage

### HTML Table Scraper


```
from pyscraper import scraper

scraperT = scraper.Scraper('https://rds2.northsouth.edu/index.php/common/showofferedcourses')

print(scraperT.extract())

```
**result**

```
[['1.', 'ACT201', '1', 'RNH', 'MW 01:00 PM - 02:30 PM', 'NAC201', '0'],
['2.', 'ACT201', '2', 'TsA', 'MW 08:00 AM - 09:30 AM', 'NAC311', '0'],
['3.', 'ACT201', '3', 'MdM', 'MW 02:40 PM - 04:10 PM', 'NAC201', '0'], 
['4.', 'ACT201', '4', 'HHq1', 'MW 04:20 PM - 05:50 PM', 'NAC210', '0'],
['5.', 'ACT201', '5', 'ASy', 'MW 09:40 AM - 11:10 AM', 'NAC201', '0'],
['6.', 'ACT201', '6', 'ASy', 'MW 11:20 AM - 12:50 PM', 'NAC201', '0'],
['7.', 'ACT201', '7', 'Aru', 'RA 01:00 PM - 02:30 PM', 'NAC203', '0'],
['8.', 'ACT201', '8', 'SHA1', 'RA 01:00 PM - 02:30 PM', 'NAC410', '0'],
['9.', 'ACT201', '9', 'KSR', 'RA 09:40 AM - 11:10 AM', 'NAC203', '0'],
['10.', 'ACT201', '10', 'SmR1', 'RA 09:40 AM - 11:10 AM', 'NAC210', '0'],
['11.', 'ACT201', '12', 'SmR1', 'RA 11:20 AM - 12:50 PM', 'NAC203', '0'],
['12.', 'ACT201', '13', 'FHW', 'RA 11:20 AM - 12:50 PM', 'NAC210', '13'],
['13.', 'ACT201', '14', 'MRe', 'RA 11:20 AM - 12:50 PM', 'NAC401', '0'],
['14.', 'ACT201', '15', 'SHA1', 'RA 11:20 AM - 12:50 PM', 'NAC402', '0'],
['15.', 'ACT201', '16', 'SHA1', 'ST 01:00 PM - 02:30 PM', 'NAC202', '0'],
['16.', 'ACT201', '17', 'SoR', 'ST 01:00 PM - 02:30 PM', 'NAC203', '0'],
['17.', 'ACT201', '18', 'IAC', 'ST 02:40 PM - 04:10 PM', 'NAC201', '0']]

```



[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.
