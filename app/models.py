from dataclasses import dataclass

@dataclass
class AIModel:
    name: str
    provider: str
    capabilities: list

    def describe(self):
        return self.name + " is provided by " + self.provider

    def supports(self, capability):
        return capability in self.capabilities

