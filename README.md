# CodeMind — AI Code Review Agent with Persistent Hindsight Memory

[![Hindsight Powered](https://img.shields.io/badge/Memory-Hindsight%20Cloud-blueviolet?style=for-the-badge&logo=vectorize)](https://vectorize.io)
[![Groq LLM](https://img.shields.io/badge/LLM-Groq%20Llama%203.3%2070B-orange?style=for-the-badge&logo=groq)](https://groq.com)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Next.js 14](https://img.shields.io/badge/Frontend-Next.js%2014-000000?style=for-the-badge&logo=next.js)](https://nextjs.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

> **CodeMind** is an autonomous AI code review agent designed to solve the fundamental flaw of traditional code review tools: **statelessness**. Powered by **Hindsight by Vectorize** as a long-term memory engine and **Groq LLM** for high-speed structured reasoning, CodeMind **retains** findings from every code review, **recalls** historical mistakes and coding conventions, and **reflects** on past experience to produce smarter, context-aware code reviews that improve over time.

---

## 💡 1. The Project Story

### The Problem: Traditional AI Code Reviewers are Stateless

Traditional AI code review bots (and simple LLM prompts) review source code in total isolation. Each run starts from zero context, meaning they suffer from persistent operational deficiencies:

* ❌ **They forget previous reviews:** If you fixed a SQL injection last week, the AI won't remember that your team prefers parameterized query builders over raw strings.
* ❌ **They repeat identical warnings:** The AI continues pointing out the same low-priority style nitpicks that your team explicitly rejected.
* ❌ **They lack project context:** They cannot enforce project-specific architecture rules or remember custom error-handling conventions established in prior commits.
* ❌ **They don't learn from developer habits:** Recurring developer mistakes (e.g., bare `except:` blocks or missing input sanitization) are treated as random events rather than recognizable patterns.

### The Solution: CodeMind with Persistent Hindsight Memory

**CodeMind** introduces a **continuous learning loop** for AI code reviews:

```
                  ┌─────────────────────────────────────────┐
                  │          Developer Submits Code         │
                  │   (GitHub Repository URL or ZIP Upload) │
                  └────────────────────┬────────────────────┘
                                       │
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │       Static AST Analysis & Pre-Check   │
                  └────────────────────┬────────────────────┘
                                       │
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │  1. RECALL: Hindsight Memory Lookup     │
                  │  (Fetches past bugs, fixes & rules)     │
                  └────────────────────┬────────────────────┘
                                       │
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │  2. REFLECT: Groq LLM Structured Review │
                  │  (Synthesizes code + historical memory) │
                  └────────────────────┬────────────────────┘
                                       │
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │  3. RETAIN: Save Learnings to Hindsight │
                  │  (Stores new findings & conventions)    │
                  └────────────────────┬────────────────────┘
                                       │
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │     Interactive Monaco Review Report    │
                  │    (Line precision, fix & memory badge) │
                  └─────────────────────────────────────────┘
```

When code is submitted, CodeMind doesn't just read the files—it queries **Hindsight** for relevant historical memories, injects those learnings into the **Groq LLM** prompt context, presents a structured report with line-level code fixes and memory attribution badges (`memory_influenced: true`), and finally **retains** the newly discovered patterns into Hindsight vector memory so that future reviews become progressively smarter.

---

## 🧠 2. Hackathon Requirement: Why Hindsight?

Hindsight by Vectorize is **not merely a vector database** in CodeMind—it serves as the **cognitive long-term memory system** that transforms a stateless LLM into an evolving software engineering agent.

### 🔄 Comparison: Without Hindsight vs. With Hindsight

| Feature | Without Hindsight (Stateless AI) | With Hindsight (CodeMind Agent) |
| :--- | :--- | :--- |
| **Review State** | Resets completely on every run | Persists across reviews and projects |
| **Historical Awareness** | Zero awareness of past vulnerabilities | Recalls previously detected bugs and fixes |
| **Developer Conventions** | Recommends generic internet defaults | Adapts to team-specific coding standards |
| **Pattern Recognition** | Sees each file as an isolated snippet | Detects recurring developer error habits |
| **Long-Term Utility** | Value remains flat over time | Value increases exponentially with usage |

### 📐 Hindsight Integration Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│                          CODEMIND ENGINE                               │
│                                                                        │
│   ┌──────────────────┐               ┌─────────────────────────────┐   │
│   │ Static AST Engine│               │       Groq LLM Engine       │   │
│   │ (Python AST)     │               │ (llama-3.3-70b-versatile)   │   │
│   └────────┬─────────┘               └──────────────▲──────────────┘   │
│            │                                        │                  │
│            └──────────────┐        ┌────────────────┘                  │
│                           ▼        │ (Prompt + Memory Context)         │
│                      ┌─────────────┴──────────────┐                    │
│                      │   Hindsight Memory Adapter │                    │
│                      └─────────────┬──────────────┘                    │
└────────────────────────────────────┼───────────────────────────────────┘
                                     │
                                     │ REST API (Bearer Auth)
                                     ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        HINDSIGHT CLOUD BANK                            │
│                 (https://api.hindsight.vectorize.io)                   │
│                                                                        │
│   ┌───────────────────────┐                 ┌──────────────────────┐   │
│   │    RECALL Endpoint    │                 │   RETAIN Endpoint    │   │
│   │  /memories/recall     │                 │   /memories          │   │
│   └───────────────────────┘                 └──────────────────────┘   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## ✨ 3. Main Features

### 🔐 Authentication & Access Control
- **Email & Password Authentication**: Full user signup and login with Bcrypt password hashing and JWT sessions.
- **GitHub OAuth 2.0**: Native sign-in via GitHub OAuth app flow.
- **Google OAuth 2.0**: Native sign-in via Google Identity OAuth flow.
- **User Profile Management**: View user credentials, connected accounts, and avatar initials.

### 📦 Code Ingestion & Analysis
- **Public GitHub Repository Review**: Input any public GitHub repository URL (e.g., `https://github.com/owner/repo`) for automated git cloning and analysis.
- **ZIP File Upload Review**: Upload local source code `.zip` archives with built-in **Zip Slip path-traversal security protection** and size cap validations (25MB zip / 100MB uncompressed).
- **Multi-Language AST Analysis**: Automated static syntax tree extraction for Python, JavaScript, TypeScript, HTML, CSS, JSON, and YAML files.
- **Security Vulnerability Scanning**: AST & rule-based detection for SQL Injection, Cross-Site Scripting (XSS), Server-Side Request Forgery (SSRF), Hardcoded API Keys/Secrets, Bare `except:` catch blocks, and Unsafe Dynamic Execution (`eval`/`exec`).

### 📊 Review Reports & Intelligence
- **Comprehensive Score System**: Calculates Overall Review Score, Code Quality Score, Security Score, and Maintainability Score (0-100 scale).
- **Issue Severity Classification**: Categorizes findings into **Critical**, **High**, **Medium**, **Low**, and **Info**.
- **Interactive Monaco Code Viewer**: Embedded Monaco editor displaying source code with exact line highlighting, side-by-side issue panels, and one-click code copy.
- **Hindsight Memory Influence Attribution**: Distinct visual badges highlighting when a recommendation was directly influenced by recalled Hindsight memory (`memory_influenced: true`).

### 🧠 Hindsight Memory & Analytics
- **Learning Dashboard (`/app/learning`)**: Real-time display of stored Hindsight memories, top recurring issue patterns, team coding rules, and historical review score trends.
- **Review History (`/app/history`)**: Filterable timeline of past code reviews with instant report reloading.

### 🚧 Planned Features
- 🚧 **GitHub Pull Request Integration**: Automated PR review bot posting inline PR comments.
- 🚧 **CI/CD Pipeline Integration**: GitHub Actions and GitLab CI runner plugins.
- 🚧 **Automated Fix Generation**: One-click Git branch creation with applied code patches.
- 🚧 **Team Memory Workspaces**: Shared Hindsight banks across organization teams.

---

## 📑 4. Code Review Report Breakdown

After submitting a repository or ZIP archive, CodeMind generates an engineering-grade report designed for modern software teams:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ CODEMIND REVIEW REPORT                                  [Score: 84/100]         │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Scores: Quality: 85.0  |  Security: 78.0  |  Maintainability: 88.0                 │
│ Statistics: Critical: 1 | High: 2 | Medium: 3 | Low: 1 | Info: 0                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ FINDING #1: Unsanitized User Input in SQL Query [CRITICAL] [SECURITY]           │
│ File: backend/app/db/users.py:L42                                               │
│ Code Snippet: query = f"SELECT * FROM users WHERE email = '{user_email}'"       │
│                                                                                 │
│ Problem Description:                                                            │
│ Direct string interpolation creates a critical SQL Injection vulnerability.      │
│                                                                                 │
│ Fix Recommendation:                                                             │
│ Use parameterized query bindings:                                               │
│ db.execute("SELECT * FROM users WHERE email = :email", {"email": user_email})   │
│                                                                                 │
│ 🟣 HINDSIGHT MEMORY INFLUENCE:                                                   │
│ Recalled Hindsight Memory: Previous review in project 'AuthService' noted       │
│ developer tendency to interpolate raw SQL strings. Applied team standard for    │
│ parameterized bindings.                                                         │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🧪 5. Hindsight Learning Concrete Examples

CodeMind's memory is demonstrated across successive reviews:

### Example 1: Security Pattern (SQL Injection)
* **Review 1 (Initial Code):** Developer submits `db.execute(f"SELECT * FROM users WHERE id = {user_id}")`. CodeMind flags `CRITICAL — SQL Injection` and suggests prepared statements. CodeMind calls **Hindsight Retain**: `"CodeMind Learned Pattern: In Security, issue 'SQL Injection' was identified. Fix: Use parameterized query bindings."`
* **Review 2 (Subsequent Code):** Developer submits a new module containing `cursor.execute("SELECT * FROM items WHERE category = '%s'" % cat)`. CodeMind calls **Hindsight Recall** before generating the prompt. The agent synthesizes the prior learning and outputs:
  > **Hindsight Memory Influence**: *"Similar SQL injection patterns were detected in a previous review. Our project memory requires using parameterized query bindings instead of string formatting."*

### Example 2: Code Quality Pattern (Bare Exception Catching)
* **Review 1 (Initial Code):** Developer writes `try: process_data() except: pass`. CodeMind flags `HIGH — Bare Except Clause` and notes that silent failures mask critical runtime bugs. CodeMind retains the rule into Hindsight.
* **Review 2 (Subsequent Code):** Developer writes `try: connect_db() except Exception: return None`. CodeMind recalls the previous exception handling guidance and advises catching specific errors (e.g., `DatabaseConnectionError`), citing past review history.

### Example 3: Project-Specific Convention (Environment Variable Configuration)
* **Review 1 (Initial Code):** Code contains `STRIPE_SECRET_KEY = "sk_test_12345"`. CodeMind flags `CRITICAL — Hardcoded API Key`. CodeMind retains the project rule: *"Store API keys in environment variables via .env."*
* **Review 2 (Subsequent Code):** Developer writes `JWT_SECRET = "super_secret_jwt_key"`. CodeMind recalls the project's credential management rule from Hindsight and explicitly highlights:
  > **Hindsight Memory Influence**: *"In accordance with previously established security conventions in your team's memory bank, sensitive secrets must be retrieved via `os.getenv()` or `pydantic_settings`."*

---

## 🏗️ 6. System Architecture

CodeMind follows a decoupled, modular architecture built for speed, safety, and scalability:

```
                               ┌──────────────────────────┐
                               │   React / Next.js 14 UI  │
                               │   (Monaco Editor & CSS)  │
                               └────────────┬─────────────┘
                                            │
                                            │ HTTP / JSON API
                                            ▼
                               ┌──────────────────────────┐
                               │   FastAPI Python Server  │
                               └──────┬────────────┬──────┘
                                      │            │
             ┌────────────────────────┘            └────────────────────────┐
             ▼                                                              ▼
┌──────────────────────────┐                                   ┌──────────────────────────┐
│ SQLite Database          │                                   │ Ingestion Engine         │
│ (Users, Reviews, Token)  │                                   │ (Git Clone / ZIP Unpack) │
└──────────────────────────┘                                   └────────────┬─────────────┘
                                                                            │
                                                                            ▼
                                                               ┌──────────────────────────┐
                                                               │ Static AST Analysis      │
                                                               │ (Python AST Parser)      │
                                                               └────────────┬─────────────┘
                                                                            │
                                                                            ▼
                                                               ┌──────────────────────────┐
                                                               │ Hindsight Memory Adapter │
                                                               └──────┬────────────▲──────┘
                                                               RETAIN │            │ RECALL
                                                                      ▼            │
                                                               ┌──────────────────────────┐
                                                               │ Hindsight Cloud API      │
                                                               │ (Vector Memory Storage)  │
                                                               └──────────────────────────┘
                                                                            │
                                                                            ▼
                                                               ┌──────────────────────────┐
                                                               │ Groq LLM Inference Engine│
                                                               │ (Llama 3.3 70B Versatile)│
                                                               └──────────────────────────┘
```

### Component Breakdown
1. **Frontend (Next.js 14 App Router)**: Provides an interactive UI with top navigation, Monaco code editor, dynamic statistics charts, and live login state.
2. **Backend (FastAPI & SQLAlchemy)**: Manages API endpoints (`/api/auth`, `/api/reviews`, `/api/learning`, `/api/history`), handles authentication, and orchestrates review tasks.
3. **Ingestion Engine**: Safe repository fetcher that validates public GitHub URLs and extracts ZIP uploads while enforcing Zip Slip path-traversal protection.
4. **Static AST Engine (`backend/app/analysis/ast_analyzer.py`)**: Pre-scans source files for syntax trees and known security vulnerabilities before calling LLM APIs.
5. **Hindsight Memory Adapter (`backend/app/hindsight`)**: Interfaces with Hindsight Cloud to perform vector recall, store retained review findings, and format memory context.
6. **Groq LLM Engine (`backend/app/llm`)**: Sends structured prompt instructions to `llama-3.3-70b-versatile` and parses strictly formatted JSON code review reports.

---

## 🔄 7. Hindsight Data Flow: Retain, Recall & Reflect

### 📥 1. Retain (Memory Storage)
After every review, CodeMind filters all **Critical**, **High**, and **Medium** severity findings. It formats actionable learnings and transmits them to Hindsight Cloud via the `/v1/default/banks/{bank_id}/memories` endpoint:

```json
{
  "items": [
    {
      "content": "CodeMind Learned Pattern (AuthService): In Security, issue 'Unsanitized User Input in SQL Query' was identified: Direct string interpolation into SQL query. Best Practice / Fix: Use parameterized query bindings.",
      "context": "code_review_security"
    }
  ]
}
```

### 🔍 2. Recall (Memory Retrieval)
Before submitting a new codebase to the LLM, CodeMind queries Hindsight Cloud via `/v1/default/banks/{bank_id}/memories/recall` using context-aware search queries based on the project's target languages and file types. Hindsight returns vector-relevant historical memories.

### 🧠 3. Reflect (AI Reasoning & Prompt Injection)
The recalled memories are injected directly into the **Groq System & User Prompts**. The LLM reads both the current source code and the recalled Hindsight memories, allowing it to reflect on past experiences and attach `memory_influenced: true` attributes to its structured JSON output.

---

## 🛠️ 8. Tech Stack

| Category | Technology / Library | Description |
| :--- | :--- | :--- |
| **Frontend Framework** | Next.js 14 (App Router) | Server-rendered React framework with TypeScript |
| **Styling & UI** | Tailwind CSS & Lucide Icons | Responsive layout styling and icon set |
| **Code Editor** | `@monaco-editor/react` | Embedded Monaco code editor with line highlighting |
| **Backend Framework** | Python 3.11+ / FastAPI | High-performance async Python Web Framework |
| **Database & ORM** | SQLite & SQLAlchemy 2.0 | Lightweight SQL database for user and review storage |
| **AI / LLM Engine** | Groq API (`llama-3.3-70b-versatile`) | Ultra-fast structured LLM inference |
| **Long-Term Memory** | Hindsight Cloud REST API | Vectorize Hindsight memory bank engine |
| **Authentication** | Passlib (Bcrypt) & PyJWT | Password hashing & JWT token sessions |
| **OAuth Providers** | GitHub OAuth 2.0 & Google OAuth 2.0 | Social authentication flows |
| **Static Analysis** | Python `ast` module | Automated AST parsing & rule check engine |
| **Testing** | `pytest` & `httpx` | Unit and integration test suite |

---

## 📂 9. Project Structure

```
CodeMind/
├── backend/                  # FastAPI Python Backend
│   ├── app/
│   │   ├── analysis/         # AST Static Analyzer, Evidence Verifier & Scorer
│   │   │   ├── ast_analyzer.py
│   │   │   ├── evidence_verifier.py
│   │   │   └── scorer.py
│   │   ├── api/              # API Route Handlers
│   │   │   └── routes/
│   │   │       ├── auth.py       # Authentication & OAuth Routes
│   │   │       ├── history.py    # Review History API
│   │   │       ├── learning.py   # Hindsight Memory Analytics API
│   │   │       ├── projects.py   # Project Management API
│   │   │       └── reviews.py    # Code Review Submission & Report API
│   │   ├── core/             # Application Settings & Security Config
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── db/               # Database Models & Session Management
│   │   │   ├── database.py
│   │   │   └── models.py
│   │   ├── github/           # Public GitHub Repository Loader
│   │   ├── hindsight/        # Hindsight REST Client (Retain, Recall, List)
│   │   │   ├── client.py
│   │   │   ├── learning.py
│   │   │   └── recall.py
│   │   ├── llm/              # Groq LLM Client & System Prompts
│   │   │   ├── client.py
│   │   │   └── prompts.py
│   │   └── main.py           # FastAPI Application Entrypoint
│   └── requirements.txt      # Python Dependencies
├── frontend/                 # Next.js 14 React Frontend
│   ├── src/
│   │   ├── app/              # Next.js App Router Pages
│   │   │   ├── app/
│   │   │   │   ├── history/  # Review History Page (/app/history)
│   │   │   │   ├── learning/ # Hindsight Memory Dashboard (/app/learning)
│   │   │   │   ├── profile/  # User Profile Page (/app/profile)
│   │   │   │   ├── reviews/  # Individual Code Review Page (/app/reviews/[id])
│   │   │   │   └── page.tsx  # Main Application Workspace (/app)
│   │   │   ├── login/        # Login Page (/login)
│   │   │   ├── signup/       # Signup Page (/signup)
│   │   │   ├── layout.tsx    # Root Layout
│   │   │   └── page.tsx      # Landing Page
│   │   ├── components/       # UI & Navigation Components
│   │   └── lib/              # Client Utilities & API Hooks
│   └── package.json          # Node.js Dependencies
├── data/                     # Local SQLite Database Storage (`codemind.db`)
├── tests/                    # Backend Pytest Test Suite
│   └── backend/
├── .env.example              # Environment Variable Template
├── docker-compose.yml        # Docker Multi-Container Configuration
├── Dockerfile                # Backend Container Build Spec
└── README.md                 # Project Documentation
```

---

## ⚙️ 10. Setup & Local Development

### Prerequisites
- **Python**: `v3.11` or higher
- **Node.js**: `v18` or higher (`npm` included)
- **Git**: Installed on local system

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/CodeMind.git
cd CodeMind
```

### 2. Configure Environment Variables
Copy `.env.example` to `.env` in the root folder:
```bash
cp .env.example .env
```
*(Fill in your actual `GROQ_API_KEY`, `HINDSIGHT_API_KEY`, `GITHUB_CLIENT_ID`, and `GOOGLE_CLIENT_ID` inside `.env`).*

### 3. Start Backend Server (FastAPI)
```bash
cd backend
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

pip install -r requirements.txt
python app/main.py
```
*Backend server will start at `http://localhost:8000`.*

### 4. Start Frontend Server (Next.js)
Open a new terminal window:
```bash
cd frontend
npm install
npm run dev
```
*Frontend application will start at `http://localhost:3000`.*

---

## 🔑 11. Environment Variables

Create a `.env` file in the project root directory. Use the following structure:

```env
# Groq LLM API Configuration
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile

# Hindsight Cloud API Configuration
HINDSIGHT_API_KEY=your_hindsight_api_key_here
HINDSIGHT_BASE_URL=https://api.hindsight.vectorize.io
HINDSIGHT_BANK_ID=codemind

# OAuth Credentials (GitHub)
GITHUB_CLIENT_ID=your_github_client_id_here
GITHUB_CLIENT_SECRET=your_github_client_secret_here

# OAuth Credentials (Google)
GOOGLE_CLIENT_ID=your_google_client_id_here
GOOGLE_CLIENT_SECRET=your_google_client_secret_here

# Security & Database
DATABASE_URL=sqlite:///./data/codemind.db
SESSION_SECRET=your_super_secret_session_key_change_in_production
FRONTEND_URL=http://localhost:3000
BACKEND_URL=http://localhost:8000
```

> [!WARNING]
> **SECURITY MANDATE:** Never commit `.env` or any files containing live API keys or client secrets to public Git repositories. Verify `.env` is listed in your `.gitignore`.

---

## 🌐 12. OAuth Configuration Guide

### GitHub OAuth Setup
1. Go to **GitHub Settings** -> **Developer Settings** -> **OAuth Apps** -> **New OAuth App**.
2. Set **Application Name**: `CodeMind AI Reviewer`.
3. Set **Homepage URL**: `http://localhost:3000`.
4. Set **Authorization Callback URL**: `http://localhost:8000/api/auth/github/callback`.
5. Copy the generated **Client ID** and **Client Secret** into your `.env` file.

### Google OAuth Setup
1. Go to the **Google Cloud Console** -> **APIs & Services** -> **Credentials**.
2. Click **Create Credentials** -> **OAuth Client ID** (Application type: Web application).
3. Add **Authorized JavaScript Origins**: `http://localhost:3000`.
4. Add **Authorized Redirect URIs**: `http://localhost:8000/api/auth/google/callback`.
5. Copy the generated **Client ID** and **Client Secret** into your `.env` file.

---

## 🚀 13. How to Use CodeMind

1. **Access CodeMind**: Open `http://localhost:3000` in your web browser.
2. **Sign In**: Log in using Email/Password, GitHub OAuth, or Google OAuth.
3. **Choose Input Mode**:
   - **GitHub Repo**: Paste any public repository URL (e.g., `https://github.com/pallets/flask`).
   - **ZIP Archive**: Upload a `.zip` file containing source code.
4. **Trigger Review**: Click **Start AI Code Review**.
5. **Automatic Workflow**:
   - CodeMind fetches and statically parses the files using Python AST.
   - Hindsight recalls relevant historical memories.
   - Groq LLM synthesizes the code and memories into a structured JSON report.
   - Newly discovered issues are retained into Hindsight Cloud.
6. **Inspect Results**: View the overall score, severity breakdown, file tree, Monaco code viewer with highlighted lines, and **Hindsight Memory Influence** tags.
7. **Track Progress**: Visit `/app/learning` to observe how Hindsight stores recurring findings and improves team scores over time.

---

## 🏆 14. Hackathon Demo Scenario

To showcase CodeMind during judge evaluation:

### Step 1: Run Review #1 (Initial Flawed Codebase)
* **Action**: Upload a ZIP archive containing a Python file with a raw SQL query string interpolation (`query = f"SELECT * FROM users WHERE id = {user_id}"`).
* **Result**: CodeMind flags a `CRITICAL — SQL Injection` finding.
* **Hindsight Action**: CodeMind automatically calls `retain()`, storing the SQL injection finding and fix rule into Hindsight Cloud Bank `codemind`.

### Step 2: Run Review #2 (Subsequent Codebase with Similar Pattern)
* **Action**: Upload a second ZIP archive containing another database script with raw SQL formatting.
* **Result**: CodeMind calls `recall()`, retrieves the stored memory from Review #1, and injects it into Groq LLM reasoning.
* **Outcome**: The generated report highlights the finding with a purple badge:
  `🟣 HINDSIGHT MEMORY INFLUENCE: Recalled previous SQL injection finding. Recommending team-standard parameterized query bindings.`

This proves that **CodeMind actively learns and adapts using Hindsight memory**.

---

## 🖼️ 15. Screenshots

| Visual Component | Preview |
| :--- | :--- |
| **Landing Page** | ![Landing Page](docs/screenshots/landing_page.png) |
| **Login & OAuth** | ![Login Page](docs/screenshots/login_page.png) |
| **Review Workspace** | ![Workspace](docs/screenshots/workspace.png) |
| **Code Review Report** | ![Review Report](docs/screenshots/review_report.png) |
| **Learning Dashboard** | ![Learning Dashboard](docs/screenshots/learning_dashboard.png) |

---

## 🎨 16. Results & Visual Report Interface

CodeMind's report dashboard is engineered for high-density developer productivity:

- **Executive Metric Cards**: Instant display of overall score, security score, quality score, and maintainability score.
- **Severity & Category Filters**: Filter findings by Critical, High, Medium, Low, or Category (Security, Quality, Bug, Performance).
- **Monaco Code Viewer**: Full syntax-highlighted editor displaying source code files with line markers pointing directly to flagged code.
- **Actionable Fix Recommendations**: Side-by-side code snippets showing the original bug vs. the recommended fix.
- **Hindsight Attribution**: Clear indicators linking specific review findings back to Hindsight vector memory items.

---

## 🔒 17. Security & Risk Management

CodeMind implements multi-layered security controls:

- **Strict AST Static Parsing**: Code uploaded or cloned is analyzed purely at the Abstract Syntax Tree level—**source code is NEVER executed**.
- **Zip Slip Mitigation**: File upload extraction strictly validates target paths to prevent directory traversal attacks (`../`).
- **OAuth CSRF Protection**: OAuth state parameters and tokens are validated via secure session handlers.
- **Password Hashing**: Passwords stored using industry-standard `bcrypt` password hashing.
- **Secret Hygiene**: Zero plain-text credentials in source code. All keys are managed via environment variables.

---

## ⚠️ 18. Limitations

- **Public Repositories Only (Default)**: GitHub repository cloning currently supports public repositories (private repository access requires user PAT configuration).
- **File Upload Limits**: ZIP uploads are capped at 25MB packed / 100MB unpacked to ensure server stability.
- **LLM Context Caps**: Large projects automatically select the top 15 most critical source files for LLM prompt context to stay within token rate limits.

---

## 🗺️ 19. Future Roadmap

- [ ] **Pull Request Integration**: Post automatic inline review comments directly on GitHub PRs (`🚧 Planned`).
- [ ] **CI/CD Pipeline Support**: Native GitHub Action and GitLab CI step integration (`🚧 Planned`).
- [ ] **Auto-Fix PR Generation**: One-click creation of Git fix branches with applied patches (`🚧 Planned`).
- [ ] **Organization Memory Isolation**: Multi-tenant Hindsight memory banks per organization (`🚧 Planned`).
- [ ] **Custom Lint Rules Engine**: User-definable YAML rules for team-specific AST checks (`🚧 Planned`).

---

## 🌟 20. Hackathon Value: Why CodeMind Stands Out

CodeMind directly addresses the core objective of **"AI Agents That Learn Using Hindsight"**:

1. **Solves a Real Developer Pain Point**: Removes repetitive code review nitpicks and prevents recurring team security mistakes.
2. **True Memory Loop**: Uses Hindsight Retain, Recall, and Reflect mechanisms to establish genuine agent memory.
3. **High-Speed Execution**: Powered by Groq's ultra-low latency Llama 3.3 70B inference engine.
4. **Developer-First UI**: Features an interactive Monaco editor, clean horizontal top navigation, and comprehensive score dashboards.
5. **Extensible & Open**: Built with clean FastAPI and Next.js 14 architecture.

---

## 👥 21. Team & Contributors

* **CodeMind Core Engineering Team**
  - **AI Engineer & Lead Maintainer** - Hindsight & Groq LLM Agent Architecture
  - **Full-Stack Developer** - FastAPI Backend & Next.js 14 Monaco Frontend

---

## 📜 22. License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🎥 23. Demo Video

[![CodeMind Demo Video](https://img.shields.io/badge/Watch-Demo%20Video-red?style=for-the-badge&logo=youtube)](#)

*Demo video walkthrough covering: OAuth Login -> GitHub Repo Submit -> Hindsight Memory Recall -> Groq AI Review -> Hindsight Memory Retain -> Second Review Context Awareness.*
