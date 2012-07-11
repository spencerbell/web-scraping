#!/bin/sh

for i in NC SC TN IN IL MO LA KS OK TX CO NM UT AZ ID NV WA OR CA HI;
do
	echo $i;
	#curl "http://jackinthebox.com/webservices/get_locations.php?state=$i&city=%" > tmp/$i.xml
	xsltproc extract.xsl tmp/$i.xml >> output/final.txt
done;

