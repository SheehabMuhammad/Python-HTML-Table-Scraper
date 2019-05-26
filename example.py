from pyscraper import scraper


scraperT = scraper.Scraper('https://rds2.northsouth.edu/index.php/common/showofferedcourses')

print(scraperT.extract())