from _typeshed import Incomplete
from cat.agents import AgentOutput, BaseAgent
from langchain.docstore.document import Document as Document

class MainAgent(BaseAgent):
    """Main Agent.
    This class manages sub agents that in turn use the LLM.
    """
    mad_hatter: Incomplete
    verbose: bool
    def __init__(self) -> None: ...
    def execute(self, stray) -> AgentOutput:
        """Execute the agents.

        Returns
        -------
        agent_output : AgentOutput
            Reply of the agent, instance of AgentOutput.
        """
    def format_agent_input(self, stray):
        """Format the input for the Agent.

        The method formats the strings of recalled memories and chat history that will be provided to the Langchain
        Agent and inserted in the prompt.

        Returns
        -------
        BaseModelDict
            Formatted output to be parsed by the Agent executor. Works both as a dict and as an object.

        Notes
        -----
        The context of memories and conversation history is properly formatted before being parsed by the and, hence,
        information are inserted in the main prompt.
        All the formatting pipeline is hookable and memories can be edited.

        See Also
        --------
        agent_prompt_episodic_memories
        agent_prompt_declarative_memories
        agent_prompt_chat_history
        """
    def agent_prompt_episodic_memories(self, memory_docs: list[tuple[Document, float]]) -> str:
        """Formats episodic memories to be inserted into the prompt.

        Parameters
        ----------
        memory_docs : List[Document]
            List of Langchain `Document` retrieved from the episodic memory.

        Returns
        -------
        memory_content : str
            String of retrieved context from the episodic memory.
        """
    def agent_prompt_declarative_memories(self, memory_docs: list[tuple[Document, float]]) -> str:
        """Formats the declarative memories for the prompt context.
        Such context is placed in the `agent_prompt_prefix` in the place held by {declarative_memory}.

        Parameters
        ----------
        memory_docs : List[Document]
            list of Langchain `Document` retrieved from the declarative memory.

        Returns
        -------
        memory_content : str
            String of retrieved context from the declarative memory.
        """
