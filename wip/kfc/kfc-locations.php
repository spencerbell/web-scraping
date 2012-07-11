<?php

# The current KFC finder URL will return all locations within a 400 mile radius.
# this means we have to make only a few requests to get all locations in the US.
#
# Note: This is similar to taco bell probably because they are owned by the same parent company

# URL: http://www.kfc.com/storelocator/services/MWS.asmx/FindNearby

$url = 'http://www.kfc.com/storelocator/services/MWS.asmx/FindNearby';

# create the curl object
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL,$url);

# set header
$headers = array(
	"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:13.0) Gecko/20100101 Firefox/13.0",
	"Referer: http://www.kfc.com/storelocator/Default.aspx?address=",
	"Host: www.kfc.com",
	"DNT:1",
	"Content-Type: application/json; charset=utf-8"
);

curl_setopt($ch, CURLOPT_HTTPHEADER, $headers); 
curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1); 

curl_setopt($ch,CURLOPT_POST,1);

# our latitude, longitues
$latlngs = array(
  array(-81.518555,27.955591),
  array(-84.375000,33.651207),
  array(-80.112305,38.203655),
  array(-75.454102,41.967659),
  array(-68.774414,45.767525),
  array(-91.318359,31.578535),
  array(-89.824219,37.718590),
  array(-84.638672,42.553082),
  array(-90.791016,45.398449),
  array(-98.833008,47.428085),
  array(-98.349609,39.334297),
  array(-98.657227,32.731842),
  array(-98.745117,26.470573),
  array(-106.303711,31.765537),
  array(-106.479492,39.943436),
  array(-108.632812,47.989922),
  array(-116.938477,47.872143),
  array(-116.630859,40.647305),
  array(-116.367188,33.394760),
  array(-123.662109,40.380028),
  array(-123.222656,47.546871)
);

$outfile = fopen('kfc_locations.csv','w');

foreach($latlngs as $k => $row) {

	# Create the json string of the formatted payload
	$payload = sprintf('{"latitude":%f,"longitude":%f,"radius":5000,"cssFilter":[{"Name":"KFC","FilterValue":true}]}',$row[1],$row[0]);

	#echo "$payload\n";
	curl_setopt($ch,CURLOPT_POSTFIELDS,$payload);
	echo curl_exec($ch);
	#$obj = json_decode(curl_exec($ch),true);

	#print_r($obj);
	#sleep(5);
	exit;

}

fclose($outfile);
echo "Done\n";
