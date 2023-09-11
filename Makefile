gendiff:
	poetry run gendiff

install:
	poetry install

publish:
	poetry publish --dry-run

build:
	poetry build

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

.PHONY: gendiff