# CodeMind Architecture Overview

CodeMind is an AI-powered code review agent that learns continuously across reviews using persistent Hindsight vector memory.

## Architecture Diagram

```
                CODEMIND
               /        \
       PUBLIC WEBSITE  APPLICATION
             |              |
             |       Top Navigation
             |        /    |     \
             |     Review History Learning
             \       /     |     /
                 FastAPI Backend
                    /   |   \
                 Groq Hindsight SQLite
                  AI    |       DB
                   \    |      /
                     Review Report
```

## System Components

1. **Frontend (Next.js 14 + TypeScript + Tailwind CSS)**:
   - Horizontal top navigation bar. NO permanent left sidebar.
   - Public Website: Landing page, `/about`, `/features`, `/how-it-works`, `/login`, `/signup`.
   - Application Shell: `/app` workspace, `/app/history`, `/app/learning`, `/app/profile`, `/app/settings`, `/app/reviews/[id]`.
   - Monaco Editor integration for inspecting source code with line highlighting.

2. **Backend (FastAPI + Python 3.11)**:
   - Modular layer separation (`api`, `auth`, `core`, `db`, `models`, `schemas`, `services`, `analysis`, `llm`, `hindsight`, `github`, `uploads`, `workers`).
   - SQLite database storing users, OAuth accounts, sessions, projects, reviews, findings, and files.

3. **Groq LLM Engine**:
   - Structured JSON reasoning for bugs, security vulnerabilities, performance issues, and quality scores.

4. **Hindsight Cloud Memory**:
   - REST API integration with bank `codemind`.
   - Recalls prior review experience before review analysis and retains newly extracted learnings after review completion.
