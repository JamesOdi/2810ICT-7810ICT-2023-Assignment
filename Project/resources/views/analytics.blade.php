<!DOCTYPE html>

<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Traffic Violation Database</title>
    <!-- Add Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body>
    <div class="container-fluid">
        <div class="row">
            <!-- Left Sidebar -->
            <nav id="sidebar" class="col-md-3 col-lg-2 d-md-block bg-light sidebar position-fixed top-0">

                <div class="position-sticky">
                    <ul class="nav flex-column">

                        <li class="nav-item">
                            <h4 class="nav-heading">Menu</h4>
                        </li>


                        <div class="dropdown">
                            <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown">
                                Penalty Cases
                            </button>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="#">Camera</a></li>
                                <li><a class="dropdown-item active" href="#">Radar</a></li>
                                <li><a class="dropdown-item disabled" href="#">Lidar</a></li>
                            </ul>
                        </div>
                </div>
                <p> </p>
                <a href="case.html" class="btn btn-success">Case Distribution</a>
                <p> </p>
                <a href="analytics.html" class="btn btn-success">Analytics</a>
                </ul>
        </div>
        </nav>

        <!-- Page Content -->
        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
            </nav>

            <div class="container mt-5">
                <h1>Analytics</h1>
                <p>Quick Glance at summary of traffic violations</p>
                <!-- Search Bars for "From" and "To" Dates -->
                <div class="row">
                    <div class="col-md-6">
                        <div class="form-group">
                            <label for="fromDate">From Date:</label>
                            <input type="date" class="form-control" id="fromDate">
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="form-group">
                            <label for="toDate">To Date:</label>
                            <input type="date" class="form-control" id="toDate">
                        </div>
                    </div>
                </div>

                <!-- "Show" Button -->
                <button class="btn btn-primary mt-3">Show</button>

                <!-- Main Content -->
                <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                    <!-- Analytics Chart -->
                    <div class="my-4">
                        <h2>Analytics Chart</h2>
                        <p></p>
                        <!-- Add your analytics chart here -->
                        <div id="analytics-chart">
                            <img src='{{asset("images/exceed_speed_percentage.png")}}' alt="">
                        </div>
                    </div>

                    <!-- Graph Chart -->
                    <div class="my-4">
                        <h2>Graph Chart</h2>
                        <p></p>
                        <!-- Add your graph chart here -->
                        <div id="graph-chart"></div>
                    </div>

                    <!-- Pie Chart -->
                    <div class="my-4">
                        <h2>Pie Chart</h2>
                        <p></p>
                        <!-- Add your pie chart here -->
                        <div id="pie-chart"></div>
                    </div>

                    <!-- Table -->
                    <div class="my-4">
                        <h2>Data Table</h2>
                        <!-- Add your data table here -->
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Column 1</th>
                                    <th>Column 2</th>
                                    <th>Column 3</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Data 1</td>
                                    <td>Data 2</td>
                                    <td>Data 3</td>
                                </tr>
                                <!-- Add more rows as needed -->
                            </tbody>
                        </table>
                    </div>
                </main>
        </main>
    </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

    <script src="search-bar-select.js"></script>
</body>

</html>