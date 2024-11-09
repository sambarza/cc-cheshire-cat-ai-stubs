from cat.agents import AgentOutput, BaseAgent

class FormAgent(BaseAgent):
    def execute(self, stray) -> AgentOutput: ...
