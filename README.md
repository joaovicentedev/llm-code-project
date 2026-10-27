# Qwen API

Requires `uv` and Python 3.14.

```sh
uv sync
uv run uvicorn main:app --reload
```

Test the endpoint in another terminal:

```sh
curl -X POST http://127.0.0.1:8000/ask \
  -H 'Content-Type: application/json' \
  -d '{"user_message":"Who are you?"}'
```

The response is JSON containing a `response` string. The first request downloads
`Qwen/Qwen3-0.6B` from Hugging Face and loads it into memory; later requests
reuse the loaded model. A network connection and enough memory for the model
are required on first use.
Interactive documentation: http://127.0.0.1:8000/docs
