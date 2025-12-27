# Hibiki Engine

A FastAPI-based application managed with uv.

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
