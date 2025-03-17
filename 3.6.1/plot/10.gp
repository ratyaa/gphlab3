set terminal svg noenhanced

outfile = "svg/10.svg"
set output outfile

set datafile separator ','
set grid xtics ytics mxtics mytics
set mytics 10
set mxtics 10
set xlabel "$\\sfrac{1}{T},\\ мс^{-1}$"
set xlabel "$\\delta\\nu$, кГц"
set xrange [0:5.5]
set yrange [0:6]

Majorgridclr = "0xD0000000"
Minorgridclr = "0xF0000000"
set grid lt -1 linecolor rgb Majorgridclr, lt -1 linecolor rgb Minorgridclr


set bars 0.25
# set title "$I(h^2),\\quad [I] = 1\\;г \\cdot м^2, \\quad [h^2] = 1\\;см^2$"
set key right bottom
set key width -16

Shadecolor = "#80E0A080"
Inputfile = "plot/9.csv"

f(x) = k*x + b
fit f(x) Inputfile using 3:4 via k, b

plot Inputfile using 3:4:7:5 with xyerrorbars ls -1 linecolor rgb 'red' title "$\\delta\\nu (\\sfrac{1}{T})$",\
     f(x) with lines title "Аппроксимация по МНК"