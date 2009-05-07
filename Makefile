default: all

all: plasmapkg

plasmapkg:
	cd nowdothis && zip -r ../nowdothis.zip . --exclude \*.gitignore

clean:
	rm -f nowdothis.zip

