# VoxPlan

> Say it. VoxPlan plans it. Turn a spoken voice note into a structured, trackable plan.

Turn a spoken voice note into a structured, trackable plan — available on mobile (Android/Google Play) and web, with reminders and manual editing built in.

## Product Brief

**User:**
Busy professionals and students who think out loud or plan verbally — people who send voice notes about tasks, ideas, or plans but have no structured place to see, track, or be reminded about them.

**Problem:**
Voice notes are fast to record but easy to forget. Once sent, they sit in a chat thread with no structure — no dates, no task list, no dedicated space to view progress, and no reminders to nudge follow-through. The person's intentions get lost between "I said it" and "I did it," because there's nowhere for the plan to live.

**Main journey:**
A user sends a voice note (via WhatsApp) describing what they want to get done. The app transcribes it, extracts tasks and timing, and turns it into a structured plan inside its own app — available on both mobile (Android, via Google Play) and web — with a calendar/board view where the user can see all their plans (day/week/month), check off completed items, and edit tasks directly. Users aren't limited to voice: they can also create and edit plans directly in the app. The app sends reminders and push notifications as deadlines approach or tasks are neglected. Whichever way a plan is created, everything stays in sync, and the user can query their history.

## Repo Layout

```
voice-note-planner/
├── backend/     # FastAPI API — auth, plans, tasks, transcription pipeline, reminders
├── mobile/      # Android client (Google Play target)
├── web/         # Web client
└── docs/        # PRD, architecture notes, decisions
```

## Status

Early scaffold — backend skeleton in place, PRD in progress (see `docs/PRD.md`), mobile/web clients not yet started.

## Tech Direction (tentative)

- **Backend:** FastAPI, PostgreSQL, Celery + Redis (background jobs, reminders), JWT auth
- **AI:** Speech-to-text for voice notes, LLM for task/date extraction, embeddings for history queries (later phase)
- **Mobile:** TBD — evaluate Flutter or React Native for a single codebase that satisfies the Google Play requirement without duplicating the web client
- **Web:** TBD — likely a lightweight SPA (React) consuming the same backend API
