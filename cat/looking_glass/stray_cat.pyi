from _typeshed import Incomplete
from cat.auth.permissions import AuthUserInfo as AuthUserInfo
from cat.convo.messages import CatMessage
from cat.memory.long_term_memory import LongTermMemory
from cat.rabbit_hole import RabbitHole
from cat.mad_hatter.mad_hatter import MadHatter
from cat.looking_glass.white_rabbit import WhiteRabbit
from cat.memory.working_memory import WorkingMemory

MSG_TYPES: Incomplete

class StrayCat:
    """User/session based object containing working memory and a few utility pointers"""
    working_memory: WorkingMemory
    def send_ws_message(self, content: str, msg_type: MSG_TYPES = 'notification'):
        """Send a message via websocket.

        This method is useful for sending a message via websocket directly without passing through the LLM
        In case there is no connection the message is skipped and a warning is logged

        Parameters
        ----------
        content : str
            The content of the message.
        msg_type : str
            The type of the message. Should be either `notification`, `chat`, `chat_token` or `error`
        """
    def send_chat_message(self, message: str | CatMessage, save: bool = False):
        """Sends a chat message to the user using the active WebSocket connection.

        In case there is no connection the message is skipped and a warning is logged

        Args:
            message (Union[str, CatMessage]): message to send
            save (bool, optional): Save the message in the conversation history. Defaults to False.
        """
    def send_notification(self, content: str):
        """Sends a notification message to the user using the active WebSocket connection.

        In case there is no connection the message is skipped and a warning is logged

        Args:
            content (str): message to send
        """
    def send_error(self, error: str | Exception):
        """Sends an error message to the user using the active WebSocket connection.

        In case there is no connection the message is skipped and a warning is logged

        Args:
            error (Union[str, Exception]): message to send
        """
    def recall_relevant_memories_to_working_memory(self, query: Incomplete | None = None) -> None:
        """Retrieve context from memory.

        The method retrieves the relevant memories from the vector collections that are given as context to the LLM.
        Recalled memories are stored in the working memory.

        Parameters
        ----------
        query : str, optional
        The query used to make a similarity search in the Cat's vector memories. If not provided, the query
        will be derived from the user's message.

        Notes
        -----
        The user's message is used as a query to make a similarity search in the Cat's vector memories.
        Five hooks allow to customize the recall pipeline before and after it is done.

        See Also
        --------
        cat_recall_query
        before_cat_recalls_memories
        before_cat_recalls_episodic_memories
        before_cat_recalls_declarative_memories
        before_cat_recalls_procedural_memories
        after_cat_recalls_memories
        """
    def llm(self, prompt: str, stream: bool = False) -> str:
        """Generate a response using the LLM model.

        This method is useful for generating a response with both a chat and a completion model using the same syntax

        Parameters
        ----------
        prompt : str
            The prompt for generating the response.

        Returns
        -------
        str
            The generated response.

        """
    def classify(self, sentence: str, labels: list[str] | dict[str, list[str]]) -> str | None:
        '''Classify a sentence.

        Parameters
        ----------
        sentence : str
            Sentence to be classified.
        labels : List[str] or Dict[str, List[str]]
            Possible output categories and optional examples.

        Returns
        -------
        label : str
            Sentence category.

        Examples
        -------
        >>> cat.classify("I feel good", labels=["positive", "negative"])
        "positive"

        Or giving examples for each category:

        >>> example_labels = {
        ...     "positive": ["I feel nice", "happy today"],
        ...     "negative": ["I feel bad", "not my best day"],
        ... }
        ... cat.classify("it is a bad day", labels=example_labels)
        "negative"

        '''
    def stringify_chat_history(self, latest_n: int = 5) -> str:
        """Serialize chat history.
        Converts to text the recent conversation turns.

        Parameters
        ----------
        latest_n : int
            Hoe many latest turns to stringify.

        Returns
        -------
        history : str
            String with recent conversation turns.

        Notes
        -----
        Such context is placed in the `agent_prompt_suffix` in the place held by {chat_history}.

        The chat history is a dictionary with keys::
            'who': the name of who said the utterance;
            'message': the utterance.

        """

    @property
    def working_memory(self) -> WorkingMemory: ...
    @property
    def user_id(self) -> str: ...
    @property
    def user_data(self) -> AuthUserInfo: ...
    @property
    def embedder(self): ...
    @property
    def memory(self) -> LongTermMemory: ...
    @property
    def rabbit_hole(self) -> RabbitHole: ...
    @property
    def mad_hatter(self) -> MadHatter:...
    @property
    def white_rabbit(self) -> WhiteRabbit: ...
