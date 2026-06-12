# brickbox

A tiny Lego brick-inventory API. Know what you can build from the bricks you own.

## Quickstart

### 1. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the server

```bash
uvicorn app.main:app --reload
```

The API is now live at `http://127.0.0.1:8000`. Interactive docs are available at
`http://127.0.0.1:8000/docs`.

### 3. Try it out

List the bricks currently in inventory:

```bash
curl http://127.0.0.1:8000/bricks
```

Add a brick (or update the quantity of an existing one):

```bash
curl -X POST http://127.0.0.1:8000/bricks \
  -H "Content-Type: application/json" \
  -d '{"id": "2x4-blue", "color": "blue", "size": "2x4", "qty": 6}'
```

Check whether you can build a known set from your current inventory:

```bash
curl http://127.0.0.1:8000/sets/cottage/buildable
```

The response reports whether the set is buildable and, if not, how many of each
brick you're missing:

```json
{"set": "cottage", "buildable": true, "missing": {}}
```

## Endpoints

| Method | Path                       | Description                                      |
| ------ | -------------------------- | ------------------------------------------------ |
| GET    | `/bricks`                  | List all bricks in inventory.                    |
| POST   | `/bricks`                  | Add a brick or update an existing one's quantity.|
| GET    | `/sets/{set_id}/buildable` | Check if a set is buildable from inventory.       |

Known sets are `cottage` and `tower`.
