from _typeshed import Incomplete
from enum import Enum
from pydantic import BaseModel as BaseModel

class CatFormState(Enum):
    INCOMPLETE = 'incomplete'
    COMPLETE = 'complete'
    WAIT_CONFIRM = 'wait_confirm'
    CLOSED = 'closed'

class CatForm:
    model_class: BaseModel
    procedure_type: str
    name: str
    description: str
    start_examples: list[str]
    stop_examples: list[str]
    ask_confirm: bool
    triggers_map: Incomplete
    def __init__(self, cat) -> None: ...
    @property
    def cat(self): ...
    def submit(self, form_data) -> str: ...
    def confirm(self) -> bool: ...
    def check_exit_intent(self) -> bool: ...
    def next(self): ...
    def update(self): ...
    def message(self): ...
    def message_closed(self): ...
    def message_wait_confirm(self): ...
    def message_incomplete(self): ...
    def extract(self): ...
    def extraction_prompt(self): ...
    def sanitize(self, model): ...
    def validate(self, model): ...