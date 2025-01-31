# FastAPI Public API

This is a simple public API built with FastAPI for HNG12. The API provides the following information:

- Your registered email address.
- The current datetime in ISO 8601 format (UTC).
- The GitHub URL of the project's codebase.

## Features

- Built with FastAPI.
- Returns JSON-formatted responses.
- Handles CORS (Cross-Origin Resource Sharing).
- Deployed to a publicly accessible URL.

## 🚀 How to Set Up & Run Locally

1. Clone the Repository

    ```bash
    git clone <your-github-repo-url>
    cd <your-repo-folder>
    ```

2. Create a Virtual Environment & Activate It

    **Windows:**

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    **Mac/Linux:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install Dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Run the API Server

    ```bash
    uvicorn main:app --reload
    ```

5. Test the API

    Open your browser and visit:

    ```bash
    http://127.0.0.1:8000/my_info
    ```

## 📖 API Documentation

### Endpoint: GET /

#### Response Format (200 OK)

```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

## 🔗 Links

- **GitHub Repository:** [https://github.com/DannyBaine-Entity/fastAPI](#)
- **Deployment URL:** [https://fastapi-4iqz.onrender.com/my_info](#)
- **Python Developer Backlink:** [https://hng.tech/hire/python-developers](#)

## 🛠️ Technologies Used

- **FastAPI** - Web framework for building APIs.
- **Uvicorn** - ASGI server for running FastAPI.
- **Python** - Main programming language.

