from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from app.core.auth import is_public_enabled
from app.core.config import config

router = APIRouter()


@router.get("/", include_in_schema=False)
async def root():
    await config.maybe_reload()
    if is_public_enabled():
        return RedirectResponse(url="/login")
    return RedirectResponse(url="/admin/login")


@router.get("/login", include_in_schema=False)
async def public_login():
    await config.maybe_reload()
    if not is_public_enabled():
        raise HTTPException(status_code=404, detail="Not Found")
    return RedirectResponse(url="/static/public/pages/login.html")


@router.get("/imagine", include_in_schema=False)
async def public_imagine():
    await config.maybe_reload()
    if not is_public_enabled():
        raise HTTPException(status_code=404, detail="Not Found")
    return RedirectResponse(url="/static/public/pages/imagine.html")


@router.get("/voice", include_in_schema=False)
async def public_voice():
    await config.maybe_reload()
    if not is_public_enabled():
        raise HTTPException(status_code=404, detail="Not Found")
    return RedirectResponse(url="/static/public/pages/voice.html")


@router.get("/video", include_in_schema=False)
async def public_video():
    await config.maybe_reload()
    if not is_public_enabled():
        raise HTTPException(status_code=404, detail="Not Found")
    return RedirectResponse(url="/static/public/pages/video.html")


@router.get("/chat", include_in_schema=False)
async def public_chat():
    await config.maybe_reload()
    if not is_public_enabled():
        raise HTTPException(status_code=404, detail="Not Found")
    return RedirectResponse(url="/static/public/pages/chat.html")
