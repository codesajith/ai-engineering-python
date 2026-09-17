from app.models import AIModel

model = AIModel(
    "Gemini",
    "Google",
    ["text", "vision"]
)

print(model)