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