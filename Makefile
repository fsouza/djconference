acceptance:
	@python manage.py harvest

bootstrap:
	@pip install -r requirements.txt

clean:
	@echo 'Cleaning...'
	@find . -name "*.pyc" -exec rm -f {} \;
