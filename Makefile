all:	zip

clean:
	-rm GEPPM.zip
	
zip: clean slides
	zip GEPPM.zip LICENSE slides.pdf code/*.py code/*.csv
	
slides:
	pandoc -s -t beamer slides.md -o slides.pdf
