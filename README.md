# Hibiki Engine

A FastAPI-based application managed with uv.

## Prerequisites

### Installing uv

This project uses [uv](https://docs.astral.sh/uv/) as the package manager. To install uv, follow the [official installation instructions](https://docs.astral.sh/uv/getting-started/installation/).

Quick install (macOS/Linux):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Quick install (Windows):
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Setup

Install dependencies using uv:

```bash
uv sync
```

## Running the Application

Run the FastAPI application with uvicorn:

```bash
uv run uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`.

## API Documentation

Once running, you can access:
- Interactive API docs (Swagger UI): `http://localhost:8000/docs`
- Alternative API docs (ReDoc): `http://localhost:8000/redoc`

## Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check endpoint
