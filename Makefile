default: all

all: cleanpyc plasmapkg

plasmapkg:
	cd nowdothis && zip -r ../nowdothis.zip . -x \*.gitignore \*.pyc \*.swp

clean: cleanpyc
	rm -f nowdothis.zip

cleanpyc:
	find ./ -iname '*.pyc' -delete

