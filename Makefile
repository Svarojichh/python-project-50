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

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff  --cov-report xml

check: selfcheck test lint

selfcheck:
	poetry check

.PHONY: install gendiff build publish package-install package-reinstall lint test test-coverage selfcheck check
