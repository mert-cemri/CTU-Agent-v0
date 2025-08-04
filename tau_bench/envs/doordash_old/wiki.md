# DoorDash Domain Wiki

## Overview
DoorDash is a food delivery platform that connects customers with local restaurants. Users can browse restaurants, view menus, place orders, and track deliveries.

## Available Actions

### Restaurant Operations
- `search_restaurants`: Search for restaurants by cuisine, location, rating, etc.
- `get_restaurant_details`: Get detailed information about a specific restaurant
- `get_restaurant_menu`: Get the menu for a specific restaurant

### User Operations
- `get_user_details`: Get user profile information
- `get_user_order_history`: Get order history for a user

### Order Operations
- `create_order`: Create a new order for a user
- `get_order_status`: Check the status of an order
- `update_order`: Update order details (address, instructions, etc.)
- `cancel_order`: Cancel an existing order

### Menu Operations
- `add_item_to_cart`: Add menu items to cart
- `get_item_details`: Get detailed information about a menu item

### Utility Operations
- `calculate`: Perform mathematical calculations
- `think`: Process reasoning steps
- `transfer_to_human_agents`: Transfer to human customer service

## Data Structure

### Restaurants
- Restaurant details with menus, hours, delivery zones
- Full menu with categories and items
- Driver assignments and delivery zones

### Users
- User profiles with addresses and payment methods
- Order history and preferences
- Membership status and loyalty points

### Orders
- Order details with items, pricing, and status
- Delivery information and tracking
- Payment and billing information

## Common Use Cases
- Searching for restaurants by cuisine type
- Viewing restaurant menus and item details
- Creating orders with multiple items
- Tracking order status and delivery
- Managing user addresses and payment methods
- Cancelling or modifying orders 