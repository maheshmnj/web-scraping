
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <title>User Registration</title>
  <?php 
  require 'connect.php';
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

$s='S.E.';
$t='T.E.';
$b='B.E.';
$se=Analysis($s);
// echo "<Br>";
// print_r($se);

$te=Analysis($t);
// echo "<Br>";
// print_r($te);
$be=Analysis($b);
// echo "<Br>";
// print_r($be);
?>
<!-- Font Awesome -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
<!-- Bootstrap core CSS -->
<link href="css/bootstrap.min.css" rel="stylesheet">
<!-- Material Design Bootstrap -->
<link href="css/mdb.min.css" rel="stylesheet">
<!-- Your custom styles (optional) -->
<link href="css/style.css" rel="stylesheet">
</head>

<body>

  <div class="container-fluid mb-5">

    <div class="card col-lg-6 col-md-10 col-sm-10 mt-5" style=" margin: auto auto; /* Added */
    float: none; border-radius: 20px /* Added */;">
    <div class="card-body">
      <h2 class="text-primary" style="text-align: center;" >SRTMUN Results Notifier </h2>

      <form action="registered.php" method="get">

        <div class="row">
          <div class="col-lg-6 col-md-12 col-sm-12 ">
            <div class="md-form mt-5">
              <input type="text" name="first" class="form-control">
              <label for="name">Name</label> 
            </div>
          </div>
          <div class="col-lg-6 col-md-12 col-sm-12">
            <div class="md-form mt-lg-5 mt-1">
              <input type="text" name="branch" class="form-control">
              <label for="branch">Branch</label> 
            </div>
          </div>
        </div>  
        <div class="md-form mt-0">
          <input type="email" id="email" class="form-control" name="email" autocomplete="off" required/>
          <label for="email">Email</label>           
        </div>
        <div class="md-form mt-0">
          <input type="text" id="seat" class="form-control" name="seatno" autocomplete="off" required/>
          <label for="seat">Seat Number </label>           
        </div>

        <div class="row">
          <div class="col-6">  
            <div class="md-form" style="bottom: 50%">
              <label for="Class">Class</label> 
            </div>
          </div>
          <div class="col-6">
            <div class="form-group">
              <div class="col-8" style="left: 20%">
                <select id="company" name="class" class="form-control">
                  <option>SE</option>
                  <option>TE</option>
                  <option>BE</option>
                </select> 
              </div>
            </div>
          </div>
        </div> 
        <div style="text-align: center;">
          <button class="btn btn-primary btn-circle"
          style=" word-wrap:break-word;">Notify</button>
        </div>
      </form>
    </div>
  </div>
  <h3 class="mt-5" style="text-align: center;">Statistics</h3>

  <div class="row">
    <div class="col-lg-4 col-md-12 col-sm-12 mb-5" id="piechart1" style="text-align: center;height: auto"></div>
    <div class="col-lg-4 col-md-12 col-sm-12 mb-5" id="piechart2" style="text-align: center;height: auto"></div>
    <div class="col-lg-4 col-md-12 col-sm-12 mb-5" id="piechart3" style="text-align: center;height: auto"></div>
  </div>
 

 <!-- <div class="col-lg-12 col-md-10 col-sm-12 pt-3 pb-3" style="height: auto;">
    <p>SE</p>
    <div class="container">
      <div class="skills css">
        80%
      </div>
    </div>

    <p>TE</p>
    <div class="container">
      <div class="skills js">65%</div>
    </div>

    <p>BE</p>
    <div class="container">
      <div class="skills php">60%</div>
    </div>
  </div>
</div>
<!-- SCRIPTS -->
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Draw the chart and set the chart values
function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ['Result', 'Percentage'],
    ['PASS', <?php echo $se[0];?>],
    ['RHR', <?php echo $se[1];?>],
    ['ATKT', <?php echo $se[2];?>],
    ['F-ATKT', <?php echo $se[3];?>],
    ['ABSENT', <?php echo $se[4];?>],
    ['FAIL', <?php echo $se[5];?>],
    ['DETAINED', <?php echo $se[6];?>],
    ['NOT CLEARED', <?php echo $se[7];?>],
    ]);

  // Optional; add a title and set the width and height of the chart
  var options = {'title':'SE Analysis', 'width':550, 'height':400};

  // Display the chart inside the <div> element with id="piechart"
  var chart = new google.visualization.PieChart(document.getElementById('piechart3'));
  chart.draw(data, options);
}

</script>
<script type="text/javascript">
// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Draw the chart and set the chart values
function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ['Result', 'Percentage'],
    ['PASS', <?php echo $te[0];?>],
    ['RHR', <?php echo $te[1];?>],
    ['ATKT', <?php echo $te[2];?>],
    ['F-ATKT', <?php echo $te[3];?>],
    ['ABSENT', <?php echo $te[4];?>],
    ['FAIL', <?php echo $te[5];?>],
    ['DETAINED', <?php echo $te[6];?>],
    ['NOT CLEARED', <?php echo $te[7];?>],
    ]);

  // Optional; add a title and set the width and height of the chart
  var options = {'title':'TE Analysis', 'width':550, 'height':400};

  // Display the chart inside the <div> element with id="piechart"
  var chart = new google.visualization.PieChart(document.getElementById('piechart2'));
  chart.draw(data, options);
}

</script>
<script type="text/javascript">
// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Draw the chart and set the chart values
function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ['Result', 'Percentage'],
    ['PASS', <?php echo $be[0];?>],
    ['RHR', <?php echo $be[1];?>],
    ['ATKT', <?php echo $be[2];?>],
    ['F-ATKT', <?php echo $be[3];?>],
    ['ABSENT', <?php echo $be[4];?>],
    ['FAIL', <?php echo $be[5];?>],
    ['DETAINED', <?php echo $be[6];?>],
    ['NOT CLEARED', <?php echo $be[7];?>],
    ]);

  // Optional; add a title and set the width and height of the chart
  var options = {'title':'BE Analysis', 'width':550, 'height':400};

  // Display the chart inside the <div> element with id="piechart"
  var chart = new google.visualization.PieChart(document.getElementById('piechart1'));
  chart.draw(data, options);
}

</script>
<!-- JQuery -->
<script type="text/javascript" src="js/jquery-3.3.1.min.js"></script>
<!-- Bootstrap tooltips -->
<script type="text/javascript" src="js/popper.min.js"></script>
<!-- Bootstrap core JavaScript -->
<script type="text/javascript" src="js/bootstrap.min.js"></script>
<!-- MDB core JavaScript -->
<script type="text/javascript" src="js/mdb.min.js"></script>
</body>

</html>
