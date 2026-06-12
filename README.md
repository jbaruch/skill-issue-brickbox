# brickbox

A tiny Lego brick-inventory API. Know what you can build from the bricks you own.

## Quickstart

Install dependencies (a virtualenv is recommended):

```sh
pip install -r requirements.txt
```

Run the server:

```sh
uvicorn app.main:app --reload
```

The API is now at `http://127.0.0.1:8000`. Interactive docs are at
`http://127.0.0.1:8000/docs`.

### Example requests

List the current brick inventory:

```sh
curl http://127.0.0.1:8000/bricks
```

Add (or update) a brick:

```sh
curl -X POST http://127.0.0.1:8000/bricks \
  -H 'Content-Type: application/json' \
  -d '{"id": "2x2-blue", "color": "blue", "size": "2x2", "qty": 6}'
```

Check whether a set is buildable from the current inventory:

```sh
curl http://127.0.0.1:8000/sets/cottage/buildable
```

Inventory and sets are in-memory only, so they reset every time the server
restarts.
