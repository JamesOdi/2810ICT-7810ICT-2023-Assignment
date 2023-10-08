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
                        <p></p>
                        <li class="nav-item">
                            <h4> Menu</h4>
                            <p></p>
                        </li>

                        <div class="dropdown">
                            <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown">
                                Penalty Cases
                            </button>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="index.html">Camera</a></li>
                                <li><a class="dropdown-item active" href="#">Radar</a></li>
                                <li><a class="dropdown-item disabled" href="#">Lidar</a></li>
                            </ul>
                        </div>
                </div>
                <p> </p>
                <a href="case" class="btn btn-success">Case Distribution</a>
                <p> </p>
                <a href="analytics" class="btn btn-success">Analytics</a>
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

                <!-- Main Content -->
                <div class="my-4">
                    <div class="row">
                        <div class="col-sm-6 col-md-12 col-lg-4 col-xl-6 col-xxl-4">
                            <h2>Exceed Speed <a href="speed">
                                    <img src="" id="analytics-chart" width="300" height="200">
                            </h2><br>
                            <p>
                        </div> </a>

                        <div class="col-sm-12 col-md-6 col-lg-4 col-xl-6 col-xxl-4">
                            <h2>Mobile Phone Usage <a href="mobile"><img src="pie.png" id="pie-chart" href="mobile"
                                        width="300" height="200"></h2><br>
                            <p>
                        </div></a>
                    </div>
        </main>
    </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>

        document.addEventListener("DOMContentLoaded", function () {
            const showButton = document.querySelector("#showButton");
            const fromDateInput = document.querySelector("#fromDate");
            const toDateInput = document.querySelector("#toDate");

            showButton.addEventListener("click", function () {
                // Get the selected "From" and "To" dates
                const fromDate = fromDateInput.value;
                const toDate = toDateInput.value;

                // You can perform actions with the selected dates here
                // For example, you can send them to a backend server for data retrieval

                // For now, let's just display the selected dates in an alert
                alert(`Selected From Date: ${fromDate}\nSelected To Date: ${toDate}`);
            });
        });

        document.addEventListener("DOMContentLoaded", function () {
            const showButton = document.querySelector("#showButton");
            const fromDateInput = document.querySelector("#fromDate");
            const toDateInput = document.querySelector("#toDate");
            const resultsTableBody = document.querySelector("#resultsTableBody");

            showButton.addEventListener("click", function () {
                // Get the selected "From" and "To" dates
                const fromDate = fromDateInput.value;
                const toDate = toDateInput.value;

                // You can perform actions with the selected dates here
                // For now, let's just create a sample result and display it in the table
                const sampleResult = [
                    { date: "2023-10-10", violationType: "Speeding" },
                    { date: "2023-10-12", violationType: "Running a red light" },
                    // Add more sample data or retrieve data from your database
                ];

                // Clear existing table rows
                resultsTableBody.innerHTML = "";

                // Populate the table with results
                sampleResult.forEach((result) => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                    <td>${result.date}</td>
                    <td>${result.violationType}</td>
                `;
                    resultsTableBody.appendChild(row);
                });
            });
        });
    </script>
</body>

</html>