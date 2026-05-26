# My Portfolio

Personal portfolio project with a separate frontend app and AI chatbot backend.

## Project Structure

```text
my_portfolio/
+-- frontend/   # Next.js-style frontend built with TanStack Start and Vite
`-- backend/    # AI Portfolio Copilot backend APIs
```

Use the top-level `frontend/` directory for the website frontend. Ignore any `frontend` folder inside `backend/`; it is not the frontend for this project.

## Requirements

- Node.js 18+
- Python 3.10+
- API keys for the backend, such as `OPENAI_API_KEY` or `GROQ_API_KEY`

## Backend Setup

Open a terminal from the project root:

```bash
cd backend
```

Create and activate a Python virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Install Node.js dependencies for the backend gateway:

```bash
npm install
```

Create your environment file:

```bash
copy .env.example .env
```

Then edit `backend/.env` and add your API keys.

## Run The Backend

The backend uses two services:

- Python FastAPI service on `http://localhost:8000`
- Node.js Express gateway on `http://localhost:3000`

Start the Python API in one terminal:

```bash
cd backend
venv\Scripts\activate
python -m api.server
```

Start the Node.js gateway in a second terminal:

```bash
cd backend
npm start
```

Test the backend:

```bash
curl http://localhost:3000/health
```

Chat endpoint:

```bash
curl -X POST http://localhost:3000/api/chat -H "Content-Type: application/json" -d "{\"message\":\"Tell me about your projects\"}"
```

## Frontend Setup

Open a new terminal from the project root:

```bash
cd frontend
npm install
```

## Run The Frontend

```bash
cd frontend
npm run dev
```

The frontend dev server will print the local URL, usually:

```text
http://localhost:5173
```

## Build

Build the frontend:

```bash
cd frontend
npm run build
```

Build or verify the backend by installing dependencies and starting both backend services.

## Notes

- Keep backend commands inside `backend/`.
- Keep frontend commands inside the top-level `frontend/`.
- Do not use `backend/frontend` for the portfolio frontend.
- Make sure the Python API is running before using the Node.js gateway chat endpoint.
