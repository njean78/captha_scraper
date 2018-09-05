rem echo off
rem process an image using imagemagick and do the parsing with tesseract
rem example : converter.bat captha.jpg 60 90
set filename=%1
set perc=%2
set perc2=%3
rem set filename=%filename_complete=:~0,7%
magick convert "%filename%" -threshold %perc%"%%" "%filename%_grey.jpg"
magick convert "%filename%_grey.jpg" -negate "%filename%_grey_neg.jpg"
magick convert "%filename%_grey_neg.jpg" -morphology dilate rectangle:1x10  -threshold %perc2%"%%" "%filename%_grey_neg.jpg"
magick convert "%filename%_grey.jpg" -morphology dilate rectangle:1x10  -threshold %perc2%"%%" "%filename%_grey.jpg"
tesseract -l ita --psm 13 "%filename%_grey_neg.jpg" "%filename%_out_neg"
tesseract -l ita --psm 13 "%filename%_grey.jpg" "%filename%_out"
head "%filename%_out_neg.txt"
head "%filename%_out.txt"
