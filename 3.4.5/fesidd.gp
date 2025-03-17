set terminal svg noenhanced

outfile = "fesidd.svg"
set output outfile

set datafile separator ','
set grid xtics ytics mxtics mytics
set mytics 10
set mxtics 10
set xlabel "$H,\\ А/м$"
set ylabel "$\\frac{dB}{dH},\\ мТл \\cdot м/А$"
# set xrange [0:400]
# set yrange [0:0.22]

Majorgridclr = "0xD0000000"
Minorgridclr = "0xF0000000"
set grid lt -1 linecolor rgb Majorgridclr, lt -1 linecolor rgb Minorgridclr


set bars 0.25
# set title "$I(h^2),\\quad [I] = 1\\;г \\cdot м^2, \\quad [h^2] = 1\\;см^2$"
set key right bottom
set key width -16

Shadecolor = "#80E0A080"
Inputfile = "fesi.csv"

y0=NaN
x0=NaN

plot Inputfile using (dx=$16-x0,x0=$16,$16-dx/2):(dy=$13-y0,y0=$13,dy/dx) smooth csplines title "approx",\
     Inputfile using (dx=$16-x0,x0=$16,$16-dx/2):(dy=$13-y0,y0=$13,dy/dx) title "$\\frac{dB}{dH}$"


