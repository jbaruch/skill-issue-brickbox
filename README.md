# brickbox

A tiny Lego brick-inventory API. Know what you can build from the bricks you own.

`uvicorn app.main:app --reload`

## Quickstart

1. Install dependencies:

   ```bash
   pip install fastapi uvicorn
   ```

2. Start the server:

   ```bash
   uvicorn app.main:app --reload
   ```

   The API is now running at `http://127.0.0.1:8000`. Interactive docs live at
   `http://127.0.0.1:8000/docs`.

3. List the bricks currently in inventory:

   ```bash
   curl http://127.0.0.1:8000/bricks
   ```

4. Add a brick to inventory:

   ```bash
   curl -X POST http://127.0.0.1:8000/bricks \
     -H 'Content-Type: application/json' \
     -d '{"id": "2x4-blue", "color": "blue", "size": "2x4", "qty": 6}'
   ```

5. Check whether you can build a set from what you own:

   ```bash
   curl http://127.0.0.1:8000/sets/cottage/buildable
   ```
