from cat.agents import AgentOutput, BaseAgent

class MemoryAgent(BaseAgent):
    def execute(self, stray, prompt_prefix, prompt_suffix) -> AgentOutput: ...
