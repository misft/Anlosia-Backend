<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Storage;

class TestController extends Controller
{
    public function form() {
        return view('form');
    }
    public function index(Request $req) {
        $file = $req->file('file');;
        Storage::disk('public')->put('new.png', file_get_contents($file->getClientOriginalName(), $file));

        echo Storage::disk('public')->exists('new.png');
        // $process = new Process(['py'], 'F:\TA\anlosia\public\index.py');
        // $process->run();

        // // executes after the command finishes
        // if (!$process->isSuccessful()) {
        //     throw new ProcessFailedException($process);
        // }

        // echo $process->getOutput();
        // exit;
    }
}
