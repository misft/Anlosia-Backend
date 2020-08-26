import numpy as np
import os
import cv2

pengenalwajah = cv2.face.LBPHFaceRecognizer_create()
detektor = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")

def perolehCitradanLabel(lintasan):
    daftarFolderCitra = [os.path.join(lintasan, f)\
        for f in os.listdir(lintasan)]

    daftarSampelWajah =[]
    daftarIdWAJAH =[]

    for foldercitra in daftarFolderCitra:
        daftarBerkas = os.listdir(foldercitra)
        for berkas in daftarBerkas:
            berkasCitra = foldercitra + "\\" + berkas
            print("Pemrosesan berkas citra", berkasCitra)

            citra = cv2.imread(berkasCitra, 0)

            idWajah = os.path.basename(foldercitra)[1:]
            idWajah = int(idWajah)

            daftarWajah = detektor.detectMultiScale(citra)

            for(x,y,w,h) in daftarWajah:
                daftarSampelWajah.append(
                    citra[y : y + h, x : x + w])
                daftarIdWAJAH.append(idWajah)
                
    return daftarSampelWajah, daftarIdWAJAH
daftarWajah, daftarIdWAJAH = perolehCitradanLabel("data-wajah")
pengenalwajah.train(daftarWajah, np.array(daftarIdWAJAH))
pengenalwajah.save(("pelatihan.yml"))