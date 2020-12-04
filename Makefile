install:
	poetry install

brain-games:
    poetry run brain-games

build: check
	poetry build

publish:
    poetry publish --dry-run

package-install:
    pip install --user dist/*.whl.

.PHONY: install
