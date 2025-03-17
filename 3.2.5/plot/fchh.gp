set terminal svg noenhanced

outfile = "svg/fchh.svg"
set output outfile

set datafile separator ','
set grid xtics ytics mxtics mytics
set mytics 10
set mxtics 10
set xlabel "$\\nu$, кГц"
set ylabel "$\\varphi$"

# set xrange [0:110]

Majorgridclr = "0xD0000000"
Minorgridclr = "0xF0000000"
set grid lt -1 linecolor rgb Majorgridclr, lt -1 linecolor rgb Minorgridclr


set bars 0.25
# set title "$I(h^2),\\quad [I] = 1\\;г \\cdot м^2, \\quad [h^2] = 1\\;см^2$"
set key right bottom
set key width -16

Shadecolor = "#80E0A080"
Inputfile = "plot/fachh.csv"

set samples 10000
set table "plot/smooth_fchh.dat"
plot Inputfile using 3:6 smooth csplines
unset table

plot Inputfile using 3:6:8:12 with xyerrorbars ls -1 linecolor rgb 'red' title "Измерения $\\varphi(\\nu)$",\
     Inputfile using 3:6 smooth csplines notitle