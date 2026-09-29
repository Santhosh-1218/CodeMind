# Authentication Documentation

CodeMind supports real authentication with multiple providers:

1. **Email / Password**:
   - Passwords hashed using bcrypt salt via `app.core.security`.
   - JWT sessions stored in HttpOnly cookies and localStorage tokens.

2. **Google OAuth 2.0**:
   - Uses `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`.
   - Redirects to `/api/auth/google/callback` to verify code and retrieve user profile.

3. **GitHub OAuth**:
   - Uses `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET`.
   - Redirects to `/api/auth/github/callback`.
