# brickbox

A tiny Lego brick-inventory API. Know what you can build from the bricks you own.

## Quickstart

1. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run the API:

   ```bash
   uvicorn app.main:app --reload
   ```

3. Open the interactive docs at http://127.0.0.1:8000/docs, or try the endpoints directly:

   ```bash
   # List your current brick inventory
   curl http://127.0.0.1:8000/bricks

   # Add (or update) a brick
   curl -X POST http://127.0.0.1:8000/bricks \
     -H "Content-Type: application/json" \
     -d '{"id": "2x4-blue", "color": "blue", "size": "2x4", "qty": 6}'

   # Check whether you can build a set from your inventory
   curl http://127.0.0.1:8000/sets/cottage/buildable
   ```
