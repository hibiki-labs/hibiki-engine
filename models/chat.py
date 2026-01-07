from typing import List, Literal
from pydantic import BaseModel, Field, model_validator


Role = Literal["system", "user", "assistant"]


class ChatMessage(BaseModel):
    role: Role = Field(..., description="The role of the message author")
    content: str = Field(
        ..., min_length=1, description="The textual content of the message"
    )


# note: ellipses (...) mean: There is no default. You must provide this.

# For future use
# class GenerationParameters(BaseModel):
#     temperature: float = Field(0.7, ge=0.0, le=2.0)
#     max_tokens: Optional[int] = Field(None, gt=0)


class ChatCompletionRequest(BaseModel):
    messages: List[ChatMessage]
    # parameters: Optional[GenerationParameters] = None

    @model_validator(mode="after")
    def ensure_user_message_exists(self):
        if not any(m.role == "user" for m in self.messages):
            raise ValueError("At least one user message is required")
        return self
