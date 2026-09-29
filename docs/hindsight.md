# Hindsight Memory Integration

Hindsight provides continuous, persistent vector memory for CodeMind.

## The Learning Loop

```
Previous review experience
        ↓
Hindsight recall (/v1/default/banks/{bank_id}/memories/recall)
        ↓
Current code review (Groq reasoning + static analysis)
        ↓
Review result & finding generation
        ↓
Useful learning extracted
        ↓
Hindsight retain (/v1/default/banks/{bank_id}/memories)
```

## API Endpoints Used

- `POST /v1/default/banks/{bank_id}/memories/recall`: Recalls relevant memories for given programming languages and security context.
- `POST /v1/default/banks/{bank_id}/memories`: Stores durable learnings derived from critical and high severity findings.
- `GET /v1/default/banks/{bank_id}/memories/list`: Lists recent bank memories displayed on the Learning Dashboard.
