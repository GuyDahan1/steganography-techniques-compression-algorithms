from scipy.fftpack import dct, idct
from skimage.io import imread, imsave
from PIL import Image


# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')


# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')


if __name__ == '__main__':
    flag = 1
    while flag:
        path = input("Please enter the image path\n")
        im = Image.open('images/' + path)
        imagePath, imageFormat = path.split(".")
        formats = ['jpg', 'jpeg', 'jfif', 'bmp', 'jp2', 'JPG', 'JPEG', 'JFIF', 'BMP', 'JP2']

        if imageFormat in formats:
            flag = 0
            rgb_im = im.convert('RGB')
            jpgImagePath = imagePath + '-jpg.jpg'
            rgb_im.save(jpgImagePath)
            im2 = imread(jpgImagePath)
            imF = dct2(im2)
            im1 = idct2(imF)
            dctImagePath = imagePath + '-dct.jpg'
            imsave(dctImagePath, im1)
        else:
            flag = input("invalid format! works only on --jpg,jpeg,jfif,bmp,jp2-- format\nif you want to try again press 1 "
                          "else press 0:")