# genai-agent-framework

An end-to-end autonomous generative AI agent with tool support, persistent memory, and a web interface.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
  - [REPL Agent](#repl-agent)
  - [API Server](#api-server)
  - [Streamlit UI](#streamlit-ui)
- [Configuration](#configuration)
- [Architecture](#architecture)
  - [Core Loop](#core-loop)
  - [Tools](#tools)
  - [Prompt Strategy](#prompt-strategy)
  - [Memory Backend](#memory-backend)
  - [Web Interface](#web-interface)
- [Testing](#testing)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

`genai-agent-framework` provides a concrete implementation of an autonomous agent that:
1. Interacts via a REPL or HTTP API.
2. Utilizes external tools (web search, calculator, file I/O).
3. Employs Chain-of-Thought and ReAct reasoning via OpenAI.
4. Persists context in a FAISS-backed vector store.
5. Offers a Streamlit-based UI for exploration.

---

## Features

- **Agent Loop**: Handles user input, generates reasoning, selects actions, executes tools, and updates memory.
- **Tool Plugins**:
  - Web search using SerpAPI
  - Safe calculator with AST-based evaluation
  - File read/write operations
- **Reasoning Engine**: OpenAI GPT model for intermediate thoughts and action selection.
- **Memory**: FAISS vector index with SentenceTransformers embeddings.
- **Web UI**: FastAPI server and Streamlit frontend.

---

## Prerequisites

- Python 3.9+
- FAISS (`faiss-cpu`)
- SerpAPI key
- OpenAI API key

---

## Setup

1. Clone the repo:
   ```bash
   git clone https://your.git.repo/genai-agent-framework.git
   cd genai-agent-framework
   ```

2. Create a `.env` file:
   ```bash
   cp .env.example .env
   ```

3. Populate `.env`:
   ```ini
   SERPAPI_KEY=your_serpapi_key
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### REPL Agent

```bash
python -m src.agent.core
```

Type queries, view thoughts, action, and results.  
Type `exit` or Ctrl+C to quit.

### API Server

```bash
uvicorn app.fastapi_app:app --reload
```

Endpoint: `GET /agent?q=<your query>`

### Streamlit UI

```bash
streamlit run app/streamlit_app.py
```

---

## Configuration

| Variable        | Description                         |
|-----------------|-------------------------------------|
| `SERPAPI_KEY`   | SerpAPI API key for web searches    |
| `OPENAI_API_KEY`| OpenAI key for Chat completions     |
| `API_URL`       | (Optional) Custom API endpoint URL  |

---

## Architecture

### Core Loop

- **src/agent/core.py**: Initializes memory, tools, and prompt strategy. Runs REPL loop.

### Tools

- **WebSearchTool**: Interfaces with SerpAPI.
- **CalculatorTool**: Evaluates math expressions safely.
- **FileTool**: Reads and writes local files.

### Prompt Strategy

- **src/agent/prompt_strategy.py**: Builds context prompt, calls OpenAI, parses `THOUGHTS||ACTION`.

### Memory Backend

- **src/agent/memory/faiss_memory.py**: Manages FAISS index, persists to disk, supports add and query.

### Web Interface

- **app/fastapi_app.py**: Exposes `/agent` endpoint.
- **app/streamlit_app.py**: Interactive UI to visualize thoughts, actions, and results.

---

## Testing

## Docker Usage

Build the Docker image:
```bash
docker build -t genai-agent-framework .
```

Run the container:
```bash
docker run -p 8000:8000 \
  -e SERPAPI_KEY=$SERPAPI_KEY \
  -e OPENAI_API_KEY=$OPENAI_API_KEY \
  genai-agent-framework
```

Or using Docker Compose:
```bash
docker-compose up --build
```

## Continuous Integration

A GitHub Actions workflow is included under `.github/workflows/ci.yml` that:
- Installs dependencies
- Runs pytest
- Lints code with flake8

Ensure you have the secrets `SERPAPI_KEY` and `OPENAI_API_KEY` set in your repository settings.


Run unit tests with:
```bash
pytest
```

---

## Development

- Create new tools under `src/agent/tools/`
- Extend prompt logic in `prompt_strategy.py`
- Customize memory model in `faiss_memory.py`

---

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit changes & open a pull request.
4. Ensure all tests pass.

---

## License

MIT License
