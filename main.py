from app.models import AIModel
from app.services import get_model_summary

model = AIModel(
    "Gemini",
    "Google",
    ["text", "vision"]
)

print(model)
print(model.describe())

print(model.supports("vision"))
print(model.supports("audio"))
print(get_model_summary(model))