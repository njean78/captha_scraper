rem C:\Program Files (x86)\Tesseract-OCR
rem C:\Program Files\ImageMagick-7.0.8-Q16
rem
rem convert image in gray scale for tesseract
rem

rem magick convert captcha.jpg -set colorspace Gray -separate -average captcha_grey.jpg

rem magick convert captcha.jpg -type bilevel -separate -average captcha_grey2.jpg

rem magick convert captcha.jpg -monochrome -negate captcha_grey3.jpg

rem magick convert captcha.jpg -monochrome -negate -threshold 64% captcha_grey4.jpg
rem echo off
set filename=%1
set perc=%2
set perc2=%3
rem set filename=%filename_complete=:~0,7%
magick convert "%filename%" -threshold %perc%"%%" "%filename%_grey.jpg"
magick convert "%filename%_grey.jpg" -negate "%filename%_grey_neg.jpg"
magick convert "%filename%_grey_neg.jpg" -morphology dilate rectangle:1x10  -threshold %perc2%"%%" "%filename%_grey_neg.jpg"
magick convert "%filename%_grey.jpg" -morphology dilate rectangle:1x10  -threshold %perc2%"%%" "%filename%_grey.jpg"
tesseract -l eng --psm 7 "%filename%_grey_neg.jpg" "%filename%_out_neg.txt"
tesseract -l eng --psm 7 "%filename%_grey.jpg" "%filename%_out.txt"
