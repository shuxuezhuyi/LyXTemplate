LYXFILELIST = $(shell find . -name "*.lyx")
IPEFILELIST = $(shell find . -name "*.ipe")
PDFFILELIST = $(patsubst %.ipe,%.pdf,$(IPEFILELIST))
PgfList = $(shell find . -wholename "*/picture/*.tex")
PgfPdfList = $(patsubst %.tex,%-figure0.pdf,$(PgfList))
plantumlList = $(shell find . -name "*.plantuml")
pdf_from_plantuml = $(patsubst %.plantuml,%.pdf,$(plantumlList))
LearningMath.pdf : $(LYXFILELIST) $(PDFFILELIST) preamble.tex reference.bib mathmacros $(PgfPdfList)
	lyx -e pdf4 LearningMath.lyx
$(PDFFILELIST) : %.pdf : %.ipe
	iperender -pdf $< $@
$(PgfPdfList) : %-figure0.pdf : %.tex
	cd $(shell dirname $<); pdflatex -shell-escape $(shell basename $<); rm $(shell basename $< .tex).aux $(shell basename $< .tex).auxlock $(shell basename $< .tex).log $(shell basename $< .tex).pdf $(shell basename $< .tex)-figure0.dpth $(shell basename $< .tex)-figure0.log $(shell basename $< .tex)-figure0.md5
$(pdf_from_plantuml) : %.pdf : %.plantuml
	cd $(shell dirname $<); plantuml -tlatex $(shell basename $<); sed -i '2 i \\\usepackage{ctex}' $(shell basename $< .plantuml).latex; xelatex $(shell basename $< .plantuml).latex 1>/dev/null; rm $(shell basename $< .plantuml).aux $(shell basename $< .plantuml).latex $(shell basename $< .plantuml).log
.PHONY : install clean ipetopdf mathmacros depend zhmakeindex config preamble pgftopdf plantumltopdf
install : config depend zhmakeindex preamble
	@echo '这只是做了些准备工作, 你还需要运行一次 make 以编译出 pdf.'
clean :
	find . -name "*.pdf" | xargs rm -f
	find . -name "*.eps" | xargs rm -f
ipetopdf : $(PDFFILELIST)
pgftopdf : $(PgfPdfList)
plantumltopdf : $(pdf_from_plantuml)
mathmacros :
	lyx -e xetex ./Other/MathMacros/MathMacros.lyx
	python3 ./tools/mathmacros.py
depend :
	cp -vur --backup=numbered ./.depend/lyx/. ~/.lyx/
	cd ~/.lyx; python -tt "/usr/share/lyx/configure.py" --binary-dir=~
zhmakeindex :
	python3 ./tools/zhmakeindex.py
config :
	python3 ./tools/pre_config.py
preamble :
	python3 ./tools/pre_preamble.py

