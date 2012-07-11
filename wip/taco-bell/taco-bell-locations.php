<?php

# The current taco bell finder URL will return all locations within a 400 mile radius.
# this means we have to make only a few requests to get all locations in the US.

# URL: http://www.tacobell.com/storelocatorjson/BsdsJSONHandler.ashx

$url = 'http://www.tacobell.com/storelocatorjson/BsdsJSONHandler.ashx';

# create the curl object
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL,$url);

# set header
$headers = array(
	"Referer: http://www.tacobell.com/storelocatorjson/BsdsJSONHandler.ashx?test",
	"X-Requested-With: XMLHttpRequest",
	"DNT:1",
	"Accept: text/html, application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8",
	"X-JSON-RPC: findNearbyStores"
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

$outfile = fopen('taco_bell_locations.csv','w');

foreach($latlngs as $k => $row) {

	# Create the json string of the formatted payload
	$payload = sprintf('{"id":4,"method":"findNearbyStores","params":{ "latitude" : "%f", "longitude" : "%f", "distance" : 400 }}',$row[1],$row[0]);

	#echo "$payload\n";
	curl_setopt($ch,CURLOPT_POSTFIELDS,urlencode($payload));
	$obj = json_decode(curl_exec($ch),true);

	print_r($obj);

	exit;

	# create header row (just once)
	if($k==0) {
		array_pop($obj['result'][0]);
		fputcsv($outfile,array_keys($obj['result'][0]));
	}

	foreach($obj['result'] as $line) {
		# the last elennt is distance from the lat,lng above. We don't want that in there.
		array_pop($line);
		fputcsv($outfile,array_values($line));
	}
	echo ($k+1). " of " . count($latlngs) . " " . count($obj['result']) ."\n";
	sleep(2);
	
}

fclose($outfile);
echo "Done\n";
