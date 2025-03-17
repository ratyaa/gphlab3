set terminal svg noenhanced

outfile = "svg/Cu_KI.svg"
set output outfile

set datafile separator ','
set grid xtics ytics mxtics mytics
set mytics 10
set mxtics 10
set xlabel "$I$, A"
set ylabel "$k$, нВ/мТл"

# set xrange [0:110]

Majorgridclr = "0xD0000000"
Minorgridclr = "0xF0000000"
set grid lt -1 linecolor rgb Majorgridclr, lt -1 linecolor rgb Minorgridclr


set bars 0.25
# set title "$I(h^2),\\quad [I] = 1\\;г \\cdot м^2, \\quad [h^2] = 1\\;см^2$"
set key left bottom
set key width -16

Shadecolor = "#80E0A080"
Inputfile = "plot/Cu_KI.csv"


f(x) = k*x
fit f(x) Inputfile using 1:2 via k

plot Inputfile using 1:2:4:3 with xyerrorbars ls -1 linecolor rgb 'red' title "Измерения $k(I)$",\
     f(x) with lines title "Аппроксимация по МНК"