# Use official Python image
FROM python:3.10.12

# Set working directory
WORKDIR /app

# Copy files to container
COPY lookup-cli.py /app/lookup-cli.py
COPY data.yaml /app/data.yaml

# Install dependencies
RUN pip install pyyaml

# Set entrypoint
ENTRYPOINT ["python", "lookup-cli.py"]
