def get_model_summary(model):
    return {
        "name": model.name,
        "provider": model.provider,
        "supports_vision": model.supports("vision")
    }

def get_capability_summary(model):
    return {
        "name": model.name,
        "capability_count": len(model.capabilities),
        "supports_vision": model.supports("vision"),
        "supports_audio": model.supports("audio")
    }