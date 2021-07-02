FROM bitnami/python:3.9-prod

WORKDIR /app

# Install poetry first reuse layer with changing Python dependencies
RUN pip install --no-cache-dir poetry==1.1.7

# Copy in the project config/dependency files
COPY pyproject.toml poetry.lock ./

# Install only dev dependencies
RUN poetry install --no-root --no-dev

# Copy the actual Python app
COPY main.py ./

# Install actual app to make it available as poetry command
RUN poetry install --no-dev

CMD ["poetry", "run", "sketchbench-data-ingestion-tester"]
