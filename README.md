# brickbox

A tiny Lego brick-inventory API. Know what you can build from the bricks you own.

## Quickstart

Requires Python 3.10+.

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the API (reloads on change)
uvicorn app.main:app --reload
```

The server starts at `http://127.0.0.1:8000`. Interactive API docs are at
`http://127.0.0.1:8000/docs`.

### Try it

```bash
# List the bricks currently in inventory
curl http://127.0.0.1:8000/bricks

# Add (or update) a brick
curl -X POST http://127.0.0.1:8000/bricks \
  -H 'Content-Type: application/json' \
  -d '{"id": "2x4-blue", "color": "blue", "size": "2x4", "qty": 6}'

# Check whether a set is buildable from current inventory
curl http://127.0.0.1:8000/sets/cottage/buildable
```

> Inventory is in-memory only — restarting the server resets it to the defaults.
