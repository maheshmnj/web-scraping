 <?php 
  require 'connect.php';
// if ($conn->connect_error) {
// 		die("Connection failed to db: " . $conn->connect_error);
// 	}
// 	else{
// 		echo "Connected successfully in search";
// 	}
  $seatno=$_GET['seatnosearch'];
  $class=$_GET['classsearch'];
  $fetch_query = "SELECT Result from data where seat_no='$seatno'";
  $result = mysqli_query($conn, $fetch_query);
  $row=mysqli_fetch_assoc($result);
  $yourresult = $row['Result'];
  
  function Analysis($class){
    require 'connect.php';
    $total_se="select count(*) as total from data where  class='$class'";
    $pass="select count(*)as pass  from data where  class='$class' and result='PASS' or result='CLEARED'";
    $rhr="select count(*)as rhr from data  where  class='$class' and result='RHR'";
    $atkt="select count(*)as atkt from data  where  class='$class' and result='ATKT'";
    $f_atkt="select count(*)as f_atkt from data  where  class='$class' and result='F-ATKT'";
    $absent="select count(*)as absent from data  where  class='$class' and result='ABSENT'";
    $fail="select count(*)as fail from data  where  class='$class' and result='FAIL'";
    $detained="select count(*)as detained from data  where  class='$class' and result='DETAINED'";
    $notcleared="select count(*)as notcleared from data  where  class='$class' and result='NOT CLEARED'";

    $res=mysqli_query($conn,$total_se);
    $row_total=mysqli_fetch_assoc($res); 
    $total= $row_total['total'];
  // print_r($total);
  // echo "<Br>";
    $res1=mysqli_query($conn,$pass);
    $row_pass=mysqli_fetch_assoc($res1);
    $pass1=$row_pass['pass'];
// echo "\n";
// echo $pass1;
    $res2=mysqli_query($conn,$rhr);
    $row_rhr=mysqli_fetch_assoc($res2);
    $rhr1=$row_rhr['rhr'];



    $res3=mysqli_query($conn,$atkt);
    $row_atkt=mysqli_fetch_assoc($res3);
    $atkt1=$row_atkt['atkt'];

    $res4=mysqli_query($conn,$f_atkt);
    $row_fatkt=mysqli_fetch_assoc($res4);
    $fatkt1=$row_fatkt['f_atkt'];

    $res5=mysqli_query($conn,$absent);
    $row_absent=mysqli_fetch_assoc($res5);
    $absent1=$row_absent['absent'];


    $res6=mysqli_query($conn,$fail);
    $row_fail=mysqli_fetch_assoc($res6);
    $fail1=$row_fail['fail'];


    $res7=mysqli_query($conn,$detained);
    $row_detained=mysqli_fetch_assoc($res7);
    $detained1=$row_detained['detained'];

    $res8=mysqli_query($conn,$notcleared);
    $row_notcleared=mysqli_fetch_assoc($res8);
    $notcleared1=$row_notcleared['notcleared'];

    $a=array($pass1,$rhr1,$atkt1,$fatkt1,$absent1,$fail1,$detained1,$notcleared1);
    return $a;
  }

  if($class=='SE'){
 	 $classs='S.E.';
	}
	if($class=='TE'){
 	$classs='T.E.';
  	}
	if($class=='BE'){
 	 $classs='B.E.';
	}
	
  $analysis=Analysis($classs);

  ?>

  <!DOCTYPE html>
  <html>
  <head>
  	<title>Your Result</title>
 	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
  <!-- Bootstrap core CSS -->
  <link href="css/bootstrap.min.css" rel="stylesheet">
  <!-- Material Design Bootstrap -->
  <link href="css/mdb.min.css" rel="stylesheet">
  <!-- Your custom styles (optional) -->
  <link href="css/style.css" rel="stylesheet">
  </head>
  <body>
  <div class="container-fluid">
  		<div class="col-12">
  		<h2 style="text-align: center;vertical-align: middle;line-height: 200px;">Your Result is <strong><?php echo $yourresult ?></strong></h2>
  		<div style="height: 1px;width: 100%;background-color: black"></div>
  		<h3 class="mt-3" style="text-align: center;"><?php echo $class; ?> Class Statistics</h3>
  	  	<div class="col-6 mb-5" id="piechart1" style=" margin: auto auto;height: auto"></div>
  	  	</div>

  </div>

 <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Draw the chart and set the chart values
function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ['Result', 'Percentage'],
    ['PASS', <?php echo $analysis[0];?>],
    ['RHR', <?php echo $analysis[1];?>],
    ['ATKT', <?php echo $analysis[2];?>],
    ['F-ATKT', <?php echo $analysis[3];?>],
    ['ABSENT', <?php echo $analysis[4];?>],
    ['FAIL', <?php echo $analysis[5];?>],
    ['DETAINED', <?php echo $analysis[6];?>],
    ['NOT CLEARED', <?php echo $analysis[7];?>],
    ]);

  // Optional; add a title and set the width and height of the chart
  var options = {'width':550, 'height':400};

  // Display the chart inside the <div> element with id="piechart"
  var chart = new google.visualization.PieChart(document.getElementById('piechart1'));
  chart.draw(data, options);
}
</script>
  </body>
  </html>