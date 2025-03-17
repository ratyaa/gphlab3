set terminal svg noenhanced

outfile = "svg/lnu2.svg"
set output outfile

set datafile separator ','
set grid xtics ytics mxtics mytics
set mytics 10
set mxtics 10
set xlabel "$\\nu^2$, \Гц"
set ylabel "$\\frac{L_{max}-L_{min}}{L-L_{min}}$"
# set xrange [0:110]

Majorgridclr = "0xD0000000"
Minorgridclr = "0xF0000000"
set grid lt -1 linecolor rgb Majorgridclr, lt -1 linecolor rgb Minorgridclr


set bars 0.25
# set title "$I(h^2),\\quad [I] = 1\\;г \\cdot м^2, \\quad [h^2] = 1\\;см^2$"
set key right bottom
set key width -16

Shadecolor = "#80E0A080"
Inputfile = "plot/lnu2.csv"

f(x) = k*x
fit f(x) Inputfile every ::0::8 using 5:6 via k

plot Inputfile every ::0::8 using 5:6:7:8 with xyerrorbars ls -1 linecolor rgb 'red' title "Измерения $\\frac{L_{max}-L_{min}}{L-L_{min}}(\\nu^2)$",\
     f(x) with lines title "Аппроксимация по МНК"