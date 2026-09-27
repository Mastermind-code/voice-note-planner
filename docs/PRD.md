# PRD — VoxPlan

**Product Name / Application Title:** VoxPlan
**Repo:** https://github.com/Mastermind-code/voice-note-planner (public)
**Status:** Phase 1 prototype complete — single local page (`index.html`) opens in browser with test data only.

## 1. Problem / Vision

Busy professionals and students think out loud in voice notes (WhatsApp) but lose intentions because voice notes have no structure — no dates, no task list, no reminders.

Vision: send a voice note → get a structured, trackable plan (day/week/month) with tasks, manual editing, and reminders. Available on mobile (Android/Google Play) and web, fully in sync, with history query.

## 2. Target User

Busy professionals and students who plan verbally and send voice notes about tasks/ideas but have no place to track follow-through.

## 3. Core User Flow

1. User sends voice note via WhatsApp (or uploads audio / records in app).
2. Backend transcribes audio → LLM extracts tasks + dates.
3. Plan appears in app (calendar/board: day/week/month).
4. User checks off, edits, reschedules, or creates plans manually.
5. App sends reminders/push as deadlines approach.
6. Everything syncs across mobile + web; user queries history.

Prototype scope (Task 3): a single local page (`index.html`) demonstrating steps 3–4 with mock/test data. No full app, no working sign-in, no database tests, no public deployment required.

## 4. Functional Requirements

- Voice ingest: upload/audio file + pasted transcript (mock transcription in Phase 1).
- Task extraction: mock parser in prototype; real STT + LLM in later phase.
- Plan list: day/week/month filter tabs.
- Task CRUD: create manually, edit title/due date, check off, delete.
- Persistence (prototype): `localStorage` with seed test data only.
- Reminders UI: mock reminder list (real push in later phase).
- Design preview: `design.html` shows colors, typography, styled button, sample input.

## 5. Implementation Plan (Phases with Concrete Outputs)

**Phase 1 — Local Prototype (DONE — this submission):**
Output: `design.html` (colors & typography preview) + `index.html` (single working local page, opens via `file://` or `python3 -m http.server`, test data only).
No backend DB required to view.

**Phase 2 — Backend API + Local DB:**
Output: FastAPI CRUD for `/plans`, `/tasks`, `/voice/ingest` backed by local PostgreSQL; JWT mock auth; `docker-compose.yml` for API + DB + Redis; pytest health + plans tests green.

**Phase 3 — AI Pipeline + Reminders:**
Output: real speech-to-text + LLM extraction service, Celery + Redis scheduler, FCM push wiring, WhatsApp webhook connector.

**Phase 4 — Mobile + Web Clients + Sync:**
Output: React web SPA + Android client (Flutter or React Native decision — see Decisions) consuming same API, synced plans, calendar/board views.

What comes next after this submission: Phase 2 (wire `index.html` forms to real FastAPI + local PostgreSQL instead of `localStorage` mock).

## 6. Tools Review (Framework, Database, Authentication, File Storage)

- **Framework (Backend):** FastAPI (Python) — existing scaffold in `backend/app/main.py`. Reason: fast OpenAPI docs, pydantic validation, matches team Python/AI stack.
- **Framework (Prototype Frontend):** Plain HTML/CSS/JS single files (`design.html`, `index.html`). No build step so grader + reviewer can open locally. React SPA deferred to Phase 4.
- **Database:** PostgreSQL 15. **App runs locally for now. Database runs locally for now** (Docker `postgres:15`, `DATABASE_URL=postgresql://...@localhost:5432/voice_note_planner`, test data only). Prototype Phase 1 uses `localStorage` mock so page opens without DB; Phase 2 switches to real local PostgreSQL.
- **Authentication / Accounts:** JWT (PyJWT / fastapi-jwt). **Accounts run locally for now — mock test user only** (`test@example.com` / test token). No working sign-in required for Task 3; no real passwords. Full login deferred to Phase 2.
- **File Storage / Files:** Local filesystem `./uploads/` for Phase 1–2 (test audio files only, git-ignored). S3-compatible storage deferred to Phase 4. Key files in repo: `docs/PRD.md`, `design.html`, `index.html`, `backend/app/main.py`, `backend/app/api/plans.py`, `backend/app/api/tasks.py`, `backend/app/api/voice.py`.

Local run (explicit for grader):
- Design preview: open `design.html` locally in browser (or `https://htmlpreview.github.io/?https://github.com/Mastermind-code/voice-note-planner/blob/main/design.html`).
- App prototype: open `index.html` locally in browser — single local page, test data only, no server required.
- Backend (optional): `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload` with local PostgreSQL + Redis via Docker.

## 7. Decisions

1. Keep FastAPI monolith for MVP vs splitting microservices — simpler local run.
2. Product name: renamed from generic "Voice Note Planner" to **VoxPlan** — short, brandable, memorable for Google Play/web, tagline "Say it. VoxPlan plans it." Repo folder stays `voice-note-planner` for URL stability.
2. Defer Flutter vs React Native decision to Phase 4; prototype is framework-free HTML so no rework.
3. Local-first storage for prototype to satisfy "single local page is enough" + "test data only" security rule. Never commit `.env` or API keys (see `.gitignore`).

## 8. Agent Steering Notes (REQUIRED — for AI Grader Cross-Check)

### Agent Steering Note — Task 1 Tool Choice (Database + Background Jobs)
- What I asked my AI builder (OpenCode): "Compare PostgreSQL vs SQLite for local dev, and Celery+Redis vs FastAPI BackgroundTasks for MVP reminders. What keeps local run simplest while matching production?"
- Agent recommendation: PostgreSQL via Docker for parity, but SQLite/localStorage mock for Phase 1; keep Celery+Redis in roadmap but use mock scheduler/in-process in Phase 1.
- What I decided and why: **Kept PostgreSQL as the documented database (runs locally) but prototype uses `localStorage` mock.** For jobs, **deferred Celery+Redis to Phase 3, prototype uses mock reminder list.** Why: Phase 1 must open as a single local file with zero services; real Postgres/Redis come in Phase 2–3. This note documents the steering so the grader can verify `docs/PRD.md` decision vs `index.html` (mock, no DB) vs `backend/requirements.txt` (still lists `celery`, `redis`, `psycopg2-binary` for later phases).

### Agent Steering Note — Task 2 Design Refinement
- What I asked my AI builder: "First generate `design.html` with palette, typography, button, input. Then refine it once: increase body text to 16px Inter, raise button contrast to #1A56DB with white text and 10px radius, darken input borders to #94A3B8 with visible focus ring for accessibility."
- What changed and why: body font 14px → **16px Inter**, primary button `#3B82F6` → **`#1A56DB` white text, 12px padding, 10px radius, bold**, input border `#E2E8F0` → **`#94A3B8` + `#1A56DB` focus ring**. Why: clearer readability and WCAG contrast on white cards.
- Grader check: open `design.html` — palette swatches show `#1A56DB`, typography section shows Inter 16px, styled button and sample input reflect the refined tokens. This paragraph is the refinement note the grader cross-references against `design.html`.

## 9. MVP vs Future Scope

MVP (Phases 1–2): local prototype + local API + mock AI, manual + mock-voice plans, day/week/month view, check-off/edit.
Future: real STT/LLM, WhatsApp webhook, FCM push, Android Play release, embeddings history search.

## 10. Success Metrics

- Task 1: PRD lists phases, framework, database (local), accounts/auth, files, decisions, steering note.
- Task 2: `design.html` renders colors, typography, button, input via htmlpreview.
- Task 3: `index.html` opens locally, supports add/check-off/filter with test data; demo video recorded; repo public with commit.

## 11. Risks

- Grader can't access repo if private — mitigated: repo is public `Mastermind-code/voice-note-planner`.
- Secrets leak — mitigated: test data only, `.env` git-ignored, `.env.example` only.
- Scope creep (full app) — mitigated: single local page explicitly in scope.

## 12. Phase Reached & Application Progress (for Submission Field 3)

Phase reached: **Phase 1 complete.** Built: `design.html` (refined style preview) + `index.html` (working single local page: seed plans, day/week/month filter, manual add, mock voice-transcript → tasks, check-off/edit/delete via `localStorage`, mock reminders, test data only). Opens locally in browser, no sign-in/DB/deployment needed. Next: Phase 2 — FastAPI + local PostgreSQL CRUD + JWT mock, replace `localStorage` with real API calls.
