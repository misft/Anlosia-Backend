import numpy as np
import os
import cv2
import sys

pengenalWajah = cv2.face.LBPHFaceRecognizer_create()
detektor = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")

def prediksiWajah(namaBerkas):
    citra = cv2.imread(namaBerkas)

    if citra is None:
        print("Tidak dapat membaca berkas citra")
        return

    abuAbu = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)
    daftarwajah = detektor.detectMultiScale(abuAbu,scaleFactor= 1.3,minNeighbors= 5)
    if daftarwajah is None:
        print("wajah tidak terdeteksi")
        return
    for(x,y,w,h) in daftarwajah:
        cv2.rectangle(citra, (x,y),(x+w,y+h),
        (255,0,0),2)
        wajah = abuAbu[y:y+h, x:x+w]
        labelId, konfiden = pengenalWajah.predict(wajah)
        if konfiden <150:
            cv2.putText(citra,"(%s) %.0f"%
                (labelId,konfiden),
                (x,y-2),
                cv2.FONT_HERSHEY_PLAIN,
                1,(0,255,0)),
        else:
            cv2.putText(citra,"Data Tidak Terdaftar",(x,y-2),
            cv2.FONT_HERSHEY_PLAIN,1,
            (0,255,0))
    cv2.imshow("Hasil",citra)
    print(konfiden)

pengenalWajah.read("pelatihan.yml")
prediksiWajah(sys.argv[1])


