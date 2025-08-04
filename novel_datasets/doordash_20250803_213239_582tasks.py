"""
Generated tasks for doordash domain.
Generated at: 2025-08-03T22:39:18.465029
Total tasks: 582
"""

from tau_types import Task, Action

TASKS_TRAIN = [
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are polite, independent, cautious. search_restaurants(location=\"Downtown\", cuisine=\"Italian\", price_range=\"medium\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "medium"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are polite, logical. First, search for Mexican restaurants in San Francisco with a moderate price range ($$) to find a suitable dining option for your upcoming dinner. Once you have identified a promising restaurant, retrieve detailed information about the restaurant to ensure it meets your expectations in terms of ambiance and customer reviews. After confirming the restaurant's suitability, explore their menu specifically focusing on the Tacos category to decide on the items you wish to order. Finally, add three of your chosen taco items to your cart, ensuring that they are from the selected restaurant, to prepare for a seamless checkout process on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U048", "restaurant_id": "R001", "item_id": "I001", "quantity": 1}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U048", "restaurant_id": "R001", "item_id": "I002", "quantity": 1}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U048", "restaurant_id": "R001", "item_id": "I003", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U187",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are independent, cautious. Get the restaurant menu for restaurant ID R987 to browse available Italian dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are optimistic, independent. You are planning a cozy dinner at home and have decided to order Italian food. First, search_restaurants(location=\"Downtown\", cuisine=\"Italian\", price_range=\"$$\") to find a suitable place to order from. Once you have selected a restaurant, get_restaurant_menu(restaurant_id=\"R123\") to explore their offerings. After choosing your favorite dish, add_item_to_cart(user_id=\"U001\", restaurant_id=\"R123\", item_id=\"I456\", quantity=2) to ensure you have enough for yourself and a guest.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U085", "restaurant_id": "R123", "item_id": "I456", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U020",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are patient, polite. First, search for restaurants in the downtown area with a price range of $10-$20 to find suitable dining options for a customer. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R2345 to check if it's open and meets the customer's order requirements. Finally, create an order for user ID U1234 at restaurant ID R2345 with selected items, ensuring the delivery address is 123 Elm St and the payment method is Credit Card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U020", "restaurant_id": "R2345", "items": [{"item_id": "I001", "quantity": 2}, {"item_id": "I002", "quantity": 1}], "delivery_address": "123 Elm St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is James Williams and your email is james.williams9904@email.com. You are flexible, logical. First, search for Mexican restaurants in Patricia's area with a mid-range price level to identify potential dining options. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R205 to find available tacos. This will help you determine if the restaurant offers a variety of taco options that meet Patricia's preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R205", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U163",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are direct, independent, cautious. Search for restaurants in the downtown area with a cuisine preference for Italian and a price range of moderate. Then, get detailed information for restaurant R456 to verify it meets user preferences. This will help ensure that the restaurant aligns with the quality and dining experience expected by DoorDash users.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U138",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson5028@email.com. You are logical, cautious. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$30 to explore potential dining options. Once you have identified a suitable restaurant, get restaurant details for restaurant ID R567 to confirm its opening hours and delivery zone, ensuring it meets your logistical needs. Finally, get the restaurant menu for restaurant ID R567 to check available items and categories, allowing you to make an informed decision before proceeding with any orders.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are logical, patient. Search for restaurants offering Mexican cuisine in the San Francisco area within a mid-range price bracket.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are cautious, logical, patient, flexible. Search for restaurants offering Mexican cuisine in Linda's area with a price range of $10-$30. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R567 to find available taco options. This will help ensure that Linda can choose from a variety of tacos that fit her preferences and budget on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are cautious, logical, polite, confident. Get the menu for restaurant ID R567, focusing on the pasta category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U193",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are confident, patient, independent, polite. add_item_to_cart(user_id=\"U001\", restaurant_id=\"R123\", item_id=\"I456\", quantity=2, customizations={\"extra cheese\": \"yes\"})",
        actions=[
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U193", "restaurant_id": "R123", "item_id": "I456", "quantity": 2, "customizations": {"extra cheese": "yes"}}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U002",
        instruction="Your name is Robert Williams and your email is robert.williams9426@email.com. You are logical, confident, flexible, optimistic. Search for Italian restaurants in Patricia Brown's area with a mid-range price category and get the restaurant menu for R1023 to find available pasta dishes. This will help ensure that Patricia has a variety of options to choose from when ordering through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Patricia Brown's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are polite, flexible. First, search for Italian restaurants in the downtown area with a price range of $$. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R5678, focusing on the \"Pasta\" category. After reviewing the menu, add item ID I234 (Spaghetti Carbonara) to cart for user ID U1234 with quantity 1.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U030", "restaurant_id": "R5678", "item_id": "I234", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are independent, polite. First, search for Italian restaurants in the San Francisco area with a price range of \"$$\" to find a suitable dining option. Once you have identified a restaurant, get the menu for restaurant ID R1024 to view available pasta dishes. If Spaghetti Carbonara is available, add item ID I5678 (Spaghetti Carbonara) to cart for user ID U314 with quantity 1.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1024"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U167", "restaurant_id": "R1024", "item_id": "I5678", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are optimistic, patient, logical, independent. Get the restaurant menu for restaurant ID R1023 to view available items in the \"Tacos\" category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are patient, optimistic, logical. Search for restaurants offering Mexican cuisine in the 94103 area with a price range of $$.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "94103", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are direct, organized, optimistic. First, search for Mexican restaurants in the San Francisco area with a price range of $$. Once you have identified a suitable restaurant, get the menu for restaurant R200 to review available taco options. This will help you decide on the best items to order for a customer.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R200", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U007",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are patient, logical, optimistic. First, search for restaurants offering Mexican cuisine in Michael Smith's area with a price range of $10-$20 to identify potential options for a Doordash delivery. Once you have identified a suitable restaurant, get detailed information for restaurant R234 to check its operating hours and customer reviews. This will help ensure that the restaurant is open and has positive feedback before proceeding with any orders.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Michael Smith's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are patient, organized. First, search for Italian restaurants in the vicinity of Patricia's delivery address to find suitable options for her dinner. Once you have identified a restaurant, specifically R234, get the menu focusing on the pasta category. This will help ensure that Patricia has a variety of pasta options to choose from for her order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Patricia's delivery address"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are organized, optimistic, logical, direct. Begin by searching for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$20 to find a suitable dining option. Once you have identified a restaurant, get the restaurant menu for restaurant ID R456 to view available items in the \"Tacos\" category. After reviewing the menu, add item ID I789 (Chicken Taco) to the cart for user ID U102 with a quantity of 3 and no customizations. This sequence will help you efficiently plan a meal order for a user looking to enjoy affordable Mexican cuisine through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U158", "restaurant_id": "R456", "item_id": "I789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U016",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are logical, cautious, polite, independent. Search for Italian restaurants in Jennifer Johnson's area with a price range of $10-$30, and then get the restaurant menu for restaurant R567 to view available Italian dishes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Jennifer Johnson's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U002",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are logical, patient. First, search for Mexican restaurants in San Francisco within the price range of $$. Once you find a suitable restaurant, get the restaurant details using the restaurant ID. After reviewing the details, proceed to get the restaurant menu to explore the available options. Finally, choose an item you like, and add it to your cart with a quantity of 2, ensuring you use your user ID for the order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U002", "restaurant_id": "R001", "item_id": "I001", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is Linda Davis and your email is linda.davis2351@email.com. You are polite, independent, optimistic, direct. First, search for restaurants with Mexican cuisine in the downtown area with a price range of $$. Once you have identified potential options, get restaurant details for restaurant ID R56789 to check its hours and delivery zone. This information will help ensure that the restaurant meets the delivery requirements for DoorDash customers seeking Mexican cuisine in the specified area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R56789"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is Patricia Miller and your email is patricia.miller3271@email.com. You are confident, logical. First, search for Mexican restaurants in the San Francisco area with a price range of $$ to $$$ to identify potential new partners for DoorDash. Once you have identified a restaurant of interest, such as one with the restaurant ID R2023, get the restaurant details to verify it is open for delivery. This will help ensure that our platform offers a variety of quality dining options for our customers.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are cautious, flexible. First, search for restaurants with Italian cuisine in New York, NY within a medium price range to identify potential options for partnership. Once you have a list, get detailed information for restaurant R1023 to verify its operating hours and customer ratings. This will help ensure that the restaurant meets DoorDash's standards for quality and reliability before proceeding with any further business discussions.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York, NY", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U101",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are confident, cautious. First, search for restaurants offering Italian cuisine in the downtown area with a moderate price range. Once you find a suitable restaurant, get the menu for restaurant ID R2345, focusing on the pasta category.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U055",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9197@email.com. You are flexible, patient, logical. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to identify potential new partners for DoorDash. Once you have identified a suitable restaurant, get the menu details for restaurant ID R1023 with a focus on the pasta category to assess the variety and quality of offerings that could be featured on our platform.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U170",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are confident, logical. First, search for restaurants in the Midtown area that offer Mexican cuisine and have a moderate price range to find suitable dining options for our customers. Once you have identified potential restaurants, get restaurant details for restaurant R250 to verify their operating hours and delivery zones, ensuring they can serve the Midtown area efficiently. Finally, create an order for user james.johnson8780@email.com from restaurant R250 with items [I678, I679], delivery address \"123 Elm Street, Apt 4B\", and payment method \"Credit Card\" to complete the transaction and ensure customer satisfaction.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Midtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R250"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U170", "restaurant_id": "R250", "items": [{"item_id": "I678", "quantity": 1}, {"item_id": "I679", "quantity": 1}], "delivery_address": "123 Elm Street, Apt 4B", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U176",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are patient, confident, independent, polite. Search for Italian restaurants in the San Francisco area with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a restaurant, get the restaurant menu for restaurant ID R4567 to view available pasta dishes, ensuring there are options that meet your preferences for a potential order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R4567", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U176",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are independent, polite, patient. First, use `search_restaurants` with `cuisine=\"Mexican\"`, `location=\"San Francisco\"`, and `price_range=\"$\"` to find budget-friendly Mexican restaurants in San Francisco. Once you have identified a suitable restaurant, call `get_restaurant_details` with `restaurant_id=\"R001\"` to retrieve its operating hours and delivery zones to ensure it can deliver to your location. After confirming the restaurant's delivery capabilities, use `get_restaurant_menu` with `restaurant_id=\"R001\"` to access the full menu and explore the available options before making your selection.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are optimistic, independent. First, search for Italian restaurants located in downtown with a moderate price range of $$. Once you find a suitable restaurant, retrieve the pasta menu from the restaurant with ID R345 to explore your options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R345", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is James Williams and your email is james.williams9904@email.com. You are independent, patient, optimistic, organized. First, search for restaurants in the downtown area with a price range of $10-$20 to find suitable dining options for a client meeting. Once you identify a restaurant, get the menu for restaurant R234, focusing on the 'Pasta' category, to ensure it meets the client's preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U190",
        instruction="Your name is Linda Miller and your email is linda.miller5151@email.com. You are confident, organized. First, search for Italian restaurants in San Francisco with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a restaurant, get the restaurant menu for restaurant ID R234 to view available items. This will help you decide on the best dishes to order for a delightful dining experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$ to $$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U123",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are independent, flexible, direct. Get restaurant menu for restaurant ID R234 to view available Italian dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Italian"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are polite, logical, organized, optimistic. Create an order for user U9999 at restaurant R2345 with items: I6789 (Chicken Tacos), delivery address 123 Main St, payment method credit card, and special instructions \"No onions\".",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R2345", "item_id": "I6789"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U049", "restaurant_id": "R2345", "items": [{"item_id": "I6789", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "No onions"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U007",
        instruction="Your name is Robert Brown and your email is robert.brown1066@email.com. You are logical, optimistic, polite, organized. First, search for restaurants with cuisine type \"Mexican\" in the location \"San Francisco\" within a moderate price range to explore dining options. Next, get restaurant details for restaurant ID R234 to check hours and delivery zones, ensuring it fits your schedule and delivery needs. Finally, create an order for user ID U6151 at restaurant ID R234 with items I6789 (Chicken Tacos) and delivery address \"123 Main St, San Francisco, CA\" to enjoy a delicious meal at home.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U007", "restaurant_id": "R234", "items": [{"item_id": "I6789", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are flexible, optimistic, direct, patient. You have been tasked with arranging a lunch delivery for a client meeting in the downtown area. First, search for Italian restaurants in the downtown area that offer medium-priced meals. Once you have identified a suitable restaurant, retrieve the restaurant's details to ensure it meets the client's preferences and dietary requirements. After confirming the restaurant's suitability, proceed to get the menu for the pizza category. Finally, add two Margherita pizzas to the cart for the user with the email john.brown7947@email.com, ensuring that the order is ready for delivery in time for the meeting.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "pizza"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U006", "restaurant_id": "R001", "item_id": "I123", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are optimistic, patient. First, search for restaurants with cuisine \"Mexican\" in \"San Francisco\" within the price range \"$$\" to find a suitable dining option. Once you have identified a restaurant, get the menu for restaurant ID \"R5678\" to view available items. Then, add item ID \"I1234\" (Chicken Tacos) to the cart for user ID \"U8314\" with quantity 2, ensuring your order is ready for checkout on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U180", "restaurant_id": "R5678", "item_id": "I1234", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U077",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are direct, optimistic, patient. First, search for Mexican restaurants in the Brooklyn area with a price range of $$ to identify potential new partners for DoorDash. Once you have a list, focus on restaurant R5678 to get their menu and find available taco options, ensuring they align with customer preferences and DoorDash's delivery offerings.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Brooklyn", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U101",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are optimistic, confident, polite, patient. First, search for restaurants in San Francisco offering Chinese cuisine with a price range of $10-$30 to find suitable dining options. Once you have identified a restaurant of interest, get the restaurant details for restaurant ID R1024 to verify opening hours and delivery zones, ensuring that it fits your schedule and location. Finally, create an order for user ID U1001 at restaurant ID R1024 with items Kung Pao Chicken and Spring Rolls, using the delivery address 123 Main St, and payment method credit card ending in 1234, to enjoy a delightful meal delivered to your doorstep.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1024"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U101", "restaurant_id": "R1024", "items": [{"item_id": "I001", "quantity": 1}, {"item_id": "I002", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card ending in 1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U081",
        instruction="Your name is Linda Davis and your email is linda.davis2351@email.com. You are logical, organized, independent. Search for Italian restaurants in Jennifer Brown's area with a price range of $10-$30.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Jennifer Brown's area", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U087",
        instruction="Your name is Robert Brown and your email is robert.brown1066@email.com. You are confident, direct. First, search for Mexican restaurants in San Francisco with a moderate price range of $$. Once you have identified a suitable restaurant, proceed to get the restaurant menu focusing on the Entrees category. This will help you decide on the best dish to recommend to a client who is looking for authentic Mexican cuisine at a reasonable price point.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Entrees"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are direct, independent, flexible, optimistic. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to identify potential options for a client meeting. Once you have identified a suitable restaurant, get the menu for restaurant R5678, focusing on the pasta category, to ensure they offer a variety of pasta dishes that can cater to diverse preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are organized, polite. First, search for restaurants with Mexican cuisine in the 90210 area code with a price range of $$. Once you have identified a suitable restaurant, update order O1234 to include the new dessert item from cart before preparation starts, ensuring the order is complete and ready for processing.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "90210", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U177", "restaurant_id": "R001", "item_id": "I123", "quantity": 1}
            ),
            Action(
                name="update_order",
                kwargs={"order_id": "O1234", "special_instructions": "Include dessert item from cart"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U128",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are independent, polite, patient, flexible. Search for restaurants offering vegan cuisine in the San Francisco area with a price range of $$ to $$$.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "vegan", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are organized, flexible, confident, polite. First, search for Italian restaurants in the downtown area with a price range of $$-$$$ to find suitable dining options. Once you have identified a potential restaurant, retrieve the restaurant details for restaurant R5678 to check its operating hours, ensuring it fits within your desired dining schedule. Finally, create an order for user U98765 at restaurant R5678 with item I1234, using the default delivery address and payment method, to ensure a seamless dining experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U143", "restaurant_id": "R5678", "items": [{"item_id": "I1234", "quantity": 1}]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are independent, confident, flexible, direct. First, search for Mexican restaurants in San Francisco with a mid-range price tier to find potential dining options. Next, get restaurant details for restaurant R5678 to verify delivery hours and address, ensuring it fits within your schedule and location. Finally, create an order for user U101 at restaurant R5678 with items [I987, I654], delivery address \"123 Market St, San Francisco, CA,\" and payment method \"credit card\" to complete the transaction efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U158", "restaurant_id": "R5678", "items": [{"item_id": "I987", "quantity": 1}, {"item_id": "I654", "quantity": 1}], "delivery_address": "123 Market St, San Francisco, CA", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are patient, optimistic, logical, confident. First, search for restaurants in San Francisco with cuisine \"Mexican\" and price range \"$$\" to identify potential options for expanding our delivery service. Once you have a list of restaurants, get restaurant details for restaurant ID R200 to check its opening hours and delivery zone. This will help ensure that the restaurant fits within our operational hours and delivery capabilities for optimal service integration.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R200"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are confident, organized, optimistic, cautious. Get the restaurant menu for restaurant ID R2345 to view available Italian dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are cautious, optimistic, confident, independent. Search for Italian restaurants in the San Francisco area with a price range of $$ to $$$. Once you find a suitable restaurant, get the menu for restaurant R12345, focusing on the pasta category. This will help you decide on the best pasta options to include in an order for user U56789. After reviewing the menu, create an order at restaurant R12345 with items [I67890, I67891], ensuring delivery to \"123 Elm Street, San Francisco, CA\" using a credit card for payment. Make sure to include the special instructions \"Leave at the door\" for a seamless delivery experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R12345", "category": "pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U085", "restaurant_id": "R12345", "items": [{"item_id": "I67890", "quantity": 1}, {"item_id": "I67891", "quantity": 1}], "delivery_address": "123 Elm Street, San Francisco, CA", "payment_method": "credit_card", "special_instructions": "Leave at the door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U077",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are confident, logical, cautious, flexible. First, search for Mexican restaurants in Linda Garcia's delivery area with a price range of $10-$20 to find suitable options. Then, get restaurant details for restaurant ID R567 to verify if it's open and check its delivery zone to ensure it can deliver to your location. Finally, create an order for user ID U4109 with restaurant ID R567, items [T111, B222], delivery address 123 Main St, payment method credit card, and special instructions \"Leave at door\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U077", "restaurant_id": "R567", "items": [{"item_id": "T111", "quantity": 1}, {"item_id": "B222", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is John Brown and your email is john.brown5124@email.com. You are logical, patient. First, search for Mexican restaurants in the San Francisco area with a price range of $$. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R345 and filter by Tacos category. After reviewing the options, add item I789 (Chicken Tacos) to cart for user ID U1234 with quantity 3.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R345", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U151", "restaurant_id": "R345", "item_id": "I789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U138",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are organized, polite, direct, flexible. Create order for user U3456 from restaurant R5678 with items [I2345] and delivery address 123 Main St, using credit card payment.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R5678", "item_id": "I2345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U138", "restaurant_id": "R5678", "items": [{"item_id": "I2345", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are organized, logical, patient. First, search for restaurants near Patricia's location offering Mexican cuisine within a moderate price range to find suitable dining options. Once you have identified a potential restaurant, get restaurant details for restaurant ID R1023 to verify its hours and delivery zone coverage, ensuring it meets Patricia's needs. Finally, create an order for user ID U3517 from restaurant ID R1023 with items [I205, I207], specifying the delivery address as \"123 Main St, Apt 4\" and using the payment method \"Visa ending in 1234\" to complete the transaction smoothly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Patricia's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U124", "restaurant_id": "R1023", "items": [{"item_id": "I205", "quantity": 1}, {"item_id": "I207", "quantity": 1}], "delivery_address": "123 Main St, Apt 4", "payment_method": "Visa ending in 1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are confident, cautious. First, get detailed information about restaurant R234 to verify opening hours and delivery zones, as this will ensure that the restaurant can deliver to the specified address. Once confirmed, proceed to create an order for user U001 at restaurant R234 with items: I678 (Spaghetti Carbonara) and delivery address 123 Main St, San Francisco, using credit card as payment method. This sequence ensures that the order can be successfully placed and delivered within the operational parameters of the restaurant.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U151", "restaurant_id": "R234", "items": [{"item_id": "I678", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U016",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are polite, logical, patient. First, search for restaurants offering Mexican cuisine in Jennifer Johnson's area with a mid-range price. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R234 to find available taco options. This will help you ensure that you are selecting a restaurant that offers a good variety of tacos, which is important for the order Jennifer wants to place through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer Johnson's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U128",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are independent, cautious, patient. Get the menu for restaurant ID R234 to browse available items in the \"Tacos\" category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U077",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are direct, polite, confident, independent. Search for Mexican restaurants in Linda Garcia's area with a price range of $10-$30.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Garcia", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U170",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are flexible, polite. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$20 to find potential options for a new lunch spot. Next, get restaurant details for restaurant ID R150 to verify its opening hours and delivery area, ensuring it fits within your schedule and location. Finally, create an order for user ID U123 with restaurant ID R150, including items [I300], delivery address: 123 Main St, payment method: credit card, and special instructions: extra napkins, to complete the lunch order process seamlessly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R150"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U170", "restaurant_id": "R150", "items": [{"item_id": "I300", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "extra napkins"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U178",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are patient, organized, optimistic. First, get restaurant details for restaurant ID R1023 to ensure it meets the preferences of our client, Mary Jones. Next, retrieve the restaurant menu for restaurant ID R1023 to verify the availability of her desired items. Finally, create an order for user Mary Jones at restaurant ID R1023 with items [(I560, 1), (I561, 2)] and ensure the delivery is set to 1234 Market St, San Francisco, CA.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U178", "restaurant_id": "R1023", "items": [{"item_id": "I560", "quantity": 1}, {"item_id": "I561", "quantity": 2}], "delivery_address": "1234 Market St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U128",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are confident, polite, cautious, flexible. First, search for restaurants offering Mexican cuisine in the downtown area with a price range of $10-$20 to identify potential options for a customer's dinner delivery. Once you find a suitable restaurant, get the menu for restaurant ID R456 to explore available Mexican dishes. This will allow you to recommend specific items to the customer, ensuring they have a delightful dining experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U087",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are cautious, organized, direct. First, search for restaurants in the 94103 ZIP code area with a price range of $$ to $$$ that serve Mexican cuisine. Once you have identified potential options, get the restaurant details for restaurant ID R1023 to verify operating hours and delivery zones. This will ensure that the restaurant is open and delivers to your area before you proceed with placing an order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "94103", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U178",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown2003@email.com. You are flexible, cautious. Search for Italian restaurants in Mary Jones' area, focusing on mid-range prices. Once you have identified a suitable restaurant, get the menu for restaurant ID R123, paying particular attention to the pizza category. After reviewing the menu, add item I456 (Margherita Pizza) to the cart for user Mary Jones with quantity 2 and extra cheese customization.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Mary Jones' area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "pizza"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U178", "restaurant_id": "R123", "item_id": "I456", "quantity": 2, "customizations": "extra cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U125",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are cautious, flexible, direct. First, search for Mexican restaurants in Jennifer's area with a price range of medium to identify potential options for her dinner plans. Once you have identified a suitable restaurant, specifically restaurant R456, get the restaurant menu to view available tacos. This will allow you to ensure that the menu includes the desired options before proceeding with any orders.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U093",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are confident, optimistic. Get the menu for restaurant ID R123 to explore available Italian dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U170",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are patient, flexible, independent. First, search for restaurants offering Mexican cuisine in San Francisco with a price range of $10-$30 to find potential dining options. Once you have identified a suitable restaurant, get the menu for restaurant ID R200 to view available Mexican dishes and ensure they meet your preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R200"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U055",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are independent, patient. First, search for Chinese restaurants in San Francisco with a moderate price range of $$. Once you find a suitable restaurant, retrieve the main course menu from the restaurant with ID R5678. After reviewing the options, add your chosen item with ID I8901 to your cart with a quantity of 1, using your user ID U1234.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "main course"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U055", "restaurant_id": "R5678", "item_id": "I8901", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U045",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are independent, direct. First, search for restaurants in San Francisco offering Mexican cuisine within a mid-range price range to find suitable dining options. Once you have identified a restaurant, get the restaurant menu for restaurant ID R567 to explore available items. This will help you decide on the best dishes to order for a team lunch through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are polite, confident, optimistic. First, search for restaurants offering Mexican cuisine in the vicinity of Jennifer's current location to find a suitable dining option. Once you have identified a restaurant of interest, get the menu for restaurant ID R256, focusing on the \"Tacos\" category to explore the available options. After reviewing the menu, add item ID I987 (Chicken Tacos) to the cart for user ID U6303 with a quantity of 3 and include extra guacamole for a delightful meal experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer's current location"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R256", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U019", "restaurant_id": "R256", "item_id": "I987", "quantity": 3, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U075",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are optimistic, organized, polite, flexible. Search for restaurants in downtown that offer Chinese cuisine within a moderate price range.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "downtown", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U077",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are patient, organized, logical, optimistic. Search for Italian restaurants in Linda Garcia's location with a moderate price range",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U077"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda Garcia's location", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are polite, cautious. First, search for Italian restaurants in the downtown area with a price range of $$. Once you find a suitable restaurant, get the restaurant menu for restaurant R567 focusing on pasta dishes. After reviewing the menu, add item I890 (Spaghetti Carbonara) to cart for user Patricia Jones (patricia.jones3517@email.com) with quantity 1.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U124", "restaurant_id": "R567", "item_id": "I890", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U045",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are patient, organized. Search for Italian restaurants in the 94102 area with a price range of $$",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "94102", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are flexible, independent, direct, cautious. Get the menu for restaurant ID R1023, focusing on the pasta category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U178",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are independent, optimistic. First, search for restaurants with American cuisine in the San Francisco area within a medium price range to find a suitable dining option. Next, get the menu for restaurant ID R456 to find available burgers and sides, ensuring they meet your preferences. Finally, create an order for user ID U101 at restaurant ID R456 with items [I789, I790], delivery address \"123 Main St, San Francisco, CA\", and payment method \"credit card\" to complete your meal delivery through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "American", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U178", "restaurant_id": "R456", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U163",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are organized, cautious, flexible. First, search for Italian restaurants in the downtown area with a price range of $10-$20 to find a suitable dining option. Once you have identified a restaurant, get the restaurant menu for restaurant ID R5678 to explore available pasta dishes. After reviewing the menu, add item I234 (Spaghetti Carbonara) to cart for user U3607 with quantity 1 and no customizations.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U163", "restaurant_id": "R5678", "item_id": "I234", "quantity": 1, "customizations": null}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U187",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are logical, direct, polite, optimistic. First, search for Italian restaurants in the San Francisco area with a moderate price range to find a suitable dining option for our upcoming team lunch. Once you identify a restaurant that matches our criteria, get the menu for restaurant ID R245, focusing on the pasta category, to explore potential dish options that could be added to our order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R245", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are patient, direct, organized, cautious. First, search for Mexican restaurants in the San Francisco area with a price range of $$ to $$$ to identify potential partners for a new promotional campaign. Next, get restaurant details for restaurant ID R2345 to verify opening hours and delivery zone, ensuring it aligns with our campaign's delivery parameters. Finally, get the restaurant menu for restaurant ID R2345 to check available taco items, as we plan to feature a taco promotion.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are cautious, direct. Search for restaurants offering Mexican cuisine near Mary Miller's location within a moderate price range, and once you identify a potential option, get details for restaurant R542 to verify if it is open and meets minimum order requirements. This will help ensure that Mary can enjoy a satisfying meal delivered through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Mary Miller's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R542"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U118",
        instruction="Your name is Michael Smith and your email is michael.smith2502@email.com. You are organized, logical. First, search for restaurants offering Mexican cuisine in the Chicago area with a price range of $10-$20 to identify potential options for a customer interested in affordable dining. Next, get restaurant details for restaurant ID R245 to verify opening hours and delivery zones, ensuring that the restaurant can deliver to the customer's location at the desired time. Finally, get the restaurant menu for restaurant ID R245 to view available items in the Tacos category, focusing on adding item I567 (Chicken Tacos) to the cart for user U1001 with quantity 3 and extra cheese customization, as the customer has expressed a specific preference for this dish.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Chicago", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R245"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R245", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U118", "restaurant_id": "R245", "item_id": "I567", "quantity": 3, "customizations": "extra cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are direct, patient. First, search for restaurants in Patricia Jones's area that serve Chinese cuisine within a moderate price range. Once you have identified a suitable restaurant, get detailed information for restaurant R4521 to check its hours and delivery zones to ensure it meets Patricia's needs.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "Patricia Jones", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R4521"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U037",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are direct, confident, patient, independent. Search for Italian restaurants in the San Francisco area with a price range of $$. Once you have identified a suitable restaurant, get the menu for restaurant R234 focusing on the pasta category. After reviewing the menu, create an order for user U123 at restaurant R234 with items I567 (Spaghetti Carbonara) and I890, including delivery address 123 Market St, and use a credit card for payment.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U037", "restaurant_id": "R234", "items": [{"item_id": "I567", "quantity": 1}, {"item_id": "I890", "quantity": 1}], "delivery_address": "123 Market St", "payment_method": "credit_card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U046",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9197@email.com. You are flexible, direct. Search for Indian restaurants in San Francisco with a price range of $$ to identify potential new partners for DoorDash. Once you have a list, get restaurant details for restaurant ID R2345 to evaluate its suitability for collaboration.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Indian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U187",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are optimistic, logical. Get the menu for restaurant_id \"R2023\".",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is Mary Williams and your email is mary.williams2739@email.com. You are optimistic, confident, organized. Search for restaurants in the Chicago area with a price range of $$ to $$$ and offering Mexican cuisine. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R1023 to find available items in the \"Tacos\" category. This will help you identify the best options to recommend to customers who are looking for authentic Mexican tacos through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Chicago", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are confident, patient, logical. First, search for restaurants in San Francisco with cuisine type 'Mexican' and price range '$$' to find a suitable dining option. Once you have identified a potential restaurant, get restaurant details for restaurant ID R001 to verify its operational hours, ensuring it is open for service. After confirming the restaurant's availability, get the menu for restaurant ID R001 to check available items in the 'Tacos' category. With this information, proceed to create an order for user ID U9426 at restaurant ID R001 with items [I1001] and delivery address '123 Market St, San Francisco, CA', ensuring a smooth and timely delivery experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Tacos"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U095", "restaurant_id": "R001", "items": [{"item_id": "I1001", "quantity": 1}], "delivery_address": "123 Market St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U045",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are direct, patient, organized. First, search for American cuisine restaurants in New York City with a price range of $$. Once you have identified potential options, get detailed information for restaurant R1023 to check its operating hours and delivery zone. This will help ensure that the restaurant is open and able to deliver to the desired location before proceeding with any orders.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "American", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are logical, confident, organized, patient. Get the menu for restaurant ID R101, focusing on the pasta category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U081",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are polite, organized. Get the menu for restaurant R789, focusing on the \"Tacos\" category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R789", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are optimistic, direct, logical, flexible. Search for restaurants offering Mexican cuisine in the location of Jennifer's last order delivery address to ensure a variety of options are available for her next meal. Once you have identified a suitable restaurant, get the menu for restaurant R567 to explore available vegetarian options, focusing on dishes that might appeal to Jennifer's dietary preferences.",
        actions=[
            Action(
                name="get_user_order_history",
                kwargs={"user_id": "U076", "limit": 1}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer's last order delivery address"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "vegetarian"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are logical, flexible, polite. First, search for restaurants offering Mexican cuisine in the downtown area with a price range of $10-$20 to find potential dining options. Once you have identified a restaurant, get the menu for restaurant R234 to explore available items and decide on your order. Finally, create an order for user U101 at restaurant R234 with items [I567, I568] and delivery address 123 Main St, ensuring the selection meets the desired preferences and delivery requirements.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U167", "restaurant_id": "R234", "items": [{"item_id": "I567", "quantity": 1}, {"item_id": "I568", "quantity": 1}], "delivery_address": "123 Main St"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is Mary Brown and your email is mary.brown1791@email.com. You are cautious, confident, polite, direct. Search for restaurants in Linda's area with a preference for Mexican cuisine and moderate price range.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda's area", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U105",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are organized, logical, patient, direct. First, search for Italian restaurants in the downtown area with a price range of $$. Once you have identified a suitable restaurant, get the menu for restaurant R101 to find available pasta dishes. This will help us determine the best options for our DoorDash customers looking for Italian cuisine.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U110",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are cautious, independent, flexible. First, search for Mexican restaurants in the Los Angeles area within a moderate price range to find a suitable place for a casual dinner. Once you have a list, get restaurant details for restaurant ID R5678 to confirm opening hours, ensuring it fits your schedule. After confirming the restaurant is open, get the restaurant menu for restaurant ID R5678, focusing on the Tacos category, to explore your options. Finally, add item I234 (Chicken Tacos) to cart for user ID U1234 with quantity 3 and extra guacamole, preparing for a convenient and delicious meal delivery through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Los Angeles", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U110", "restaurant_id": "R5678", "item_id": "I234", "quantity": 3, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Robert Williams and your email is robert.williams9426@email.com. You are optimistic, organized, confident. First, search for restaurants in the downtown area with a price range of \"$$\" and cuisine \"Mexican\" to identify potential dining options. Once you find a suitable restaurant, get the restaurant details for restaurant_id R1023 to verify the hours of operation and delivery zone, ensuring it fits within your schedule and location. Finally, create an order for user_id U314 with restaurant_id R1023, including items M456 and delivery address \"123 Main St\" to enjoy a delicious Mexican meal delivered to your doorstep.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U167", "restaurant_id": "R1023", "items": [{"item_id": "M456", "quantity": 1}], "delivery_address": "123 Main St"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U190",
        instruction="Your name is Patricia Miller and your email is patricia.miller3271@email.com. You are organized, confident, flexible. First, search for Italian restaurants in the Chicago area with a price range of $10-$20 to find a suitable dining option for a budget-conscious client meeting. Once you have identified a restaurant, get the restaurant menu for restaurant ID R101 with the category \"Pasta\" to ensure they have a variety of options available. After confirming the menu, add item ID I789 (Spaghetti Carbonara) to the cart for user ID U5151 from restaurant ID R101 with quantity 1, as this is a popular choice for the meeting.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Chicago", "price_range": "$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U190", "restaurant_id": "R101", "item_id": "I789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are direct, polite, flexible, cautious. Search for Italian restaurants in Linda Williams' area with a moderate price range.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U175"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda Williams' area", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are patient, cautious, optimistic. First, search for restaurants offering Mexican cuisine in the 90210 ZIP code area with a price range of $$ to $$$, focusing on finding a place with a good reputation for tacos. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R23456, specifically looking at the Tacos category. This will help in deciding if the offerings meet your preferences before proceeding with any orders.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "90210", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R23456", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are patient, logical. First, search for restaurants offering Mexican cuisine in John's location with a price range of $10-$30 to find suitable dining options. Once you identify a restaurant, get restaurant details for restaurant ID R5678 to check their operating hours and delivery zones to ensure they can deliver to your area. Next, get the restaurant menu for restaurant ID R5678 focusing on the 'Tacos' category to explore available taco options. Finally, add item I890 (Chicken Tacos) to cart for user ID U6337 with quantity 3 and extra cheese customization to complete your order preparation on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U030", "restaurant_id": "R5678", "item_id": "I890", "quantity": 3, "customizations": "extra cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are logical, confident, polite, independent. First, search for Mexican restaurants in the San Francisco area with a price range of $$ to $$$ to identify potential dining options for a new promotional campaign. Once you have identified a suitable restaurant, get the menu for restaurant ID R789, focusing on the \"Tacos\" category, to ensure the menu aligns with the campaign's theme and offers a variety of appealing options for customers.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R789", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U081",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are direct, patient, independent, polite. First, search for restaurants in the New York area offering vegan cuisine with a price range of $10-$20. Once you identify a suitable restaurant, get the restaurant menu for restaurant_id R5678 to check available vegan options. This will help ensure that the menu items align with the customer's dietary preferences before proceeding with any order placements.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "vegan", "location": "New York", "price_range": "$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U055",
        instruction="Your name is Jennifer Garcia and your email is jennifer.garcia3233@email.com. You are confident, organized, direct, independent. search_restaurants(location=\"San Francisco\", cuisine=\"Italian\", price_range=\"$$\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"location": "San Francisco", "cuisine": "Italian", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U050",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are organized, polite. First, search for Italian restaurants in San Francisco with a price range between $10 and $30 to find suitable dining options for our upcoming team lunch. Once you have identified a restaurant, specifically look for the restaurant menu for restaurant ID R1024, focusing on the pasta category, to ensure they offer a variety of pasta dishes that meet our preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1024", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U190",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are independent, direct, flexible. First, search for Italian restaurants in downtown San Francisco with a price range of $10-$30 to find a suitable dining option. Once you identify a restaurant that fits your criteria, get the restaurant menu for restaurant ID R5678 to explore available pasta dishes, ensuring they offer a variety of options that align with your taste preferences. This will help you make an informed decision on where to order your next meal through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U138",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are optimistic, cautious. Search for restaurants with Mexican cuisine in the downtown area with a mid-range price category. Once you find a suitable option, get the menu for restaurant ID R2345 to view available items, ensuring they have your favorite dishes before considering placing an order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U163",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are confident, organized, direct, logical. Create order for user ID U3607 at restaurant ID R2001 with items [I345, I678], delivery address 123 Maple St, and payment method as credit card.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2001"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R2001", "item_id": "I345"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R2001", "item_id": "I678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U163", "restaurant_id": "R2001", "items": [{"item_id": "I345", "quantity": 1}, {"item_id": "I678", "quantity": 1}], "delivery_address": "123 Maple St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is Mary Williams and your email is mary.williams2739@email.com. You are direct, logical. First, search for Mexican restaurants in the San Francisco area with a price range of $$. Once you have identified a suitable option, get the restaurant details for restaurant ID R234 to confirm it is open and meets order requirements. This will ensure that you can proceed with placing an order for a customer on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U105",
        instruction="Your name is Linda Miller and your email is linda.miller5151@email.com. You are polite, direct, optimistic. First, search for restaurants in Jennifer's location offering Mexican cuisine and priced moderately. Once you have identified a suitable option, get detailed information for restaurant R567 to verify its opening hours and delivery zone. After confirming that restaurant R567 can deliver to Jennifer's address, get the menu for restaurant R567, focusing on the \"Tacos\" category, to assist Jennifer in making an informed choice for her meal.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U105"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown2003@email.com. You are direct, organized, independent. First, add item I6790 (Churros) to the cart for user Linda Brown with a quantity of 2. Then, update the existing order O5678 to include the newly added churros. Ensure that the order reflects this addition accurately for seamless processing at restaurant R2345.",
        actions=[
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U104", "restaurant_id": "R2345", "item_id": "I6790", "quantity": 2}
            ),
            Action(
                name="update_order",
                kwargs={"order_id": "O5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U002",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are organized, confident, direct, independent. First, search for Italian restaurants in San Francisco with a price range of $$. Once you have identified potential options, get restaurant details for restaurant ID R1023 to verify opening hours and location to ensure it fits the delivery schedule. After confirming the restaurant's availability, get the restaurant menu for restaurant ID R1023, focusing on the 'Pasta' category, to select appropriate items for an order. Finally, create an order for user U1418 from restaurant ID R1023 with items [I2345, I2346] and delivery address \"123 Main St, San Francisco, CA\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U002", "restaurant_id": "R1023", "items": [{"item_id": "I2345", "quantity": 1}, {"item_id": "I2346", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is John Brown and your email is john.brown5124@email.com. You are patient, optimistic. Create order for user Jennifer Garcia at restaurant R5678 with items [I345: Chicken Taco, quantity: 3] and delivery address 123 Main St, payment method credit card.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U042", "restaurant_id": "R5678", "items": [{"item_id": "I345", "quantity": 3}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U123",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are polite, flexible, direct. Create order for user Jennifer Miller with restaurant ID R102, including items I202 and I203, using default delivery address and credit card payment.",
        actions=[
            Action(
                name="create_order",
                kwargs={"user_id": "U123", "restaurant_id": "R102", "items": [{"item_id": "I202", "quantity": 1}, {"item_id": "I203", "quantity": 1}], "delivery_address": null, "payment_method": null}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are organized, direct, flexible, logical. First, search for Mexican restaurants in San Francisco within the mid-price range to find a suitable dining option. Once you have identified a promising restaurant, retrieve detailed information about it using its restaurant ID. After confirming that the restaurant meets your expectations, proceed to explore their menu, specifically focusing on the Main Dishes category. If a dish catches your interest, add it to your cart, specifying the quantity you wish to order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Main Dishes"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U049", "restaurant_id": "R001", "item_id": "I001", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U134",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are polite, flexible. Create order for user robert.brown1066@email.com with restaurant ID R987, including items I321 and I322, and specify delivery address as 123 Market St, San Francisco, CA.",
        actions=[
            Action(
                name="create_order",
                kwargs={"user_id": "U134", "restaurant_id": "R987", "items": [{"item_id": "I321", "quantity": 1}, {"item_id": "I322", "quantity": 1}], "delivery_address": "123 Market St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are direct, organized, independent. First, search for restaurants with cuisine \"Mexican\" in the location \"San Francisco\" within the price range \"$$\". Once you have identified a suitable restaurant, get the menu for restaurant with ID \"R102\" to explore available Mexican dishes. This will help you decide which items to order for user with ID \"U8314\". Then, create an order at restaurant ID \"R102\" with items [(I205, 3), (I207, 1)], ensuring delivery to \"123 Main St, Apt 4B\" using the payment method \"credit_card\". Remember to include the special instructions \"Leave at door\" to ensure a smooth delivery experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U180", "restaurant_id": "R102", "items": [{"item_id": "I205", "quantity": 3}, {"item_id": "I207", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "credit_card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are organized, patient. Get the restaurant menu for restaurant R987 to explore available Italian dishes",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are patient, organized, logical. First, search for Mexican restaurants in Los Angeles with a price range of $10-$20 to find suitable dining options. Once you have identified a restaurant, get the menu for restaurant R5678 to review their offerings. This will help you make an informed decision for placing an order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Los Angeles", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are logical, polite. First, get the restaurant menu for restaurant R2456, focusing on the pasta category, to ensure that all available options are considered for the order. Then, add item I789 (Spaghetti Carbonara) to the cart for user U3517 with quantity 1 and no customizations. This will help in confirming the availability of the item and preparing to create an order for user U3517 at restaurant R2456, ensuring a smooth and efficient ordering process through DoorDash.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2456", "category": "pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U124", "restaurant_id": "R2456", "item_id": "I789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U020",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are flexible, patient. First, search for Italian restaurants in the San Francisco area with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a potential restaurant, get restaurant details for restaurant ID R5678 to ensure it meets your preferences. After confirming the restaurant's suitability, create an order for user ID U1122 with restaurant ID R5678, including items [I910] and delivery address \"123 Main St, San Francisco, CA\", using credit card payment.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U020", "restaurant_id": "R5678", "items": [{"item_id": "I910", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U016",
        instruction="Your name is John Garcia and your email is john.garcia7961@email.com. You are independent, optimistic, polite, direct. Get the menu for restaurant R10234 using get_restaurant_menu to view available items.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R10234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U075",
        instruction="Your name is Mary Jones and your email is mary.jones4200@email.com. You are polite, patient. Get the restaurant menu for restaurant ID R123 to view available pasta dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U046",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are optimistic, logical. Create an order for user Patricia Williams using restaurant ID R234, including items I345, with delivery address 123 Main Street, payment method as credit card, and special instructions to leave at the door.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R234", "item_id": "I345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U046", "restaurant_id": "R234", "items": [{"item_id": "I345", "quantity": 1}], "delivery_address": "123 Main Street", "payment_method": "credit card", "special_instructions": "leave at the door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is Mary Miller and your email is mary.miller1688@email.com. You are flexible, patient, direct, optimistic. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to find a suitable option for a new partnership. Once you identify a potential restaurant, get the restaurant details for restaurant ID R234 to verify hours and delivery zone, ensuring it aligns with our service area. Finally, create an order for user ID U3192 with restaurant ID R234, including items [I567, I568], delivery address \"123 Main St, Apt 4B\", and payment method \"Credit Card\" to test the ordering process and ensure seamless delivery integration.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U090", "restaurant_id": "R234", "items": [{"item_id": "I567", "quantity": 1}, {"item_id": "I568", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U077",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are direct, patient, cautious, flexible. First, search for Mexican restaurants in Linda Garcia's location with a price range of moderate to identify potential options for her dining preferences. Then, get details for restaurant R205 to check Linda's preferred menu items and operating hours, ensuring it aligns with her taste and schedule.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U077"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Garcia's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R205"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R205"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are cautious, confident, patient, direct. Create order for user Linda Garcia with restaurant ID R567 and items [I890, I891] using her default delivery address and credit card",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U106"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U106", "restaurant_id": "R567", "items": [{"item_id": "I890", "quantity": 1}, {"item_id": "I891", "quantity": 1}], "delivery_address": "default", "payment_method": "default"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are organized, confident. Get restaurant menu for restaurant ID R1010, focusing on the pasta category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1010", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U075",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are polite, optimistic. First, search for restaurants in San Francisco with a focus on Mexican cuisine and a price range of $10-$20 to find a suitable option for a casual dining experience. Once you have identified a restaurant, get the menu for restaurant ID R5678 to check available items in the \"Tacos\" category, ensuring they offer a variety of options. After confirming the menu meets your preferences, add item ID I345 (Chicken Taco) to the cart for user ID U2502 with a quantity of 3 and customize with extra guacamole. Finally, create an order for user ID U2502 at restaurant ID R5678 with the selected items and set the delivery address to \"123 Main St, San Francisco,\" ensuring a seamless and satisfying dining experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U075", "restaurant_id": "R5678", "item_id": "I345", "quantity": 3, "customizations": "extra guacamole"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U075", "restaurant_id": "R5678", "items": [{"item_id": "I345", "quantity": 3}], "delivery_address": "123 Main St, San Francisco"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are logical, patient, confident, flexible. First, search for restaurants offering Mexican cuisine in Michael Johnson's location with a price range of $10-$20 to find suitable dining options. Once you have identified a restaurant, get the restaurant menu for restaurant ID R1023 to view available items. This will help you determine if the restaurant offers the desired Mexican dishes, such as Chicken Tacos, which can be added to the cart if available.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Michael Johnson's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U176",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are organized, cautious. First, search for restaurants offering vegan options in the San Francisco area with a price range of $10-$20. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R1023 to find available vegan items. This will help you ensure the selected restaurant meets the dietary preferences and budget constraints for the task at hand.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "vegan", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is John Garcia and your email is john.garcia7961@email.com. You are patient, confident, flexible, polite. First, search for Italian restaurants located in Downtown with a price range of $$. Once you find a suitable option, get the restaurant details for the restaurant with ID \"R234\" to ensure it meets your expectations. After confirming the restaurant, proceed to create an order using your user ID \"U6303\" from the restaurant with ID \"R234\". Include the items with IDs \"I789\" and \"I790\" in your order, and have them delivered to 123 Main St, Apt 4. Use a Credit Card for payment and add a special instruction to leave the order at the door.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U019", "restaurant_id": "R234", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St, Apt 4", "payment_method": "Credit Card", "special_instructions": "Leave the order at the door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are polite, flexible. Add item I6789 (Tacos Al Pastor) to cart for user Linda Garcia with quantity 3.",
        actions=[
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U106", "restaurant_id": "R001", "item_id": "I6789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U020",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are organized, polite, flexible, independent. Add item 'Tacos' (item_id 'I678') to cart for user 'john.brown7795@email.com' with restaurant_id 'R2345' and quantity 3",
        actions=[
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U020", "restaurant_id": "R2345", "item_id": "I678", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U101",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are polite, organized. First, search for Chinese restaurants in the San Francisco area with a price range of $10-$20 to find potential dining options. Once you have identified a suitable restaurant, proceed to get the restaurant menu for restaurant R250 to review available dishes. This will help you make informed decisions when placing an order for a customer.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R250"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9197@email.com. You are patient, flexible. First, search for vegetarian restaurants in the downtown area with a price range of $10-$20 to explore potential dining options. Once you have identified a suitable restaurant, get the restaurant details for restaurant R102 to check their operating hours and delivery zones to ensure they can deliver to your location. Finally, create an order for user U001 at restaurant R102 with item I205, using delivery address \"123 Main St\" and payment method \"Credit Card\" to complete your meal order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Vegetarian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U112", "restaurant_id": "R102", "items": [{"item_id": "I205", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U075",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are independent, flexible, polite. Cancel order ID O67891 due to restaurant closure, providing reason: \"Restaurant closed unexpectedly.\"",
        actions=[
            Action(
                name="cancel_order",
                kwargs={"order_id": "O67891", "reason": "Restaurant closed unexpectedly"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are cautious, flexible. First, search for restaurants offering Mexican cuisine in the downtown area with a price range of $10-$20 to find suitable dining options. Once you identify a restaurant, get the menu for restaurant ID R234 to browse available Mexican dishes. This will help you decide on your order for a seamless experience on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are direct, flexible, confident. First, search for Italian restaurants in the downtown area with a price range of $$. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R234 to view available Italian dishes. This will help you decide on the best options to offer your customers on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are confident, direct. Search for Italian restaurants in San Francisco with price range $15-$30",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are direct, logical, organized. Get the menu for restaurant R5678 to explore available Chinese cuisine options.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are optimistic, flexible. Search for restaurants offering Mexican cuisine in Patricia Miller's location within a mid-range price.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U177"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Patricia Miller's location", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U050",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson5028@email.com. You are cautious, confident, independent. Get the restaurant menu for restaurant ID R102, focusing on the \"Tacos\" category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are polite, confident, flexible, logical. search_restaurants(cuisine=\"Italian\", location=\"downtown\", price_range=\"medium\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "medium"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U087",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are patient, polite. Get restaurant menu for restaurant ID R2001 with a focus on the 'Pasta' category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2001", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U093",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are patient, logical, independent, confident. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$20. Once you have identified a suitable restaurant, get the menu for restaurant ID R1023 to explore available tacos and burritos. This will help you decide on the best items to create an order for user ID U4200. Ensure the order includes items I345 and I567, with delivery to 123 Main St, San Francisco, and use the payment method as credit card ending in 1234.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U093", "restaurant_id": "R1023", "items": [{"item_id": "I345", "quantity": 1}, {"item_id": "I567", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card ending in 1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are organized, logical. First, search for restaurants in the New York area with a price range of $$ to $$$ and cuisine type \"Mexican\" to find suitable dining options. Once you have identified a restaurant that meets these criteria, such as one with the restaurant ID R5678, proceed to get the restaurant menu to explore available items. This will help you decide on the best dishes to order. After reviewing the menu, create an order for user ID U101 with restaurant ID R5678 including items (Chicken Tacos x3, Guacamole x1) and ensure the delivery address is \"123 Main St, New York, NY\". This process will ensure that the customer receives a satisfying meal from a well-reviewed restaurant within their budget.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "New York", "price_range": "$$,$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U019", "restaurant_id": "R5678", "items": [{"name": "Chicken Tacos", "quantity": 3}, {"name": "Guacamole", "quantity": 1}], "delivery_address": "123 Main St, New York, NY"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are cautious, logical, confident. Create a new order for user mary.miller1688@email.com with restaurant R345, including items from the cart and specifying delivery address as 123 Elm Street, payment via credit card, and no special instructions.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U132", "restaurant_id": "R345", "items": [{"item_id": "I001", "quantity": 2}, {"item_id": "I002", "quantity": 1}], "delivery_address": "123 Elm Street", "payment_method": "credit card", "special_instructions": null}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U093",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are patient, organized. First, search for Italian restaurants in the Brooklyn area with a price range of $$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R456 to review available pasta dishes. This will help you ensure that the options meet the preferences of our customers.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Brooklyn", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is Mary Jones and your email is mary.jones4200@email.com. You are cautious, patient. First, search for Italian restaurants in San Francisco within a medium price range to find suitable dining options. Once you identify a restaurant you are interested in, such as the one with restaurant ID R678, get the restaurant menu focusing on the pasta category to explore their offerings. This will help ensure you select dishes that meet your preferences and budget.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R678", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson5028@email.com. You are confident, independent, patient, flexible. First, search for Italian restaurants in San Francisco with a price range of $$ to $$$ to identify potential new partners for DoorDash. Once you have a list, get restaurant details for restaurant R102 (Luigi's Italian Bistro) to assess its suitability for a partnership, focusing on its location, customer reviews, and popularity.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are independent, confident, logical, optimistic. First, search for Italian restaurants in the San Francisco area with a price range of $10-$30 to identify potential options for a client meeting. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R2345 to review available pasta dishes. This will help you decide if the menu aligns with the preferences of the attendees.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U075",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are polite, cautious, organized, confident. First, search for Italian restaurants in San Francisco within a mid-range price bracket to find potential dining options for a customer. Once you have identified a suitable restaurant, get restaurant details for restaurant ID R2345 to confirm hours of operation. This will ensure the restaurant is open and available for placing an order, providing a seamless experience for the customer.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U193",
        instruction="Your name is Michael Smith and your email is michael.smith2502@email.com. You are organized, cautious, direct. First, search for restaurants in the San Francisco area with a price range of $$ to $$$ to find suitable dining options for the upcoming client meeting. Once you identify a potential restaurant, get the menu for restaurant ID R1023 to view available items in the \"Entrees\" category to ensure they meet dietary preferences. Finally, create an order for user ID U1015 with restaurant ID R1023, including items I204 and I305, and deliver to 123 Main St, San Francisco, CA, to finalize the arrangements for the meeting.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Entrees"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U193", "restaurant_id": "R1023", "items": [{"item_id": "I204", "quantity": 1}, {"item_id": "I305", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are optimistic, logical. First, search for Italian restaurants in San Francisco with a price range of $$. Once you have identified a suitable restaurant, create an order for user U5118 at the selected restaurant with item I101, specifying the delivery address as 123 Main St, San Francisco, and use a credit card as the payment method.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U162", "restaurant_id": "R001", "items": [{"item_id": "I101", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are confident, logical, cautious. Search for restaurants in the downtown area with a price range of $$ and offering Mexican cuisine.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are independent, optimistic. First, search for Mexican restaurants in the downtown area within a mid-range price category to find suitable options for a casual lunch meeting. Once you identify restaurant R567 as a potential choice, get details to verify its opening hours and delivery zone to ensure it can accommodate your schedule and location. Finally, get the menu for restaurant R567, focusing on the \"Tacos\" category, and add item I234 (Chicken Tacos) to cart for user U101 with quantity 3 and extra salsa, preparing for a convenient delivery order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U143", "restaurant_id": "R567", "item_id": "I234", "quantity": 3, "customizations": "extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U046",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson5028@email.com. You are organized, cautious. First, search for restaurants in Patricia's area with cuisine 'Mexican' and price range '$$' to find a suitable dining option. Once you have identified a potential restaurant, get the restaurant menu for restaurant ID R5678 to view available items in the 'Tacos' category. This will help you decide on the best items to order for a satisfying meal experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U193",
        instruction="Your name is Robert Brown and your email is robert.brown1066@email.com. You are optimistic, independent, patient, logical. First, search for restaurants with Mexican cuisine in San Francisco with a price range of $$. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R5678 to check their menu options. After reviewing the menu, get the menu for restaurant ID R5678 and filter by category \"Tacos\" to find specific taco options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U142",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are logical, independent. search_restaurants(cuisine=\"Italian\", location=\"downtown\", price_range=\"moderate\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "moderate"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are direct, optimistic, organized, independent. Search for Italian restaurants in the San Francisco area with a price range of $$ and a rating above 4.0. Once you find a suitable restaurant, get the menu for restaurant ID R342 to review available items in the pasta category. This will help you recommend the best pasta options to our users and ensure a delightful dining experience with DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R342"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R342", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are optimistic, logical, cautious. First, search for restaurants with Italian cuisine in New York City with a price range of $10-$30 to find a suitable dining option. Once you identify a potential restaurant, get the menu for restaurant ID R2345 to find available pasta dishes. After confirming the menu includes your desired pasta dish, add item I5678 (Spaghetti Carbonara) to the cart for user ID U101 with quantity 1 and no customizations.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U098", "restaurant_id": "R2345", "item_id": "I5678", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson5028@email.com. You are independent, polite, cautious, confident. Search for restaurants in the midtown area offering Mexican cuisine within the price range of $10-$20. Once you find a suitable restaurant, get the menu for restaurant R567, focusing on the Tacos category. This will help you decide if the restaurant offers the variety of tacos you are interested in.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "midtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are direct, logical. First, search for restaurants in Patricia's location with a cuisine preference for 'Italian' and a price range of '$$' to find suitable dining options. Once you have the list, get the restaurant details for the restaurant ID 'R001' to confirm its hours of operation and delivery zones, ensuring it meets Patricia's needs. Finally, create an order for user Patricia Miller (U001) with restaurant ID 'R001', including items I101 and I102, with the delivery address '123 Main St', and use the payment method 'Credit Card' to complete the transaction efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Patricia's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U177", "restaurant_id": "R001", "items": [{"item_id": "I101", "quantity": 1}, {"item_id": "I102", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown2003@email.com. You are cautious, direct, logical. Get the restaurant menu for restaurant ID R5678 to view available items.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U087",
        instruction="Your name is Michael Smith and your email is michael.smith2502@email.com. You are cautious, logical. Start by searching for Italian restaurants in the San Francisco area with a price range of $$ to $$$ to explore dining options. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R5678 to check its hours and delivery zones, ensuring it fits your schedule and location. After confirming the restaurant's suitability, get the menu for restaurant ID R5678 to find available pasta dishes. If Spaghetti Carbonara is available and appealing, add item ID I2345 (Spaghetti Carbonara) to the cart for user ID U101 with quantity 1, preparing for a seamless order placement on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U087", "restaurant_id": "R5678", "item_id": "I2345", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are optimistic, independent, organized. First, search for restaurants offering Mexican cuisine in the downtown area with a price range of $10-$20. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R202 to explore available items. This will help you decide what to order for a team lunch through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R202"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are confident, flexible. First, search for Italian restaurants in the San Francisco area with a price range of $$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R1024 to view available pasta dishes. This will help you decide on the best options for placing an order for a client through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1024", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is Patricia Jones and your email is patricia.jones4973@email.com. You are independent, optimistic. Get the restaurant menu for restaurant ID R2345 to explore available tacos",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Patricia Miller and your email is patricia.miller3271@email.com. You are patient, organized, confident. First, search for restaurants with Mexican cuisine in Patricia's area with a price range of $$-$$$. Once you have found restaurant R567, a popular Mexican restaurant, get the restaurant details to confirm its suitability. Then, proceed to get the restaurant menu for restaurant R567, focusing on the \"Tacos\" category. Finally, add item I789 (Chicken Tacos) to cart for user Patricia Jones with quantity 3 and extra guacamole.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U192", "restaurant_id": "R567", "item_id": "I789", "quantity": 3, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U170",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are independent, organized, direct. First, search for Mexican restaurants in the San Francisco area with a price range of $$. Once you have identified restaurant R2458, get the restaurant details to confirm their operating hours. After confirming the restaurant is open, proceed to create an order for user james.johnson8780@email.com with restaurant R2458, including items I789 and I790, to be delivered to 123 Main St using a credit card as the payment method.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2458"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U170", "restaurant_id": "R2458", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U101",
        instruction="Your name is Patricia Jones and your email is patricia.jones4973@email.com. You are direct, polite, logical, organized. First, search for Chinese restaurants in the San Francisco area with a price range of $$. Once you have identified a suitable restaurant, get the menu for restaurant R1023 to view available dishes. This will help you decide on the best options to recommend to the user.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U101",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are logical, patient, direct. First, search for restaurants serving Mexican cuisine in the downtown area with a price range of $10-$20 to find suitable dining options for a potential order. Once you have identified a restaurant, get the restaurant menu for restaurant ID R5678 to explore available Mexican dishes and ensure they meet your preferences. This will allow you to make an informed decision for placing an order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is Jennifer Garcia and your email is jennifer.garcia3233@email.com. You are direct, cautious. First, search for Mexican restaurants in San Francisco with a price range of $$ to find potential dining options. Once you identify a restaurant, get the restaurant menu for restaurant R2345 in the category of \"Tacos\" to explore their offerings. This will help you decide on the best options to recommend for a Doordash promotion.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U110",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are logical, optimistic, confident. First, search for Italian restaurants in San Francisco with a price range of $$. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R2345 to check the availability of Fettuccine Alfredo. If Fettuccine Alfredo is available, add item I6789 to the cart for user ID U1234 with quantity 1.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U110", "restaurant_id": "R2345", "item_id": "I6789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are direct, logical, confident. First, search for Mexican restaurants in the San Francisco area with a price range of $$. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R2345 to check opening hours and delivery zones, ensuring it fits the customer's needs. Finally, create an order for user ID U1122 at restaurant ID R2345 with items I6789 and set the delivery address to 123 Main St. This sequence ensures that the customer has a variety of options, confirms the restaurant's availability, and completes the order efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U042", "restaurant_id": "R2345", "items": [{"item_id": "I6789", "quantity": 1}], "delivery_address": "123 Main St"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are optimistic, direct, organized. Search for restaurants in John's area with cuisine type \"Mexican\" and price range \"$$\". Once you have identified a potential restaurant, get the restaurant menu for restaurant ID R987 to choose potential items for order. This will help ensure that the options align with John's preferences and facilitate a smooth ordering process through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are polite, flexible, logical, patient. First, search for restaurants offering Mexican cuisine in the San Francisco area with a moderate price range to find potential options for our delivery service. Once you identify a suitable restaurant, get the restaurant details for restaurant R2345 to confirm its operational hours and delivery zone, ensuring it aligns with our delivery capabilities. After confirming the restaurant's operational details, create an order for user U9904 with restaurant_id R2345, including items I5678 and I6789, with the delivery address \"123 Main St, San Francisco, CA\" and payment method \"credit_card,\" ensuring a seamless ordering experience for the customer.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U048", "restaurant_id": "R2345", "items": [{"item_id": "I5678", "quantity": 1}, {"item_id": "I6789", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA", "payment_method": "credit_card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are optimistic, direct, patient. First, search for Italian restaurants in the vicinity of San Francisco with a price range of medium to identify potential dining options. Once you have a list, get restaurant details for restaurant R5678 to verify its opening hours and delivery areas, ensuring it fits your schedule and location. After confirming this restaurant is suitable, get the menu for restaurant R5678 to find available items in the pasta category, focusing on options that meet your preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U105",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are cautious, polite. Get the menu for restaurant R567 to explore available taco options.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U075",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are patient, logical, flexible, confident. First, search for restaurants with Mexican cuisine in San Francisco with a price range of $$. Once you have identified a suitable restaurant, get the menu for restaurant R5678 and look for the availability of Chicken Tacos. If Chicken Tacos are available, proceed to add item I2345 (Chicken Tacos) to the cart for user U1234 with quantity 2 and extra salsa.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U075", "restaurant_id": "R5678", "item_id": "I2345", "quantity": 2, "customizations": "extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are confident, logical, organized, polite. Create an order for user linda.garcia5307@email.com at restaurant ID R2345 with items [I9876] and delivery address 1234 Market St, Apt 5.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R2345", "item_id": "I9876"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U106", "restaurant_id": "R2345", "items": [{"item_id": "I9876", "quantity": 1}], "delivery_address": "1234 Market St, Apt 5"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U190",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are cautious, patient, independent, optimistic. First, search for restaurants offering Italian cuisine in Linda Miller's area within a moderate price range to find suitable dining options. Next, get the menu for restaurant ID R1023 to find available pasta dishes, ensuring the selection matches your preferences. Finally, create an order for user ID U5151 with restaurant ID R1023, including items I250 and I251, for delivery to 123 Maple St, using the credit card ending in 1234.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda Miller's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U190", "restaurant_id": "R1023", "items": [{"item_id": "I250", "quantity": 1}, {"item_id": "I251", "quantity": 1}], "delivery_address": "123 Maple St", "payment_method": "credit card ending in 1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are polite, flexible. Get the restaurant menu for restaurant ID R2345, focusing on the 'Tacos' category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are confident, independent, direct. Get the menu for restaurant R101, focusing on the pasta category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are logical, direct, confident. First, search for restaurants with Mexican cuisine in San Francisco with a price range of $$. Once you identify a suitable restaurant, get the menu for restaurant R202, focusing on the 'Tacos' category. This will help you ensure that the restaurant offers a variety of taco options before proceeding with placing an order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R202", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is Jennifer Garcia and your email is jennifer.garcia3233@email.com. You are optimistic, direct, patient, independent. Get restaurant menu for restaurant ID R987 to find available pasta dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are confident, logical. First, search for restaurants specializing in Mexican cuisine near Patricia's location to identify potential options for her dinner plans. Once you have a list, get details for restaurant R245 to check if it's open and meets minimum order requirements, ensuring it is a viable choice for a DoorDash order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Patricia's location"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R245"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams7359@email.com. You are direct, optimistic, independent, organized. search_restaurants(cuisine=\"Italian\", location=\"San Francisco\", price_range=\"$$\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are cautious, optimistic, organized. Get the menu for restaurant R5678 to check available items in the Tacos category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U020",
        instruction="Your name is Michael Smith and your email is michael.smith2502@email.com. You are organized, polite, flexible, independent. Get restaurant menu for restaurant ID R101 to explore available pasta dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U125",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are logical, polite. First, search for restaurants offering Mexican cuisine in the downtown area with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a promising restaurant, get the restaurant details for restaurant ID R234 to verify their hours and delivery zones, ensuring they can deliver to your location. Finally, create an order for user ID U101 with restaurant ID R234, including items I678 and I679, and set the delivery address to 123 Main St, Apt 4B, using the credit card ending in 5678 for payment.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U125", "restaurant_id": "R234", "items": [{"item_id": "I678", "quantity": 1}, {"item_id": "I679", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "credit_card_5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams7359@email.com. You are flexible, logical, optimistic. First, search for Mexican restaurants in San Francisco within the price range of $$. After identifying a suitable restaurant, retrieve the menu of the restaurant with the ID 'R101' to explore the available options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are optimistic, independent, polite, logical. Search for restaurants offering Mexican cuisine in the Brooklyn area with a moderate price range. Once you find a suitable restaurant, create an order for user ID U1001 with the selected restaurant's ID, including items: Chicken Taco x3, delivery to 123 Main St, using credit card payment, with special instructions: \"Extra salsa.\"",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Brooklyn", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U180", "restaurant_id": "R001", "items": [{"item_id": "I123", "quantity": 3}], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "Extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown2003@email.com. You are confident, patient, direct, logical. First, search for restaurants in the Midtown area offering Asian cuisine with a price range of $10-$20 to find suitable options for a client meeting. Once you have identified a restaurant, get the menu for restaurant R23456 to check available appetizers and ensure they have a good selection. Finally, create an order for user U1610 at restaurant R23456 with items I98765 and I87654, ensuring the delivery address is 123 Main St and the payment method is credit card, to finalize the lunch arrangements for the meeting.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Asian", "location": "Midtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R23456", "category": "Appetizers"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U175", "restaurant_id": "R23456", "items": [{"item_id": "I98765", "quantity": 1}, {"item_id": "I87654", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are independent, optimistic. First, search for Mexican restaurants in the San Francisco area with a price range of moderate to find suitable dining options. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R5678 to check their operating hours and delivery zones, ensuring they can deliver to your area. Finally, create an order for user ID U5307 at restaurant ID R5678 with items [I9012, I3456], delivery address \"123 Main St, San Francisco\", and payment method \"credit card\" to complete your meal planning.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U106", "restaurant_id": "R5678", "items": [{"item_id": "I9012", "quantity": 1}, {"item_id": "I3456", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U020",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown2003@email.com. You are independent, direct, confident. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to identify potential new partners for DoorDash. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R12345, focusing on the pasta category, to evaluate the variety and quality of offerings that could be featured on the platform.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$,$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R12345", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are polite, flexible, cautious. First, search for restaurants with Mexican cuisine in San Francisco within the price range of $10-$30 to find a suitable place for a casual lunch meeting. Once you have identified a restaurant, get the menu for restaurant R234 to explore available items under the Tacos category. This will help you decide if they offer a variety that suits your taste and dietary preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are confident, direct, patient. First, search for restaurants in the downtown area with cuisine \"Italian\" and price range \"$$\" to find potential dining options. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R2345 to ensure it meets your expectations in terms of ambiance and customer reviews. After confirming that this restaurant is a good choice, create an order for user ID U7411 at restaurant ID R2345 with items [I5678, I6789], ensuring the delivery address is \"123 Main St\" and the payment method is \"Credit Card\". This process will help you efficiently manage a seamless dining experience for the customer through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U122", "restaurant_id": "R2345", "items": ["I5678", "I6789"], "delivery_address": "123 Main St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U133",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are optimistic, organized. Search for Italian restaurants in the San Francisco area within a moderate price range.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are logical, optimistic, cautious, confident. Search for restaurants with cuisine \"Mexican\" in Patricia's location with a price range of \"$$\". Once you find a suitable restaurant, get the restaurant menu for restaurant ID R202 to explore available Mexican dishes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Patricia's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R202"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are independent, direct, patient, flexible. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $$ to $$$ to find potential dining options for a client meeting. Next, get restaurant details for restaurant ID R5678 to verify hours of operation and delivery zones to ensure it fits the meeting schedule and location. Finally, create an order for user ID U3192 at restaurant ID R5678 with items I1234 and I5678, delivery address 123 Market St, and payment method as credit card to finalize the arrangements for the meeting.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U090", "restaurant_id": "R5678", "items": [{"item_id": "I1234", "quantity": 1}, {"item_id": "I5678", "quantity": 1}], "delivery_address": "123 Market St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are cautious, confident, logical, polite. Begin by searching for Mexican restaurants in the Boston area with a price range of $10-$20 to identify potential new partners for DoorDash. Once you have identified a promising restaurant, such as one with the ID R1025, proceed to get the restaurant details to check its opening hours. This information will help determine the feasibility of integrating the restaurant into DoorDash's delivery schedule.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Boston", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1025"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U020",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are flexible, polite, optimistic, cautious. Get the menu for restaurant R458 to explore available Italian dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R458"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U123",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are independent, direct, patient. First, search for restaurants serving Mexican cuisine in the 94103 area with a mid-range price to find potential options for a dinner delivery. Once you identify a restaurant, such as restaurant R2345, get the restaurant details to check operational hours and delivery zones to ensure they can deliver to your location. After confirming delivery availability, get the restaurant menu for restaurant R2345 to find available items in the \"Tacos\" category. If Chicken Tacos are available, add item I9876 (Chicken Tacos) to the cart for user U1023 with quantity 3 and no customizations, preparing for a seamless ordering experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "94103", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U123", "restaurant_id": "R2345", "item_id": "I9876", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are cautious, patient. First, search for Mexican restaurants in San Francisco with a moderate price range to find a suitable dining option. Once you have identified a restaurant, get the menu for restaurant R2345 to find available items. This will help you decide on the best meal choices for your upcoming order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U046",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are confident, polite, optimistic, organized. Search for restaurants offering Mexican cuisine in Patricia Williams' local area with a price range of $10-$30.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Patricia Williams' local area", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U187",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are direct, patient. Search for Italian restaurants in Mary Williams's area with a price range of $10-$20.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Mary Williams's area", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U086",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are direct, polite, organized. Begin by searching for sushi restaurants in Linda's area with a moderate price range to find suitable dining options. Once you have identified potential places, focus on getting restaurant details for restaurant ID R102, a sushi place Linda is particularly interested in. After reviewing the restaurant details, retrieve the menu for restaurant ID R102 to explore the available sushi options. This will allow Linda to make an informed decision on what to order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Sushi", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U170",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are flexible, independent, direct, logical. First, search for restaurants offering Mexican cuisine in the Los Angeles area with a price range of $$. Once you identify a suitable restaurant, get the restaurant menu for restaurant ID R234 to explore available taco options. This will help you decide on the best items to include in your order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Los Angeles", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are optimistic, confident, flexible, direct. First, search for restaurants offering Mexican cuisine in the downtown area within a moderate price range to ensure a variety of options for our users. Next, get restaurant details for restaurant R202 to verify it's open and meets minimum order requirements, as this will help in making informed decisions for customer orders. Finally, create an order for user U101 at restaurant R202 with items I789 and I790, ensuring the delivery address is 123 Elm St and the payment method is a credit card, to provide a seamless and efficient service experience for the customer.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R202"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U049", "restaurant_id": "R202", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Elm St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is Jennifer Garcia and your email is jennifer.garcia3233@email.com. You are organized, independent. First, search for restaurants in the downtown area with cuisine \"Mexican\" and price range \"$$\" to find suitable options for a potential order. Once you have identified a restaurant, get the restaurant menu for restaurant ID R102 to check available items. This will help you decide on the best dishes to include in an order for a user.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U061",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are optimistic, cautious, independent. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$20 to find potential options for a new promotional campaign. Next, get the restaurant details for restaurant R987 to check their hours and delivery zone, ensuring it aligns with your marketing strategy. Finally, get the restaurant menu for restaurant R987, focusing on the \"Tacos\" category, to identify popular items that could be featured in the campaign.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R987"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9197@email.com. You are polite, flexible, patient. First, search for restaurants offering Mexican cuisine in the vicinity of 123 Main St with a price range of $$. Once you find a suitable restaurant, get the restaurant menu for restaurant R2345 to view available items in the Tacos category.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "123 Main St", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are flexible, cautious, polite. First, search for restaurants with cuisine \"Mexican\" in the location \"Uptown\" with a price range of \"$$\" to identify potential dining options for our customer. Once you have the list, proceed to get restaurant details for restaurant ID \"R2048\" to confirm menu availability and opening status, ensuring the restaurant can fulfill orders. After confirming availability, add item ID \"I307\" (Chicken Tacos) to cart for user ID \"U6337\" with quantity 2 and extra salsa. If any issues arise, such as menu items being unavailable or the restaurant being closed, promptly notify the customer and suggest alternative options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Uptown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2048"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2048"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U030", "restaurant_id": "R2048", "item_id": "I307", "quantity": 2, "customizations": "extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U133",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are optimistic, patient, flexible, logical. Search for restaurants offering Mexican cuisine in the downtown area with a price range of $10-$20. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R2345 to identify available taco varieties. This will help you make an informed decision for a DoorDash order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U110",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are patient, cautious. First, search for restaurants offering Chinese cuisine in the San Francisco area with a price range of $$. Once you have identified a potential restaurant, such as restaurant R1023, get the menu for this restaurant, focusing on the 'Main Dishes' category. This will help you decide if the offerings meet the preferences of your customers on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Main Dishes"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U163",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are polite, logical, independent, direct. First, search for restaurants offering Chinese cuisine in the Midtown area with a moderate price range to identify potential dining options for delivery. Once you have identified a suitable restaurant, get the menu for restaurant ID R234 to review available dishes and pricing. This will help you decide on the best items to order for user ID U3607, ensuring a satisfying dining experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "Midtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U193",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown2003@email.com. You are confident, independent, cautious. Begin by searching for Italian restaurants in the downtown area with a price range of $$ and above to find a suitable dining option. Once you have identified a restaurant, retrieve the restaurant menu for restaurant ID R123 to identify available pasta dishes. This will help you decide on a delicious pasta dish to order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U178",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are logical, cautious. First, search for restaurants with cuisine \"Mexican\" in the location \"San Francisco\" with a price range of \"$$\". Once you have identified a potential restaurant, get restaurant details for restaurant_id \"R789\" to verify operating hours and delivery zones. This will ensure that the restaurant can deliver to the desired location during the preferred time, which is crucial for coordinating a successful meal delivery through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R789"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are organized, logical, direct. First, search for Italian restaurants located in downtown with a medium price range to find a suitable dining option for a business lunch. Once you have identified a restaurant, proceed to get the restaurant menu focusing on the Pasta category to review available dishes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are cautious, flexible, patient. First, search for Mexican restaurants in San Francisco with a price range of $$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R789 to check available tacos. After confirming the availability of Chicken Tacos, create an order for user ID U456 at restaurant ID R789 with items (I234 - Chicken Tacos) and (I789 - Chocolate Cake), delivery address 123 Main St, payment method credit card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R789"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U140", "restaurant_id": "R789", "items": [{"item_id": "I234", "quantity": 1}, {"item_id": "I789", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U002",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are flexible, logical, polite, patient. First, search for restaurants with Chinese cuisine in the downtown area with a price range of $$. Once you have identified potential options, get restaurant details for restaurant ID R102 to verify its opening hours and delivery zones, ensuring it aligns with the delivery needs. After confirming the restaurant's availability, get the restaurant menu for restaurant ID R102 to explore available items in the 'Main Course' category. This will allow you to create an order for user Patricia Brown with user ID U1418 at restaurant ID R102, including items I305 and I306, with delivery address 123 Main St, Apt 4B, and payment method set to credit card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102", "category": "Main Course"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U002", "restaurant_id": "R102", "items": [{"item_id": "I305", "quantity": 1}, {"item_id": "I306", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are direct, optimistic. First, search for Mexican restaurants in the downtown area with a price range of $$ using the search_restaurants tool to identify potential options for a team lunch. Once you have found a suitable restaurant, get the menu for restaurant R101 to explore available taco options using the get_restaurant_menu tool.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U077",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are confident, polite, cautious, logical. First, search for Mexican restaurants in the San Francisco area with a price range of $$ to $$$ to identify potential new partners for DoorDash. Once you have a list, focus on restaurant R345 to get its operating hours and customer reviews. This will help assess its suitability for collaboration and ensure it meets our quality standards.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are patient, logical, confident, direct. First, search for restaurants offering sushi cuisine in San Francisco within a moderate price range. Once you have identified a suitable restaurant, get the menu for restaurant ID R5678, focusing on the \"Sushi Rolls\" category. After reviewing the menu, add item ID I234 (California Roll) to the cart for user ID U1234 with quantity 3 and no customizations.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Sushi", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Sushi Rolls"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U113", "restaurant_id": "R5678", "item_id": "I234", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U037",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are independent, optimistic, direct, polite. First, search for restaurants offering Mexican cuisine in Linda Davis's area to identify potential options for her meal. Once you have found a suitable restaurant, get the restaurant details for restaurant R456 to check operating hours and delivery zones to ensure they can deliver to Linda's location. After confirming delivery availability, get the menu for restaurant R456 to explore available items under the \"Tacos\" category, and add item I789 (Chicken Taco) to the cart for user U234 (Linda Davis) with a quantity of 3.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Davis"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U037", "restaurant_id": "R456", "item_id": "I789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are optimistic, cautious, organized, direct. Create an order for Linda using restaurant R456, including items I789 and I790, and specify her home address for delivery.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U175"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U175", "restaurant_id": "R456", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "Linda's home address"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U110",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are organized, patient. First, get restaurant details for restaurant R2345 to check their operating hours and delivery zones to ensure they can deliver to your address. Next, get the restaurant menu for restaurant R2345, focusing on the Tacos category, to explore the available options. Finally, add item I5678 (Chicken Tacos) to cart for user U101 (Mary Smith) with quantity 3 and extra salsa, preparing for your order.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U110", "restaurant_id": "R2345", "item_id": "I5678", "quantity": 3, "customizations": "extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Linda Miller and your email is linda.miller5151@email.com. You are patient, cautious. First, search for restaurants in the New York City area offering Chinese cuisine to explore potential dining options. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R987, focusing on the \"Dinner Specials\" category. This will help you decide on the best dishes to order for a delightful dinner experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "New York City"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987", "category": "Dinner Specials"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U007",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are cautious, optimistic, polite. You are planning a dinner for two and want to enjoy some Italian cuisine. First, search_restaurants(cuisine=\"Italian\", location=\"Downtown\", price_range=\"$$\") to find a suitable place. Once you have identified a promising option, get_restaurant_details(restaurant_id=\"R123\") to learn more about the restaurant's ambiance and customer reviews. After confirming it meets your expectations, get_restaurant_menu(restaurant_id=\"R123\", category=\"Pizzas\") to explore their pizza offerings. Finally, add_item_to_cart(user_id=\"U001\", restaurant_id=\"R123\", item_id=\"I456\", quantity=2) to order your favorite pizza for the evening.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R123"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "Pizzas"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U007", "restaurant_id": "R123", "item_id": "I456", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson8206@email.com. You are optimistic, logical, independent, polite. You are planning a dinner for your friends in San Francisco and want to treat them to some delicious Mexican cuisine. First, search for Mexican restaurants in San Francisco within a medium price range to find a suitable place. Once you have identified a restaurant, proceed to get the menu for that restaurant, focusing on the entrees category, to decide which dishes you would like to order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "entrees"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U081",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are organized, logical, independent, flexible. Search for restaurants with Asian cuisine in Jennifer's area (location: San Francisco, price_range: $$)",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Asian", "location": "San Francisco", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U037",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are optimistic, confident, direct. First, search for Italian restaurants in the San Francisco area with a price range of $$. Once you have identified a suitable restaurant, get the menu for restaurant ID R102 to explore available pasta dishes. Finally, create an order for user ID U2351 with restaurant ID R102, including items I301 (Spaghetti Carbonara) and I302, and ensure the delivery address is 123 Main St, San Francisco, CA.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U037", "restaurant_id": "R102", "items": [{"item_id": "I301", "quantity": 1}, {"item_id": "I302", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U125",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are polite, cautious, optimistic. Get restaurant details for restaurant ID R234 (El Camino) to check its hours and ratings.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U016",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are polite, optimistic, logical, organized. First, search for Italian restaurants in the Downtown area with a moderate price range to find a suitable dining option. Once you have identified a restaurant of interest, retrieve the restaurant's details to ensure it meets your expectations in terms of ambiance and customer reviews. After confirming the restaurant's suitability, proceed to get the menu, specifically focusing on the Pasta category, to decide on the dishes you would like to order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are flexible, direct, logical, independent. First, search for American cuisine restaurants in the San Francisco area with a price range of $10-$20 to identify potential new partners for DoorDash. Once you have identified a promising restaurant, get the restaurant details for restaurant ID R102 to check its operation hours and availability. This information will help ensure that the restaurant can meet DoorDash's delivery requirements and provide customers with accurate delivery times.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "American", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are flexible, logical, organized, direct. Search for restaurants offering Chinese cuisine within the delivery zone of User U001 (Michael Williams) located at 123 Main St. Once you have identified a suitable restaurant, get the restaurant menu for restaurant R234 to find available Chinese dishes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "123 Main St"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are independent, confident, logical. get_restaurant_menu(restaurant_id=\"R123\")",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U035",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are independent, cautious, logical. First, search for restaurants in the downtown area with a cuisine preference of Italian and a price range of $$ (moderate). Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R3456 to verify their hours of operation and delivery zones. After confirming that the restaurant is open and delivers to your area, get the menu for restaurant ID R3456, focusing on the pasta category, to decide on your order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R3456"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R3456", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are independent, polite, patient. Add item I5678 (Spaghetti Carbonara) to the cart for user Mary Williams (mary.williams6067@email.com) from restaurant ID R2345 with quantity 2.",
        actions=[
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U112", "restaurant_id": "R2345", "item_id": "I5678", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are independent, organized. First, search for Italian restaurants in San Francisco with a price range of $10-$20 to find a suitable dining option for a budget-conscious client. Once you identify a restaurant, get the menu for restaurant R1023 focusing on the Pizza category to ensure they offer a variety of pizza options that meet the client's preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Pizza"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U007",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are organized, flexible, logical. First, search for Italian restaurants in the New York City area with a price range of $$. Once you identify a suitable restaurant, get the restaurant menu for restaurant ID R101, focusing on pasta dishes. This will help you determine if they offer the Spaghetti Carbonara dish. If available, proceed to add item I202 (Spaghetti Carbonara) to the cart for user U6151 with quantity 1 and no customizations. This task is aimed at ensuring a seamless and efficient ordering process for the user on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U007", "restaurant_id": "R101", "item_id": "I202", "quantity": 1, "customizations": null}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U118",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are direct, cautious, confident. Create an order for user U6714 at restaurant R567 with items I234 and I235, using delivery address 123 Market St and payment method 'Credit Card'.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R567", "item_id": "I234"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R567", "item_id": "I235"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U118", "restaurant_id": "R567", "items": [{"item_id": "I234", "quantity": 1}, {"item_id": "I235", "quantity": 1}], "delivery_address": "123 Market St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are organized, patient, direct. First, search for Italian restaurants in the Brooklyn area with a price range of $$-$$$. Once you have identified potential options, get restaurant details for restaurant ID R5678 to verify its operating hours. This will help ensure that the restaurant is open during peak delivery times, which is crucial for optimizing Doordash's delivery service in the area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Brooklyn", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U134",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are confident, independent, organized, polite. Get the menu for restaurant R567, focusing on the \"Pasta\" category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U193",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are direct, cautious, patient. Get the menu for restaurant R567 to find available items in the \"Tacos\" category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U123",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are confident, cautious, polite, organized. First, search for Italian restaurants in the San Francisco area with a moderate price range to find a suitable dining option. Once you have identified a promising restaurant, such as restaurant R2345, get the restaurant details to check their opening hours and location to ensure they are convenient for a visit. After confirming the restaurant is a good fit, get the restaurant menu for restaurant R2345 to find available pasta dishes. If Spaghetti Carbonara is available, add item I6789 (Spaghetti Carbonara) to cart for user U102 with quantity 1 to complete the order on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U123", "restaurant_id": "R2345", "item_id": "I6789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U123",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are polite, organized, confident. Get restaurant menu for restaurant ID R102 to find available pasta dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are polite, logical. Search for Mexican restaurants in San Francisco with a price range of $$ and identify restaurant R234. Once identified, get the menu for restaurant R234, focusing on the Tacos category. After reviewing the menu, add item I678 (Chicken Tacos) to the cart for user U123 (John Garcia) with a quantity of 3.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U151", "restaurant_id": "R234", "item_id": "I678", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U163",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are flexible, organized, logical, polite. First, search for Italian restaurants in the New York City area with a price range of $$ to $$$. Once you have identified a suitable restaurant, get the menu for restaurant ID R1023, focusing on the Pasta category. After reviewing the menu, create an order for user ID U3607 at restaurant ID R1023 with items I567 and I568. Use the delivery address 123 Main Street, NYC, and select the payment method as credit card. Include the special instructions \"Leave at door\" to ensure a smooth delivery process.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U163", "restaurant_id": "R1023", "items": [{"item_id": "I567", "quantity": 1}, {"item_id": "I568", "quantity": 1}], "delivery_address": "123 Main Street, NYC", "payment_method": "credit card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U142",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are cautious, optimistic. Get the menu for restaurant ID R123 to identify available pasta dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are independent, polite, flexible, direct. Begin by searching for restaurants in San Francisco with cuisine type \"Mexican\" and price range \"$$\" to find suitable dining options for a client. Once you identify a potential restaurant, such as restaurant R2345, proceed to get the menu details, focusing specifically on the \"Tacos\" category to ensure it meets the client's preferences. Finally, add item I6789 (Chicken Taco) to the cart for user Michael Brown, ensuring you select a quantity of 3 with no customizations, to complete his order seamlessly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U180", "restaurant_id": "R2345", "item_id": "I6789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U055",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are direct, patient, cautious. First, search for restaurants offering Mexican cuisine in the San Francisco area with a moderate price range to identify potential dining options for our customers. Once you have identified a suitable restaurant, get the menu for restaurant R001 to find available Mexican dishes. This will help us ensure that we are offering a diverse selection of authentic Mexican dishes to our users.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is Patricia Jones and your email is patricia.jones4973@email.com. You are cautious, patient, organized. First, search for restaurants offering Mexican cuisine in San Francisco within a mid-range price category to find suitable dining options. Once you have identified a potential restaurant, get restaurant details for restaurant ID R2345 to verify operational hours and minimum order requirement to ensure it fits your schedule and budget. After confirming the restaurant meets your criteria, create an order for user ID U1001 at restaurant ID R2345 with items [I987, I543 (Guacamole Dip)] using delivery address \"123 Market St, San Francisco, CA\" and payment method \"Credit Card\" to complete your dining experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U098", "restaurant_id": "R2345", "items": [{"item_id": "I987", "quantity": 1}, {"item_id": "I543", "quantity": 1}], "delivery_address": "123 Market St, San Francisco, CA", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are independent, direct, logical, optimistic. Get the menu for restaurant R456, focusing on the Tacos category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U123",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are logical, patient, cautious. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to find a suitable dining option for a business lunch. Once you have identified a restaurant, get the restaurant menu for restaurant ID R2345, focusing on the pasta category, to ensure they have a variety of pasta dishes available for your guests.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are confident, organized, independent. First, search for Mexican restaurants in the San Francisco area with a price range of $10-$20 to find a suitable dining option for a business lunch. Once you have identified a potential restaurant, retrieve the menu for restaurant R202, focusing on the 'Main Course' category, to ensure they offer a variety of options that meet dietary preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R202", "category": "Main Course"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U101",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are patient, organized, confident. First, search for Italian restaurants in San Francisco within a moderate price range to find a suitable dining option. Once you have identified a restaurant that fits your criteria, retrieve its menu to explore the available dishes. After selecting a dish you would like to order, add it to your cart with a quantity of two.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U101", "restaurant_id": "R001", "item_id": "I001", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson8206@email.com. You are confident, flexible. Create an order for user U001 at restaurant R005 with items [I102, I207], delivery address 123 Main St, payment method credit card.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R005"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R005"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R005", "item_id": "I102"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R005", "item_id": "I207"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U132", "restaurant_id": "R005", "items": [{"item_id": "I102", "quantity": 1}, {"item_id": "I207", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are polite, confident. Please search for Italian restaurants located in downtown with a price range of $$ to find a suitable dining option. After identifying a restaurant of interest, retrieve the menu for the restaurant with ID \"R123\" to explore their offerings and make an informed decision on what to order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are direct, logical, patient, flexible. search_restaurants(cuisine=\"Italian\", location=\"downtown\", price_range=\"medium\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "medium"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are polite, independent, cautious. First, search for Italian restaurants in San Francisco with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a restaurant, get the restaurant details for restaurant ID R98765 to ensure it meets your preferences. After confirming the restaurant's suitability, get the menu for restaurant ID R98765, focusing on the pasta category, to decide on your order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R98765"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R98765", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are flexible, organized, cautious. Use search_restaurants with cuisine set to \"Mexican\" and location set to \"San Francisco\" to find available options. Once you have identified a suitable restaurant, get_restaurant_menu for restaurant_id \"R234\" to view available dishes and select items.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U093",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are organized, polite. First, get the menu for restaurant ID R123 focusing on the 'Pasta' category to ensure the availability of Spaghetti Carbonara. Once confirmed, add item I456 (Spaghetti Carbonara) to cart for user U001 with quantity 1 and extra cheese customization.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U093", "restaurant_id": "R123", "item_id": "I456", "quantity": 1, "customizations": "extra cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U035",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are confident, organized, cautious. First, search for Italian restaurants in Linda's location with a price range of $$. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R456 to check their hours of operation to ensure they are open for dinner. After confirming the restaurant is open, get the restaurant menu for restaurant ID R456, focusing on the pasta category, to explore options. If Spaghetti Carbonara is available, add item I789 (Spaghetti Carbonara) to cart for user ID U5883 with quantity 1 and no customizations.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U035", "restaurant_id": "R456", "item_id": "I789", "quantity": 1, "customizations": null}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are cautious, optimistic, flexible, direct. First, search for Italian restaurants in the San Francisco area with a price range of $10-$30 to identify potential options for a dinner order. Once you have found a suitable restaurant, get the menu for restaurant R456 to explore available items. This will help ensure you can make an informed choice for your meal selection on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U125",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are logical, organized, flexible. First, search for Italian restaurants in Jennifer's area with a moderate price range to identify potential dining options. Once you have identified a restaurant, get the restaurant details for restaurant ID R456 to check its opening status and delivery zone to ensure it can serve Jennifer's location. Finally, create an order for user U101 (Jennifer Jones) at restaurant ID R456 with items I789 and I790, specifying the delivery address as 123 Maple Street and the payment method as credit card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Jennifer's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U125", "restaurant_id": "R456", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Maple Street", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Robert Williams and your email is robert.williams9426@email.com. You are patient, logical. Search for restaurants offering Mexican cuisine in Jennifer Brown's location.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U122"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer Brown's location"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are patient, logical, flexible, optimistic. Search for restaurants offering Japanese cuisine in San Francisco with a price range of $$ to $$$",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Japanese", "location": "San Francisco", "price_range": "$$ to $$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U101",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are confident, optimistic, organized. Search for restaurants with cuisine \"Mexican\" in San Francisco within a price range of $10-$30.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are logical, organized. First, search for Italian restaurants in Linda Brown's area with a mid-range price to find suitable dining options. Once you have identified a potential restaurant, get restaurant details for restaurant ID R1023 to check operating hours and ensure it fits within your schedule. After confirming the restaurant's availability, create an order for user ID U2988 at restaurant ID R1023 with items (I567, I568) using delivery address \"123 Main St, Apt 4B\" and payment method \"Credit Card\" to complete the transaction efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda Brown's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U104", "restaurant_id": "R1023", "items": [{"item_id": "I567", "quantity": 1}, {"item_id": "I568", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are independent, patient, flexible. Get the menu for restaurant R456 to check available pasta dishes",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are confident, independent. First, search for Mexican restaurants in the San Francisco area with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a restaurant, get the restaurant menu for restaurant ID R5678, focusing on the \"Tacos\" category to explore the available options. After reviewing the menu, add item I890 (Chicken Tacos) to the cart for user ID U7411 with a quantity of 3 and include extra guacamole customization for a personalized touch.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U122", "restaurant_id": "R5678", "item_id": "I890", "quantity": 3, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U128",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are optimistic, independent, direct, logical. Get the restaurant menu for restaurant R2345, focusing on the taco category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "taco"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U178",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are optimistic, polite, cautious, direct. Get the restaurant menu for restaurant ID R5678 to check available pasta dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are cautious, flexible. Get the menu for restaurant R789 to explore available categories and items.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R789"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are independent, confident, logical, organized. Search for restaurants in Patricia's area with cuisine \"Mexican\" and price_range \"moderate\". Once you have identified a suitable restaurant, add item I567 (Chicken Taco) to cart for user Patricia Garcia with quantity 3 and no customizations. This will ensure that Patricia can enjoy a delicious meal from a restaurant that fits her preferences and budget.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U049", "restaurant_id": "R001", "item_id": "I567", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U193",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are confident, independent, optimistic. First, search for Thai restaurants in the San Francisco area with a price range of $10-$20 to find suitable dining options. Once you have identified restaurant R2021, get details to check its operating hours and customer reviews to ensure it meets your expectations. Finally, get the menu for restaurant R2021 focusing on the \"Appetizers\" category, and add item I789 (Spring Rolls) to cart for user U1015 with quantity 3, preparing for a delightful meal through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Thai", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2021"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2021", "category": "Appetizers"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U193", "restaurant_id": "R2021", "item_id": "I789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are optimistic, organized. First, search for restaurants in Michael Williams' area offering Asian cuisine within a moderate price range to ensure there are suitable options available. Once you have identified a restaurant, specifically check restaurant ID R1023 to see if it is open and meets the minimum order requirements. If it does, proceed to create an order for user ID U3137 from restaurant ID R1023 with items [I5678, I5680], using the default delivery address and credit card as the payment method. This sequence ensures that Michael Williams can enjoy a delightful Asian meal delivered efficiently through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Asian", "location": "Michael Williams' area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U167", "restaurant_id": "R1023", "items": [{"item_id": "I5678", "quantity": 1}, {"item_id": "I5680", "quantity": 1}]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U123",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are independent, polite. search_restaurants(location=\"San Francisco\", cuisine=\"Italian\", price_range=\"$$\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"location": "San Francisco", "cuisine": "Italian", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U123",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are optimistic, independent. First, add item ID I876 (Chicken Tacos) to the cart for user ID U123 from restaurant ID R234 with quantity 3. Then, create an order for user ID U123 from restaurant ID R234 with items including Chicken Tacos, using home delivery address and credit card payment.",
        actions=[
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U123", "restaurant_id": "R234", "item_id": "I876", "quantity": 3}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U123", "restaurant_id": "R234", "items": [{"item_id": "I876", "quantity": 3}], "delivery_address": "home", "payment_method": "credit_card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U055",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are direct, patient, cautious, polite. Get the restaurant menu for restaurant ID R1023 to find available taco options.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are cautious, direct, optimistic, patient. First, search for restaurants in John's area with cuisine \"Italian\" and price range \"$$\". After identifying a suitable option, get details for restaurant R12345 to check the menu and hours, focusing specifically on the \"Pasta\" category. This will help you assess the best Italian dining options for a potential partnership with DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "John's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R12345"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R12345", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U118",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are optimistic, polite, flexible, patient. Search for restaurants offering Mexican cuisine in Linda Smith's current location with a moderate price range.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U118"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Smith's current location", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U016",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are logical, organized, flexible. search_restaurants(cuisine=\"Italian\", location=\"Downtown\", price_range=\"medium\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "medium"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson5028@email.com. You are cautious, polite, flexible. Search for American restaurants in San Francisco within a moderate price range to explore dinner options for Linda Williams. Once you have identified a potential restaurant, get the restaurant menu for restaurant R567 to choose suitable items for Linda's order. This will help ensure that the options align with her dining preferences and facilitate a seamless ordering experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "American", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U138",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are logical, polite. search_restaurants(location=\"downtown\", cuisine=\"Italian\", price_range=\"$$\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U190",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are flexible, organized. Get the menu for restaurant R234 focusing on the pasta category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are cautious, flexible. First, search for restaurants offering Mexican cuisine in San Francisco with a moderate price range to find a suitable dining option. Once you have identified a restaurant, get the menu for restaurant ID R1023 to explore available items. This will help you decide on the best dishes to order for a delightful meal experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are flexible, confident, organized, logical. Search for restaurants offering Mexican cuisine in the Los Angeles area within a mid-range price bracket.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Los Angeles", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are flexible, logical, patient, optimistic. First, search for restaurants in New York City with a cuisine preference for Italian and a price range of $$. Once you have identified potential options, get the restaurant menu for restaurant ID R789 with a focus on the 'Pasta' category to ensure it offers a variety of dishes that align with customer preferences. This will help in curating a selection of Italian restaurants for DoorDash that not only fit the budget but also offer diverse pasta options, enhancing customer satisfaction and choice.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R789", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson5028@email.com. You are polite, optimistic, independent, flexible. First, search for restaurants offering Mexican cuisine in the downtown area with a mid-range price. Once you have identified a potential restaurant, specifically restaurant R234, proceed to get the restaurant menu focusing on the 'Tacos' category. This will help you evaluate if the menu options align with customer preferences and ensure they fit within the delivery service's offerings.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U077",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are optimistic, independent, patient, direct. First, search for Thai restaurants in San Francisco with a price range of $$ to $$$ to find a suitable dining option for a client meeting. Once you have identified a restaurant, create an order for user ID U101112 at the selected restaurant with items I67890, ensuring the delivery address is 123 Market St and the payment method is Credit Card. This will help ensure a seamless dining experience for the client.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Thai", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U077", "restaurant_id": "R001", "items": [{"item_id": "I67890", "quantity": 1}], "delivery_address": "123 Market St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is Mary Brown and your email is mary.brown1791@email.com. You are flexible, patient, cautious, organized. First, search for Mexican restaurants in Linda Garcia's area with a price_range of \"$$\" to find suitable dining options. Once a restaurant is selected, get the restaurant menu for restaurant R1023 to review the available items. After reviewing the menu, add the item Chicken Tacos (item_id I204) to the cart for user Linda Garcia (user_id: U5307) with a quantity of 2.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Garcia's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U106", "restaurant_id": "R1023", "item_id": "I204", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are direct, patient, cautious. Get the menu for restaurant R2345, focusing on the Pasta category",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U110",
        instruction="Your name is John Brown and your email is john.brown5124@email.com. You are direct, confident, organized. Create an order for Mary Smith with restaurant R234, including items I567 and I568, and specify the delivery address as 123 Elm Street.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U110", "restaurant_id": "R234", "items": [{"item_id": "I567", "quantity": 1}, {"item_id": "I568", "quantity": 1}], "delivery_address": "123 Elm Street"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are patient, optimistic. \"Get the menu for restaurant ID R2345 to find available sushi options\"",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "sushi"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U110",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are cautious, independent. First, search for Mexican restaurants in the San Francisco area with a price range of $10-$20 to find potential dining options. Once you have identified a suitable restaurant, get details for restaurant R5678 to check opening hours and contact information to ensure it fits your schedule. After confirming the restaurant is open, get the menu for restaurant R5678 with a focus on the taco category, and proceed to add item I6789 (Chicken Tacos) to cart for user U1234 with quantity 3 and no customizations, finalizing your order on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "taco"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U110", "restaurant_id": "R5678", "item_id": "I6789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are independent, logical, direct, cautious. Search for Mexican restaurants in the Brooklyn area with a price range of $$. Once you find a suitable restaurant, get the restaurant menu for restaurant R234 to view available items.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Brooklyn", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are logical, flexible. Search for restaurants serving Mexican cuisine in Mary Miller's neighborhood and then get the menu for restaurant R5678 to explore available items. This will help in identifying suitable dishes for Mary, who is interested in trying something new from a local spot.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Mary Miller's neighborhood"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U110",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are patient, organized. Create an order for user U001 from restaurant R101 with items [I202, I203], delivery address \"123 Main St, Apt 4\", and special instructions \"Leave at the door\".",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R101", "item_id": "I202"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R101", "item_id": "I203"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U110", "restaurant_id": "R101", "items": [{"item_id": "I202", "quantity": 1}, {"item_id": "I203", "quantity": 1}], "delivery_address": "123 Main St, Apt 4", "special_instructions": "Leave at the door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U110",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are confident, polite. Create an order for user Mary Smith with restaurant ID R110, including items I210 and I215, using home address and credit card ending in 1234.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U110"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R110"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R110"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U110", "restaurant_id": "R110", "items": [{"item_id": "I210", "quantity": 1}, {"item_id": "I215", "quantity": 1}], "delivery_address": "home", "payment_method": "credit card ending in 1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are optimistic, patient. First, search for restaurants offering Mexican cuisine in New York City within a mid-range price to find potential options for a dinner plan. Once you have identified a suitable restaurant, get the menu for restaurant ID R234 to review available items in the 'Tacos' category. After confirming the menu meets your preferences, create an order for user ID U101 from restaurant ID R234 with items [I678 (Chicken Taco) x3], delivery address '123 Main St, New York, NY', and payment method 'credit_card'.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Tacos"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U030", "restaurant_id": "R234", "items": [{"item_id": "I678", "quantity": 3}], "delivery_address": "123 Main St, New York, NY", "payment_method": "credit_card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are direct, optimistic. First, search for Mexican restaurants in San Francisco with a price range of $$. Once you have identified a suitable option, get the restaurant details for restaurant R5678 to check if they are currently open. If the restaurant is open, proceed to create an order for user U123 at restaurant R5678 with items: Chicken Tacos (quantity 3), delivery address: 123 Main St, payment method: credit card, and include special instructions for extra salsa.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U140", "restaurant_id": "R5678", "items": [{"name": "Chicken Tacos", "quantity": 3}], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is James Williams and your email is james.williams9904@email.com. You are direct, cautious, confident, flexible. First, search for restaurants offering Asian cuisine in the 94103 area code within a moderate price range. Once you find a suitable restaurant, get the menu for restaurant ID R5678, focusing on the 'Main Dishes' category. This will help you decide on a meal option that fits your preference and budget.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Asian", "location": "94103", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Main Dishes"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U110",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are confident, polite, cautious, patient. Get the menu for restaurant R5678 to find available pasta dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U046",
        instruction="Your name is James Williams and your email is james.williams9904@email.com. You are direct, organized, flexible. First, search for Mexican restaurants in San Francisco with a price range of $10-$20 to identify potential options for our delivery service expansion. Once you have identified a promising restaurant, get the restaurant details for restaurant ID R201 to check its operating hours and customer reviews to ensure it meets our quality standards. After confirming the restaurant's suitability, get the menu for restaurant R201 to identify available vegetarian options, ensuring we can cater to diverse customer preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R201"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R201", "category": "Vegetarian"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are polite, optimistic, patient. First, search for Mexican restaurants in the Chicago area with a price range of $10-$20 to find a suitable dining option. Once you have identified a restaurant, get the restaurant menu for restaurant ID R345 to find available tacos. After confirming the availability of Chicken Tacos, add item I789 (Chicken Tacos) to the cart for user ID U567 with a quantity of 3 and no customizations. This will help ensure that the user can enjoy their meal seamlessly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Chicago", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R345"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U192", "restaurant_id": "R345", "item_id": "I789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U007",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are confident, independent, cautious, organized. search_restaurants(location=\"downtown\", cuisine=\"Italian\", price_range=\"$$\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U176",
        instruction="Your name is John Garcia and your email is john.garcia7961@email.com. You are organized, direct, cautious. First, search for Mexican restaurants in San Francisco within a moderate price range to find potential dining options. Next, get the restaurant menu for restaurant ID R2458 to find available tacos, ensuring that the menu aligns with your preferences. Finally, create an order for user U12345 at restaurant R2458 with items [I789] and delivery address 123 Main St, Apt 4B, using credit card payment to complete the transaction.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2458"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U176", "restaurant_id": "R2458", "items": [{"item_id": "I789", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "credit_card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are confident, direct. Get the menu for restaurant ID R5678 to find available sushi items.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "sushi"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is Robert Brown and your email is robert.brown1066@email.com. You are independent, cautious, organized. First, search for restaurants offering Mexican cuisine in the downtown area to identify potential options for a new delivery partnership. Once you have identified restaurant R2023, get the menu to check available items in the Tacos category. This will help in deciding the variety and quality of offerings for our customers.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2023", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U002",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are optimistic, polite, patient. Create order for user Patricia Brown with restaurant ID R567 including items I890 and I891, delivering to 123 Main St, using credit card payment.",
        actions=[
            Action(
                name="create_order",
                kwargs={"user_id": "U002", "restaurant_id": "R567", "items": [{"item_id": "I890", "quantity": 1}, {"item_id": "I891", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are cautious, patient. Get the menu for restaurant ID R102, focusing on the \"Tacos\" category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are independent, confident, optimistic. First, search for restaurants offering Chinese cuisine in the San Francisco area to identify potential options for expanding DoorDash's delivery network. Once you've identified a promising restaurant, get the restaurant details for restaurant ID R345 to check for delivery options and hours to ensure they align with DoorDash's operational standards.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U118",
        instruction="Your name is Mary Williams and your email is mary.williams2739@email.com. You are logical, confident, optimistic, patient. First, search for restaurants offering Mexican cuisine in the San Francisco area with a mid-range price to find a suitable dining option. Once you identify a restaurant, specifically retrieve the menu for restaurant ID R345, focusing on the 'tacos' category to explore their offerings. This will help you decide on the best tacos to order for a satisfying meal experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R345", "category": "tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are cautious, independent, polite. You are planning a quiet dinner at home and want to order Italian food. First, search for Italian restaurants in New York City that fall within a moderate price range. Once you find a suitable restaurant, obtain the restaurant's details to ensure it meets your dining preferences. After confirming the restaurant's ambiance and reviews, proceed to explore their main course menu. Finally, select a dish you like, and add it to your cart with the customization of extra cheese to enhance your meal.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Main Course"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U019", "restaurant_id": "R001", "item_id": "I001", "quantity": 1, "customizations": "extra cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are logical, flexible. create_order(user_id=\"U001\", restaurant_id=\"R101\", items=[{\"item_id\": \"I203\", \"quantity\": 1}], delivery_address=\"123 Main St\", payment_method=\"credit_card\")",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R101", "item_id": "I203"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U095", "restaurant_id": "R101", "items": [{"item_id": "I203", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit_card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U055",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are polite, optimistic. search_restaurants(cuisine=\"Italian\", location=\"San Francisco\", price_range=\"$10-$30\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$10-$30"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U075",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are independent, cautious, flexible, polite. Search for Italian restaurants in the San Francisco area with a price range of $$-$$$.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are polite, optimistic. First, search for Mexican restaurants in the Los Angeles area with a price range of $10-$20 to find potential dining options. Once you have identified restaurant R5687 as a suitable choice, get details for restaurant R5687 to confirm operating hours and delivery zone, ensuring they can deliver to your area. Finally, create an order for user U102 with restaurant R5687, including items I2345 and I2346, and arrange for delivery to \"123 Elm St, Los Angeles, CA\" using a \"Credit Card\" as the payment method.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Los Angeles", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5687"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U180", "restaurant_id": "R5687", "items": [{"item_id": "I2345", "quantity": 1}, {"item_id": "I2346", "quantity": 1}], "delivery_address": "123 Elm St, Los Angeles, CA", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U133",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are polite, cautious. First, search for restaurants offering Mexican cuisine in the San Francisco area within a moderate price range to find suitable dining options for our customers. Once you have identified a restaurant, get the menu for restaurant R2345 to identify available items in the Tacos category, ensuring that the selection meets customer preferences. After confirming the menu options, add item I5678 (Chicken Tacos) to cart for user U5124 with quantity 3 and extra salsa customization, as per the user's request. This sequence of tasks will help streamline the ordering process on DoorDash and enhance customer satisfaction.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U133", "restaurant_id": "R2345", "item_id": "I5678", "quantity": 3, "customizations": "extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are independent, confident, direct. Get the restaurant menu for restaurant ID R101 to check available items in the \"Tacos\" category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U187",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are direct, cautious, confident. Search for restaurants offering vegetarian cuisine in Mary Williams' location with a price range of $10-$20. Once you have identified a suitable restaurant, get the menu of restaurant ID R1023 to find available vegetarian options. This will help ensure that the restaurant meets the dietary preferences and budget constraints before proceeding with any order.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U187"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Vegetarian", "location": "Mary Williams' location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U016",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are independent, polite, direct. First, search for Italian restaurants in Jennifer Johnson's location with a moderate price range to find suitable dining options. Once you have identified a restaurant, get the menu for restaurant R156 to find available Italian dishes. After reviewing the menu, add item I789 (Spaghetti Carbonara) to cart for user U001 from restaurant R156 with quantity 1.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Jennifer Johnson's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R156"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U016", "restaurant_id": "R156", "item_id": "I789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are independent, cautious, polite. First, search for Italian restaurants in the San Francisco area with a price range of $$ to $$$ to find a suitable dining option for a client's dinner meeting. Once you have identified a restaurant, specifically R789, get the restaurant menu to find available pasta dishes. This will help you decide if the menu aligns with the client's preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R789", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U075",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are direct, organized, flexible, optimistic. First, search for Italian restaurants located in Downtown to find a suitable place for a business lunch. Once you have identified a potential restaurant, retrieve the pasta menu from the restaurant with ID \"R123\" to review the available options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U105",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are direct, cautious. First, search for restaurants in the downtown area with a preference for Asian cuisine and moderate price range to find suitable dining options. Once you identify a potential restaurant, get restaurant details for restaurant R567 to check its location and opening hours to ensure it fits your schedule. Finally, create an order for user U101 at restaurant R567 with items (I789, I790), specifying delivery address as \"123 Main St, Apt 4B\" and payment method as \"Credit Card\" to complete the transaction efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Asian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U105", "restaurant_id": "R567", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U020",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are logical, confident, independent, polite. First, search for restaurants in the New York area offering Mexican cuisine within a moderate price range to expand our delivery options on DoorDash. Once you have identified potential restaurants, get the menu for restaurant ID R56789 to check available items in the \"Tacos\" category, ensuring we can offer a diverse selection to our customers.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "New York", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R56789", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U061",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are patient, polite, organized. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to ensure a variety of options for our customers. Next, get the restaurant details for restaurant ID R1023 to verify hours and delivery zones, ensuring that we can provide accurate information to our users. Finally, create an order for user ID U001 at restaurant ID R1023 with items I202 and I203, using delivery address \"123 Main St, Apt 4B\" and payment method \"Credit Card\", ensuring a seamless ordering experience for our customer.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$,$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U061", "restaurant_id": "R1023", "items": [{"item_id": "I202", "quantity": 1}, {"item_id": "I203", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U170",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are independent, flexible, polite. First, search for Italian restaurants in the New York City area with a price range of $$ to $$$ to find suitable dining options. Once you have identified a potential restaurant, get restaurant details for restaurant ID R5678 to verify hours of operation and ensure it fits your schedule. After confirming the restaurant's availability, proceed to create an order for user ID U101 with restaurant ID R5678 and items [I1234, I5678] using delivery address 123 Main St, Apt 4B, New York, NY and payment method Visa ending in 1234.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U170", "restaurant_id": "R5678", "items": [{"item_id": "I1234", "quantity": 1}, {"item_id": "I5678", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B, New York, NY", "payment_method": "Visa ending in 1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are cautious, optimistic, polite. Search for restaurants offering Mexican cuisine in the downtown area within a mid-range price bracket. Once you have identified a suitable option, get the full menu for restaurant R203 to explore available Mexican dishes. This will help you make informed recommendations for DoorDash customers seeking authentic Mexican dining experiences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R203"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are cautious, patient, polite, optimistic. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to identify potential options for expanding DoorDash's restaurant partnerships. Once you have identified a restaurant, get the restaurant details for restaurant ID R1001 to check its hours and address, ensuring it aligns with DoorDash's delivery service hours and location requirements.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is John Brown and your email is john.brown5124@email.com. You are logical, direct, patient. Search for restaurants offering Mexican cuisine in Jennifer's area (location: Jennifer's delivery address)",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U076"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer's delivery address"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are polite, logical, flexible, confident. Create an order for user Mary Miller with restaurant ID R1234, including item I5678, using default delivery address and credit card payment method.",
        actions=[
            Action(
                name="create_order",
                kwargs={"user_id": "U132", "restaurant_id": "R1234", "items": [{"item_id": "I5678", "quantity": 1}]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are patient, polite, organized. First, search for Italian restaurants in San Francisco with a price range of $$-$$$ to find suitable dining options for a client meeting. Once you have identified a restaurant, get the restaurant details for restaurant ID R1023 to check their hours of operation and ensure they are open during your preferred meeting time. After confirming the restaurant is open, get the restaurant menu for restaurant ID R1023, focusing on the Pasta category, to select a popular dish. Finally, add item ID I204 (Spaghetti Carbonara) to cart for user ID U1001 with quantity 1 to prepare for a seamless dining experience during the meeting.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U030", "restaurant_id": "R1023", "item_id": "I204", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are organized, confident, cautious, direct. First, search for Mexican restaurants in San Francisco with a price range of $$ to identify potential dining options. Next, get details for restaurant R567 to verify operating hours and delivery range, ensuring it meets the user's requirements. Finally, create an order for user U123 at restaurant R567 with items [I890] and delivery address \"123 Main St, San Francisco,\" confirming that the selected restaurant can fulfill the delivery within the specified area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U151", "restaurant_id": "R567", "items": [{"item_id": "I890", "quantity": 1}], "delivery_address": "123 Main St, San Francisco"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U142",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are polite, cautious. search_restaurants(location=\"downtown\", cuisine=\"Italian\", price_range=\"medium\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "medium"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are organized, cautious. First, search for restaurants with Italian cuisine within the San Francisco area and a price range of $10-$30 to find potential dining options for our users. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R5678, focusing on the Pasta category, to ensure we have a comprehensive list of available dishes for our customers.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are independent, direct, polite, patient. First, search for restaurants with Mexican cuisine in the downtown area within a mid-range price to find potential options for a customer looking to enjoy a meal. Once you have identified a suitable restaurant, get restaurant details for restaurant ID R456 to verify its opening hours and delivery zone, ensuring it can deliver to the customer's location. After confirming the delivery feasibility, get the restaurant menu for restaurant ID R456 to check available items in the \"Tacos\" category. This will help you recommend specific dishes to the customer. Finally, create an order for user ID U9904 with restaurant ID R456, including items [(I789, quantity: 3)] and delivery address \"123 Main St, Apt 4B\", to complete the customer's request for a delicious Mexican meal delivered to their home.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "Tacos"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U048", "restaurant_id": "R456", "items": [{"item_id": "I789", "quantity": 3}], "delivery_address": "123 Main St, Apt 4B"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are independent, polite, logical. Get restaurant menu for restaurant ID R987, focusing on the 'Tacos' category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U190",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are logical, organized, confident. Search for restaurants in Linda Miller's location with a preference for Italian cuisine and a mid-range price.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U190"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda Miller's location", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are logical, optimistic, independent, polite. First, get details for restaurant R101 (Gourmet Burger House) to check operational hours and rating, ensuring they are open and well-rated for a positive dining experience. Then, create an order for user U9808 with restaurant R101, including items I301 and I302, to be delivered to \"123 Elm St, San Francisco, CA,\" using \"credit card\" as the payment method. This ensures the order is placed with a reputable restaurant that is currently operational.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U085", "restaurant_id": "R101", "items": [{"item_id": "I301", "quantity": 1}, {"item_id": "I302", "quantity": 1}], "delivery_address": "123 Elm St, San Francisco, CA", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are patient, cautious, confident, organized. Get the menu for restaurant ID R203 to check available items and categories",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R203"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U007",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are flexible, logical, polite. First, search for restaurants serving Mexican cuisine in the Chicago area with a price range of $10-$20 to find potential options for your next meal. Once you have identified a restaurant of interest, get the restaurant details for restaurant ID R101 to verify opening hours and delivery zones, ensuring it fits your schedule and location. After confirming the restaurant is suitable, get the restaurant menu for restaurant ID R101 to browse available items and decide on your order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Chicago", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U093",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are flexible, optimistic. Search for Italian restaurants in Mary Jones' area with a moderate price range, and once you find a suitable option, get the menu for restaurant R567, focusing on the pasta category. This will help you recommend a delightful pasta dish to Mary Jones, ensuring she enjoys a satisfying meal through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Mary Jones' area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are patient, optimistic, flexible, organized. First, search for restaurants serving Mexican cuisine in Patricia Garcia's location with a price range of $10-$30 to find suitable dining options. Once you have identified a potential restaurant, get detailed information for restaurant R567 to check its operating hours and delivery zone, ensuring it can deliver to Patricia's address. Finally, create an order for user U123 (Patricia Garcia) at restaurant R567 with items Chicken Tacos and Churros, using her default delivery address and credit card ending in 1234.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Patricia Garcia's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U049", "restaurant_id": "R567", "items": [{"name": "Chicken Tacos", "quantity": 1}, {"name": "Churros", "quantity": 1}], "payment_method": "credit card ending in 1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Linda Miller and your email is linda.miller5151@email.com. You are logical, polite, confident. Search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $$. Once you find a suitable restaurant, get the menu for restaurant ID R456 focusing on the \"Tacos\" category. This will help you assist customers like Mary Miller, who are looking to place an order for Mexican food via DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U055",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are polite, logical, independent. Create an order for user U1558 at restaurant R987 with item I123, delivery address 123 Main St, San Francisco, payment method as credit card, and special instructions \"Leave at the door.\"",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R987"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R987", "item_id": "I123"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U055", "restaurant_id": "R987", "items": [{"item_id": "I123", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card", "special_instructions": "Leave at the door."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are logical, confident. First, search for restaurants in San Francisco offering Mexican cuisine with a price range of $10-$20. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R567 to confirm its operating hours and delivery zone, ensuring it aligns with your schedule and location. After confirming the restaurant's availability, get the restaurant menu for restaurant ID R567, focusing on the \"Tacos\" category, to review the options. Finally, add item I234 (Chicken Tacos) to the cart for user ID U001 with a quantity of 3 and no customizations, preparing for a seamless order experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U175", "restaurant_id": "R567", "item_id": "I234", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are flexible, cautious. First, search for Italian restaurants in the San Francisco area with a price range of $$ to $$$ to identify potential new partners for DoorDash. Once you have identified a promising option, get the restaurant details for restaurant ID R2341 to check its hours and contact information, ensuring they align with DoorDash's operational requirements.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$,$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2341"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is Mary Miller and your email is mary.miller1688@email.com. You are polite, optimistic, direct, confident. Get the restaurant menu for restaurant ID R2345 to view available items in the Tacos category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U061",
        instruction="Your name is Mary Miller and your email is mary.miller1688@email.com. You are logical, organized. First, search for Chinese restaurants in the San Francisco area with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a restaurant, get the restaurant details for restaurant ID R1023 to verify hours of operation, ensuring it is open for delivery. After confirming the restaurant is open, create an order for user U456 at restaurant ID R1023 with items I202 and I203, ensuring the delivery address is 123 Main St and the payment method is credit card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U061", "restaurant_id": "R1023", "items": [{"item_id": "I202", "quantity": 1}, {"item_id": "I203", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are cautious, confident, independent. Create order for user U1610 with restaurant R345, including items I789 and I790, delivery address 123 Main St, San Francisco, CA, and payment method credit card.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R345"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R345"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R345", "item_id": "I789"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R345", "item_id": "I790"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U175", "restaurant_id": "R345", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U125",
        instruction="Your name is John Brown and your email is john.brown5124@email.com. You are logical, confident. First, search for restaurants with cuisine 'Thai' in the 'Midtown' area with a price range of '$$' to find suitable dining options. Once you identify a restaurant of interest, get restaurant details for restaurant ID 'R234' to verify its operating hours and delivery zone, ensuring it meets your logistical needs. Finally, create an order for user ID 'U6091' with restaurant ID 'R234' including items 'I789' and 'I790', and provide special instructions 'No peanuts' to accommodate dietary preferences. This sequence ensures you select the right restaurant and place a thoughtful order on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Thai", "location": "Midtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U125", "restaurant_id": "R234", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "special_instructions": "No peanuts"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams7359@email.com. You are patient, cautious. First, search for restaurants offering Mexican cuisine in the downtown area with a price range of $10-$20. After identifying a suitable restaurant, get the restaurant menu for restaurant ID R567, focusing on the Tacos category, to ensure they have a variety of taco options available.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U075",
        instruction="Your name is Robert Williams and your email is robert.williams9426@email.com. You are direct, flexible, optimistic. First, search for restaurants offering Mexican cuisine in the San Francisco area within a moderate price range to find potential options for a user interested in tacos. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R5678, focusing on the \"Tacos\" category, to ensure they offer a variety of taco options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U016",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are direct, flexible. First, search for restaurants offering Thai cuisine in the Chicago area with a price range of $15-$30. Once you have identified a potential restaurant, get restaurant details for restaurant ID R5678 to check their opening hours and delivery zones. This will help ensure that the restaurant is available for delivery during peak times and covers the desired delivery area, making it a suitable option for Doordash customers looking for Thai cuisine.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Thai", "location": "Chicago", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Mary Jones and your email is mary.jones4200@email.com. You are confident, direct. First, search for Italian restaurants in the downtown area with a price range of $$ and above to find a suitable dining option for a client meeting. Once you've identified a promising restaurant, get the menu for restaurant R456 to explore available pasta dishes, focusing on their variety and quality. After reviewing the menu, add item I789 (Spaghetti Carbonara) to the cart for user U1688 with quantity 1 and no customizations, ensuring a seamless ordering process for the client.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U132", "restaurant_id": "R456", "item_id": "I789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U081",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are confident, organized, cautious. First, search for Mexican restaurants in the East Village with a price range of $$. Once you have identified a suitable restaurant, get the menu for restaurant ID R234 to view available tacos and burritos. This will help you decide on the best options for creating an order for user ID U102.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "East Village", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": null}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U105",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are patient, confident, optimistic. First, search for Italian restaurants in the San Francisco area with a price range of $$ to $$$ to identify potential new partners for our platform. Once you have identified a promising restaurant, get the menu for restaurant ID R1025, focusing on the pasta category, to assess the variety and quality of offerings that could appeal to our customer base.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$ to $$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1025", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are polite, optimistic, cautious. Search for restaurants in Jennifer's location with a preference for Italian cuisine and a moderate price range.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U076"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Jennifer's location", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is Linda Miller and your email is linda.miller5151@email.com. You are confident, organized. First, search for Italian restaurants in Patricia's area with a price range of $$ to $$$ to ensure you have a selection of quality dining options. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R2345 and filter for the pasta category to review their offerings. This will help you make an informed decision on what to recommend or order for Patricia through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Patricia's area", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are patient, confident. First, search for Mexican restaurants in the Los Angeles area within a moderate price range to find suitable options for a family dinner. Once you have identified a restaurant, get the menu for restaurant R456, focusing on the 'Tacos' category, to ensure they offer a variety of choices. This will help you decide if it meets your family's preferences for the evening.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Los Angeles", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson8206@email.com. You are optimistic, cautious, independent, patient. First, search for Mexican restaurants in the San Francisco area with a price range of $10-$30 to find a suitable option for a customer request. Once you have identified a potential restaurant, get detailed information for restaurant R2345 to ensure it meets the customer's preferences and requirements.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are direct, independent, optimistic, organized. First, search for Italian restaurants in Linda Brown's area with a moderate price range to ensure a good selection for potential delivery options. Once you have identified a suitable restaurant, such as restaurant R234, get details to check its hours and delivery zone. This will help determine if it fits within DoorDash's delivery capabilities and customer preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda Brown's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are logical, patient, flexible, direct. First, search for Mexican restaurants in Linda Williams' area with a moderate price range to find suitable dining options. Once you have identified a promising restaurant, get details for restaurant R234 to verify its hours and location to ensure it is convenient for Linda. After confirming the restaurant's details, get the menu for restaurant R234 to view available items in the tacos category. If Chicken Tacos are available, add item I567 (Chicken Tacos) to cart for user U1610 with quantity 3 and extra guacamole to complete the order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Williams' area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U175", "restaurant_id": "R234", "item_id": "I567", "quantity": 3, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U101",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are flexible, logical. Get the menu for restaurant R987 to explore available Mexican dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987", "category": "Mexican"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U020",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are independent, optimistic, patient. search_restaurants(cuisine=\"Italian\", location=\"San Francisco\", price_range=\"$20-$40\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$20-$40"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are organized, flexible. Search for Mexican restaurants in San Francisco with a price range of $$. Once you find a suitable option, get restaurant details for restaurant R1023. After reviewing the details, get the restaurant menu for restaurant R1023, focusing on the 'Tacos' category. If the menu includes a Carne Asada Taco, add item I567 (Carne Asada Taco) to cart for user U001 with quantity 3, customizing with extra guacamole.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U042", "restaurant_id": "R1023", "item_id": "I567", "quantity": 3, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U086",
        instruction="Your name is John Brown and your email is john.brown5124@email.com. You are independent, logical. First, search for Italian restaurants in San Francisco with a price range of $$ to $$$ to find a suitable dining option for a business meeting. Once you have identified a potential restaurant, get the restaurant details for restaurant R1023 to ensure it meets your requirements for ambiance and location. After confirming the restaurant's suitability, get the menu for restaurant R1023 in the category 'Pasta' to review the available options. If the Spaghetti Carbonara looks appealing, add item I567 (Spaghetti Carbonara) to cart for user U5308 with quantity 1, as it will be a perfect choice for your meeting attendees who appreciate classic Italian cuisine.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U086", "restaurant_id": "R1023", "item_id": "I567", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are organized, logical. You are planning a dinner for your family and want to order Italian food from a restaurant in San Francisco, CA, within a moderate price range. First, search_restaurants(cuisine=\"Italian\", location=\"San Francisco, CA\", price_range=\"$$\") to find suitable dining options. Once you have selected a restaurant, get_restaurant_menu(restaurant_id=\"R1023\") to view their offerings and decide on the dishes you would like to order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco, CA", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U178",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are confident, cautious, optimistic, logical. First, search for restaurants offering Mexican cuisine in the downtown area within a mid-range price bracket to find potential options for a business lunch. Once a suitable restaurant is identified, get the menu for restaurant R234, focusing on the 'Main Course' category, to explore popular dishes that can cater to diverse tastes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Main Course"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U110",
        instruction="Your name is Mary Williams and your email is mary.williams2739@email.com. You are patient, direct, organized. Search for restaurants offering Mexican cuisine in Mary Smith's area with a moderate price range.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Mary Smith's area", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U193",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are direct, polite. First, search for restaurants in New York City with cuisine type 'Italian' and price range '$$' to identify potential partners for expanding our delivery options. Once you have a list, get restaurant details for restaurant_id R1024 to check if it's open for orders, ensuring we can provide timely service to our customers.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is John Garcia and your email is john.garcia7961@email.com. You are cautious, logical, organized, polite. Search for restaurants with Chinese cuisine in San Francisco within a moderate price range.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are optimistic, confident, flexible, polite. First, search for restaurants with Mexican cuisine in the downtown area and a price range of $10-$20 to identify potential options for expanding the delivery service. Once you have identified a restaurant, get the restaurant details for restaurant ID R567 to check if they are open and meet the delivery zone requirements, ensuring they can be seamlessly integrated into the Doordash platform.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U163",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are logical, patient, polite, confident. First, search for Italian restaurants in New York, NY with a moderate price range ($$) to find a suitable dining option. Once you identify a restaurant that meets your criteria, obtain the restaurant details using its unique restaurant ID. This information will help you make an informed decision about placing an order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York, NY", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U178",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are cautious, patient. Search for restaurants in New York City with a cuisine of \"Mexican\" and a price range of \"$$\". Once you identify a potential restaurant, get the restaurant details for restaurant ID R234 to check its hours and location. This information will help you assess whether the restaurant is a viable option for listing on DoorDash, ensuring it meets the platform's standards and operational hours for optimal delivery service.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are optimistic, patient, cautious. First, search for Italian restaurants in the New York City area with a price range of $$. Once you have identified potential options, get restaurant details for restaurant R1023 to verify its hours and delivery options. This will help ensure that the restaurant can accommodate delivery requests during peak hours for DoorDash customers.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U190",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are cautious, polite. First, search for restaurants with cuisine 'Mexican' in the location 'San Francisco' with a price range of '$$' to find a suitable option for a client meeting. Once you have identified a potential restaurant, get the restaurant details for restaurant_id 'R102' to verify opening hours and delivery zone, ensuring it fits the schedule and location requirements. Finally, create an order for user_id 'U202' with restaurant_id 'R102', including items ['I305'], delivery_address '123 Market St, San Francisco, CA', payment_method 'Credit Card', and special_instructions 'Leave at doorstep' to ensure a seamless delivery experience for the client.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U190", "restaurant_id": "R102", "items": ["I305"], "delivery_address": "123 Market St, San Francisco, CA", "payment_method": "Credit Card", "special_instructions": "Leave at doorstep"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U187",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are cautious, polite, logical. Get restaurant menu for restaurant ID R102 to explore available dishes and prices.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is John Brown and your email is john.brown5124@email.com. You are patient, confident, direct, independent. First, search for Mexican restaurants in the downtown area with a price range of $$. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R256 to view available items. After reviewing the menu, add item I789 (Chicken Tacos) to the cart for user ID U9607 from restaurant ID R256 with quantity 3.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R256"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U140", "restaurant_id": "R256", "item_id": "I789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are direct, logical, polite. First, search for restaurants in Patricia Jones's area with a focus on vegan cuisine to identify potential dining options. Next, get the restaurant details for restaurant R5678 to check if it's open and confirm its delivery zone to ensure it can serve Patricia's location. Finally, get the menu for restaurant R5678, focusing on the 'Entrees' category, to explore suitable dishes for Patricia's vegan preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Vegan", "location": "Patricia Jones's area"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Entrees"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are flexible, independent, polite. Get the restaurant menu for restaurant ID R1023, focusing on the Tacos category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U105",
        instruction="Your name is Mary Miller and your email is mary.miller1688@email.com. You are patient, logical. First, search for restaurants with cuisine \"Italian\" in the downtown area of ZIP code 94105, within a price range of $10-$30. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R1023 to check business hours and delivery zones to ensure they can deliver to the specified address. Finally, create an order for user ID U5678 with restaurant ID R1023, including items I234, I567, delivery address 123 Main St, payment method \"Credit Card\", and special instructions \"Leave at door\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown 94105", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U105", "restaurant_id": "R1023", "items": [{"item_id": "I234", "quantity": 1}, {"item_id": "I567", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are flexible, confident, cautious. Search for restaurants with cuisine 'Italian', location 'San Francisco', and price range '$$'.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U176",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson5028@email.com. You are flexible, organized, patient, direct. First, search for Italian restaurants in the San Francisco area with a price range of $$. Once you have identified a suitable restaurant, get restaurant details for restaurant ID R202 to check operating hours to ensure they are open during your preferred dining time. After confirming the restaurant is open, get the restaurant menu for restaurant ID R202 focusing on the 'Pasta' category to decide on your order. Finally, create an order for user ID U101 from restaurant ID R202 with items I301 and I302, ensuring the delivery address is 123 Main St and the payment method is 'Credit Card'.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R202"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R202", "category": "Pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U176", "restaurant_id": "R202", "items": [{"item_id": "I301", "quantity": 1}, {"item_id": "I302", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are cautious, logical. Get the menu for restaurant ID R456 to browse available items in the \"Main Course\" category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "Main Course"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U138",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are polite, direct, optimistic, logical. First, search for Mexican restaurants in the Los Angeles area with a price range of $10-$20 to explore dining options. Once you have identified a suitable restaurant, get the menu for restaurant R5678, focusing on the \"Tacos\" category, to review their offerings. After confirming the availability of Chicken Tacos, add item I7890 (Chicken Tacos) to cart for user U3457 with quantity 3 and no customizations, ensuring a seamless ordering experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Los Angeles", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U138", "restaurant_id": "R5678", "item_id": "I7890", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are logical, flexible, polite. You have a craving for Italian food and want to order dinner through DoorDash. First, search for Italian restaurants located in Downtown within a moderate price range. Once you find a suitable restaurant, proceed to check the menu specifically for Pizzas and decide on your choice. After reviewing the options, add two of your selected pizza item to your cart for purchase.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Pizzas"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U167", "restaurant_id": "R001", "item_id": "I001", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are logical, direct, organized, flexible. First, search for Mexican restaurants in San Francisco with a price range of $10-$20 to find suitable dining options for a business lunch. Once you have identified a restaurant, get the restaurant menu for restaurant ID R245 to explore available tacos and burritos. After reviewing the menu, add item I789 (Chicken Burrito) to the cart for user john.garcia7961@email.com from restaurant ID R245 with quantity 1 and extra guacamole, ensuring the order is ready for a lunchtime delivery.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R245"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U151", "restaurant_id": "R245", "item_id": "I789", "quantity": 1, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are polite, cautious, organized. First, search for Italian restaurants in San Francisco, CA with a price range of $$. Once you have identified a suitable restaurant, specifically restaurant R23456, get details to check its menu and hours. This information is crucial for assessing whether the restaurant can be added to the DoorDash platform, ensuring it offers a variety of menu options and operates during peak delivery times.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco, CA", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R23456"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R23456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U134",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson8206@email.com. You are polite, confident, flexible. First, search for Mexican restaurants in San Francisco with a medium price range to find a suitable dining option. Once you have identified a promising restaurant, get the restaurant details using the restaurant_id \"R2345\" to check their hours and delivery zone to ensure they can deliver to your location. After confirming the delivery zone, proceed to create an order for user_id \"U5678\" from the selected restaurant, including items such as \"I6789\" with a quantity of 1, and set the delivery address to \"123 Main St, San Francisco,\" using a credit card as the payment method.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U134", "restaurant_id": "R2345", "items": [{"item_id": "I6789", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is James Williams and your email is james.williams9904@email.com. You are logical, polite, optimistic. Get the menu for restaurant ID R987 to explore available taco options.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U035",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are patient, logical. Begin by searching for restaurants offering Mexican cuisine in the San Francisco area within a moderate price range to find potential options for a business lunch. Once you identify a suitable restaurant, get the restaurant details for restaurant ID R1023 to review its operating hours and location, ensuring it aligns with your schedule. Finally, get the restaurant menu for restaurant ID R1023 to explore available items under the 'Main Course' category, focusing on selecting a variety of dishes that would appeal to your colleagues.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Main Course"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is Linda Davis and your email is linda.davis2351@email.com. You are independent, direct, flexible, patient. First, search for restaurants in San Francisco with a price range of $$ and Chinese cuisine to identify potential dining options for a client. Next, get restaurant details for restaurant ID R102 to verify operating hours and delivery zone, ensuring it meets the client's delivery needs. Finally, create an order for user U001 at restaurant ID R102 with items [I234] and delivery address 123 Market St, San Francisco, CA, to complete the client's request efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U085", "restaurant_id": "R102", "items": [{"item_id": "I234", "quantity": 1}], "delivery_address": "123 Market St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U176",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are optimistic, organized, logical, patient. First, search for Italian restaurants in the San Francisco area with a price range of $$ to $$$ to identify potential new partners for DoorDash. Once you have identified a promising restaurant, specifically restaurant R234, get the restaurant details to check its opening hours and delivery zones. This information will help determine if the restaurant's schedule and delivery capabilities align with DoorDash's service requirements.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is John Garcia and your email is john.garcia7961@email.com. You are organized, flexible, direct, polite. First, search for Mexican restaurants in San Francisco with a price range of $$. Once you have identified a suitable restaurant, get the menu for restaurant ID R1024 to check available taco options. This will help us ensure that we are offering a variety of choices to our customers on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U045",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are confident, polite. Get the restaurant menu for restaurant ID R321 to explore available dishes",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R321"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U105",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are logical, optimistic. First, search for restaurants in the downtown area with a price range of $$ to $$$ to identify potential new partners for DoorDash. Once you have a list, get the restaurant details for restaurant ID R12345 to verify it is open and check delivery zones, ensuring it aligns with our current service areas.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"location": "downtown", "price_range": "$$ to $$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R12345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U016",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are organized, polite. Begin by searching for restaurants in San Francisco offering Mexican cuisine within a moderate price range. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R1023 to review hours of operation and user reviews, ensuring it meets your dining preferences. After confirming the restaurant's suitability, get the restaurant menu for restaurant ID R1023, focusing on the Tacos category. Finally, add item I202 (Chicken Taco) to the cart for user ID U8206 with quantity 3 and extra guacamole customization, preparing the order for a delightful meal through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U016", "restaurant_id": "R1023", "item_id": "I202", "quantity": 3, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U081",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are flexible, cautious, logical. Search for restaurants offering Mexican cuisine in Jennifer's area with a moderate price range and get the menu for restaurant R567 focusing on the 'Tacos' category. This will help in deciding the best options for a potential partnership with DoorDash to expand delivery services in that area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are patient, optimistic. You are planning a cozy dinner at home and want to enjoy some Italian cuisine. First, search for Italian restaurants in San Francisco with a moderate price range of $$ to find a suitable option. Once you have identified a restaurant that catches your interest, get the restaurant details to ensure it meets your expectations. After confirming the restaurant's details, proceed to create an order for a delicious Italian meal, ensuring it will be delivered to your address at 123 Main St, San Francisco, using your credit card for payment.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U095", "restaurant_id": "R001", "items": [{"item_id": "I001", "quantity": 2}, {"item_id": "I002", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit_card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U093",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are patient, organized, direct, polite. First, search for Italian restaurants in the downtown area with a price range of $$. Once you have identified a few options, get restaurant details for restaurant R102 to check its menu and hours, specifically focusing on the pasta category. This information will help in making informed decisions for potential partnerships with DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U046",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are flexible, patient. Search for Italian restaurants in Patricia Williams' area with a price range of $$.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U046"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Patricia Williams", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U110",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are organized, independent, logical. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to identify potential options for a dinner order. Once you have a list, get details for restaurant R101 to verify it meets the delivery zone and is currently open, ensuring it can fulfill the order. Finally, get the menu for restaurant R101 to find available pasta dishes, so you can proceed with creating an order for user U5441 with items [I202, I203], using delivery address \"123 Main St, Apt 4B\" and payment method \"Credit Card\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U110", "restaurant_id": "R101", "items": [{"item_id": "I202", "quantity": 1}, {"item_id": "I203", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is Mary Williams and your email is mary.williams2739@email.com. You are independent, direct. Create order for user Linda Brown with restaurant ID R2345, including items I6789 and I6790, with delivery address 123 Main St, using credit card payment method.",
        actions=[
            Action(
                name="create_order",
                kwargs={"user_id": "U104", "restaurant_id": "R2345", "items": [{"item_id": "I6789", "quantity": 1}, {"item_id": "I6790", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are organized, independent, polite, flexible. Get the menu for restaurant ID R1024 to view available items in the Tacos category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1024", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are flexible, confident, independent. Get the menu for restaurant R234 to review available items.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are confident, optimistic, organized, patient. First, search for Italian restaurants in San Francisco within a mid-range price category to find suitable dining options for potential customers. Once you have identified a promising restaurant, get the restaurant details for restaurant ID R1023 to check its operating hours and location, ensuring it fits the delivery schedule and area. Finally, create an order for user Mary Miller (user ID U1688) at restaurant ID R1023 with items I567 and I568, specifying delivery to 123 Main St, San Francisco, with payment via credit card and no special instructions, ensuring a smooth and efficient ordering process for our valued customer.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U132", "restaurant_id": "R1023", "items": [{"item_id": "I567", "quantity": 1}, {"item_id": "I568", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9197@email.com. You are independent, flexible. get_restaurant_menu(restaurant_id=\"R123\")",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is Mary Williams and your email is mary.williams2739@email.com. You are polite, patient, organized, direct. Get the restaurant menu for restaurant R987 to browse available items.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are optimistic, polite. First, search for restaurants with Italian cuisine in San Francisco with a mid-range price to explore dining options for a family gathering. Once you have identified a suitable restaurant, get restaurant details for restaurant ID R2468 to check operating hours and delivery zones, ensuring it fits your schedule and location. Finally, create an order for user ID U5428 at restaurant ID R2468 with items I1357 and I2468, using delivery address 123 Market St, San Francisco, and payment method ending in 1234, to enjoy a delightful Italian meal delivered to your doorstep.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2468"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U113", "restaurant_id": "R2468", "items": [{"item_id": "I1357", "quantity": 1}, {"item_id": "I2468", "quantity": 1}], "delivery_address": "123 Market St, San Francisco", "payment_method": "1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are organized, direct, cautious, flexible. First, search for Mexican restaurants in San Francisco with a price range of $$. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R987 to check their operational hours. After confirming that the restaurant is open, create an order for user ID U7947 with restaurant ID R987, including items [I321, I654], delivery address 123 Main St, payment method credit card, and special instructions \"Leave at door.\"",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R987"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U006", "restaurant_id": "R987", "items": ["I321", "I654"], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is Mary Miller and your email is mary.miller1688@email.com. You are confident, logical, organized. Get the restaurant menu for restaurant ID R102 to view available Mexican dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102", "category": "Mexican"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U123",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are logical, organized. Create order for user Jennifer Miller with restaurant ID R567 including items I234 and I345, using saved delivery address.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U123"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U123", "restaurant_id": "R567", "items": [{"item_id": "I234", "quantity": 1}, {"item_id": "I345", "quantity": 1}], "delivery_address": "saved", "payment_method": "default"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are polite, organized, flexible. search_restaurants(location=\"San Francisco\", cuisine=\"Italian\", price_range=\"$$\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U002",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are patient, logical. First, search for restaurants in the downtown area with a cuisine of \"Italian\" and a price_range of \"$$\" to find suitable dining options. Once you have identified a potential restaurant, get restaurant details for restaurant_id R001 to check the menu and hours of operation. If the restaurant meets the requirements, proceed to get the restaurant menu for restaurant_id R001 with category \"Pasta\" to explore specific dishes. Finally, add item I123 (Spaghetti Carbonara) to the cart for user Patricia Brown (user_id U1001) with quantity 1 and no customizations, ensuring a seamless ordering experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U002", "restaurant_id": "R001", "item_id": "I123", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U037",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are polite, organized. First, search for Italian restaurants located in the downtown area with a moderate price range of $$. Once you find a suitable restaurant, obtain its menu by using the restaurant's unique ID. This will help you decide on items to add to your cart for a seamless DoorDash order experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are optimistic, polite, patient. Get the menu for restaurant R001 to view available Italian dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Italian"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U123",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are cautious, logical, patient, flexible. First, search for Mexican restaurants in San Francisco with a price range of $$ and above to find suitable options for a team lunch. Once you have identified a promising restaurant, get the restaurant details for restaurant R5678 to ensure it meets the team's preferences and dietary needs. After confirming the restaurant's suitability, get the menu for restaurant R5678, specifically the Tacos category, and add item I789 (Chicken Tacos) to cart for user U1234 with quantity 3 and extra salsa customization to prepare for the order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U123", "restaurant_id": "R5678", "item_id": "I789", "quantity": 3, "customizations": "extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are patient, confident, direct, independent. First, get details for restaurant R987 to check its opening hours and contact information, as this will help determine the best time to place an order. Then, create an order for user U001 at restaurant R987 with items [I321], using delivery address \"123 Main St, San Francisco\" and payment method \"credit card\". This sequence ensures that you have all necessary information to efficiently coordinate the delivery process for DoorDash.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R987"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U158", "restaurant_id": "R987", "items": [{"item_id": "I321", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Linda Davis and your email is linda.davis2351@email.com. You are optimistic, independent, patient, direct. First, search for Italian restaurants in the San Francisco area with a price range of $$. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R2345 to check opening hours to ensure it fits your schedule. After confirming the restaurant is open, create an order for user ID U1234 from restaurant ID R2345 with items I6789 and I6790, using delivery address \"123 Market St, San Francisco, CA\" and payment method \"credit card\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U030", "restaurant_id": "R2345", "items": [{"item_id": "I6789", "quantity": 1}, {"item_id": "I6790", "quantity": 1}], "delivery_address": "123 Market St, San Francisco, CA", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U187",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are polite, logical. Search for restaurants offering Mexican cuisine in the downtown area with a price range of $$.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U110",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are direct, confident, polite. First, search for Thai restaurants in the Los Angeles area with a price range of $$. Once you have identified restaurant R345, get the menu for this restaurant and focus on the 'Entrees' category. This information will help us enhance our offerings on DoorDash by ensuring we have up-to-date and diverse entree options from popular local Thai restaurants.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Thai", "location": "Los Angeles", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R345", "category": "Entrees"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U061",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are optimistic, logical, confident. Search for restaurants in Patricia Miller's area with cuisine type 'Italian' and price range '$$'. After identifying potential options, get detailed information for restaurant ID R101 to verify opening hours and delivery zones, ensuring it fits Patricia's schedule and location. Once confirmed, get the menu for restaurant ID R101 to explore available pasta dishes and add item ID I301 (Spaghetti Carbonara) to Patricia Miller's cart with quantity 1, preparing her order for a delightful Italian meal through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Patricia Miller's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U061", "restaurant_id": "R101", "item_id": "I301", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are optimistic, patient, polite, direct. First, search for Mexican restaurants in San Francisco with a price range of $$ to $$$ to find a suitable option for a potential order. After identifying a promising restaurant, get details for restaurant R5678 to check the menu and operating hours, ensuring it meets the user's preferences and timing needs.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson8206@email.com. You are polite, direct. Please search for Mexican restaurants in the downtown area within the mid-price range to find potential options for our upcoming team lunch. Once you have identified a suitable restaurant, get the menu for restaurant ID R2345 to explore available taco options, as our team is particularly interested in trying different taco varieties.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are patient, cautious. First, search for restaurants offering Mexican cuisine in San Francisco within a mid-range price bracket to find suitable dining options. Once you have identified a potential restaurant, get detailed information for restaurant R987 to verify its opening hours and delivery zone, ensuring it fits your schedule and location. After confirming these details, get the menu for restaurant R987, focusing on the \"Tacos\" category to explore available options. This will help you decide on the best meal choice.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R987"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U035",
        instruction="Your name is Robert Williams and your email is robert.williams9426@email.com. You are flexible, patient. First, search for Italian restaurants in Linda's location with a moderate price range to find suitable dining options. Then, get restaurant details for the restaurant with ID R2345 to check its opening hours, ensuring it fits within Linda's schedule. Finally, create an order for user U5883 with restaurant ID R2345, including items I6789 and I6790, and set the delivery address to Linda's address, ensuring a seamless dining experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U035", "restaurant_id": "R2345", "items": [{"item_id": "I6789", "quantity": 1}, {"item_id": "I6790", "quantity": 1}], "delivery_address": "Linda's address"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U046",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are logical, flexible. Search for restaurants with cuisine type 'Italian' within Patricia Williams' location.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U046"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Patricia Williams' location"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U061",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are patient, cautious. search_restaurants(location=\"San Francisco\", cuisine=\"Mexican\", price_range=\"medium\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"location": "San Francisco", "cuisine": "Mexican", "price_range": "medium"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are direct, organized, confident, logical. First, search for restaurants in the San Francisco area offering Mexican cuisine within a moderate price range. Once you have identified potential options, get detailed information about the restaurant with ID R5678 to check its location and hours of operation. This will help us ensure that the restaurant is conveniently located and open during our desired delivery times for DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U176",
        instruction="Your name is Michael Smith and your email is michael.smith2502@email.com. You are optimistic, flexible, polite. Search for Mexican restaurants in San Francisco within the price range of $10-$20, focusing on those that offer takeout and delivery options. Once you have identified a suitable restaurant, get the menu for restaurant R4567 to identify available items that fit within the budget and preferences of the user. This will help ensure a smooth and efficient ordering process for DoorDash customers.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U016",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are patient, independent. Search for Chinese restaurants in Jennifer's neighborhood with a price range of $10-$30",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "Jennifer's neighborhood", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are organized, optimistic, direct, logical. First, get the restaurant menu for restaurant R456 to find available taco options. Once you confirm that Chicken Taco is available, add item I789 (Chicken Taco) to cart for user linda.garcia2772@email.com with quantity 3.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U041", "restaurant_id": "R456", "item_id": "I789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are direct, independent. First, search for restaurants with Chinese cuisine in the San Francisco area with a mid-range price to expand our delivery options. Once you identify a potential restaurant, get the menu for restaurant ID R101, focusing on the 'Entrees' category, to ensure it meets our quality standards and offers a variety of dishes that appeal to our customer base.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Entrees"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U176",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are confident, logical, optimistic, independent. First, search for restaurants in the downtown area offering Mexican cuisine with a price range of $10-$20 to find potential dining options. Once you have identified a potential restaurant, get restaurant details for restaurant ID R5678 to verify hours of operation and delivery zones, ensuring it fits your schedule and location. Finally, get the menu for restaurant ID R5678 to explore available items for order, and then add item ID I234 (Chicken Tacos) to the cart for user ID U1234 with quantity 3 and no customizations, preparing for a seamless ordering experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U176", "restaurant_id": "R5678", "item_id": "I234", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U077",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are logical, flexible. Create order for user Linda Garcia using restaurant ID R5678 with items [I2345, I6789] and delivery address \"123 Main St, Apt 4B\"",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R5678", "item_id": "I2345"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R5678", "item_id": "I6789"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U077", "restaurant_id": "R5678", "items": [{"item_id": "I2345", "quantity": 1}, {"item_id": "I6789", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U105",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are organized, flexible, logical. Search for restaurants offering Mexican cuisine in Jennifer Brown's location with a price range of $10-$30.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U105"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer Brown's location", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are direct, patient, optimistic. First, search for restaurants offering Mexican cuisine in Linda Williams' local area within a moderate price range to find suitable dining options. Once you have identified a potential restaurant, get detailed information for restaurant R3412 to check its hours of operation to ensure it fits within the desired dining time. After confirming the restaurant's availability, get the menu for restaurant R3412, focusing on the 'Tacos' category to see available options. This will help in making an informed decision for placing an order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Williams' local area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R3412"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R3412", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are direct, organized, optimistic, polite. Begin by searching for Italian restaurants in San Francisco with a price range of $$ to identify potential new partners for DoorDash. Once you have a list, focus on restaurant R10234 and get details to confirm their opening hours and delivery area, ensuring they align with our service requirements.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R10234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson5028@email.com. You are confident, polite. First, search for Italian restaurants located in Downtown with a price range of $$ to find a suitable dining option. Once you have identified a restaurant of interest, retrieve its details to ensure it meets your preferences and expectations. After confirming the restaurant choice, proceed to explore the pasta category of its menu and add a pasta dish to your cart, making sure to customize it with extra cheese, if desired, to enhance your dining experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U180", "restaurant_id": "R001", "item_id": "I001", "quantity": 1, "customizations": "extra cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U128",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are flexible, confident. Search for restaurants offering Mexican cuisine in Jennifer Williams' local area. Once you have identified a suitable restaurant, get the menu for restaurant ID R567 to find available items for ordering.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer Williams' local area"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is Patricia Miller and your email is patricia.miller3271@email.com. You are optimistic, independent, polite. Search for Mexican restaurants in the San Francisco area with a price range of $$.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are confident, optimistic. First, search for Italian restaurants in Linda Jones' area with a mid-range price preference to identify potential dining options for her upcoming dinner plans. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R102 to check its ratings and operational hours. This will help ensure that the restaurant meets her expectations and is open during her preferred dining time.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda Jones' area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are polite, cautious. First, search for Italian restaurants in Jennifer Smith's location with a price range of moderate to find suitable dining options. Once you have identified a restaurant, get the restaurant menu for restaurant ID R456 to explore available Italian dishes. This will help Jennifer make an informed decision about her order through DoorDash.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U158"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Jennifer Smith's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is John Brown and your email is john.brown5124@email.com. You are cautious, direct. First, search for Italian restaurants in San Francisco with a price range of medium to identify potential dining options. Once you have a list, get restaurant details for restaurant ID R234 to verify if it's open and its delivery zone, ensuring it can deliver to your area. After confirming the restaurant's availability, create an order for user ID U1001 at restaurant ID R234 with items I567 and I568, using delivery address 123 Main St, payment method credit card, and special instructions \"Leave at door.\"",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U030", "restaurant_id": "R234", "items": [{"item_id": "I567", "quantity": 1}, {"item_id": "I568", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are organized, optimistic, cautious, direct. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a restaurant, get the restaurant menu for restaurant ID R245, focusing on the 'Pasta' category, to explore their offerings. If Spaghetti Carbonara is available, proceed to add item I678 (Spaghetti Carbonara) to cart for user ID U123 with quantity 1 and extra cheese customization. This will ensure the user has a delightful meal ready for order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R245", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U158", "restaurant_id": "R245", "item_id": "I678", "quantity": 1, "customizations": "extra cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are direct, independent. search_restaurants(cuisine=\"Italian\", location=\"New York, NY\", price_range=\"$$\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York, NY", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U046",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are cautious, organized, direct. First, search for Italian restaurants located downtown with a moderate price range. Once you find a suitable restaurant, add a Margherita pizza to your cart from the restaurant with ID R123, ensuring to customize it with extra sauce and no cheese.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U046", "restaurant_id": "R123", "item_id": "I001", "quantity": 1, "customizations": {"extra_sauce": true, "no_cheese": true}}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U055",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are independent, confident, flexible. Get the menu for restaurant ID R2345 to explore available taco options.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U193",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are confident, flexible, direct, organized. Search for restaurants offering Mexican cuisine in the San Francisco downtown area, and once you find a suitable option, get the menu for restaurant ID R2345, focusing on the \"Tacos\" category. This will help you ensure that the restaurant offers a good variety of tacos, which is important for your upcoming team lunch order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco downtown"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U046",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are direct, patient, organized. First, search for Italian restaurants in the downtown area with a price range of moderate to find potential dining options for our users. Next, get restaurant details for restaurant ID R001 to verify business hours, ensuring it aligns with our delivery schedule. Finally, create an order for user ID U001 at restaurant ID R001 with items I101 and I102, using the delivery address 123 Main St, and process the payment method via credit card to complete the transaction efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U046", "restaurant_id": "R001", "items": [{"item_id": "I101", "quantity": 1}, {"item_id": "I102", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U002",
        instruction="Your name is Mary Jones and your email is mary.jones4200@email.com. You are confident, optimistic. First, search for restaurants offering Mexican cuisine in Patricia Brown's vicinity to find suitable dining options. Once you identify a restaurant, get the menu for restaurant R567, focusing on the \"Main Dishes\" category, to ensure they offer items Patricia might enjoy. This will help you make an informed decision about adding items to her cart on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Patricia Brown's vicinity"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Main Dishes"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are direct, patient, logical, polite. First, get restaurant details for restaurant ID R231 to verify opening hours and delivery zone, ensuring the restaurant can deliver to 123 Main St. Next, get the restaurant menu for restaurant ID R231 to view available items and categories, confirming that Chicken Tacos are offered. Then, add item I789 (Chicken Tacos) to cart for user Linda Garcia (user ID U5307) with quantity 3, preparing for order placement.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R231"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R231"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U106", "restaurant_id": "R231", "item_id": "I789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are flexible, confident, patient, polite. First, get the menu for restaurant R567, focusing on the \"Main Course\" category to understand the available options. Then, create an order for user U9607 at restaurant R567 with items [I789, I790], ensuring the delivery address is 123 Main St, and use a credit card as the payment method.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Main Course"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U140", "restaurant_id": "R567", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are polite, organized, confident. Search for restaurants in the downtown area specializing in Mexican cuisine to identify potential options for a new promotional campaign. Once you have identified a suitable restaurant, get the menu for restaurant R5678 to find available taco options, ensuring that the menu aligns with the campaign's focus on authentic Mexican dishes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are flexible, independent. Search for restaurants offering Mexican cuisine in the user’s area with a moderate price range, and once you find a suitable option, get the restaurant menu for restaurant ID R1023 to explore available items.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U190",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are confident, direct. Search for Italian restaurants in the San Francisco area with a price range of $$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R56789 to explore available pasta dishes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R56789"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are flexible, confident, organized, polite. First, search for Mexican restaurants in the downtown area with a price range of $$ to $$$ to find potential dining options for our customers. Next, get restaurant details for restaurant_id R234 to check if it's open and meets delivery zone requirements, ensuring it can serve our target area. Finally, create an order for user_id U1001 at restaurant_id R234 with items [I567, I890], delivery_address \"123 Main St, Downtown\", and payment_method \"credit_card\" to provide a seamless dining experience for our customer.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U041", "restaurant_id": "R234", "items": [{"item_id": "I567", "quantity": 1}, {"item_id": "I890", "quantity": 1}], "delivery_address": "123 Main St, Downtown", "payment_method": "credit_card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are polite, patient, optimistic. Add item I789 (Spaghetti Carbonara) to Mary's cart for restaurant R1023 with quantity 1.",
        actions=[
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U112", "restaurant_id": "R1023", "item_id": "I789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is Patricia Jones and your email is patricia.jones4973@email.com. You are organized, direct. Search for restaurants offering Mexican cuisine in San Francisco within a moderate price range. Once you have identified a suitable restaurant, get details for restaurant R2023 to verify it is open and check for minimum order requirements. If the restaurant meets the criteria, create an order for user U6303 at restaurant R2023 with items I789 and I790, ensuring the delivery address is 123 Market St, San Francisco, and the payment method is a credit card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2023"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U019", "restaurant_id": "R2023", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Market St, San Francisco", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are polite, optimistic, direct, confident. Search for restaurants in the downtown area offering Mexican cuisine with a price range of $10-$20",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are independent, patient, optimistic, confident. Search for restaurants with Mexican cuisine in San Francisco within a mid-range price bracket to find potential dining options. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R567 to explore available items. This will help you decide on the best dishes to recommend for a meal delivery service like DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U176",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are polite, independent, cautious. add_item_to_cart(user_id=\"U1234\", restaurant_id=\"R001\", item_id=\"I1001\", quantity=2)",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U176"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R001", "item_id": "I1001"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U176", "restaurant_id": "R001", "item_id": "I1001", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U105",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are independent, patient, optimistic. First, search for Italian restaurants in the Madison Square area with a price range of $$. Once you have identified potential options, focus on restaurant R1023. Get the restaurant details for R1023 to verify its opening hours, ensuring it aligns with peak delivery times. This information will help you assess its suitability for a potential partnership with DoorDash, focusing on optimizing delivery availability during high-demand periods.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Madison Square", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are organized, optimistic, polite. First, search for restaurants offering Mexican cuisine in the downtown area to identify potential partners for expanding Doordash's delivery options. Once you have a list, focus on restaurant R567 by getting its details to check operational hours and ratings. This will help assess its suitability for a partnership based on customer satisfaction and availability.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Robert Brown and your email is robert.brown1066@email.com. You are polite, patient. Search for Chinese restaurants in the user's location with a moderate price range.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U095"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are cautious, polite, confident, patient. You are planning a dinner for your family and want to order Italian food from a restaurant in San Francisco. First, search for Italian restaurants in San Francisco within the $$ price range. After finding a suitable restaurant, retrieve the menu for the Pasta category from the restaurant with ID \"R2345\". Once you've decided on a pasta dish, add the item with ID \"I6789\" to your cart with a quantity of 1, using your user ID \"U1024\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U112", "restaurant_id": "R2345", "item_id": "I6789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are patient, polite, cautious, logical. First, search for restaurants in the downtown area with a cuisine preference for Italian and a price range of $$. Once you have identified a suitable restaurant, get the menu for restaurant ID R1023 focusing on the Pasta category. This will help you find the perfect pasta dish to recommend to a customer looking for a delicious Italian meal.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U118",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are polite, patient. First, search for Mexican restaurants located in New York, NY that have a budget-friendly price range indicated by a single dollar sign. Once you have identified a potential option, proceed to get the restaurant's menu focusing specifically on the Tacos category. This information will help you determine the best restaurant to partner with for expanding DoorDash's affordable Mexican cuisine offerings in the area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "New York, NY", "price_range": "$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are confident, patient, organized, direct. First, search for restaurants offering vegan options in Linda's area with a moderate price range. Once you find a suitable restaurant, add item I123 (Vegan Burger) to the cart for user U3192 with quantity 1 and no customizations. This will ensure that Linda can enjoy a meal that aligns with her dietary preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Vegan", "location": "Linda's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U090", "restaurant_id": "R001", "item_id": "I123", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U134",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are organized, cautious, logical. First, search for restaurants with Mexican cuisine in the New York City area with a price range of $$ to $$$ to find an ideal option for a family dinner. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R234 to view available items in the Tacos category. After reviewing the menu, add item ID I678 (Chicken Tacos) to the cart for user ID U101 with a quantity of 3 and include extra guacamole customization, ensuring the order meets everyone's preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "New York City", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U134", "restaurant_id": "R234", "item_id": "I678", "quantity": 3, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are flexible, patient, polite, optimistic. Search for restaurants in Linda Garcia's location with a preference for Mexican cuisine.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U106"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Garcia's location"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Patricia Jones and your email is patricia.jones4973@email.com. You are patient, polite, organized, cautious. Search for restaurants in the downtown area offering Mexican cuisine with a price range of $10-$20. Once you find a suitable restaurant, get the menu for restaurant R567 to explore available taco options. This will help you make an informed decision for placing an order on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U133",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are optimistic, cautious. Get the menu for restaurant R5678 to explore available items.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are cautious, logical. First, search for Japanese restaurants in the San Francisco area with a price range of $$. Once you have identified a suitable restaurant, get the menu for restaurant R5678 focusing on the Sushi category. This will help you decide if the menu items align with your preferences before placing an order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Japanese", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Sushi"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is Mary Miller and your email is mary.miller1688@email.com. You are flexible, optimistic, polite. First, search for Mexican restaurants in San Francisco with a price range of $$ to find a suitable dining option for a client meeting. Once you have identified a promising restaurant, get restaurant details for restaurant ID R567 to check their operating hours and ensure they align with your meeting schedule. After confirming that the restaurant is open during your desired time, get the restaurant menu for restaurant ID R567 to view available tacos and add item I789 (Carne Asada Taco) to your cart for user U001 with quantity 3 and no onions, as per your client's preference.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U113", "restaurant_id": "R567", "item_id": "I789", "quantity": 3, "customizations": "no onions"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U128",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are patient, polite, flexible. First, search for restaurants in the Midtown area offering Mexican cuisine with a price range of $10-$20 to find suitable dining options for our customers. Next, get restaurant details for restaurant ID R245 to verify operating hours and location, ensuring that it fits within the desired timeframe and is conveniently located for delivery. Finally, create an order for user ID U567 at restaurant ID R245 with items [I1023], delivery address 123 Pine St, payment method credit card, and special instructions \"Leave at door,\" ensuring a seamless and satisfactory delivery experience for the customer.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Midtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R245"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U128", "restaurant_id": "R245", "items": [{"item_id": "I1023", "quantity": 1}], "delivery_address": "123 Pine St", "payment_method": "credit card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are polite, flexible, cautious, logical. First, search for Mexican restaurants in Linda Garcia's area with a price range of $10-$20 to find suitable dining options. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R234 to check if it is open and delivers to Linda Garcia's address. If the restaurant is open and delivers, proceed to get the menu for restaurant ID R234 to see available items in the Tacos category. If Chicken Tacos are available, add item I678 (Chicken Taco) to the cart for user Linda Garcia with quantity 3 and extra guacamole customization to complete the order preparation.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Garcia's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U041", "restaurant_id": "R234", "item_id": "I678", "quantity": 3, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are optimistic, independent, flexible, patient. Get the restaurant menu for restaurant ID R234, focusing on the 'Tacos' category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U128",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are direct, optimistic. First, search for Italian restaurants in San Francisco within the $$ price range to find a suitable dining option. Once you have identified a restaurant, get the restaurant menu focusing on the Pasta category to explore available dishes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is John Garcia and your email is john.garcia7961@email.com. You are cautious, direct. First, search for Italian restaurants in San Francisco with a price range of $$ to $$$ to identify potential dining options for a client meeting. Once you have selected a suitable restaurant, get the restaurant menu for restaurant ID R321, focusing on the pasta category, to ensure it meets the client's preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$,$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R321", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U075",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are patient, flexible, optimistic, organized. Search for Italian restaurants in the downtown area with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a restaurant, get the restaurant menu for restaurant ID R456 to view available Italian dishes. This will help you make an informed decision for placing an order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$,$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U118",
        instruction="Your name is Mary Brown and your email is mary.brown1791@email.com. You are direct, polite, organized. Please search for Italian restaurants in San Francisco with a moderate price range ($$). Once you have identified a suitable restaurant, obtain the restaurant details to ensure it meets your requirements. After confirming the restaurant, proceed to get the menu specifically for the Pasta category. If you find a desirable pasta dish, add two portions of it to the cart for user ID U6714.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U118", "restaurant_id": "R001", "item_id": "I001", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U190",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are confident, independent. Get the menu for restaurant ID R567 to find available pasta dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U190",
        instruction="Your name is John Brown and your email is john.brown5124@email.com. You are polite, direct, organized. First, search for restaurants with cuisine 'Mexican' in 'San Francisco' with a price range of '$$' to find a suitable dining option. Once you have identified a restaurant, get the restaurant menu for restaurant ID 'R1001' to view available items. This will help you decide on the best items to order for user ID 'U5151' with delivery to '123 Market St, San Francisco, CA'.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are independent, patient, logical, organized. You need to search for restaurants with Mexican cuisine in the Los Angeles area within a moderate price range to expand DoorDash's delivery options. Once you have identified potential restaurants, get the restaurant details for restaurant R1024 to verify opening hours and delivery zones, ensuring they align with DoorDash's operational requirements.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Los Angeles", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U050",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are polite, confident. First, search for Italian restaurants located in the downtown area with a moderate price range of $$. Once you have identified a restaurant of interest, get the details of the restaurant using its ID, R123, to ensure it meets your dining preferences. After confirming the restaurant's suitability, proceed to explore their menu, specifically focusing on the pizzas category, to find a dish that appeals to you. Finally, add two quantities of your selected pizza item, identified by item ID I456, to your cart for a seamless ordering experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R123"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "pizzas"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U050", "restaurant_id": "R123", "item_id": "I456", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are polite, optimistic, logical, confident. First, search for restaurants in Midtown with Italian cuisine and a price range of $$. Once you find a suitable restaurant, get the restaurant details for restaurant ID R2345 to confirm it is open and meets delivery zone requirements. After confirming these details, create an order for user U9904 with restaurant ID R2345, including items I6789 and I6790, with the delivery address 123 Main St, and use a credit card as the payment method.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Midtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U048", "restaurant_id": "R2345", "items": [{"item_id": "I6789", "quantity": 1}, {"item_id": "I6790", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U035",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are independent, optimistic. Get the restaurant menu for restaurant ID R234, focusing on the entrees category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "entrees"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U142",
        instruction="Your name is Mary Miller and your email is mary.miller1688@email.com. You are optimistic, polite. Search for Italian restaurants in the San Francisco area with a price range of $$ to $$$, focusing on those that might be suitable for a new partnership with DoorDash. Once you have identified potential candidates, get restaurant details for restaurant R102 (an Italian restaurant found in the previous search) to confirm its operating hours, ensuring it aligns with peak delivery times.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U138",
        instruction="Your name is Patricia Jones and your email is patricia.jones4973@email.com. You are optimistic, polite, logical, patient. Get the restaurant menu for restaurant ID R1234, focusing on the pizza category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1234", "category": "pizza"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9197@email.com. You are patient, logical. Get restaurant menu for restaurant ID R987 to view available menu items",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are organized, patient, flexible. Get the restaurant menu for restaurant ID R987 to view available items.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are direct, cautious, confident, organized. Get the menu for restaurant ID R345 to identify available items and categories.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are organized, cautious. First, search for sushi restaurants in the San Francisco area with a price range of $$ to $$$ to ensure a variety of options for potential orders. Next, get restaurant details for restaurant ID R5678 to verify operating hours and delivery zones, ensuring the restaurant is operational and can deliver to the desired location. Finally, create an order for user ID U1234 with restaurant ID R5678, including item I7890 (Spicy Tuna Roll) and delivery address 123 Main St, using the payment method 'credit card' to complete the transaction efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"location": "San Francisco", "price_range": "$$,$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U076", "restaurant_id": "R5678", "items": [{"item_id": "I7890", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is Michael Smith and your email is michael.smith2502@email.com. You are confident, polite, optimistic. Search for restaurants offering vegan cuisine in the downtown area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "vegan", "location": "downtown"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U050",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are cautious, polite. Get restaurant menu for restaurant ID R102 to find available pasta dishes",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are organized, direct, patient, optimistic. First, search for restaurants in Patricia's area with a focus on vegetarian cuisine to ensure a wide selection of options. Next, get the menu for restaurant ID R456 to check for available vegetarian options, ensuring that Patricia has choices that suit her dietary preferences. Finally, create an order for user Patricia Jones with restaurant ID R456, including items I789 (Vegetarian Burger) and I790, with delivery address as Patricia's home address and payment method set to credit card, providing a seamless and satisfying ordering experience on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Vegetarian", "location": "Patricia's area"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U192", "restaurant_id": "R456", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "Patricia's home address", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are cautious, optimistic, organized, direct. Search for Italian restaurants in the downtown area with a price range of $10-$30. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R101 to check opening hours and delivery zones. If the restaurant meets your criteria, proceed to get the menu for restaurant ID R101, focusing on the \"Pasta\" category, to decide on potential dishes for an upcoming order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U105",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are optimistic, polite. search_restaurants(location=\"San Francisco\", cuisine=\"Mexican\", price_range=\"$$\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"location": "San Francisco", "cuisine": "Mexican", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U087",
        instruction="Your name is Robert Williams and your email is robert.williams9426@email.com. You are organized, polite, logical, optimistic. First, search for restaurants offering vegan options in the downtown area to identify potential dining choices for a client meeting. Once you have identified a suitable restaurant, get the menu for restaurant ID R1023, focusing on the \"Vegan Delights\" category, to ensure they offer a variety of appealing dishes. After confirming the menu meets the client's preferences, add item ID I234 (Vegan Burger) to cart for user ID U567 with quantity 1 and no bun customization. This will help finalize the order for the client, ensuring a smooth and efficient dining experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "vegan", "location": "downtown"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Vegan Delights"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U087", "restaurant_id": "R1023", "item_id": "I234", "quantity": 1, "customizations": "no bun"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are optimistic, flexible, logical, direct. Add item I789 (Spaghetti Carbonara) to cart for user Jennifer Davis with restaurant ID R567.",
        actions=[
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U076", "restaurant_id": "R567", "item_id": "I789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U016",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are direct, independent, cautious. Search for restaurants offering Mexican cuisine in the vicinity of Jennifer Johnson's location within a moderate price range.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U016"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer Johnson's location", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U007",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are organized, optimistic. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$20 to find a suitable dining option for a client's lunch meeting. Once you have identified a restaurant, get the menu for restaurant ID R2345 to find available dishes in the \"Tacos\" category, ensuring there are enough options to cater to different preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are polite, confident, direct. First, search for restaurants in New York City with Italian cuisine and a medium price range to find a suitable dining option for our customer. Once you have identified a restaurant, get the menu for restaurant ID R78956 to find available pasta dishes, as our customer has expressed a preference for pasta. After reviewing the menu, add item I23456 (Spaghetti Carbonara) to the cart for user ID U12345 with quantity 1 and no customizations. This will ensure we have the correct item ready for the order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R78956"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U143", "restaurant_id": "R78956", "item_id": "I23456", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are polite, optimistic. First, get the restaurant menu for restaurant ID R872 to view available items. Then, create an order for user Robert Garcia with restaurant ID R872, including items I231 (Chicken Tacos) and I245, delivering to 1234 Elm St, San Francisco.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R872"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U140", "restaurant_id": "R872", "items": [{"item_id": "I231", "quantity": 1}, {"item_id": "I245", "quantity": 1}], "delivery_address": "1234 Elm St, San Francisco"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U178",
        instruction="Your name is Michael Smith and your email is michael.smith2502@email.com. You are patient, independent, polite, flexible. Get the menu for restaurant ID R101, focusing on the \"Tacos\" category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Linda Miller and your email is linda.miller5151@email.com. You are organized, independent. Search for Italian restaurants in the downtown area with a price range of $$. Get the menu for restaurant R123 focusing on the Pasta category. Create order for user U001 at restaurant R123 including item I456 with delivery to 123 Elm Street, payment by card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "Pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U076", "restaurant_id": "R123", "items": [{"item_id": "I456", "quantity": 1}], "delivery_address": "123 Elm Street", "payment_method": "card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U105",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are patient, flexible, organized. search_restaurants(location=\"Downtown\", cuisine=\"Italian\", price_range=\"$$\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U007",
        instruction="Your name is James Williams and your email is james.williams9904@email.com. You are polite, independent, patient, cautious. First, search for restaurants with cuisine type 'Italian' in the neighborhood of 'Greenwood' with a price range of '$$'. Once you have identified potential options, get details for restaurant R1024 to verify its current operational status and minimum order requirement. This will ensure that you can confidently recommend this restaurant to DoorDash customers looking for Italian cuisine in the area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Greenwood", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are independent, flexible, organized. First, search for restaurants in the downtown area with cuisine type 'Mexican' and price range '$$' to identify potential new partners for DoorDash. Once you have a list, get restaurant details for restaurant ID R345 to check if it is open and meets delivery requirements, ensuring it aligns with our service standards and can be added to our platform.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U093",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams7359@email.com. You are patient, independent, logical, organized. First, search for Mexican restaurants in San Francisco within a mid-range price to identify potential dining options for a client meeting. Once you have identified a suitable restaurant, get the restaurant menu for restaurant R1023 to explore available tacos. This will help you decide if their offerings meet the client's preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U134",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are confident, direct, organized. Begin by searching for mid-priced Mexican restaurants in San Francisco to find suitable options for a team lunch. Once you have identified a promising restaurant, proceed to retrieve its menu to ensure they offer a variety of dishes that cater to different dietary preferences within your team.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are patient, flexible, optimistic, independent. First, search for restaurants offering Mexican cuisine in the downtown area with a price range of $10-$20 to find a suitable option for a customer looking to enjoy an affordable meal. Once you have identified a restaurant, get the restaurant menu for restaurant ID R567 to view available items and ensure they offer Chicken Tacos. If they do, add item I678 (Chicken Tacos) to the cart for user U101 with a quantity of 3 and no customizations, ensuring a seamless ordering experience for the customer.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U177", "restaurant_id": "R567", "item_id": "I678", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U050",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are flexible, direct, patient, organized. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $$. Once you have identified a suitable restaurant, get details for restaurant R56789 to check their operating hours and delivery zone to ensure they can deliver to the desired location. After confirming the restaurant's availability, get the menu for restaurant R56789, focusing on the \"Tacos\" category, and add item I2345 (Chicken Tacos) to cart for user U12345 with quantity 3 and extra guacamole.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R56789"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R56789", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U050", "restaurant_id": "R56789", "item_id": "I2345", "quantity": 3, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are flexible, patient. First, search for restaurants offering Mexican cuisine in Linda's vicinity with a moderate price range. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R567 to explore available items under the 'Tacos' category.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is Mary Brown and your email is mary.brown1791@email.com. You are organized, patient, optimistic, flexible. Create order for user John Brown at restaurant ID R202 with items T101 and T102, including delivery address 123 Main St.",
        actions=[
            Action(
                name="create_order",
                kwargs={"user_id": "U006", "restaurant_id": "R202", "items": [{"item_id": "T101", "quantity": 1}, {"item_id": "T102", "quantity": 1}], "delivery_address": "123 Main St"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Linda Miller and your email is linda.miller5151@email.com. You are logical, flexible, confident, cautious. Begin by searching for restaurants offering Mexican cuisine in the 94103 area with a price range of $10-$20 to find a suitable option for an upcoming order. Once you have identified a restaurant, retrieve the restaurant menu for restaurant ID R245 to find available tacos in the menu category \"Entrees.\" After confirming the availability of tacos, proceed to add item ID I789 (Chicken Taco) to the cart for user mary.miller1688@email.com with a quantity of 3 and no customizations. This sequence of actions will ensure a seamless order placement for the user on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "94103", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R245", "category": "Entrees"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U132", "restaurant_id": "R245", "item_id": "I789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are independent, confident, polite, organized. Create order for user John Williams with restaurant ID R210, including items Kung Pao Chicken and Spring Rolls, with delivery address as John's home.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R210"}
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "U030"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U030", "restaurant_id": "R210", "items": [{"item_id": "I001", "quantity": 1}, {"item_id": "I002", "quantity": 1}], "delivery_address": "John's home"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are independent, direct. First, use `get_user_details` with `user_id: mary.williams6067@email.com` to retrieve Mary's account information and verify her delivery address. Once you have confirmed her address, use `search_restaurants` with `cuisine: Italian`, `location: Mary's address`, `price_range: $$` to find Italian restaurants near Mary. This will help in providing her with suitable dining options for her next meal delivery.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U112"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Mary's address", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is Robert Brown and your email is robert.brown1066@email.com. You are independent, confident. Get restaurant menu for restaurant ID R234 to explore available Mexican dishes",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson8206@email.com. You are organized, independent. Search for restaurants with Mexican cuisine within 5 miles of Michael Miller's address.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U098"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Michael Miller's address"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are direct, optimistic, patient. Search for restaurants in Linda's location with cuisine \"Italian\" and price_range \"$$\"",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda's location", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are cautious, independent, polite. Get the menu for restaurant ID R6789 to find available taco options.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R6789"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U061",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are patient, logical. Search for restaurants offering vegan cuisine in Patricia Miller's location with a moderate price range. Once you find a suitable restaurant, get the menu for restaurant ID R234 to select vegan dishes.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U061"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Vegan", "location": "Patricia Miller's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U081",
        instruction="Your name is Mary Brown and your email is mary.brown1791@email.com. You are flexible, cautious, optimistic, polite. First, search for restaurants with Italian cuisine in San Francisco within a mid-range price to ensure a good selection for our customers. Once you have identified potential options, get restaurant details for restaurant ID R001 to verify operating hours and location, ensuring it meets our delivery criteria. Finally, create an order for user U9197 at restaurant ID R001 with items [I101, I102], delivering to 123 Main St, using a credit card for payment, and include the special instructions to \"Leave at doorstep.\" This sequence will ensure a smooth and satisfactory customer experience with DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U081", "restaurant_id": "R001", "items": [{"item_id": "I101", "quantity": 1}, {"item_id": "I102", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit_card", "special_instructions": "Leave at doorstep"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U016",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are polite, direct, logical. First, search for restaurants offering Mexican cuisine near Jennifer's location to find a suitable option for her dinner plans. Once you have identified a restaurant, specifically get the menu for restaurant R1023, focusing on the taco category, to ensure they offer a variety of taco options that might appeal to Jennifer.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer's location"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "taco"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are confident, optimistic, polite. First, search for Italian restaurants in San Francisco with a price range of $$-$$$ to find a suitable dining option. Once you have identified a restaurant, add item I305 (Spaghetti Carbonara) to cart for user U5678 with restaurant ID R1024, quantity 1, as part of preparing for a potential order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U167", "restaurant_id": "R1024", "item_id": "I305", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are direct, organized, polite. First, search for Italian restaurants in the San Francisco area with a price range of moderate to identify potential dining options. Once you have a list, get restaurant details for restaurant R5678 to confirm hours of operation and delivery zones, ensuring it fits within the desired criteria. Finally, create an order for user U1023 at restaurant R5678 with items [I2345, I6789], using the default delivery address and credit card payment, to complete the transaction seamlessly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U180", "restaurant_id": "R5678", "items": [{"item_id": "I2345", "quantity": 1}, {"item_id": "I6789", "quantity": 1}]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U007",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are polite, organized. First, search for Chinese restaurants in the 94103 area with a price range of $10-$20 per person to find a suitable dining option. Once you identify a restaurant, get the restaurant menu for restaurant ID R1023 to identify available dumplings. After confirming the availability of dumplings, add item ID I567 (Chicken Dumplings) to the cart for user ID U001 with a quantity of 3 and no customizations.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "94103", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U007", "restaurant_id": "R1023", "item_id": "I567", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is Patricia Miller and your email is patricia.miller3271@email.com. You are cautious, direct, confident, logical. Begin by searching for Mexican restaurants in San Francisco within a moderate price range to find suitable dining options. Once you have identified a potential restaurant, get details for restaurant ID R5678 to check its operating hours and customer reviews, ensuring it meets your expectations. Finally, create an order for user ID U123 at restaurant ID R5678 with items [I101, I102] and set the delivery address to 123 Main St, using a credit card as the payment method.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U151", "restaurant_id": "R5678", "items": [{"item_id": "I101", "quantity": 1}, {"item_id": "I102", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are flexible, optimistic. First, search for restaurants in New York City with cuisine type 'Mexican' and price range '$$' to identify potential new partners for DoorDash. Once you have identified a promising restaurant, get the restaurant details for restaurant ID R202 to verify hours of operation and location, ensuring it aligns with peak delivery times and accessibility for our delivery drivers.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R202"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are independent, polite. First, search for Italian restaurants in the Brooklyn area with a price range of $$ to $$$ to find suitable dining options. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R345 to check their operating hours and delivery zone, ensuring they can deliver to your location. After confirming the delivery zone, create an order for user U123 at restaurant R345 with items I567 and I568, using delivery address 123 Main St, payment method Credit Card, and special instructions \"Leave at doorstep\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Brooklyn", "price_range": "$$,$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U143", "restaurant_id": "R345", "items": [{"item_id": "I567", "quantity": 1}, {"item_id": "I568", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card", "special_instructions": "Leave at doorstep"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are logical, direct, confident, patient. Get the menu for restaurant ID R101 and filter by category 'Pasta'.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are confident, patient, polite, independent. search_restaurants(cuisine=\"Mexican\", location=\"San Francisco\", price_range=\"medium\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "medium"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U046",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are cautious, optimistic. First, search for Italian restaurants in the downtown area with a price range of $$-$$$ using the search_restaurants tool to identify potential partners for a new DoorDash promotion. Once you have a list, get detailed information for restaurant R567 using the get_restaurant_details tool to evaluate its suitability for the promotion based on factors like location, ambiance, and customer reviews.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U133",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are polite, patient. First, search for Italian restaurants in San Francisco with a price range of $$. Once you have identified potential options, get restaurant details for restaurant ID R1024 to verify it is open for orders. This will help ensure that the restaurant is available for delivery through DoorDash, providing customers with the best dining experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are polite, cautious, organized. First, search for restaurants with cuisine \"Italian\" in the location \"San Francisco\" with a price range of \"medium\" to explore dining options. Once you have identified a potential restaurant, get the restaurant details for restaurant_id \"R001\" to verify the hours and address, ensuring it fits your schedule and location preferences. After confirming the restaurant's suitability, proceed to get the restaurant menu for restaurant_id \"R001\" to find available pasta dishes. If \"Pasta Primavera\" is available and meets your taste preferences, add the item from restaurant_id \"R001\" to the cart for user_id \"U123\" with a quantity of 1, preparing for a delightful meal delivery.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U006", "restaurant_id": "R001", "item_id": "I001", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are logical, confident, patient. Search for restaurants offering Mexican cuisine in the user's area with a moderate price range.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is Mary Jones and your email is mary.jones4200@email.com. You are patient, organized, cautious, polite. First, search for restaurants with cuisine \"Mexican\" in the location \"San Francisco\" with a price range of \"$$\" to find suitable dining options for a customer. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R202 to confirm it is open and accepts orders, ensuring the customer can place an order without any issues. Finally, create an order for user ID U9904 with restaurant ID R202, including items I789 and I790, using the delivery address \"123 Market St, San Francisco\" and payment method \"Credit Card\" to complete the customer's request efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R202"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U048", "restaurant_id": "R202", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Market St, San Francisco", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are logical, optimistic, patient. First, search for restaurants offering Mexican cuisine in the Midtown area with a budget-friendly price range to find suitable options for user U9904. Once you identify restaurant R234 as a potential choice, get the menu for this restaurant and identify available taco offerings to ensure they have what the user desires. After confirming that Chicken Tacos are available, add item I567 (Chicken Tacos) to the cart for user U9904 with a quantity of 3 and no customizations.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Midtown", "price_range": "$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U048", "restaurant_id": "R234", "item_id": "I567", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are cautious, organized. First, search for restaurants with cuisine type \"Mexican\" in the location \"San Francisco\" within a moderate price range to identify potential options for a team lunch. Once you have a list of options, get restaurant details for restaurant ID \"R2345\" to confirm their hours and delivery zone, ensuring it fits within our schedule and delivery area for a seamless DoorDash order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are direct, optimistic, organized, patient. First, search for restaurants offering Mexican cuisine in the San Francisco area with a mid-range price. Once you have identified a suitable restaurant, obtain the restaurant menu for restaurant ID R234 to find available taco options. This will help you ensure that the restaurant offers the desired items before proceeding with any orders.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U105",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are logical, direct, confident, polite. First, search for Italian restaurants in the Midtown area with a price range of $$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant R456 to review available pasta dishes. This will help us ensure that the menu aligns with our customer's preferences and budget for a seamless DoorDash experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Midtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are polite, patient. First, search for Italian restaurants in John's area with a price range of $10-$30 to find a suitable dining option. Once you identify a restaurant that matches the criteria, get the menu for restaurant ID R456 focusing on the \"Pasta\" category. This will help you decide on a pasta dish to order. If Spaghetti Carbonara is available, proceed to add item I789 (Spaghetti Carbonara) to the cart for user U123 with quantity 1 and no customizations.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U006", "restaurant_id": "R456", "item_id": "I789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is Michael Smith and your email is michael.smith2502@email.com. You are patient, independent, cautious. First, search for restaurants with Mexican cuisine near the San Francisco area with a price range of $10-$30 to find a suitable dining option. Once you have identified a potential restaurant, get the menu for restaurant R2345, focusing on the \"Tacos\" category to explore available options. After reviewing the menu, add item I5678 (Chicken Taco) to the cart for user U8901 with quantity 3 and extra cheese customization to complete your order on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U085", "restaurant_id": "R2345", "item_id": "I5678", "quantity": 3, "customizations": "extra cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U118",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are patient, independent, confident, optimistic. First, search for restaurants in Linda Smith's area with a preference for Mexican cuisine and a moderate price range to find suitable dining options. Once you have identified a restaurant, get the restaurant details for restaurant ID R987 to check their ratings and operational hours to ensure it meets quality standards and is open during your preferred dining time. Finally, get the menu for restaurant ID R987 with a focus on the 'Tacos' category, and add item ID I234 (Chicken Tacos) to the cart for user ID U123 with a quantity of 3 and extra salsa customization to complete the order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Smith's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R987"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U118", "restaurant_id": "R987", "item_id": "I234", "quantity": 3, "customizations": "extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U187",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are confident, cautious, organized, flexible. Get the restaurant menu for restaurant ID R102 to find available taco options.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U134",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are optimistic, logical. First, search for Mexican restaurants in San Francisco with a moderate price range. Once you have identified a potential restaurant, get the details of the restaurant with ID \"R001\" to ensure it meets your preferences. After confirming the restaurant is a good choice, proceed to get the menu for the entrees category to decide on your order. Finally, create an order for two of the selected entree items from restaurant \"R001\" and have them delivered to 123 Main St, San Francisco, CA, using your credit card as the payment method.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "entrees"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U134", "restaurant_id": "R001", "items": [{"item_id": "I001", "quantity": 2}, {"item_id": "I002", "quantity": 2}], "delivery_address": "123 Main St, San Francisco, CA", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are cautious, logical, confident, independent. First, search for restaurants with cuisine \"Mexican\" in location \"San Francisco\" with price_range \"$$\" to find a suitable dining option. Once you have identified a restaurant, get the restaurant menu for restaurant_id \"R458\" to find available tacos. If \"Taco Al Pastor\" is available, proceed to add item \"Taco Al Pastor\" (item_id \"I102\") to cart for user_id \"U9607\" with quantity 3.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R458"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U140", "restaurant_id": "R458", "item_id": "I102", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are optimistic, cautious, confident, polite. First, search for restaurants with Italian cuisine in the New York City area with a price range of $$ to $$$ to identify potential options for expanding DoorDash's delivery offerings. Once you have identified a promising restaurant, get the restaurant details for restaurant ID R2021 to check its availability and location, ensuring it aligns with DoorDash's service areas and operational capabilities.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2021"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U010",
        instruction="Your name is Mary Brown and your email is mary.brown1791@email.com. You are organized, direct. First, search for Italian restaurants in New York City with a price range of $$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R001 and filter by category 'Pasta'. This will help you confirm the availability of specific pasta dishes. If Spaghetti Carbonara is available, add item I001 (Spaghetti Carbonara) to cart for user ID U2478 with quantity 1. This task will ensure that you efficiently find and order a pasta dish within the desired price range for a seamless Doordash experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U010", "restaurant_id": "R001", "item_id": "I001", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are direct, organized, confident. Get the menu for restaurant ID R5678 to review available items in the \"Tacos\" category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is Mary Williams and your email is mary.williams2739@email.com. You are patient, confident, organized, polite. First, search for Italian restaurants located in downtown with a medium price range to find a suitable dining option for our client. Once you have identified a potential restaurant, retrieve the menu of the restaurant with ID \"R102\" to review the available dishes and ensure they meet the client's preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U134",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are organized, direct, flexible. First, search for Mexican restaurants in the downtown area with a price range of $$. Once you identify a suitable option, get the restaurant menu for restaurant R202 to check available taco options. This will help ensure we can fulfill specific customer preferences for upcoming orders.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R202", "category": "tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U035",
        instruction="Your name is Linda Miller and your email is linda.miller5151@email.com. You are independent, organized, confident, polite. Get the restaurant menu for restaurant ID R202 to check available items in the 'Tacos' category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R202", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are polite, cautious. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R234 to check operational hours and available services to ensure it fits your schedule and dining preferences. After confirming the restaurant's suitability, get the restaurant menu for restaurant ID R234 to view available pasta dishes, focusing on adding item ID I789 (Spaghetti Carbonara) to your cart for user ID U101 with quantity 1 and no customizations, ensuring a smooth and satisfying order experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U048", "restaurant_id": "R234", "item_id": "I789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown2003@email.com. You are patient, polite, direct, confident. First, search for Italian restaurants in the downtown area with a moderate price range to find suitable dining options. Once you have identified restaurant R567 as a potential choice, get detailed information to check their operational hours to ensure they are open when you plan to order. After confirming their hours, get the menu for restaurant R567 to explore available Italian dishes. Then, create an order for user U123 with restaurant R567, including items I890 and I891, and arrange for delivery to 123 Main St, Apt 4B.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U112", "restaurant_id": "R567", "items": [{"item_id": "I890", "quantity": 1}, {"item_id": "I891", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are logical, polite, cautious. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$20 to find suitable dining options. Once you have identified a potential restaurant, get restaurant details for restaurant ID R200 to verify it is open and within delivery range, ensuring it meets your criteria for convenience. Finally, create an order for user ID U5428 at restaurant ID R200 with items I300 and I301, using the saved delivery address and credit card payment method, to complete your dining experience seamlessly through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R200"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U113", "restaurant_id": "R200", "items": [{"item_id": "I300", "quantity": 1}, {"item_id": "I301", "quantity": 1}]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson5028@email.com. You are cautious, direct, organized. Get the restaurant menu for restaurant ID R102 to view available Italian dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102", "category": "Italian"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are patient, optimistic, confident. First, search for Italian restaurants in San Francisco with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a promising restaurant, get the menu for restaurant ID R12345, focusing on the \"Pasta\" category, to ensure they offer a variety of dishes that meet your preferences. This will help you make an informed decision on where to order from using DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$,$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R12345", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are confident, flexible, direct. First, search for restaurants with Mexican cuisine in downtown San Francisco within a moderate price range to find suitable dining options. Once you identify a promising restaurant, get the menu for restaurant ID R1023 to review available Mexican dishes. This will help you decide on the best items to order for user ID U5118.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U037",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are polite, flexible, optimistic. search_restaurants(cuisine=\"Mexican\", location=\"San Francisco\", price_range=\"$$\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U075",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are cautious, logical, polite, confident. First, search for restaurants in the New York City area with a cuisine type of \"Italian\" and a price range of \"$$\" to find suitable dining options. Once you have identified a potential choice, get restaurant details for restaurant ID R5678 to verify opening hours and delivery zones, ensuring it fits your schedule and location. After confirming the restaurant's availability, get the menu for restaurant ID R5678 to explore available items in the \"Pasta\" category. If you find Spaghetti Carbonara appealing, add item I2345 to cart for user U1001 with quantity 1 and no customizations, completing the order process efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U075", "restaurant_id": "R5678", "item_id": "I2345", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U138",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are optimistic, independent, patient, cautious. First, search for restaurants offering Mexican cuisine in the downtown area with a price range of $10-$20 to find a suitable option for a casual dinner. Once you identify a restaurant, get the menu for restaurant R101 to identify available taco options, ensuring they offer a variety that suits different tastes. After confirming the menu, add item I202 (Chicken Taco) to the cart for user U3457 with a quantity of 3 and extra cheese customization to enhance the flavor.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U138", "restaurant_id": "R101", "item_id": "I202", "quantity": 3, "customizations": "extra cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U101",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are logical, flexible, optimistic. First, search for restaurants offering Mexican cuisine within a 5-mile radius of Michael's location to find potential dining options. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R1023 to check their operating hours and confirm if they deliver to Michael's area. After confirming the delivery zone, get the menu for restaurant ID R1023 to find available items in the \"Tacos\" category. Finally, add item I204 (Chicken Tacos) to the cart for user ID U4985 with a quantity of 3 and extra guacamole to complete the order for delivery.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Michael's location"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U101", "restaurant_id": "R1023", "item_id": "I204", "quantity": 3, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U133",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are polite, flexible. First, search for restaurants with Chinese cuisine in the San Francisco area with a price range of $$. Once you identify restaurant R234 as a suitable option, get the restaurant details to check their opening hours and delivery zones to ensure they can deliver to your area. After confirming delivery availability, get the menu for restaurant R234 to find available dim sum items. Finally, create an order for user U5124 from restaurant R234 with items I567, delivery address 123 Main St, payment method credit card, and special instructions \"please include extra soy sauce.\"",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "dim sum"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U133", "restaurant_id": "R234", "items": [{"item_id": "I567", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "please include extra soy sauce"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U077",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are direct, optimistic, logical, patient. Get the menu for restaurant R101, specifically looking for the 'Tacos' category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are cautious, flexible, independent, logical. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to identify potential dining options. Once you have a list, get details for restaurant R1023 to check their menu and hours, ensuring they have suitable offerings and are open during your preferred dining time. After confirming the restaurant's details, focus on the pasta category of the menu to decide on specific dishes. Finally, create an order for user U7947 at restaurant R1023 with items I567 and I789, ensuring delivery to 123 Main St and using a credit card for payment.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U006", "restaurant_id": "R1023", "items": [{"item_id": "I567", "quantity": 1}, {"item_id": "I789", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U170",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are cautious, organized. search_restaurants(location=\"Downtown\", cuisine=\"Italian\", price_range=\"$$\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"location": "Downtown", "cuisine": "Italian", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are optimistic, confident. Search for Italian restaurants in the downtown area with a price range of $$.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U178",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are direct, organized, polite, independent. Get the menu for restaurant ID R102 to view available sushi options.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102", "category": "sushi"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U134",
        instruction="Your name is Patricia Miller and your email is patricia.miller3271@email.com. You are organized, polite. Get restaurant menu for restaurant ID R1023 to check available Mexican dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Mexican"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U105",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are organized, polite. Begin by searching for restaurants offering Mexican cuisine in the downtown area with a moderate price range to explore dining options for a potential client meeting. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R567 to check its opening hours and delivery zone, ensuring it fits the schedule and location needs. Finally, create an order for user ID U101 at restaurant ID R567 with items I890 and I892, specifying delivery address as 123 Elm Street, Apt 4B, and payment method as credit card, to test the delivery service and food quality before recommending it to clients.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U105", "restaurant_id": "R567", "items": [{"item_id": "I890", "quantity": 1}, {"item_id": "I892", "quantity": 1}], "delivery_address": "123 Elm Street, Apt 4B", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are optimistic, flexible. Get the full menu for restaurant R567 to explore available vegan options.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are flexible, patient, optimistic. First, search for restaurants in Seattle with cuisine 'Italian' and price range '$$' to find a suitable dining option. Once you have identified a restaurant, get the restaurant menu for restaurant ID R234 to view available items. This will help you decide on the best dishes to include in your order for a seamless DoorDash experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Seattle", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are polite, organized, flexible. First, search for Italian restaurants in the San Francisco area with a price range of $10-$20 to find suitable dining options. Next, get restaurant details for restaurant ID R101 to check its operating hours and delivery zone, ensuring it fits within the desired timeframe and location for delivery. Finally, create an order for user U001 at restaurant ID R101 with items [I202], delivery address 123 Main St, San Francisco, and payment method as credit card, ensuring a smooth transaction and timely delivery.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U158", "restaurant_id": "R101", "items": [{"item_id": "I202", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson8206@email.com. You are organized, direct, cautious, optimistic. search_restaurants(cuisine=\"Italian\", location=\"Downtown\", price_range=\"$$\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
]
