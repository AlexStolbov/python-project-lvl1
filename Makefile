install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --force --user dist/*.whl

lint:
	poetry run flake8 brain_games_pac

.PHONY: install
