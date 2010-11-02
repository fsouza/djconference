app=core

all: tests acceptance

tests:
	@specloud --with-coverage --cover-package=$(app) --with-django --verbose --nocapture --where=$(app)/tests

acceptance: clean
	@python manage.py harvest

functional: clean
	@specloud --with-coverage --cover-package=$(app) --with-django --verbose --nocapture --where=$(app)/tests/functional

unit: clean
	@specloud --with-coverage --verbose --nocapture --where=$(app)/tests/unit

bootstrap:
	@pip install -r requirements.txt

clean:
	@echo 'Cleaning...'
	@find . -name "*.pyc" -exec rm -f {} \;
