set terminal svg noenhanced

outfile = "svg/6.svg"
set output outfile

set datafile separator ','
set grid xtics ytics mxtics mytics
set mytics 10
set mxtics 10
set xlabel "$I_M$, А"
set ylabel "$B$, мТл"

# set xrange [0:110]
set yrange [0:1200]

Majorgridclr = "0xD0000000"
Minorgridclr = "0xF0000000"
set grid lt -1 linecolor rgb Majorgridclr, lt -1 linecolor rgb Minorgridclr


set bars 0.25
# set title "$I(h^2),\\quad [I] = 1\\;г \\cdot м^2, \\quad [h^2] = 1\\;см^2$"
set key right bottom
set key width -16

Shadecolor = "#80E0A080"
Inputfile = "plot/6.csv"


f(x) = k*(x**n) + b
# g(x) = exp(6.94288)*(x**0.886667)
fit f(x) Inputfile using 2:3 via k, n, b

plot Inputfile using 2:3:4:5 with xyerrorbars ls -1 linecolor rgb 'red' title "Измерения $B(I_M)$",\
     f(x) with lines title "Аппроксимация функцией $f(x) = kx^n + b$"
     # g(x) with lines title "Аппроксимация"
     