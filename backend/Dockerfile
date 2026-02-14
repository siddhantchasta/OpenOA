FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential git && \
    rm -rf /var/lib/apt/lists/*

# Copy entire project (so openoa installs from source)
COPY . /app

# Install OpenOA (editable install)
RUN pip install --upgrade pip && \
    pip install -e . && \
    pip install fastapi uvicorn[standard]

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
