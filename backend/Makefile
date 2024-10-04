# Variables
PYTHON := python3
PIP := $(PYTHON) -m pip
DJANGO_MANAGE := $(PYTHON) manage.py

# Create a virtual environment
venv:
	$(PYTHON) -m venv venv
	@echo "Virtual environment created. Run 'source venv/bin/activate' to activate it."

# Install project dependencies
install:
	$(PIP) install -r requirements.txt
	@echo "Dependencies installed."

# Install development dependencies via pyproject.toml
install-dev:
	$(PIP) install --upgrade pip
	$(PIP) install .

# Run Django server
run:
	$(DJANGO_MANAGE) runserver

# Run Django migrations
migrate:
	$(DJANGO_MANAGE) migrate

# Create a new migration based on models
makemigrations:
	$(DJANGO_MANAGE) makemigrations

# Start a Django shell
shell:
	$(DJANGO_MANAGE) shell

# Run tests
test:
	$(DJANGO_MANAGE) test

# Format code with Black
format:
	black .

# Lint code with flake8
lint:
	flake8 .

# Create Django superuser
createsuperuser:
	$(DJANGO_MANAGE) createsuperuser
