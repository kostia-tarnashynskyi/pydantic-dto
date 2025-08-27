from pydantic import BaseModel, ConfigDict, Field


class NotificationDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str = Field(..., description="Notification id")
    user_id: str = Field(..., description="User id")
    title: str = Field(..., description="Notification title")
    message: str = Field(..., description="Notification message")
    message_id: str = Field(..., description="Message id")
    icon: str | None = Field(default=None)
    is_read: bool = Field(default=False, description="Notification read status")
    created_at: str = Field(..., description="Creation timestamp")
    updated_at: str = Field(..., description="Last update timestamp")
