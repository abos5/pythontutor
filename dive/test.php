<?php

$i = 10000;
while($i--){
    echo sprintf("i %d: %s\n", $i, chr($i));
}

die;
$i = 0;
while($i--) {
    $url = "http://www.yii2cms.com";
    $htmlSource = file_get_contents($url);
}

echo $htmlSource;

// array(31, )
