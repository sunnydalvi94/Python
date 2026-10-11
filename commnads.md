## Run FastAPI

```powershell
# Activate the virtual environment (PowerShell)
.\.venv\Scripts\Activate.ps1
```

```bash
# Or activate it in Git Bash
source .venv/Scripts/activate
```

```bash
# Start the server with the specific FastAPI app (run one command)
python -m uvicorn Backend.fast_API.Crud_operation:app --reload
python -m uvicorn Backend.fast_API.exception_handeling:app --reload
python -m uvicorn Backend.fast_API.get:app --reload
python -m uvicorn Backend.fast_API.parameter:app --reload
python -m uvicorn Backend.fast_API.pydantic_test:app --reload
```

## Run the OpenAI script (not a FastAPI server)

```bash
python Backend/fast_API/gen_ai/basic1.py
```
