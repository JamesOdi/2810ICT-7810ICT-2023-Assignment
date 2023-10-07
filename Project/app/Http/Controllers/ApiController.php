<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ApiController extends Controller
{
    public function getResults(Request $request) {
        $inputData = $request->nu; // Retrieve input data from the request

        // Invoke the Python script with the input data
        $api_file = public_path('api/script.py');
        // dd($api_file);
        $pythonPath = '/usr/bin/python3.10';
        if (file_exists($api_file)) {
            $output = shell_exec("$pythonPath $api_file $inputData");
            dd($output);
        } else {
            dd('File not found');
        }
        
        // Process the output or error as needed
        dd(response()->json(['output' => $output]));

        return response()->json(['output' => $output]);
    }

    public function getAnalytics(Request $request) {
        $inputData = $request->nu; // Retrieve input data from the request
        // Invoke the Python script with the input data
        $api_file = public_path('api/analytics.py');
        // dd($api_file);
        $pythonPath = '/usr/bin/python3.10';
        if (file_exists($api_file)) {
            $output = shell_exec("$pythonPath $api_file $inputData");
            dd($output);
        } else {
            dd('File not found');
        }
        
        // Process the output or error as needed
        dd(response()->json(['output' => $output]));
        return response()->json(['output' => $output]);
    }

    public function getMobile(Request $request) {
        $inputData = $request->nu; // Retrieve input data from the request
        // Invoke the Python script with the input data
        $api_file = public_path('api/mobile.py');
        // dd($api_file);
        $pythonPath = '/usr/bin/python3.10';
        if (file_exists($api_file)) {
            $output = shell_exec("$pythonPath $api_file $inputData");
            dd($output);
        } else {
            dd('File not found');
        }
        
        // Process the output or error as needed
        dd(response()->json(['output' => $output]));
        return response()->json(['output' => $output]);
    }
}
