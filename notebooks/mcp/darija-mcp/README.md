# Darija NLP MCP Server

mcp-name: io.github.afafelwafi/darija-mcp
<!-- mcp-name: io.github.afafelwafi/darija-mcp-->

A Model Context Protocol (MCP) server for Moroccan Darija Natural Language Processing.

This MCP server provides AI-powered tools for processing, analyzing, and generating Moroccan Darija text. It can be integrated with LLM clients such as Claude Desktop, Cursor, or any MCP-compatible application.

The server exposes NLP capabilities including Darija text normalization, transliteration, translation, sentiment analysis, entity extraction, dialect detection, embeddings, and RAG support.

---

# Features

- Moroccan Darija text normalization
- Arabic ↔ Latin transliteration
- Darija ↔ English/French translation
- Sentiment analysis
- Named Entity Recognition (NER)
- Dialect and language detection
- Text classification
- Keyword extraction
- Embedding generation
- Retrieval-Augmented Generation (RAG) support
- MCP-compatible tool interface

---

# Installation

## Prerequisites

- Python 3.10+
- UV package manager
- Claude Desktop, Cursor, or another MCP-compatible client

Install UV:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

# Setup

## 1. Clone the repository

```bash
git clone https://github.com/afafelwafi/darija-mcp.git
cd darija-mcp
```

## 2. Install dependencies

Using UV:

```bash
uv sync
```

Or using pip:

```bash
pip install -e .
```

## 3. Run the MCP server

```bash
uv run main.py
```

---

# Claude Desktop / Cursor Integration

Copy the following configuration and replace the `{{PATH}}` placeholders.

```json
{
  "mcpServers": {
    "darija-nlp": {
      "command": "{{PATH_TO_UV}}",
      "args": [
        "--directory",
        "{{PATH_TO_PROJECT}}/darija-mcp",
        "run",
        "main.py"
      ]
    }
  }
}
```

## Claude Desktop

Save the configuration file at:

```bash
~/Library/Application Support/Claude/claude_desktop_config.json
```

## Cursor

Save the configuration file at:

```bash
~/.cursor/mcp.json
```

Restart Claude Desktop or Cursor after configuration.

---

# Example Use Cases

Once connected, Claude or another MCP client can:

- Translate Darija into English or French
- Normalize informal Moroccan Arabic text
- Detect sentiment in social media comments
- Extract entities from Darija messages
- Generate embeddings for semantic search
- Build RAG pipelines using Darija corpora
- Analyze Moroccan dialect usage

Example prompts:

- "Translate this Darija sentence to English"
- "Normalize this Moroccan Arabic text"
- "Detect the sentiment of this comment"
- "Extract keywords from this Darija paragraph"

---

# MCP Tools

The server exposes tools such as:

- `normalize_text`
- `transliterate_text`
- `translate_text`
- `detect_language`
- `detect_sentiment`
- `extract_entities`
- `extract_keywords`
- `generate_embeddings`
- `classify_text`
- `search_knowledge_base`

---

# Architecture Overview

The project consists of:

## 1. MCP Server Layer

- Implements the Model Context Protocol
- Exposes NLP tools to compatible clients

## 2. NLP Engine

- Handles Darija-specific language processing
- Uses transformer models and embedding pipelines

## 3. Optional Vector Store / RAG Layer

- Stores embeddings for semantic retrieval
- Supports knowledge-grounded AI workflows

---

# Data & Privacy

- All processing can run locally
- No user data is shared externally unless configured explicitly
- Compatible with local LLM and embedding models

---

# Development

Run in development mode:

```bash
uv run main.py
```

Run tests:

```bash
pytest
```

Format code:

```bash
ruff format
```

Lint:

```bash
ruff check
```

---

# Troubleshooting

## MCP Server Not Appearing

- Verify the MCP configuration path
- Restart Claude Desktop or Cursor
- Ensure `uv` is installed and accessible

## Dependency Issues

Reinstall dependencies:

```bash
uv sync --reinstall
```

## Runtime Issues

Make sure no other process is conflicting with the MCP server runtime.

---

# Security Notice

As with many MCP servers, tool access should be carefully reviewed before connecting to sensitive environments or datasets.

Only expose tools and resources you trust to AI agents.

---

# License

MIT License