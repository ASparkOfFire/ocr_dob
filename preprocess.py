import cv2
import numpy as np

def preprocess(image_file, threshold):
    I = cv2.imread(image_file)
    gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
    orignrows, origncols = gray.shape
    M = int(np.floor(orignrows/16) + 1)
    N = int(np.floor(origncols/16) + 1)
    Mextend = round(M/2)-1
    Nextend = round(N/2)-1
    aux =cv2.copyMakeBorder(gray, top=Mextend, bottom=Mextend, left=Nextend,
                          right=Nextend, borderType=cv2.BORDER_REFLECT)
    windows = np.zeros((M,N),np.int32)
    imageIntegral = cv2.integral(aux, windows,-1)
    nrows, ncols = imageIntegral.shape
    result = np.zeros((orignrows, origncols))
    for i in range(nrows-M):
        for j in range(ncols-N):
            result[i, j] = imageIntegral[i+M, j+N] - imageIntegral[i, j+N]+ imageIntegral[i, j] - imageIntegral[i+M,j]
    binar = np.ones((orignrows, origncols), dtype=bool)
    graymult = (gray).astype('float64')*M*N
    binar[graymult <= result*(100.0 - threshold)/100.0] = False
    binar = (255*binar).astype(np.uint8)

    return binar

