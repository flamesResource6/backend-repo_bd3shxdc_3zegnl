"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal
from datetime import date

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Studio booking schema (used by the app)
class Booking(BaseModel):
    """
    Bookings for studio sessions
    Collection name: "booking"
    """
    name: str = Field(..., min_length=2, max_length=100, description="Client name")
    email: EmailStr = Field(..., description="Client email")
    phone: Optional[str] = Field(None, description="Phone number")
    service: Literal['Recording','Mixing','Production','Mastering'] = Field(..., description="Type of service")
    booking_date: date = Field(..., description="Preferred booking date (YYYY-MM-DD)")
    time: str = Field(..., pattern=r"^([01]?[0-9]|2[0-3]):[0-5][0-9]$", description="Start time HH:MM (24h)")
    duration_hours: int = Field(2, ge=1, le=12, description="Estimated duration in hours")
    notes: Optional[str] = Field(None, max_length=1000, description="Project details or references")
    status: Literal['requested','confirmed','declined'] = Field('requested', description="Booking status")
