<!-- <!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<meta http-equiv="x-ua-compatible" content="ie=edge">
	<title>Success</title>
	Font Awesome 
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
	Bootstrap core CSS 
	<link href="css/bootstrap.min.css" rel="stylesheet">
	Material Design Bootstrap
	<link href="css/mdb.min.css" rel="stylesheet">
	Your custom styles (optional)
	<link href="css/style.css" rel="stylesheet">
</head>
<BODY> -->
<?php 
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname="student";
// Create connection
	$conn = new mysqli($servername, $username, $password,$dbname);

// Check connection
	if ($conn->connect_error) {
		die("Connection failed to db: " . $conn->connect_error);
	}
	// else{
	// 	echo "Connected successfully";
	// }
 ?>
<!--  <div style="text-align: center; top: 30%" class="bg-light">
	<h2 class="text-success" style="text-align: center;">you are Successfully Registered</h2><br>
	<h4 style="text-align: center;"> You will be notified at <?php echo $email ?> once the results are out<p> </p></h4>
	</div> -->
<!-- </BODY>
</html> -->