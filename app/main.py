"""brickbox — a tiny Lego brick-inventory API (demo app for "Skill Issue").

Deliberately small and boring so the live demo stays about SKILLS, not this code.
In-memory only; no database, no auth, no tests (yet — that's a demo ticket).
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="brickbox", summary="Know what you can build from the bricks you own.")

# id -> {"color": str, "size": str, "qty": int}
BRICKS: dict[str, dict] = {
    "2x4-red": {"color": "red", "size": "2x4", "qty": 8},
    "2x2-red": {"color": "red", "size": "2x2", "qty": 4},
    "1x2-white": {"color": "white", "size": "1x2", "qty": 12},
}

# set_id -> required {brick_id: qty}
SETS: dict[str, dict[str, int]] = {
    "cottage": {"2x4-red": 4, "1x2-white": 6},
    "tower": {"2x4-red": 10, "2x2-red": 2},
}


class Brick(BaseModel):
    id: str
    color: str
    size: str
    qty: int


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/bricks")
def list_bricks() -> dict[str, dict]:
    return BRICKS


@app.post("/bricks")
def add_brick(brick: Brick) -> dict:
    BRICKS[brick.id] = {"color": brick.color, "size": brick.size, "qty": brick.qty}
    return {"added": brick.id}


@app.get("/sets/{set_id}/buildable")
def buildable(set_id: str) -> dict:
    """Can the current inventory build this set?"""
    required = SETS.get(set_id)
    if required is None:
        raise HTTPException(status_code=404, detail=f"unknown set: {set_id}")
    missing = {
        brick_id: need - BRICKS.get(brick_id, {}).get("qty", 0)
        for brick_id, need in required.items()
        if BRICKS.get(brick_id, {}).get("qty", 0) < need
    }
    return {"set": set_id, "buildable": not missing, "missing": missing}
