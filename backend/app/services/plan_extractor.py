def extract_tasks_from_transcript(transcript: str) -> list[dict]:
    """
    Send transcript to an LLM and parse out structured tasks:
    [{"title": ..., "due_date": ..., "scope": "day|week|month"}, ...]
    TODO: wire up actual LLM call + prompt design (Week 1-2 curriculum territory).
    """
    raise NotImplementedError
