<?php

use Illuminate\Support\Facades\Route;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/as', function () {
    echo shell_exec("py index.py");
    // $process = new Process(['py'], 'F:\TA\anlosia\public\index.py');
    // $process->run();

    // // executes after the command finishes
    // if (!$process->isSuccessful()) {
    //     throw new ProcessFailedException($process);
    // }

    // echo $process->getOutput();
    // exit;
});
