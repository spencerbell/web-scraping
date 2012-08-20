This is just a series of shell and PHP scripts that will scrape location data
from various business websites.

-----
INPUT
-----
company name


-----
OUTPUT
------

results.tsv	tabbed separated value (tsv) file

results.log	date of run
		time to process
		description of process

results.diff	from previous file to current file

error.log	(if applicable)

output/*	working files needed during the process

archive/*	archive of previous results.csv file.
		files are named results-mm-dd-yyyy.tsv


------------
SOURCE FILES
------------

Makefile	GNU makefile that will build up the latest sets
		multiple targets: clean, update, redo

.sh .php .xsl	Source files needed to make it all happen


-------------
LIBRARY FILES
-------------

zipcodes.php		All US zipcodes (no APO/FPO) with city, state, lat, lng

Worker.class.php	Class for eacy scraping. Developer must extend this class to use it.
				- curl
				- xml
				- xsl
				- file operations
				- log creation

