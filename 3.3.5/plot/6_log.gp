set terminal svg noenhanced

outfile = "svg/6_log.svg"
set output outfile

set datafile separator ','
set grid xtics ytics mxtics mytics
set mytics 10
set mxtics 10
set xlabel "$\\ln I_M$"
set ylabel "$\\ln B$"

# set xrange [0:110]
# set yrange [0:1200]

Majorgridclr = "0xD0000000"
Minorgridclr = "0xF0000000"
set grid lt -1 linecolor rgb Majorgridclr, lt -1 linecolor rgb Minorgridclr


set bars 0.25
# set title "$I(h^2),\\quad [I] = 1\\;г \\cdot м^2, \\quad [h^2] = 1\\;см^2$"
set key right bottom
set key width -16

Shadecolor = "#80E0A080"
Inputfile = "plot/6.csv"

f(x) = k*x + b
fit f(x) Inputfile using 6:7 via k, b

plot Inputfile using 6:7:8:9 with xyerrorbars ls -1 linecolor rgb 'red' title "Измерения $\\ln B(\\ln I_M)$",\
     f(x) with lines title "Аппроксимация по МНК"