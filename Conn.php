<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname="demo";
// Create connection
$conn = new mysqli($servername, $username, $password,$dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully";
$name=$_GET['first'];
//echo $name;
$branch=$_GET['branch'];
$email=$_GET['email'];
$seatno=$_GET['seatno'];
$class=$_GET['class'];

$sql= "INSERT INTO user (name,email,class,seatno,branch)
VALUES ('$name','$email','$class','$seatno','$branch')";
if($conn->query($sql)===TRUE)
{
	echo "Registered successfully";
}
else
{
	echo "Error: " . $sql . "<br>" . $conn->error;
}


?>