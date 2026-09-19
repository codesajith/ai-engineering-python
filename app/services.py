def get_model_summary(model):
    return {
        "name": model.name,
        "provider": model.provider,
        "supports_vision": model.supports("vision")
    }