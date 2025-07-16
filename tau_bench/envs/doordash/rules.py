"""DoorDash domain rules and constraints."""

RULES = [
    "Orders must meet minimum order requirements",
    "Restaurants must be open to accept orders",
    "Menu items must be available to be ordered",
    "Orders can only be cancelled before being prepared",
    "Delivery addresses must be within restaurant delivery zones",
    "Payment method must be valid for order processing",
    "Users must have valid account to place orders",
    "Order modifications are limited based on preparation status"
] 