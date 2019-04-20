<?php 
  $name=$_GET['first'];
  $branch=$_GET['branch'];
  $email=$_GET['email'];
  $seatno=$_GET['seatno'];
  $class=$_GET['class'];

  $sql= "INSERT INTO register(name,email,seatno,class,branch)
  VALUES ('$name','$email','$seatno','$class','$branch')";
  $ack = mysqli_query($conn,$sql);
  echo $ack;
?>


