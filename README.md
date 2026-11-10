# AI Recipe Agent

A simple AI-powered recipe agent built with **LangChain, LangGraph, Ollama, and Tavily Search**.

The agent takes a list of ingredients provided by the user, searches the web to identify suitable dishes and cooking methods, and generates an easy-to-follow recipe using the available ingredients.

## Features

- **Ingredient Analysis:** Analyzes the ingredients provided by the user.
- **Web Search:** Uses Tavily Search to discover suitable dishes and cooking methods.
- **Recipe Generation:** Uses Qwen 3.5 (4B) through Ollama to generate recipes.
- **Cooking Instructions:** Provides ingredient quantities, preparation steps, cooking temperatures, cooking times, and heat settings.
- **Conversation Memory:** Uses LangGraph checkpointing with `InMemorySaver` to maintain conversation state across interactions.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| LangChain | Agent creation and orchestration |
| LangGraph | Agent state and checkpointing |
| Ollama | Local LLM runtime |
| Qwen 3.5 (4B) | Recipe generation |
| Tavily | Web search tool |
| python-dotenv | Environment variable management |

## Architecture

```text
User
 |
 | Ingredients
 v
LangChain Agent
 |
 |-- Qwen 3.5 (Ollama)
 |
 |-- Tavily Search Tool
 |      |
 |      v
 |   Web Search
 |      |
 |      v
 |   Dish and Cooking Method Research
 |
 v
Recipe Generation
 |
 v
Final Recipe
```

## Prerequisites

- Python 3.11 or newer (use a Python version supported by your installed dependencies).
- [Ollama](https://ollama.com/) installed.
- Tavily API key.

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd LangchainExperiment
```

### 2. Install dependencies

Using `uv`:

```bash
uv sync
```

Alternatively, install the required packages:

```bash
uv add langchain langchain-ollama langgraph tavily-python python-dotenv
```

### 3. Download the Ollama model

```bash
ollama pull qwen3.5:4b
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_api_key
```

### 5. Start Ollama

```bash
ollama serve
```

Keep the Ollama server running.

### 6. Run the application

Open another terminal:

```bash
uv run python src/langchainexperiment/app.py
```

## Example

**Input:**

```text
I have chicken, rice, onions, salt, red chilli powder,
ginger garlic paste, garam masala, water, turmeric powder
and Indian spices.
```

**Expected Agent Workflow:**

1. Analyze the available ingredients.
2. Search for dishes that can be prepared using those ingredients.
3. Identify a suitable dish and cooking method.
4. Generate a recipe with ingredient quantities and cooking instructions.
5. Return the final recipe to the user.

**Expected Output:**

A complete recipe containing:
- Dish name
- Ingredient quantities
- Preparation instructions
- Step-by-step cooking instructions
- Cooking temperatures and times
- Heat settings and lid instructions

## Agent Memory

The application uses LangGraph's `InMemorySaver` checkpointer to maintain conversation state.

A configurable `thread_id` identifies each conversation, allowing the agent to retain context across multiple interactions.

**Note:** `InMemorySaver` stores checkpoints in application memory. Checkpoints are lost when the application process restarts.

