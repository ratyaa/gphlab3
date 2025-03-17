set terminal svg noenhanced

outfile = "svg/psi1.svg"
set output outfile

set datafile separator ','
set grid xtics ytics mxtics mytics
set mytics 10
set mxtics 10
set xlabel "$\\nu$, \Гц"
set ylabel "$\\tg{\\psi}$"
# set xrange [0:110]

Majorgridclr = "0xD0000000"
Minorgridclr = "0xF0000000"
set grid lt -1 linecolor rgb Majorgridclr, lt -1 linecolor rgb Minorgridclr


set bars 0.25
# set title "$I(h^2),\\quad [I] = 1\\;г \\cdot м^2, \\quad [h^2] = 1\\;см^2$"
set key right bottom
set key width -16

Shadecolor = "#80E0A080"
Inputfile = "plot/psi1.csv"

f(x) = k*x + b
fit f(x) Inputfile using 1:11 via k, b

plot Inputfile using 1:11:13:12 with xyerrorbars ls -1 linecolor rgb 'red' title "Измерения $\\tg{\\psi}(\\nu)$",\
     f(x) with lines title "Аппроксимация по МНК"