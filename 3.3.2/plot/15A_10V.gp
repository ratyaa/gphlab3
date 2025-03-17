set terminal svg noenhanced

outfile = "svg/15A_10V.svg"
set output outfile

set datafile separator ','
set grid xtics ytics mxtics mytics
set mytics 10
set mxtics 10
set xlabel "$U^{\\frac{3}{2}},\\ В^{\\frac{3}{2}}$"
set ylabel "$I$, мкА"
# set xrange [0:110]

Majorgridclr = "0xD0000000"
Minorgridclr = "0xF0000000"
set grid lt -1 linecolor rgb Majorgridclr, lt -1 linecolor rgb Minorgridclr


set bars 0.25
# set title "$I(h^2),\\quad [I] = 1\\;г \\cdot м^2, \\quad [h^2] = 1\\;см^2$"
set key right bottom
set key width -16

Shadecolor = "#80E0A080"
Inputfile = "plot/15Agay.csv"

f(x) = k*x
fit f(x) Inputfile every ::1::16 using 6:3 via k

plot Inputfile every ::1::16 using 6:3:7:4 with xyerrorbars ls -1 linecolor rgb 'red' title "Измерения $I (U^{\\frac{3}{2}})$ при $U \\le 10\\ В$",\
     f(x) with lines title "Аппроксимация по МНК"