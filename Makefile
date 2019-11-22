SHELL = /usr/bin/env bash -xeuo pipefail

isort:
	pipenv run isort -rc \
		src/ \
		tests/

lint:
	pipenv run flake8 \
		src/ \
		tests/

format:
	pipenv run black \
		src/ \
		tests/

package:
	pipenv run aws cloudformation package \
		--template-file sam.yml \
		--s3-bucket