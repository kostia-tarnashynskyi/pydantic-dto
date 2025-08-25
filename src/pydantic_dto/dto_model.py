from pydantic import BaseModel, Field


class NotificationDTO(BaseModel):
    id: str = Field(..., description="Notification id")
    user_id: str = Field(..., description="User id")
    title: str = Field(..., description="Notification title")
    message: str = Field(..., description="Notification message")
    message_id: str = Field(..., description="Message id")
    icon: str | None = Field(default=None)
    is_read: bool = Field(default=False, description="Notification read status")
    created_at: str = Field(..., description="Creation timestamp")

    class Config:
        from_attributes = True
        orm_mode = True
