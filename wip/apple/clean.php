<?php

$stdin = fopen('php://stdin','r');
$dirty_html = fread($stdin,1000000000);

require_once __DIR__ . '/../../lib/htmlpurifier/HTMLPurifier.standalone.php';

$config = HTMLPurifier_Config::createDefault();
$config->set('HTML.Allowed', 'a[href],ul,li,div');
$purifier = new HTMLPurifier($config);
$clean_html = $purifier->purify($dirty_html);

echo $clean_html;
