PROJNAME=nowdothis
PLASMOID=${PROJNAME}.plasmoid

default: all

all: cleanpyc plasmapkg

plasmapkg:
	cd nowdothis && zip -r ../${PLASMOID} . -x \*.gitignore \*.pyc \*.swp \*.pyo

clean: cleanpyc
	rm -f nowdothis.plasmoid

cleanpyc:
	find ./ -iname '*.pyc' -delete

install:
	plasmapkg --install ${PLASMOID}

uninstall:
	plasmapkg --remove ${PROJNAME}

view:
	plasmoidviewer ${PROJNAME}
