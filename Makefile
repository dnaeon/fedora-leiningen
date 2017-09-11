SHELL := /bin/bash

REL=f26
PKG=leiningen

all: review;

check: lint;

test: mock koji;

clean: cleanrpm cleandirs;

grab:
	spectool -g $(PKG).spec

lint:
	fedpkg --release $(REL) lint

local:
	fedpkg --release $(REL) local

mock:
	fedpkg --release $(REL) mockbuild

koji:
	fedpkg --release $(REL) scratch-build --target $(REL) --srpm

review:
	rm -rf review-*; fedpkg --release $(REL) srpm; fedora-review -n $(PKG)

setup:
	sudo dnf install fedora-packager fedora-review
	sudo chmod o+rwX -R /var/cache/dnf/
	kinit $(USER)@FEDORAPROJECT.ORG
	fedora-packager-setup

cleanrpm:
	rm -f *.rpm

cleandirs:
	find . -mindepth 1 -maxdepth 1 -not -path '*/\.*' -type d -exec rm -rf "{}" \;
