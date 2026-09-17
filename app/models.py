from dataclasses import dataclass

@dataclass
class AIModel:
    name: str
    provider: str
    capabilities: list