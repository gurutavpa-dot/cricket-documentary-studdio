from fastapi import FastAPI, HTTPException
from datetime import datetime
from research import create_research_report
from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="Cricket Documentary Studio",
    description="AI Cricket Match Documentary Generator",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "project": "Cricket Documentary Studio",
        "status": "Running",
        "message": "Welcome to Cricket AI Agent"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "time": datetime.now().isoformat()
    }

@app.get("/features")
def features():
    return {
        "research": True,
        "match_analysis": True,
        "hindi_script": True,
        "voice_generation": "Coming Soon",
        "video_rendering": "Coming Soon",
        "youtube_upload": "Coming Soon"
    }
@app.get("/research/{match_id}")
def research_match(match_id: str):
    try:
        return create_research_report(match_id)

    except ValueError as error:
        raise HTTPException(
            status_code=503,
            detail=str(error)
        )

    except Exception as error:
        raise HTTPException(
            status_code=502,
            detail=str(error)
        )