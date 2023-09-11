gendiff:
	poetry run gendiff

install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

.PHONY: gendiff