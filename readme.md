# AI LLM Microservice API

A production-ready, asynchronous Python API built with **FastAPI** to serve Large Language Models (LLMs) locally. This project follows **Clean Architecture** principles, drawing inspiration from Java's Spring Boot structure to ensure scalability, maintainability, and a clear separation of concerns.

## 🚀 Project Overview

This microservice acts as a bridge between local GGUF models (via Hugging Face) and client applications. It leverages **FastAPI** for high-performance asynchrony and **Pydantic** for strict data validation, ensuring that heavy LLM inference processes are managed efficiently without blocking the API's responsiveness.

---

## 🛠️ Tech Stack & Dependencies

### Core Stack
* **Language:** Python 3.10+
* **Framework:** FastAPI (Asynchronous API)
* **Server:** Uvicorn (ASGI Server)
* **Validation:** Pydantic V2 (Type safety & Serialization)

### Active Libraries in `.venv`
* `fastapi`: Core web framework.
* `uvicorn`: High-performance ASGI server.
* `pydantic`: Data schemas and validation.
* `python-dotenv`: Management of environment variables.
* `ctransformers`: LLM inference engine with GGUF support.
* `pytest`: Automated unit testing suite.
* `httpx`: Async test client for integration testing.

---

## 📁 Project Structure

```text
ai-llm-service/
├── app/
│   ├── main.py              # Application Entry point (App Factory)
│   ├── api/                 # Controllers / Routers (Equivalent to Spring RestControllers)
│   │   └── v1/
│   │       └── chat.py      # LLM Chat endpoints
│   ├── core/                # Global Config & Security
│   │   └── config.py
│   ├── services/            # Business Logic (Equivalent to @Service)
│   │   └── llm_service.py   # Model loading & inference logic
│   └── schemas/             # DTOs (Data Transfer Objects)
│       └── chat_schema.py   # Request/Response validation via Pydantic
├── tests/                   # Automated Test Suite (Pytest)
│   └── api_tests.http       # REST Client test file (Version-controlled)
├── .env                     # Local environment secrets (Not in Git)
├── openapi.json             # Exported API Contract (Swagger Source)
└── requirements.txt         # Dependency manifest
```

---

## 🏃 How to Run

1.  **Initialize Environment:**
    Ensure you have Python 3.10+ installed and create your virtual environment:
    ```bash
    python -m venv .venv
    ```

2.  **Activate Virtual Environment:**
    ```bash
    # Windows
    .venv\Scripts\activate
    # Linux/macOS
    source .venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Start the Server:**
    ```bash
    uvicorn app.main:app --reload
    ```
    *The API will be available at http://localhost:8000.*

---

## 📖 API Documentation & Swagger

This project uses **OpenAPI** standards for contract-first development. FastAPI automatically generates the documentation by reflecting on Python type hints and Pydantic models.

### Accessing the UI
* **Interactive UI (Swagger):** Navigate to http://localhost:8000/docs to test endpoints in real-time.
* **Alternative UI (Redoc):** Navigate to http://localhost:8000/redoc.

### Generating & Exporting Swagger (openapi.json)
To capture the API contract for version control or integration with external testing tools:
1. Ensure the server is running.
2. Run the following command to download the schema:
    ```bash
    curl http://localhost:8000/openapi.json -o openapi.json
    ```

---

## 🔌 VS Code Plugins Used

To maintain this project's professional workflow, the following extensions are utilized:

1.  **REST Client:** Used for executing `.http` test files directamente desde el IDE.
2.  **OpenAPI (Swagger) Editor:** Para visualizar y validar el contrato `openapi.json`.
3.  **Pylance:** Para tipado estático riguroso.
4.  **Python Debugger:** Para inspección del ciclo de vida del LLM.

---

## 📝 Development Notes
* **Asynchronous Design:** Diseñado con `async/await` para no bloquear el hilo principal durante la inferencia.
* **Mocking Strategy:** `LLMService` implementa un mock para desarrollo ágil.
* **Typing:** Uso estricto de Type Hinting para minimizar errores en tiempo de ejecución.