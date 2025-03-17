set terminal svg noenhanced

outfile = "svg/22.svg"
set output outfile

set datafile separator ','
set grid xtics ytics mxtics mytics
set mytics 10
set mxtics 10
set xlabel "$m$, \%"
set ylabel "$a_{\\mathrm{side}} / a_{\\mathrm{base}}$, \%"
set xrange [0:110]

Majorgridclr = "0xD0000000"
Minorgridclr = "0xF0000000"
set grid lt -1 linecolor rgb Majorgridclr, lt -1 linecolor rgb Minorgridclr


set bars 0.25
# set title "$I(h^2),\\quad [I] = 1\\;г \\cdot м^2, \\quad [h^2] = 1\\;см^2$"
set key right bottom
set key width -16

Shadecolor = "#80E0A080"
Inputfile = "plot/22.csv"

f(x) = k*x
fit f(x) Inputfile using 12:9 via k

plot Inputfile using 12:9 linecolor rgb 'red' title "$a_{\\mathrm{side}} / a_{\\mathrm{base}} (m)$",\
     f(x) with lines title "Аппроксимация по МНК"