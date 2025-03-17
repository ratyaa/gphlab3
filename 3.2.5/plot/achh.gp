set terminal svg noenhanced

outfile = "svg/achh.svg"
set output outfile

set datafile separator ','
set grid xtics ytics mxtics mytics
set mytics 10
set mxtics 10
set xlabel "$\\nu/\\nu_0$"
set ylabel "$U/U_0$"

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
set table "plot/smooth_achh.dat"
plot Inputfile using 5:4 smooth csplines
unset table

plot Inputfile using 5:4:11:10 with xyerrorbars ls -1 linecolor rgb 'red' title "Измерения $U/U_0(\\nu/\\nu_0)$",\
     Inputfile using 5:4 smooth csplines notitle
     



