async def transcribe_audio(file_bytes: bytes) -> str:
    """
    Send audio to a speech-to-text provider and return the transcript.
    TODO: wire up actual provider (e.g. Whisper API, or a local model).
    """
    raise NotImplementedError
