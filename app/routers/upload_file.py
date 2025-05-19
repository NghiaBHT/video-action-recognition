import os
import shutil
import tempfile
import cv2
from fastapi import APIRouter, FastAPI, HTTPException, UploadFile

router = APIRouter(prefix="/video", tags=["video"])

@router.post("/upload_video")
async def upload_video(file: UploadFile):
    if not file.filename.lower().endswith((".mp4", ".avi", ".mov")):
        raise HTTPException(status_code=400, detail="Chỉ chấp nhận file .mp4/.avi/.mov")

    suffix = os.path.splitext(file.filename)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    cap = cv2.VideoCapture(tmp_path)
    if not cap.isOpened():
        os.remove(tmp_path)
        raise HTTPException(status_code=500, detail="Không thể mở video để trích xuất frame")
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1

    cap.release()

    os.remove(tmp_path)

    return {"filename": file.filename, "frames_extracted": frame_count}