entrega2.pdf:  entrega2.tex entrega2.bib
	pdflatex entrega2.tex
	bibtex entrega2
	pdflatex entrega2.tex
	pdflatex entrega2.tex
	pdflatex entrega2.tex

clean:
	rm -f entrega2.pdf
	rm -f *.bst *.nav *.snm *.toc *.out *.dvi *.blg *.bbl *.aux *.log *.sty

exe:
	evince entrega2.pdf &
