SHELL = /bin/bash

.PHONY: test
test:
	rm {ihan,test}/*.pyc || true
	py.test --cov=ihan test/ --cov-report term-missing
	cloc bin ihan test
	flake8 bin/* ihan/*.py test/*.py

.PHONY: deploy
deploy:
	python -c 'x = open("VERSION", "r").read().split("."); open("VERSION", "w").write(x[0] + "." + x[1] + "." + str(int(x[2])+1))'
	python setup.py sdist bdist_wheel
	twine upload --skip-existing dist/ihan-*

