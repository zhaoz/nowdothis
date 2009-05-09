default: all

all: cleanpyc plasmapkg

plasmapkg:
	cd nowdothis && zip -r ../nowdothis.plasmoid . -x \*.gitignore \*.pyc \*.swp

clean: cleanpyc
	rm -f nowdothis.plasmoid

cleanpyc:
	find ./ -iname '*.pyc' -delete

