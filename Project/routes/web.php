<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ApiController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', [ApiController::class, 'getResults']);

Route::get('/test', [ApiController::class, 'getResults']);

Route::get('/case', [ApiController::class, 'getCases']);

Route::get('/analytics', [ApiController::class, 'getAnalytics']);

Route::get('/mobile', [ApiController::class, 'getMobile']);

Route::get('/speed', [ApiController::class, 'getSpeed']);
