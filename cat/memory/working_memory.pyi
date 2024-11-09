from cat.convo.messages import ModelInteraction as ModelInteraction, Role, UserMessage as UserMessage, MessageWhy
from cat.experimental.form import CatForm as CatForm

class WorkingMemory():
    """Cat's volatile memory.

    Handy class that behaves like a `dict` to store temporary custom data.

    Returns
    -------
    dict[str, list]
        Default instance is a dictionary with `history` key set to an empty list.

    Notes
    -----
    The constructor instantiates a dictionary with a `history` key set to an empty list that is further used to store
    the conversation turns between the Human and the AI.
    """
    history: list
    user_message_json: UserMessage
    active_form: None | CatForm
    recall_query: str
    episodic_memories: list
    declarative_memories: list
    procedural_memories: list
    model_interactions: list[ModelInteraction]
    def update_conversation_history(self, who: Role, message: str, why: MessageWhy) -> None:
        """Update the conversation history.

        The methods append to the history key the last three conversation turns.

        Parameters
        ----------
        who : str
            Who said the message. Can either be `Human` or `AI`.
        message : str
            The message said.

        """
    