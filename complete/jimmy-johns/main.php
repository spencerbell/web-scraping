<?php
  
include_once('../../lib/zipcodes.php');

# States where Jimmy Johns has a franchise
$states = array( 'AL', 'AR', 'AZ', 'CA', 'CO', 'DC', 'FL', 'GA', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MD', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'WA', 'WI', 'WV', 'WY');

$url = "http://www.jimmyjohns.com/services/findajjs_lookup.asmx/getLocationsByZip";

$ch = curl_init();
curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);

$xml = new DOMDocument();

@unlink(__DIR__. '/output/locations.csv');
$outfile = fopen(__DIR__ . '/output/locations.csv','w');

$header = array(
	'storeid',
	'storename',
	'hours',
	'address',
	'address2',
	'telephone',
	'allowOnlineOrdering',
	'lat',
	'long',
	'state'
);

fputcsv($outfile,$header);

foreach($zipcodes as $key => $line) {
	$zip = $line[0];
	$state = $line[4];

	try {
		if(!in_array($state,$states)) throw new Exception("No locations in this state: $state");

		curl_setopt($ch,CURLOPT_URL,"$url?zip=$zip");
		$response = curl_exec($ch);

		if(strpos($response,'There are no Jimmy Johns Locations') !== false) throw new Exception('No locations: skipped'); 

		if($xml->loadXML($response) == false) throw new Exception("Response failed");

		$xpath = new DOMXpath($xml);

		foreach($xpath->query("//locationinfo") as $element) {
			$arr = array();
			foreach($element->childNodes as $node) {
				if($node->nodeType == 1 && $node->nodeName !== 'distance') {
					$arr[$node->nodeName] = $node->nodeValue;
				}

			}
			$arr['state'] = $state;
			fputcsv($outfile,$arr);
		}

		sleep(5);

	} catch(Exception $e) {
		echo $e->getMessage() . "\n";

	}

	echo "Processed $zip (" . ($key+1) . " of " . count($zipcodes) . ")\n";

}
fclose($outfile);

echo "Done\n";

/*

<locationinfo>
	<storeid>01288</storeid>
	<storename> Houston</storename>
	<hours> Mon-Sun 11:00am-10pm</hours>
	<address> 12925 FM 1960 Rd. W.</address>
	<address2/>
	<telephone> 832-237-4440</telephone>
	<allowOnlineOrdering> True</allowOnlineOrdering>
	<lat> 29.92069</lat>
	<long> -95.60655</long>
	<distance> 3.08</distance>
</locationinfo>
 */
