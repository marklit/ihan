SHELL = /bin/bash

.PHONY: test
test:
	rm {ihan,test}/*.pyc || true
	pytest
	cloc bin ihan test
	flake8 --ignore=E1,E2,E3,W1,W2,W3 bin/* ihan/*.py test/*.py

.PHONY: deploy
deploy:
	python -c 'x = open("VERSION", "r").read().split("."); open("VERSION", "w").write(x[0] + "." + x[1] + "." + str(int(x[2])+1))'
	python setup.py sdist bdist_wheel
	twine upload --skip-existing dist/ihan-*

