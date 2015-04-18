<?php
set_time_limit(0);

$link = mysql_connect('localhost', 'root', 'iubloomington');
if (!$link) {
    die('Could not connect: ' . mysql_error());
}
mysql_select_db("eamcet2014");

$query = mysql_query("SELECT htno FROM eamcet_med WHERE status='0'");
while($row = mysql_fetch_array($query)) {
	$htno = $row['htno'];
	//$ch = curl_init("http://sakshieducation.com/results2013/EAMCET/Medicine.aspx?htno=" . $htno);
	$curl = curl_init();
	curl_setopt_array($curl, array(
	    CURLOPT_RETURNTRANSFER => 1,
	    CURLOPT_URL => 'http://www.schools9.com/andhra/eamcet-results-2014.aspx?eam2k9id=' . $htno,
	    CURLOPT_USERAGENT => 'Google Chrome 32.44'
	));
	$res = curl_exec($curl);
	curl_close($curl);
	$insert = mysql_query("UPDATE eamcet_med SET result = '$res', status = '1' WHERE htno = '$htno'");
	echo $htno . " ---- " . $res . "<br />";
}

mysql_close();
?>