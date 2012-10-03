This is just a series of shell and PHP scripts that will scrape location data
from various business websites.

How can we reliably use a single language to scrape, parse, and store all the
addresses for these companies?


Tools
-----

- Querypath (www.querypath.org)
- Gearman
- Web frontend (backbone, bootstrap)

Todo
----

Write a gearman worker thread that can dynamically load the right library to
parse the current domain(s). Gearman will work like a front-controller of sorts.

Gearman thread should have the following SOA servics ready to go:
 - querypath
 - guzzle ????
 - database connection

1. call worker with company name
2. lookup name in db, get details
3. instantiate the right class with details from db
3. call run()

How to do a rollback?


The Process
-----------

1. construct the class
2. setup

Database Schema
---------------

company
-------
 id
 name
 sic_code
 naisc_code
 created_at
 last_updated_at

scrape_version
--------------
 id
 company_id
 revision (integer) default 1
 created_at

location
--------
 id
 scrape_version_id
 address_1
 address_2
 city
 state
 postal_code
 country
 extra
 latitude
 longitude



scrape_log
----------
 id
 scrape_version_id
 action
 description
 result
 created_at




INPUT
-----
company name


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



SOURCE FILES
------------

Makefile	GNU makefile that will build up the latest sets
		multiple targets: clean, update, redo

.sh .php .xsl	Source files needed to make it all happen



LIBRARY FILES
-------------

zipcodes.php		All US zipcodes (no APO/FPO) with city, state, lat, lng

Worker.class.php	Class for eacy scraping. Developer must extend this class to use it.
				- curl
				- xml
				- xsl
				- file operations
				- log creation