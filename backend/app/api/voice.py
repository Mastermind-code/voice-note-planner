from fastapi import APIRouter, UploadFile

router = APIRouter()


@router.post("/ingest")
async def ingest_voice_note(file: UploadFile):
    """
    Receive a voice note (from WhatsApp connector or direct app upload),
    transcribe it, extract tasks/dates via LLM, and create/update a plan.
    """
    # TODO:
    # 1. Save/stream audio file
    # 2. Transcribe (speech-to-text service)
    # 3. Send transcript to LLM for task/date extraction
    # 4. Create or merge into existing plan
    return {"message": "voice note received", "filename": file.filename}
