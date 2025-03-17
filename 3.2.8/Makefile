.PHONY: plots

plots: $(patsubst %.svg,%.gp,$(wildcard *.svg))

%.svg: %.gp
	gnuplot $<
