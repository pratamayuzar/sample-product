run:
	python manage.py
	
clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

test:
	pytest tests/ -v

coverage:
	pytest --cov=src tests/

coverage_html:
	pytest --cov=src --cov-report html:_htmlcov tests/ -v

lint:
	pylint src/*

migrate:
	orator migrate -c config/orator.py -f
