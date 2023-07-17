.PHONY: docs

docs:
	cd ./docs/ && pipenv run make livehtml
