SHELL = /usr/bin/env bash -xeuo pipefail
stack_name=bookmarks-layer

isort:
	pipenv run isort -rc \
		src/layer \
		tests/

lint:
	pipenv run flake8 \
		src/layer \
		tests/

black:
	pipenv run black \
		src/layer \
		tests/

build:
	@for handler in $$(find src -maxdepth 2 -type f -name Dockerfile); do \
		package_dir=$$(dirname $$handler); \
		pwd_dir=$$PWD; \
		docker_name=build_$$(basename $$package_dir); \
		cd $$package_dir; \
		docker image build --tag $$docker_name .; \
		docker run -it --name $$docker_name $$docker_name; \
		docker container cp $$docker_name:/workdir/python/ .; \
		docker container rm $$docker_name; \
		docker image rm $$docker_name; \
		cd $$pwd_dir; \
	done

package: build
	rm -rf dist
	mkdir dist
	pipenv run aws cloudformation package \
		--template-file sam.yml \
		--s3-bucket $$ARTIFACTS_S3_BUCKET \
		--output-template-file dist/template.yml

deploy: package
	pipenv run aws cloudformation deploy \
		--template-file dist/template.yml \
		--stack-name $(stack_name) \
		--role-arn $(AWS_CFN_DEPLOY_ROLE_ARN) \
		--no-fail-on-empty-changeset

test-unit:
	@for test_dir in $$(find tests/unit -maxdepth 1 -type d); do \
		handler=$$(basename $$test_dir); \
		if [[ $$handler =~ unit|__pycache__ ]]; then continue; fi; \
		PYTHONPATH=src/layer/python \
		pipenv run pytest $$test_dir --cov-config=setup.cfg --cov=src/layer/python/$$handler; \
	done
