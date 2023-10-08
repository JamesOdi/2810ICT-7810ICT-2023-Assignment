<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ApiController extends Controller
{
    public function getResults(Request $request) {
        $toDate = $request->toDate; // Retrieve input data from the request
        $fromDate = $request->fromDate; // Retrieve input data from the request
        $date = "$toDate $fromDate";
        // Invoke the Python script with the input data
        $api_file = public_path('api/script.py');
        // dd($api_file);
        $pythonPath = '/usr/bin/python3.10';
        if (file_exists($api_file)) {
            $output = shell_exec("$pythonPath $api_file $date");
        } else {
            dd('File not found');
        }

        $filePath = public_path('api/feature_1.csv');

        // Check if the CSV file exists
        if (file($filePath)) {
            // Read the CSV file
            $csvData = array_map('str_getcsv', file($filePath));
        } else {
            abort(404); // Or handle the file not found case appropriately
        }

        // Process the output or error as needed
        return view('welcome')->with('response', $csvData);
    }

    public function getAnalytics(Request $request) {
        $inputData = $request->nu; // Retrieve input data from the request
        // Invoke the Python script with the input data
        $api_file = public_path('api/analytics.py');
        // dd($api_file);
        $pythonPath = '/usr/bin/python3.10';
        if (file_exists($api_file)) {
            $output = shell_exec("$pythonPath $api_file $inputData");
        } else {
            dd('File not found');
        }
        
        // Process the output or error as needed
        return view('analytics');
    }

    public function getSpeed(Request $request) {
        $inputData = $request->nu; // Retrieve input data from the request
        // Invoke the Python script with the input data
        $api_file = public_path('api/speed.py');
        // dd($api_file);
        $pythonPath = '/usr/bin/python3.10';
        if (file_exists($api_file)) {
            $output = shell_exec("$pythonPath $api_file $inputData");
        } else {
            dd('File not found');
        }
    
        // Process the output or error as needed
        $filePath = public_path('api/feature_5.csv');
        // Check if the CSV file exists
        if (file($filePath)) {
            // Read the CSV file
            $csvData = array_map('str_getcsv', file($filePath));
        } else {
            abort(404); // Or handle the file not found case appropriately
        }
        
        return view('speed')->with('response',$csvData);
    }

    public function getCases(Request $request) {
        $inputData = $request->off; // Retrieve input data from the request
        // Invoke the Python script with the input data
        $api_file = public_path('api/case.py');
        // dd($api_file);
        $pythonPath = '/usr/bin/python3.10';
        if (file_exists($api_file)) {
            $output = shell_exec("$pythonPath $api_file $inputData");
        } else {
            dd('File not found');
        }
        
        // Process the output or error as needed
        return view('case');
    }
    
}
