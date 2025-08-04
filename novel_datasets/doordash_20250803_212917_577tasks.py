"""
Generated tasks for doordash domain.
Generated at: 2025-08-03T22:36:09.189901
Total tasks: 577
"""

from tau_types import Task, Action

TASKS_TRAIN = [
    Task(
        annotator="gpt-4o",
        user_id="U142",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are polite, flexible, logical, organized. First, search for Italian restaurants in the San Francisco area with a price range of medium to find potential dining options. Once you have identified a suitable restaurant, such as restaurant R234, get the menu for this restaurant to explore available Italian dishes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U002",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are confident, flexible. First, search_restaurants with cuisine \"Mexican\" and location \"San Francisco\" to find available options for Patricia Brown, who is looking for a place to enjoy authentic Mexican cuisine. Once you have identified a suitable restaurant, get_restaurant_details for restaurant_id \"R345\" to verify the operating hours and ensure that it falls within the delivery zone for Patricia's address. After confirming these details, proceed to get_restaurant_menu for restaurant_id \"R345\" to explore the available Mexican dishes, focusing on options that Patricia might enjoy.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R345"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U128",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are polite, optimistic, logical. First, search for Thai restaurants in San Francisco with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R5678 to check its operational hours and ensure it fits your schedule. Finally, create an order for user ID U001 at restaurant ID R5678 with items I890 and I891, specifying the delivery address as \"123 Main St, San Francisco, CA\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Thai", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U128", "restaurant_id": "R5678", "items": [{"item_id": "I890", "quantity": 1}, {"item_id": "I891", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U163",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are cautious, polite, independent, confident. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R234 to explore available items. After reviewing the menu, add item I567 (Chicken Tacos) to the cart for user Robert Jones with user ID U3607, quantity 3.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U163", "restaurant_id": "R234", "item_id": "I567", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are polite, confident. Create an order for user U101 with restaurant R234 including items I678 and I679, delivering to 123 Main St, using credit card payment.",
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
                kwargs={"restaurant_id": "R234", "item_id": "I678"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R234", "item_id": "I679"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U019", "restaurant_id": "R234", "items": [{"item_id": "I678", "quantity": 1}, {"item_id": "I679", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are cautious, polite. Create order for user ID U3137 with restaurant ID R567, including items (I890, I891) and special instructions to include extra salsa.",
        actions=[
            Action(
                name="create_order",
                kwargs={"user_id": "U167", "restaurant_id": "R567", "items": [{"item_id": "I890", "quantity": 1}, {"item_id": "I891", "quantity": 1}], "special_instructions": "Please include extra salsa."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U010",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are organized, logical, direct, independent. First, search for Italian restaurants in New York City with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a restaurant, get restaurant details for restaurant ID R1024 to check its operating hours and address to ensure it fits your schedule. After confirming the restaurant's availability, get the restaurant menu for restaurant ID R1024, focusing on the pasta category, to decide on a dish. If Fettuccine Alfredo is available and appealing, add item I203 (Fettuccine Alfredo) to cart for user ID U2478 from restaurant ID R1024 with quantity 1 to complete the order process efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1024"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1024", "category": "pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U010", "restaurant_id": "R1024", "item_id": "I203", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are patient, optimistic, confident, organized. Search for Mexican restaurants in San Francisco with a price range of $10-$20 to find suitable dining options for a customer. Once you have identified a potential restaurant, get the restaurant menu for restaurant R00123 to explore available items and ensure they meet the customer's preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R00123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are patient, organized, optimistic, cautious. As part of your role at DoorDash, you need to search for Italian restaurants in San Francisco with a price range of $$ to expand the options available on the platform. Once you have identified potential restaurants, get details for restaurant R1123 to verify its opening hours and delivery zones to ensure it aligns with DoorDash's operational requirements.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U075",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are flexible, organized, direct, patient. First, search for restaurants offering Mexican cuisine in the San Francisco area within a medium price range to find potential options for a dinner delivery. Once you have identified a promising restaurant, get the restaurant details for restaurant ID R567 to confirm its operational hours and delivery zone to ensure it can deliver to your location. Finally, get the restaurant menu for restaurant ID R567 to view available menu items in the Tacos category, and add item I890 (Chicken Taco) to the cart for user U123 with quantity 3 and no customizations, preparing for a seamless order placement.",
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
                kwargs={"user_id": "U075", "restaurant_id": "R567", "item_id": "I890", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams7359@email.com. You are patient, polite, confident. First, search for Chinese restaurants in San Francisco within the price range of $$ to find a suitable option for your dinner plans. Once you have identified a restaurant, add an item to your cart by selecting the Kung Pao Chicken from the restaurant's menu, ensuring you specify a quantity of 2.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
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
                kwargs={"user_id": "U192", "restaurant_id": "R001", "item_id": "I123", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are confident, optimistic, patient. First, search for Italian restaurants located in downtown with a mid-range price to find a suitable dining option for your evening. Once you have identified a restaurant, retrieve the menu focusing on the pasta category to explore the available options. After selecting your desired dish, proceed to create an order for Spaghetti Carbonara from the chosen restaurant, ensuring it is delivered to 123 Main St. Don't forget to specify extra cheese in the special instructions and use your credit card for payment.",
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
                kwargs={"restaurant_id": "R001", "category": "pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U192", "restaurant_id": "R001", "items": [{"item_id": "I123", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit_card", "special_instructions": "extra cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U007",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are optimistic, flexible, polite. You are planning a cozy dinner at home and want to enjoy some delicious Italian cuisine without breaking the bank. First, search for Italian restaurants in the downtown area with a price range of $10-$30. Once you find a suitable restaurant, proceed to get the restaurant menu focusing on the Pasta category. After reviewing the menu, create an order with your user ID U001 from the selected restaurant, choosing two portions of your favorite pasta dish. Ensure the delivery address is set to 123 Main St, Apt 4B, and opt for payment via Credit Card. Kindly request the delivery person to leave the order at the doorstep for a contactless delivery experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001", "category": "Pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U007", "restaurant_id": "R001", "items": [{"item_id": "I123", "quantity": 2}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "Credit Card", "special_instructions": "Please leave the order at the doorstep for contactless delivery."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are organized, flexible, polite. First, search for restaurants offering Chinese cuisine in the Midtown area with a price range of $$. Once you have identified a suitable restaurant, specifically restaurant R345, proceed to get the restaurant menu to find available appetizers. This will enable you to add item I678 (Spring Rolls) to the cart for user U901 with a quantity of 3 from restaurant R345.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "Midtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R345"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U192", "restaurant_id": "R345", "item_id": "I678", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are flexible, logical, cautious, direct. Begin by searching for Italian restaurants in the San Francisco area with a price range of $$ to $$$ to find suitable dining options. Once you identify restaurant ID R102 as a potential choice, get the restaurant details to check current hours and delivery zones, ensuring they align with the user's needs. After confirming the restaurant's availability, create an order for user ID U4736 at restaurant ID R102 with items I305 and I309, using the delivery address \"123 Main St, San Francisco, CA\" and the payment method \"Credit Card\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U098", "restaurant_id": "R102", "items": [{"item_id": "I305", "quantity": 1}, {"item_id": "I309", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U118",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are cautious, optimistic, independent. Begin by searching for restaurants offering Chinese cuisine in the San Francisco area with a price range of $10-$30 to find suitable dining options. Once you identify restaurant R1024 as a potential choice, get the restaurant details to check its opening hours and delivery zones, ensuring it can deliver to your area. After confirming these details, proceed to get the restaurant menu for R1024, focusing on the \"Dinner Specials\" category to explore meal options. Finally, create an order for user U1001 at restaurant R1024 with items [I204, I205] and set the delivery address to \"123 Main St, San Francisco, CA\" to complete the transaction.",
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
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1024", "category": "Dinner Specials"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U118", "restaurant_id": "R1024", "items": [{"item_id": "I204", "quantity": 1}, {"item_id": "I205", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U045",
        instruction="Your name is Patricia Miller and your email is patricia.miller3271@email.com. You are direct, organized, logical. Get restaurant menu for restaurant ID R234 to browse available items in the pasta category",
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
        user_id="U105",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are polite, flexible. First, search for Italian restaurants in Jennifer's neighborhood within a moderate price range to find suitable dining options. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R2023 to check its hours and delivery zones, ensuring it can deliver to Jennifer's home. Next, get the restaurant menu for restaurant ID R2023, focusing on the pasta category, to select appealing dishes. Finally, create an order for user ID U10203 at restaurant ID R2023 with items I789 and I790, ensuring the delivery address is Jennifer's home and the payment method is the saved credit card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Jennifer's neighborhood", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2023"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2023", "category": "pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U105", "restaurant_id": "R2023", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "Jennifer's home", "payment_method": "saved credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are cautious, logical. First, search for restaurants in the user's location with a preference for Italian cuisine and a moderate price range to ensure a suitable dining option is available. Once you identify a promising Italian restaurant, obtain the restaurant details for the specific restaurant ID R567 to verify its suitability. After confirming the restaurant meets the criteria, get the restaurant menu for restaurant ID R567 to check the available Italian dishes. Finally, add item I678 (Spaghetti Carbonara) to the cart for user patricia.jones3517@email.com from restaurant ID R567 with quantity 1, ensuring the order is prepared accurately for delivery.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "price_range": "$$"}
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
                kwargs={"user_id": "U124", "restaurant_id": "R567", "item_id": "I678", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are patient, direct, organized, optimistic. First, search for restaurants with cuisine 'Italian' in the location 'Downtown' with a price range of '$$' to identify potential dining options for our customers. Once you have identified a suitable restaurant, get restaurant details for restaurant_id 'R101' to verify opening hours and delivery zone, ensuring that it can accommodate our delivery requirements. Finally, create an order for user_id 'U2988' with restaurant_id 'R101' including items I202 and I203, delivery_address '123 Main St', payment_method 'Credit Card', and special_instructions 'Leave at front door' to complete the customer’s request efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U104", "restaurant_id": "R101", "items": [{"item_id": "I202", "quantity": 1}, {"item_id": "I203", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card", "special_instructions": "Leave at front door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U123",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are logical, cautious, direct, organized. First, search for Italian restaurants in San Francisco with a price range of $$ to $$$ to ensure a variety of quality options. Next, get details for restaurant R4521 to verify it is open and accepting orders, as this will confirm its availability for placing an order. Finally, create an order for user U102 at restaurant R4521 with items [I7892, I7895], ensuring delivery to 123 Main St, San Francisco, and using a credit card as the payment method to complete the transaction smoothly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R4521"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U123", "restaurant_id": "R4521", "items": [{"item_id": "I7892", "quantity": 1}, {"item_id": "I7895", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U123",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are confident, patient, independent. Begin by searching for restaurants in Jennifer Miller's area that focus on Italian cuisine with a moderate price range. Once you have identified a suitable restaurant, specifically restaurant ID R5678, obtain its details to check its hours and delivery zone to ensure it fits Jennifer's schedule and location. After confirming this information, proceed to create an order for user ID U1010 with restaurant ID R5678, including the items [I1234, I5678] as per Jennifer's preferences, and arrange for delivery to Jennifer's home using her preferred payment method.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U123", "restaurant_id": "R5678", "items": [{"item_id": "I1234", "quantity": 1}, {"item_id": "I5678", "quantity": 1}], "delivery_address": "Jennifer's home address", "payment_method": "Jennifer's preferred payment method"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U087",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are organized, independent, direct, optimistic. Search for restaurants in the Midtown area with a price range of $$ and cuisine type \"Mexican\". Once you have identified potential options, get restaurant details for restaurant ID R234 to verify hours and location to ensure it fits your schedule and proximity needs. After confirming the restaurant's details, create an order for user ID U102 at restaurant ID R234 with items [I5678, I7890], delivery address \"123 Main St, Apt 4B\", and payment method \"Credit Card\" to complete the transaction seamlessly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Midtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U087", "restaurant_id": "R234", "items": [{"item_id": "I5678", "quantity": 1}, {"item_id": "I7890", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U086",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are confident, direct. Search for restaurants with cuisine \"Mexican\" in location \"San Francisco\" within price range \"$$\". Once you have identified a suitable restaurant, get the menu for restaurant R234 to identify available items. This will help you ensure that the restaurant offers a variety of options for a potential order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U106",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are cautious, logical, patient, direct. First, search for Mexican restaurants in the San Francisco area with a price range of $$ to $$$ to identify potential options for a business lunch. Once you have found a suitable restaurant, get the restaurant menu for restaurant ID R5678, focusing on the 'Main Dishes' category, to ensure they offer a variety of choices that cater to different preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$-$$$"}
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
        user_id="U075",
        instruction="Your name is Linda Davis and your email is linda.davis2351@email.com. You are polite, organized, cautious. First, search for Italian restaurants in New York City with a price range of $$. Once you have identified a suitable option, get restaurant details for restaurant ID R456 to verify operating hours and location to ensure it fits your schedule. After confirming the restaurant's availability, get the restaurant menu for restaurant ID R456, focusing on the pasta category, and add item I789 (Spaghetti Carbonara) to cart for user U2502 with quantity 1 and no customizations.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$"}
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
                kwargs={"user_id": "U075", "restaurant_id": "R456", "item_id": "I789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are organized, direct, cautious. Search for restaurants in San Francisco offering Mexican cuisine with a price range of $10-$30. Once you find a suitable restaurant, get the restaurant menu for restaurant R567 to explore available categories. This will help you understand the options before placing an order for a customer.",
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
        user_id="U010",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are independent, flexible. search_restaurants(cuisine=\"Mexican\", location=\"San Francisco\", price_range=\"medium\")",
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
        user_id="U134",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are polite, flexible, independent, patient. First, search for restaurants offering Mexican cuisine in the downtown area with a price range of $10-$20 to find suitable options for our users. Once you have identified a restaurant, proceed to add item ID I567 (Chicken Tacos) to the cart for user U102 with quantity 3 and no customizations, ensuring their preferences are met seamlessly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U134", "restaurant_id": "R001", "item_id": "I567", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U055",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are confident, organized, patient, flexible. First, search for Italian restaurants in the San Francisco area with a price range of $$. Then, get the restaurant details for restaurant ID R2345 to verify hours and delivery zone, ensuring it fits within the desired timeframe and location for delivery. Finally, get the restaurant menu for restaurant ID R2345 to find available pasta dishes, focusing on adding item ID I6789 (Spaghetti Carbonara) to the cart for user ID U1558 with quantity 1, to complete a seamless order process on DoorDash.",
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
                kwargs={"user_id": "U055", "restaurant_id": "R2345", "item_id": "I6789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are patient, independent, confident. \"search_restaurants\" with parameters: cuisine=\"Italian\", location=\"San Francisco\", price_range=\"moderate\"",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "moderate"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U037",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are cautious, independent, logical, organized. Search for restaurants with cuisine \"Thai\" and location \"San Francisco\" to find options for Linda Davis.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Thai", "location": "San Francisco"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are polite, organized. First, search for Italian restaurants in Linda's current location with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R2345 to review their operational hours and ratings. This will help ensure the restaurant is open and well-rated before proceeding with any further actions, such as placing an order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda's current location", "price_range": "$$ to $$$"}
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
        user_id="U050",
        instruction="Your name is Michael Smith and your email is michael.smith2502@email.com. You are organized, optimistic, polite. You are planning a dinner delivery for a small gathering at your home in San Francisco. First, search for Mexican restaurants in San Francisco with a moderate price range of $$. Once you find a suitable restaurant, get the restaurant details using the restaurant ID \"R001\" to ensure it meets your expectations. After confirming the restaurant, proceed to get the restaurant menu focusing on the \"Main Dishes\" category to select the best options for your guests. Finally, create an order using your user ID \"U123\" from the restaurant with ID \"R001\", including two quantities of the item with ID \"I789\". Ensure the delivery is sent to 123 Market St, San Francisco, CA, using a credit card for payment, and include the special instruction to leave the order at the front door for convenience.",
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
                name="create_order",
                kwargs={"user_id": "U050", "restaurant_id": "R001", "items": [{"item_id": "I789", "quantity": 2}], "delivery_address": "123 Market St, San Francisco, CA", "payment_method": "credit_card", "special_instructions": "Leave the order at the front door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U093",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are organized, direct, polite. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to find potential options for a client meeting. Once you have identified a suitable restaurant, get the menu for restaurant ID R567 to review available pasta dishes, ensuring there are appealing options for the attendees.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are optimistic, polite, patient, flexible. First, search for Italian restaurants in the downtown area with a price range of $$. Once you find a suitable restaurant, get the restaurant menu for restaurant R456 with category \"Pasta\" to ensure they offer a variety of pasta dishes. This will help you make an informed decision for your next order on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
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
        user_id="U177",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are organized, flexible, direct, logical. Search for Mexican restaurants in Patricia Miller's area with a price range of $$, and once you have identified a suitable restaurant, get the restaurant details for restaurant ID R2345 to check if it is open and meets the minimum order requirement. This information will help ensure that Patricia can order from a restaurant that fits her budget and is operational, facilitating a smooth ordering process on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
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
        user_id="U101",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are cautious, optimistic, polite. search_restaurants(location=\"downtown\", cuisine=\"Italian\", price_range=\"medium\")",
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
        user_id="U175",
        instruction="Your name is Michael Smith and your email is michael.smith2502@email.com. You are flexible, cautious, polite. Get the restaurant menu for restaurant ID R5678 to explore available sushi options.",
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
        user_id="U124",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson8206@email.com. You are patient, organized, cautious. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $$ to $$$. Once you have identified potential options, get the restaurant details for restaurant ID R5678 to check for operational hours and delivery zones. This will help ensure the restaurant is open and delivers to the desired location before proceeding with any orders on DoorDash.",
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
        user_id="U019",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are organized, logical. First, search for restaurants with Italian cuisine in the San Francisco area within a moderate price range to identify potential dining options. Once you have a list, get restaurant details for restaurant ID R1024 to verify its hours of operation and delivery zone, ensuring it fits within your criteria and service area. Finally, create an order for user ID U6303 from restaurant ID R1024 with items I567, ensuring the delivery address is set to 123 Market St, San Francisco.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1024"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U019", "restaurant_id": "R1024", "items": [{"item_id": "I567", "quantity": 1}], "delivery_address": "123 Market St, San Francisco"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U035",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are cautious, organized, independent. First, search for restaurants offering Chinese cuisine near Linda Brown's location to ensure that you find a suitable option for her meal preferences. Once you have identified a restaurant, add item I205 (Kung Pao Chicken) to Linda Brown's cart with quantity 1 to prepare for her order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "Linda Brown's location"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U035", "restaurant_id": "R001", "item_id": "I205", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are flexible, organized, independent, cautious. First, search for restaurants offering Mexican cuisine in the San Francisco area within a moderate price range to identify potential new partners for DoorDash. Once you have a list, get restaurant details for restaurant ID R1023 to verify its operating hours and location, ensuring it aligns with our delivery capabilities.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U104",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are optimistic, polite, confident, logical. Search for restaurants with cuisine \"Thai\" in the area of \"Lincoln Park\" with a price range of \"$$\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Thai", "location": "Lincoln Park", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are cautious, direct, polite. First, search for restaurants in the downtown area with cuisine \"Mexican\" and price_range \"mid-range\" to identify potential options for a client meeting. Once you find a suitable restaurant, get_restaurant_details for restaurant_id \"R001\" to confirm their operating hours and delivery area, ensuring they can accommodate your schedule and location. Finally, get_restaurant_menu for restaurant_id \"R001\" with category \"Tacos\" to view available options, allowing you to select a variety of items for the meeting, ensuring everyone has choices they will enjoy.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
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
        user_id="U132",
        instruction="Your name is John Garcia and your email is john.garcia7961@email.com. You are cautious, polite. First, search for restaurants in the downtown area with cuisine type \"Mexican\" and price range \"$$\". Once you have identified a suitable restaurant, get the restaurant details for restaurant_id \"R102\" to verify its opening hours and delivery zone, ensuring it meets your requirements. After confirming the restaurant is open and delivers to your area, proceed to get the restaurant menu for restaurant_id \"R102\" to check the availability of \"Tacos\" on the menu. Finally, if \"Tacos\" are available, add 3 Chicken Tacos (item_id \"I789\") to your cart for user_id \"U1688\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U132", "restaurant_id": "R102", "item_id": "I789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U178",
        instruction="Your name is John Brown and your email is john.brown5124@email.com. You are confident, independent, patient, logical. First, search for Mexican restaurants in the San Francisco area with a price range of $10-$20 to find suitable dining options. Once you have identified a restaurant of interest, get the restaurant details for restaurant ID R10234 to verify operating hours and delivery zones, ensuring that delivery to your location is possible. Finally, create an order for user ID U12345 with restaurant ID R10234, including items I2001 and I2002, using delivery address 123 Main St, payment method Credit Card, and special instructions \"Leave at door.\" This sequence will ensure a smooth and efficient ordering process through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R10234"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U178", "restaurant_id": "R10234", "items": [{"item_id": "I2001", "quantity": 1}, {"item_id": "I2002", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are organized, cautious, direct, optimistic. First, search for Mexican restaurants in Jennifer's neighborhood with a price range of $15-$30 to identify potential dining options. Once you have identified a suitable restaurant, get the restaurant menu for restaurant R101 to find available burrito options. This will allow you to create an order for user U6303 with restaurant R101, including items such as a Chicken Burrito (I202) and Guacamole (I303), to be delivered to Jennifer's home with the payment method set as a credit card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer's neighborhood", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U019", "restaurant_id": "R101", "items": [{"item_id": "I202", "quantity": 1}, {"item_id": "I303", "quantity": 1}], "delivery_address": "Jennifer's home", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are flexible, cautious. First, search for restaurants in the downtown area with a cuisine preference of Italian and a price range of medium to identify potential partners for DoorDash. Then, get the restaurant menu for restaurant_id R567 with a focus on the \"Pasta\" category to evaluate the variety and quality of offerings that could appeal to our customer base.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are patient, optimistic. Search for restaurants offering Mexican cuisine in Linda Garcia's location with a moderate price range.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U041"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Garcia's location", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are direct, polite, patient, flexible. Get restaurant menu for restaurant R1023 to explore available pasta dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are flexible, polite, logical. Get details for restaurant R1024 to check its operating hours and address.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are optimistic, cautious, patient. First, search for Italian restaurants in Patricia Miller's area with a price range of medium to identify potential dining options. Once you have found a suitable restaurant, get the menu for restaurant ID R345 to find available items in the \"Pasta\" category. This will help ensure you can add item I678 (Spaghetti Carbonara) to the cart for user U123 (Patricia Miller) with quantity 1 and no customizations, providing her with a delightful dining experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Patricia Miller's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R345", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U177", "restaurant_id": "R345", "item_id": "I678", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are cautious, logical, organized, direct. First, search for restaurants with cuisine \"Italian\" in the location \"San Francisco\" within the price range \"$$\" to find suitable dining options. Once you have identified a potential restaurant, get restaurant details for restaurant_id \"R123\" to check its opening hours and rating, ensuring it meets your standards for a pleasant dining experience. After confirming the restaurant's suitability, get the restaurant menu for restaurant_id \"R123\" to identify available pasta dishes, focusing on finding Spaghetti Carbonara.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R123"}
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
        user_id="U077",
        instruction="Your name is Linda Miller and your email is linda.miller5151@email.com. You are organized, optimistic, independent, logical. First, search for Italian restaurants in Linda Garcia's area within a moderate price range to find suitable dining options. Once you have identified potential restaurants, get restaurant details for restaurant ID R2345 to verify if it meets Linda's preferences, such as ambiance and customer reviews. After confirming the restaurant's suitability, get the restaurant menu for restaurant ID R2345 to check available pasta dishes, ensuring there are appealing options for Linda Garcia.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda Garcia's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
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
        user_id="U143",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are flexible, patient, organized. search_restaurants(cuisine=\"Mexican\", location=\"San Francisco\", price_range=\"medium\")",
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
        user_id="U163",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are patient, direct. Get restaurant menu for restaurant ID R2345 to view available items.",
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
        user_id="U142",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are flexible, optimistic. Get the restaurant menu for restaurant ID R2345 to review available items.",
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
        user_id="U167",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are polite, cautious. Get restaurant menu for restaurant ID R456 to view available pasta dishes",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are flexible, confident. First, search for Mexican restaurants in the San Francisco area within the price range of $10-$30 to find a suitable dining option. Once you have identified a restaurant, get details for restaurant R5678 to review operating hours and customer reviews to ensure it meets your expectations. Finally, create an order for user U001 at restaurant R5678 with items I2345 and I6789, using delivery address 123 Main St, San Francisco, and payment method \"credit card\" to complete your DoorDash order seamlessly.",
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
                kwargs={"user_id": "U042", "restaurant_id": "R5678", "items": [{"item_id": "I2345", "quantity": 1}, {"item_id": "I6789", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is John Garcia and your email is john.garcia7961@email.com. You are patient, organized, logical, direct. Create a new order for user Michael Williams at restaurant R567 with items [I678], using his saved delivery address and credit card as payment method.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U167"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U167", "restaurant_id": "R567", "items": [{"item_id": "I678", "quantity": 1}]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are cautious, direct. First, search for Italian restaurants in Linda Brown's area with a price range of $10-$30 to find suitable dining options. Once you have identified restaurant R1024 as a potential choice, get the menu for this restaurant, focusing on the pasta category, to ensure it meets the preferences and budget requirements before proceeding with any orders.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda Brown's area", "price_range": "$$"}
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
        user_id="U178",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are optimistic, confident. First, search for Mexican restaurants in San Francisco with a price range of $$ to find a suitable dining option. Once you identify a restaurant of interest, get the menu for restaurant ID R234 in the category \"Tacos\" to explore their offerings. This will help you make an informed decision on what to order, ensuring a delightful dining experience.",
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
        user_id="U055",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are optimistic, direct, polite. First, search for Mexican restaurants in San Francisco with price range $$ to identify potential options for expanding our delivery network. Next, get restaurant details for restaurant R567 to verify current hours and delivery zones, ensuring accurate information for our customers. Finally, create an order for user U101 at restaurant R567 with items [I789] and delivery address 123 Main St., to test the seamlessness of the ordering process and delivery service.",
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
                kwargs={"user_id": "U055", "restaurant_id": "R567", "items": [{"item_id": "I789", "quantity": 1}], "delivery_address": "123 Main St."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are direct, independent, polite, logical. Get the menu for restaurant R1001, focusing on the pasta category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1001", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are cautious, organized. First, search for restaurants serving Chinese cuisine in the New York City area with a price range of $10-$30. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R1023, focusing on the \"Main Course\" category. This will help you decide on a dish to order for a user on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "New York City", "price_range": "$$"}
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
        user_id="U192",
        instruction="Your name is James Williams and your email is james.williams9904@email.com. You are optimistic, organized, independent, patient. First, get the menu for restaurant ID R567, focusing on the \"Tacos\" category, to ensure that the items I234 and I235 are available for order. Then, create an order for user Patricia Jones (user ID U102) at restaurant ID R567 with these items, using delivery address 123 Main St, payment method as credit card, and special instructions \"Leave at front door\". This will ensure that Patricia receives her desired taco order promptly and accurately.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U192", "restaurant_id": "R567", "items": [{"item_id": "I234", "quantity": 1}, {"item_id": "I235", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "Leave at front door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are confident, polite. First, search for restaurants offering Mexican cuisine within a 5-mile radius of Patricia's home address to find potential dining options. Once you have identified restaurant ID R345 as a suitable choice, get the restaurant details to check their business hours and delivery zones to ensure they can deliver to Patricia's location. Finally, create an order for user Patricia Jones using restaurant ID R345, including items I789 and I790 from the menu, deliver to Patricia's home address, and pay with the saved credit card ending in 1234.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Patricia's home address"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U192", "restaurant_id": "R345", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "Patricia's home address", "payment_method": "credit card ending in 1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are flexible, optimistic, confident, logical. First, search for restaurants offering Mexican cuisine in Linda's neighborhood with a price range of $10-$20. Once you find a suitable restaurant, get detailed information for restaurant R234 to check if they have vegan options available. If they do, proceed to get the menu for restaurant R234, focusing on the \"Vegan Specials\" category, and add item I678 (Vegan Burrito) to cart for user U123 with quantity 1 and no cheese customization.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda's neighborhood", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Vegan Specials"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U090", "restaurant_id": "R234", "item_id": "I678", "quantity": 1, "customizations": "no cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U061",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are organized, direct. Search for Italian restaurants in Patricia's area with a price range of $$. Once you have the search results, get the restaurant details for restaurant ID R102. After obtaining the details, proceed to get the menu for restaurant ID R102 to find available pasta dishes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are cautious, confident. First, use search_restaurants to find Italian restaurants in Linda's area with a moderate price range, as she is looking for a cozy place to dine with her family. Once you have identified a potential restaurant, get_restaurant_details for restaurant ID R001 to check its operating hours and delivery zone, ensuring it fits her schedule and location preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda's area", "price_range": "$$"}
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
        user_id="U105",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are logical, polite, independent, confident. First, get restaurant details for restaurant R5678 to confirm it is open and meets delivery zone requirements. Once confirmed, get the restaurant menu for restaurant R5678 to explore available tacos, ensuring they meet the preferences of the customer. This will help ensure that the order process for DoorDash is smooth and efficient.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
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
        user_id="U177",
        instruction="Your name is Robert Williams and your email is robert.williams9426@email.com. You are flexible, confident, logical, patient. First, search for Italian restaurants in the downtown area with a price range of $$-$$$. Once you find a suitable restaurant, get the menu for restaurant R234, focusing on the pasta category. This will help you identify the best options available for a customer order on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
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
        user_id="U134",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are cautious, optimistic, patient, flexible. First, search for restaurants with cuisine 'Italian' near 'San Francisco' within the price range '$$' to find a suitable dining option. Once you have identified a restaurant, get restaurant details for restaurant_id 'R001' to check its operating hours and ensure it fits your schedule. After confirming the restaurant's availability, create an order for user 'U001' with restaurant_id 'R001' and items ['I101', 'I102'], ensuring delivery to '123 Main St, San Francisco, CA', and use 'Credit Card' as the payment method.",
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
                kwargs={"user_id": "U134", "restaurant_id": "R001", "items": ["I101", "I102"], "delivery_address": "123 Main St, San Francisco, CA", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are logical, cautious, optimistic. First, search for Mexican restaurants in San Francisco with a moderate price range to identify potential options for a customer order. Once you find a suitable restaurant, get restaurant details for restaurant R5678 to verify it is open and meets minimum order requirements. After confirming these details, get the menu for restaurant R5678 and check for availability of Tacos and Burritos. Finally, create an order for user U9808 with restaurant R5678, including items Chicken Tacos (x3) and Beef Burrito (x1), with delivery address 123 Main St, San Francisco, and payment method credit card ending in 1234.",
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
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U085", "restaurant_id": "R5678", "items": [{"name": "Chicken Tacos", "quantity": 3}, {"name": "Beef Burrito", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card ending in 1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U077",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are independent, flexible, confident, organized. First, get the restaurant menu for restaurant ID R5678, focusing on the Taco category, to ensure the availability and details of the Chicken Tacos. Once confirmed, add item I234 (Chicken Tacos) to the cart for user U4109 with a quantity of 3 and no customizations. This will allow you to efficiently manage the order process on DoorDash by ensuring the selected menu item is available before proceeding with the order.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Taco"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U077", "restaurant_id": "R5678", "item_id": "I234", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are optimistic, polite. First, search for restaurants in the Midtown area offering Mexican cuisine to find a suitable option for delivery. Once you have identified restaurant R101, get the restaurant details to check their operating hours and delivery zone to ensure they can deliver to your location. After confirming their availability, get the restaurant menu for restaurant R101 to explore available taco options. Finally, create an order for user U331 at restaurant R101 with items I202 and include the special instruction \"No onions\" to cater to specific dietary preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Midtown"}
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
                name="create_order",
                kwargs={"user_id": "U049", "restaurant_id": "R101", "items": [{"item_id": "I202", "quantity": 1}], "special_instructions": "No onions"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are flexible, confident, cautious, organized. First, search for restaurants offering Italian cuisine in the downtown area with a moderate price range to find potential options for a new promotion. Once you have identified a suitable restaurant, get the menu for restaurant R567 to identify available pasta dishes that could be featured in the promotion.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
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
        user_id="U104",
        instruction="Your name is Robert Williams and your email is robert.williams9426@email.com. You are direct, independent, optimistic, patient. Search for Italian restaurants in Linda Brown's location with a moderate price range",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U104"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda Brown's location", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are patient, organized. First, search for Mexican restaurants in the downtown area with a price range of $$ to $$$ to find suitable dining options for a client meeting. Once you identify a potential restaurant, get restaurant details for restaurant R1023 to check its hours and reviews to ensure it meets the client's expectations. After confirming the restaurant's suitability, get the restaurant menu for restaurant R1023 and filter for the \"Tacos\" category. Finally, add item I567 (Chicken Tacos) to cart for user U345 with quantity 3 and extra guacamole to prepare for the meeting's lunch order on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$-$$$"}
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
                kwargs={"user_id": "U049", "restaurant_id": "R1023", "item_id": "I567", "quantity": 3, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U037",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are patient, confident, flexible, polite. Search for Italian restaurants in Linda Davis's area with a price range of mid-tier. Once you have identified a suitable Italian restaurant, get restaurant details for restaurant ID R102.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "price_range": "$$"}
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
        user_id="U049",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are independent, logical. First, search for restaurants offering Mexican cuisine in the Los Angeles area within a moderate price range to identify potential dining options. Next, get restaurant details for restaurant R456 to check hours of operation, ensuring it fits within your schedule. Finally, create an order for user U123 with restaurant R456, including items I789 and I790, and set the delivery address to 123 Main St, Los Angeles, to complete the transaction seamlessly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Los Angeles", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U049", "restaurant_id": "R456", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St, Los Angeles"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are polite, independent, patient, organized. add_item_to_cart(user_id=\"U123\", restaurant_id=\"R101\", item_id=\"I234\", quantity=2)",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U167"}
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
                name="get_item_details",
                kwargs={"restaurant_id": "R101", "item_id": "I234"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U167", "restaurant_id": "R101", "item_id": "I234", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U118",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are independent, polite, confident, logical. First, search for restaurants offering Chinese cuisine in Linda Smith's location with a moderate price range to identify suitable dining options. Once you have identified a restaurant, get the menu for restaurant ID R234, focusing on the \"Dinner Specials\" category, to ensure it meets the criteria and preferences. This sequential approach will help you provide Linda with the best dining experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "Linda Smith's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Dinner Specials"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U105",
        instruction="Your name is Jennifer Garcia and your email is jennifer.garcia3233@email.com. You are polite, independent, confident, optimistic. Start by searching for restaurants with cuisine 'Mexican' near 'San Francisco' with a price range of '$$'. Once you find a suitable restaurant, get the restaurant details for restaurant ID 'R5678' to check if it is currently open. If the restaurant is open, proceed to get the menu for restaurant ID 'R5678' focusing on the 'Tacos' category. If 'Chicken Taco' is available, add item 'I890' (Chicken Taco) from restaurant ID 'R5678' to the cart for user ID 'U1234' with quantity 3.",
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
                kwargs={"user_id": "U105", "restaurant_id": "R5678", "item_id": "I890", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U020",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are confident, direct, independent. First, search for Italian restaurants in the city center with a price range of $$. Once you identify a potential option, get the restaurant details for restaurant R101 to verify business hours and delivery area. This information will help ensure that the restaurant is a viable option for expanding DoorDash's delivery services in the area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "city center", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are flexible, polite, organized. First, search for restaurants offering Japanese cuisine in the San Francisco area with a moderate price range to identify potential dining options. Once you have a list, get restaurant details for restaurant ID R234 to verify operational hours and delivery zones to ensure they can deliver to your area. Finally, create an order for user U101 from restaurant ID R234 with items I678 and I679, including delivery address 123 Main St, San Francisco, and payment method set to Credit Card, ensuring a smooth and efficient ordering process on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Japanese", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U132", "restaurant_id": "R234", "items": [{"item_id": "I678", "quantity": 1}, {"item_id": "I679", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are direct, flexible. First, search for restaurants in the Midtown area with a price range of $$ and offering Mexican cuisine. Once you find a suitable restaurant, get the menu for restaurant R567, focusing on the Tacos category. This will help you decide on the best options to recommend for a DoorDash promotion.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Midtown", "price_range": "$$"}
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
        user_id="U010",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are flexible, confident, polite, cautious. First, search for restaurants in Linda Smith's area with a focus on Asian cuisine and moderate price range to ensure a variety of options for her dinner plans. Once you have identified a suitable restaurant, get the menu for restaurant ID R234, focusing on the 'Main Dishes' category, to help Linda make an informed decision on her order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Asian", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Main Dishes"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U176",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are logical, flexible, optimistic, polite. Get the menu for restaurant ID R123 to find available pasta dishes.",
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
        user_id="U134",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are flexible, direct, patient. First, search for restaurants offering Chinese cuisine in the San Francisco area within a moderate price range. Once you find a suitable restaurant, get the menu for restaurant ID R234, focusing on the \"Main Dishes\" category. This will help you decide which dishes to order for a family dinner through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Main Dishes"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is Mary Brown and your email is mary.brown1791@email.com. You are logical, confident, organized, patient. First, search for Mexican restaurants in the San Francisco area with a price range of $10-$20 to find suitable dining options. Once you identify a restaurant that meets the criteria, get the restaurant menu for restaurant ID R567 to view available tacos and burritos. This will help you decide on the best items to order for a customer using DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos and Burritos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U035",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are direct, flexible, cautious. Start by searching for Italian restaurants in Linda's location with a price range of $$ to $$$. Once you have identified a potential option, get restaurant details for restaurant ID R10234 to check if it meets Linda's preferences. If it does, proceed to get the restaurant menu for restaurant ID R10234, focusing on the pasta category, to ensure there are suitable options available.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda's location", "price_range": "$$ to $$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R10234"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R10234", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U075",
        instruction="Your name is Robert Brown and your email is robert.brown1066@email.com. You are optimistic, logical, cautious, confident. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $$ to $$$. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R102, focusing on the Tacos category. This will help you decide which items to consider for your order on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are independent, patient, cautious. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$20 to explore potential dining options. Once you have identified a restaurant of interest, get the restaurant details for restaurant ID R245 to verify opening hours and delivery zones, ensuring it fits your schedule and location. After confirming the restaurant's availability, get the restaurant menu for restaurant ID R245, focusing on the 'Burritos' category, to decide on your meal choice.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R245"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R245", "category": "Burritos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U075",
        instruction="Your name is Robert Brown and your email is robert.brown1066@email.com. You are independent, flexible. First, search_restaurants(cuisine=\"Italian\", location=\"Downtown\", price_range=\"$$\") to find a suitable place for a client meeting. Once you have identified a promising option, get_restaurant_details(restaurant_id=\"R12345\") to ensure it meets your requirements for ambiance and service. After confirming the restaurant is a good fit, create_order(user_id=\"U2502\", restaurant_id=\"R12345\", items=[{\"id\": \"I567\", \"name\": \"Spaghetti Carbonara\", \"quantity\": 1}], delivery_address=\"123 Elm St, Downtown\", payment_method=\"Credit Card\", special_instructions=\"Extra cheese\") to have a meal delivered to your client at their office, ensuring a smooth and professional experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R12345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U075", "restaurant_id": "R12345", "items": [{"id": "I567", "name": "Spaghetti Carbonara", "quantity": 1}], "delivery_address": "123 Elm St, Downtown", "payment_method": "Credit Card", "special_instructions": "Extra cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are polite, organized, flexible, logical. First, search for restaurants in San Francisco offering Mexican cuisine with a price range of $10-$20 to identify potential dining options for a customer. Once you have identified a suitable restaurant, proceed to get the restaurant menu for restaurant ID R2025 to explore available items. This will help you make informed recommendations to the customer and facilitate their order placement through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2025"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U046",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are cautious, independent, polite, patient. First, search for restaurants with cuisine \"Mexican\" in the location \"San Francisco\" and price_range \"$$\". After finding a suitable restaurant, get the restaurant menu for restaurant_id R789 to view available dishes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R789"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U093",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are optimistic, patient. Get the restaurant menu for restaurant ID R876 to explore available items in the \"Tacos\" category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R876", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is Mary Jones and your email is mary.jones4200@email.com. You are optimistic, logical. Create an order for user U5307 at restaurant R23456 with items I67890 and I67891, delivery address 123 Main St, payment method Credit Card, and special instructions \"Leave at door\".",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R23456"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R23456"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R23456", "item_id": "I67890"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R23456", "item_id": "I67891"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U106", "restaurant_id": "R23456", "items": [{"item_id": "I67890", "quantity": 1}, {"item_id": "I67891", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are flexible, optimistic, logical. First, search for Mexican restaurants in San Francisco with a price range of $$. Once you have identified a suitable option, get the restaurant details for restaurant R101 to review its operating hours. Finally, create an order for user U5118 at restaurant R101 with items [I301] and delivery address \"123 Main St, San Francisco, CA\" with special instructions \"Leave at the door\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U162", "restaurant_id": "R101", "items": [{"item_id": "I301", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA", "special_instructions": "Leave at the door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are organized, independent, flexible. You have been tasked with finding a suitable Mexican restaurant in San Francisco for a team lunch within a moderate price range. First, search for restaurants with cuisine type \"Mexican\" in \"San Francisco\" and a price range of \"$$\". Once you have identified a potential restaurant, retrieve the restaurant details using the restaurant ID \"R2345\" to ensure it meets the team's preferences and requirements. After confirming the restaurant is a good fit, proceed to get the restaurant menu using the same restaurant ID and add a popular item with item ID \"I678\" to the cart for user ID \"U102\" with a quantity of 1 to finalize the initial order setup.",
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
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U041", "restaurant_id": "R2345", "item_id": "I678", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U035",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are flexible, logical, independent, patient. First, search for Italian restaurants in San Francisco with a price range of $$ to identify potential options for expanding DoorDash's delivery offerings in the area. Once you have a list, get details for restaurant R234 to check its opening hours and reviews, ensuring it aligns with DoorDash's quality standards and operational hours.",
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
        user_id="U178",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are confident, logical, independent. First, search for restaurants offering Mexican cuisine in the San Francisco area with a moderate price range to identify potential partners for DoorDash. Once you have a list, focus on restaurant R5678 to verify their operating hours and delivery zone. This will ensure that they meet DoorDash's logistical requirements for partnership and can effectively serve our customer base.",
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
        user_id="U041",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are independent, organized, confident. Search for restaurants offering Mexican cuisine within the delivery zone of Linda Garcia's address. Once you have identified a restaurant, specifically restaurant R567, get details to verify it is open and accepting orders. This will ensure that Linda can place an order seamlessly through DoorDash for her upcoming family gathering.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Garcia's address"}
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
        user_id="U010",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are independent, polite, optimistic, patient. Search for restaurants offering Mexican cuisine in Linda's area with a medium price range to find suitable options for a potential partnership with DoorDash. Once you have identified a promising restaurant, get the restaurant details for the restaurant with ID R5678 to confirm operating hours and service options, ensuring they align with DoorDash's delivery schedules and requirements.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda's area", "price_range": "$$"}
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
        user_id="U076",
        instruction="Your name is Jennifer Garcia and your email is jennifer.garcia3233@email.com. You are independent, patient, confident. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$30. Once you have identified potential options, get restaurant details for restaurant R567 to verify operational hours and customer reviews. This will help you ensure that the restaurant is a reliable choice for listing on DoorDash and meets customer expectations.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U098",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are independent, organized, confident, patient. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$20. Once you have identified a few options, focus on restaurant R4567 to get their menu, specifically the \"Tacos\" category. This will help you evaluate their offerings for potential inclusion in a curated list for DoorDash users seeking affordable Mexican dining options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R4567", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U020",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are optimistic, organized, direct. First, search for restaurants offering Italian cuisine within John Brown's area using his location data. Once you find a suitable restaurant, add item I789 (Spaghetti Carbonara) to John Brown's cart from restaurant ID R456 with quantity 1.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "John Brown's area"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U020", "restaurant_id": "R456", "item_id": "I789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U170",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson8206@email.com. You are flexible, confident, optimistic, direct. Start by searching for Italian restaurants in the downtown area with a price range of $$ to $$$ to find a suitable dining option. Once you identify a restaurant, get details for restaurant R001 to check if it is currently open for orders. If the restaurant is open, proceed to get the menu for restaurant R001 and filter by the 'Pasta' category to explore the available pasta dishes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
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
        user_id="U106",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams7359@email.com. You are organized, cautious, independent. Search for Mexican restaurants in the area of San Francisco with a price range of $$ to $$$ to find suitable options for a client meeting. Once you have identified a potential restaurant, get restaurant details for restaurant ID R1024 to confirm they are open and meet minimum order requirements. This will ensure that the restaurant can accommodate the order and delivery needs for the meeting.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$-$$$"}
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
        user_id="U077",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are confident, cautious, flexible, polite. search_restaurants(cuisine=\"Mexican\", location=\"San Francisco\", price_range=\"$$\")",
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
        user_id="U002",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are confident, flexible. Create order for user Patricia Brown from restaurant R567 with items [I890, I891], delivery address as Patricia's registered address, and payment method as credit card.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U002"}
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
                kwargs={"user_id": "U002", "restaurant_id": "R567", "items": [{"item_id": "I890", "quantity": 1}, {"item_id": "I891", "quantity": 1}], "delivery_address": "Patricia's registered address", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are polite, optimistic. First, search for Italian restaurants in San Francisco with a price range of '$$'. Once you have identified a suitable option, get the restaurant details for restaurant ID R2345. This information will help you assess whether the restaurant aligns with DoorDash's quality standards and customer preferences.",
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
        user_id="U175",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are logical, organized, independent, polite. Get the restaurant menu for restaurant ID R234, focusing on the \"Lunch Specials\" category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Lunch Specials"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are logical, organized, cautious. First, search for Mexican restaurants in the Midtown area with a price range of $$. Once you find a suitable restaurant, get the menu for restaurant R234, focusing on the \"Tacos\" category. After reviewing the menu, add item I789 (Carne Asada Taco) to cart for user U001 with quantity 3 and no customizations.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Midtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U049", "restaurant_id": "R234", "item_id": "I789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U010",
        instruction="Your name is John Garcia and your email is john.garcia7961@email.com. You are independent, patient. First, search for restaurants offering Chinese cuisine in the San Francisco area with a price range of $10-$20 to identify potential options for a new delivery partnership. Once you have identified a promising restaurant, get the restaurant details for restaurant ID R102 to verify their opening hours and delivery zone to ensure they align with peak delivery times and areas. Finally, create an order for user Linda Smith (user_id U001) at restaurant ID R102 with items [I203, I204] and delivery address 123 Main St, San Francisco, CA to test the restaurant's delivery service and item quality.",
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
                kwargs={"user_id": "U010", "restaurant_id": "R102", "items": [{"item_id": "I203", "quantity": 1}, {"item_id": "I204", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U002",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are flexible, independent, optimistic. Create a new order for Patricia using her user ID, the selected restaurant's ID, and the items in her cart, including her default delivery address.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U002"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "123 Main St, Springfield"}
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
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U002", "restaurant_id": "R001", "item_id": "I002", "quantity": 1}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U002", "restaurant_id": "R001", "items": [{"item_id": "I001", "quantity": 2}, {"item_id": "I002", "quantity": 1}], "delivery_address": "123 Main St, Springfield"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U035",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are organized, direct, logical. First, search for restaurants with Chinese cuisine in the area of 5th Avenue, ensuring the price range is up to $30. Once you have identified a suitable restaurant, get the menu for restaurant ID R2345, focusing on the 'Entrees' category. This will help you make an informed decision for placing an order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "5th Avenue", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Entrees"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U178",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are direct, organized, patient, logical. First, search for restaurants with the cuisine \"Mexican\" in the location \"San Francisco\" and price range \"$$\". After identifying restaurant R101 as a top choice from the search results, proceed to get the restaurant details for R101. Finally, create an order for user U001 from restaurant R101 with items [I202, I203], ensuring delivery to \"123 Elm Street, Apt 5\" using the payment method \"Credit Card\", and include the special instructions \"Leave at the front door\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U178", "restaurant_id": "R101", "items": [{"item_id": "I202", "quantity": 1}, {"item_id": "I203", "quantity": 1}], "delivery_address": "123 Elm Street, Apt 5", "payment_method": "Credit Card", "special_instructions": "Leave at the front door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is John Garcia and your email is john.garcia7961@email.com. You are optimistic, cautious. Begin by searching for Asian restaurants in San Francisco with a mid-range price to identify potential dining options. Once you have a list of restaurants, focus on getting the restaurant details for restaurant ID R2345 to check its opening hours and delivery zones, ensuring it meets the needs of your delivery area. After confirming the restaurant's suitability, proceed to get the menu for restaurant ID R2345 to explore available items. This will allow you to create an order for user Patricia Miller (user_id: U1234) with restaurant ID R2345, including items: Sushi Platter and Edamame, ensuring a delightful dining experience for her.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Asian", "location": "San Francisco", "price_range": "$$"}
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
                kwargs={"user_id": "U177", "restaurant_id": "R2345", "items": [{"item_id": "Sushi Platter", "quantity": 1}, {"item_id": "Edamame", "quantity": 1}]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U142",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are confident, cautious. First, search for restaurants offering Mexican cuisine in the user’s location with a moderate price range to ensure a variety of options. Once you have identified restaurant R567 as a suitable choice, get the restaurant details to verify its operating hours and delivery zones to ensure it meets the user’s needs. Then, create an order for user U5028 with restaurant R567, including items I789, and specify the delivery address as 123 Main St, payment method as credit card, and special instructions for no onions to complete the transaction smoothly.",
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
                kwargs={"user_id": "U142", "restaurant_id": "R567", "items": [{"item_id": "I789", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "no onions"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U133",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are confident, organized, flexible, polite. Add item I202 (Spaghetti Carbonara) to cart for user John Brown with quantity 1.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian"}
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
                kwargs={"user_id": "U133", "restaurant_id": "R001", "item_id": "I202", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U163",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are polite, patient, flexible. Get the menu for restaurant ID R567 to explore available pasta dishes.",
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
        user_id="U007",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9197@email.com. You are patient, polite, organized, cautious. First, search for restaurants in the Brooklyn area offering Mexican cuisine to explore dining options. Next, get the restaurant details for restaurant ID R1023 to check operational hours and delivery zones, ensuring it fits your schedule and location. Finally, create an order for user ID U6151 at restaurant ID R1023 with selected items from the \"Tacos\" category and set the delivery address to \"123 Main St, Brooklyn, NY\" to enjoy a delightful meal at home.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Brooklyn"}
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
                name="create_order",
                kwargs={"user_id": "U007", "restaurant_id": "R1023", "items": [{"item_id": "I001", "quantity": 2}, {"item_id": "I002", "quantity": 1}], "delivery_address": "123 Main St, Brooklyn, NY"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are patient, direct, organized, confident. Search for restaurants offering Mexican cuisine near Los Angeles with a price range of $$",
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
        user_id="U163",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are flexible, direct. First, search for Mexican restaurants in the New York City area with a price range of $10-$20 to find potential dining options. Once you identify a restaurant of interest, get the restaurant menu for restaurant ID R567 to find available items in the \"Tacos\" category. This will help you determine if they offer the variety you desire.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "New York City", "price_range": "$$"}
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
        user_id="U041",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are organized, patient. First, search for Mexican restaurants in Linda Garcia's area with a price range of $10-$20 to identify potential dining options. Once you have identified restaurant ID R234 as a suitable choice, get the menu for this restaurant, focusing on the \"Tacos\" category, to ensure they offer a variety of taco options. After confirming the menu, add item I678 (Chicken Tacos) to the cart for user ID U001 with quantity 3 to prepare for a seamless ordering experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Garcia's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U041", "restaurant_id": "R234", "item_id": "I678", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is James Williams and your email is james.williams9904@email.com. You are patient, independent. First, search for restaurants offering Mexican cuisine in the 94103 area with a price range of $$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R23456 to explore available tacos.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "94103", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R23456", "category": "tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are confident, patient. Get the restaurant menu for restaurant R567 to check available items in the Tacos category.",
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
        user_id="U125",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are independent, organized. First, search for Italian restaurants in the 90210 zip code with a price range of $$. Once you have identified potential options, get restaurant details for restaurant_id R456 to verify opening hours and delivery zone. This will help ensure that the restaurant meets the operational requirements for Doordash delivery services in the specified area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "90210", "price_range": "$$"}
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
        user_id="U046",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are independent, confident, patient, polite. First, search for restaurants with cuisine \"Mexican\" in the location \"San Francisco\" with a price range of \"$$\". Once you have identified a suitable restaurant, get the restaurant menu for restaurant_id \"R1029\". After reviewing the menu, create an order for user_id \"U6296\" from restaurant_id \"R1029\", including items [{\"item_id\": \"I205\", \"quantity\": 3}] with delivery_address \"123 Market St, San Francisco, CA\" and payment_method \"credit_card\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1029"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U046", "restaurant_id": "R1029", "items": [{"item_id": "I205", "quantity": 3}], "delivery_address": "123 Market St, San Francisco, CA", "payment_method": "credit_card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U093",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are logical, patient, optimistic. Search for Italian restaurants in the downtown area with a price range of $$ using search_restaurants.",
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
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are flexible, direct, optimistic. Search for restaurants in John's area with cuisine type \"Mexican\" and price range \"$$\". Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R456 to explore available Mexican dishes. This will help you make an informed decision for placing an order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
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
        user_id="U140",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are organized, patient. First, search for Mexican restaurants in the San Francisco area with a price range of $$ to $$$ to identify potential options for a new customer request. Next, get details for restaurant R245 to check if it meets delivery requirements for user U9607, ensuring it aligns with their preferences. Finally, create an order for user U9607 with restaurant R245 for items I678 and I679, specifying the delivery address as 123 Main St, San Francisco, CA, to complete the transaction efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R245"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U140", "restaurant_id": "R245", "items": [{"item_id": "I678", "quantity": 1}, {"item_id": "I679", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are logical, organized, optimistic. Create order for user U1234 at restaurant ID R2345 with items: I6789 (Chicken Tacos) and delivery address at 123 Main St, Los Angeles.",
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
                kwargs={"user_id": "U106", "restaurant_id": "R2345", "items": [{"item_id": "I6789", "quantity": 1}], "delivery_address": "123 Main St, Los Angeles"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U163",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are logical, independent. First, search for restaurants offering Mexican cuisine in the San Francisco area within a moderate price range. Once you have identified a few options, get detailed information for restaurant R5678 to check its operating hours and delivery zones. This will help ensure that the restaurant can deliver to the desired location during the preferred time frame, facilitating a smooth and efficient ordering process on DoorDash.",
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
        user_id="U163",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are confident, logical. First, search for Italian restaurants near the user's location with a price range of $$ to $$$ to identify potential dining options. Next, get restaurant details for restaurant ID R567 to check operating hours and delivery zones, ensuring the restaurant is open and delivers to the user's area. Finally, get the restaurant menu for restaurant ID R567 and filter by category \"Pasta\" to explore available dishes. Once you find the Spaghetti Carbonara, add item I234 to the cart for user robert.jones3607@email.com with quantity 1, facilitating a seamless order process on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "price_range": "$$ to $$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U163", "restaurant_id": "R567", "item_id": "I234", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Patricia Miller and your email is patricia.miller3271@email.com. You are direct, flexible, logical. First, search for Mexican restaurants in Patricia's area within a moderate price range to identify potential dining options. Once you have found a suitable restaurant, specifically restaurant R5678, get the menu to explore available Mexican dishes. This will help in making an informed decision on what to order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
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
        user_id="U016",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are confident, flexible. First, search for Mexican restaurants in San Francisco with a moderate price range ($$) to find a suitable place for dinner. Once you have identified a restaurant, proceed to create an order from that restaurant with user ID U8206. Include two of the selected items in your order, ensure the delivery address is 123 Main St, San Francisco, CA, and choose credit card as the payment method. Add a special instruction to leave the order at the door.",
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
                name="create_order",
                kwargs={"user_id": "U016", "restaurant_id": "R001", "items": [{"item_id": "I001", "quantity": 1}, {"item_id": "I002", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA", "payment_method": "credit card", "special_instructions": "Leave the order at the door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are confident, direct. First, search for Mexican restaurants in the San Francisco area with a moderate price range using the search_restaurants tool. Once you have identified potential options, get details for restaurant R002 to verify its operating hours using the get_restaurant_details tool. This will help ensure that DoorDash can accurately update its delivery availability and provide customers with reliable service times.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R002"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are independent, cautious. First, search for Mexican restaurants in San Francisco with a price range of $$. Next, get restaurant details for restaurant ID R23456 to ensure it meets Patricia's preferences, as she is particular about ambiance and service quality. Finally, create an order for user U001 at restaurant ID R23456 with items including I7890, delivery address 123 Main St, San Francisco, and payment method credit card, ensuring a seamless and satisfying dining experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R23456"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U049", "restaurant_id": "R23456", "items": [{"item_id": "I7890", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U055",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are independent, organized, flexible, cautious. First, search for restaurants offering Mexican cuisine in the San Francisco area within a mid-range price to find suitable dining options. Once you have identified a restaurant that meets these criteria, such as restaurant R2345, proceed to get the menu for this restaurant to explore available items and categories. This will help you make informed decisions for placing future orders on DoorDash.",
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
        user_id="U085",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are cautious, confident, logical. First, search for Mexican restaurants in San Francisco within a mid-range price category to identify potential options for expanding DoorDash's delivery partnerships. Once you have identified a promising restaurant, get the menu for restaurant ID R234 to explore available options in the 'Tacos' category, ensuring that the offerings align with customer preferences and demand trends.",
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
        user_id="U086",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are direct, optimistic, flexible, patient. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to identify potential dining options. Once you have found a suitable restaurant, get the restaurant details for restaurant ID R1024 to check their opening hours and delivery zone, ensuring they can deliver to your desired location. Finally, create an order for user ID U5308 at restaurant ID R1024, including items I230 and I231, with the delivery address as 123 Main St and the payment method as Credit Card, to complete the transaction efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1024"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U086", "restaurant_id": "R1024", "items": [{"item_id": "I230", "quantity": 1}, {"item_id": "I231", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U077",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are flexible, cautious. First, search for restaurants in San Francisco offering Mexican cuisine within a medium price range to find suitable dining options. Once you identify a restaurant, get detailed information for restaurant R1023 to ensure it meets your preferences. After confirming the restaurant's details, get the menu for restaurant R1023, focusing on the Tacos category, to explore your dining options.",
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
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U193",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are direct, independent, patient, polite. First, search for Italian restaurants in San Francisco with a moderate price range ($$) to find a suitable dining option. Once you have identified a restaurant of interest, obtain the restaurant's details to ensure it meets your dining preferences and expectations. After confirming the restaurant is a good choice, proceed to explore their menu, specifically focusing on the Pasta category, and add a desired pasta dish to your cart for a seamless DoorDash ordering experience.",
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
                kwargs={"user_id": "U193", "restaurant_id": "R001", "item_id": "I001", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown2003@email.com. You are polite, patient. First, search for restaurants offering Mexican cuisine in the downtown area of San Francisco to find potential options for a customer looking for authentic dishes. Once you have identified a suitable restaurant, get restaurant details for restaurant ID R567 to verify its opening hours and location, ensuring it fits the customer's schedule and is conveniently located. After confirming the restaurant's details, create an order for user ID U3137 with restaurant ID R567, including items I789, delivery address 123 Main St, payment method 'Credit Card', and special instructions 'Leave at door' to complete the transaction smoothly and meet the customer's delivery preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown San Francisco"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U167", "restaurant_id": "R567", "items": [{"item_id": "I789", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U077",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are patient, independent, organized, flexible. Get the restaurant menu for restaurant ID R5678, focusing on the Tacos category.",
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
        user_id="U086",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are optimistic, direct, logical, flexible. Search for Mexican restaurants in Linda's area with a price range of $10-$20. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R234 to browse available items. This will help you decide if the restaurant meets her preferences for a potential order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda's area", "price_range": "$$"}
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
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are patient, organized. First, search for Italian restaurants in the San Francisco area with a price range of $$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R5678 to review available pasta dishes. This will help you decide on the best option to recommend for a client meeting.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U138",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson8206@email.com. You are confident, logical, direct. Get the menu for restaurant R56789 focusing on the 'Tacos' category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R56789", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are organized, cautious. First, search for Mexican restaurants in San Francisco with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a potential restaurant, get restaurant details for restaurant ID R1023 to check their operation hours and ensure they are open during your desired time. After confirming the restaurant's availability, get the restaurant menu for restaurant ID R1023, focusing on the category \"Tacos,\" to decide on the best items to order. Finally, create an order for user U9426 at restaurant ID R1023 with items [I234, I235] and set the delivery address to \"123 Main St, San Francisco, CA\" to complete the process efficiently.",
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
                name="create_order",
                kwargs={"user_id": "U095", "restaurant_id": "R1023", "items": [{"item_id": "I234", "quantity": 1}, {"item_id": "I235", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are polite, patient. Get the restaurant menu for restaurant ID R5678, focusing on the pasta category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are flexible, organized, logical. First, get the restaurant menu for restaurant ID R1023 to review available items in the \"Main Course\" category. Then, create an order for user ID U5307 with restaurant ID R1023, including items I204 (Chicken Tacos) and I207, using delivery address 123 Market St, San Francisco, and payment method credit card.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Main Course"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U106", "restaurant_id": "R1023", "items": [{"item_id": "I204", "quantity": 1}, {"item_id": "I207", "quantity": 1}], "delivery_address": "123 Market St, San Francisco", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are direct, optimistic, polite. First, search for Italian restaurants in the San Francisco area with a price range of $$. Once you find a suitable option, get restaurant details for restaurant ID R102 to check hours of operation. If the restaurant is open, create an order for user Jennifer Davis using restaurant ID R102 with items I305 and I307, delivery address 123 Elm St, payment method credit card, and special instructions to leave at the door.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U076", "restaurant_id": "R102", "items": [{"item_id": "I305", "quantity": 1}, {"item_id": "I307", "quantity": 1}], "delivery_address": "123 Elm St", "payment_method": "credit card", "special_instructions": "Leave at the door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U010",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are polite, direct. Please start by searching for Italian restaurants located in Downtown with a moderate price range ($$). Once you find a suitable restaurant, proceed to get the menu for that restaurant using its unique restaurant ID.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
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
        user_id="U055",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are independent, direct, patient. First, search for restaurants with cuisine \"Mexican\" near \"San Francisco\" with a price range of \"$$\" to find potential dining options. Once you have identified a suitable restaurant, get the restaurant details for restaurant R456 to check its operating hours and delivery zones, ensuring it meets your needs for both timing and location. Finally, create an order for user U123 at restaurant R456 with items (I789) and set the delivery address as \"123 Market St, San Francisco, CA\" to complete the transaction seamlessly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U055", "restaurant_id": "R456", "items": [{"item_id": "I789", "quantity": 1}], "delivery_address": "123 Market St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U193",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are cautious, direct, patient. You are planning a dinner for a small gathering and want to order Italian food from a local restaurant. First, search_restaurants(cuisine=\"Italian\", location=\"Downtown\", price_range=\"$$\") to find suitable options within your budget. Once you have identified a potential restaurant, get_restaurant_details(restaurant_id=\"R123\") to ensure it meets your preferences and has good reviews. After confirming the restaurant, get_restaurant_menu(restaurant_id=\"R123\", category=\"Pasta\") to select a dish that suits your guests' tastes. Finally, add_item_to_cart(user_id=\"U1015\", restaurant_id=\"R123\", item_id=\"I456\", quantity=2) to ensure you have enough servings for everyone attending.",
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
                kwargs={"restaurant_id": "R123", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U193", "restaurant_id": "R123", "item_id": "I456", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U087",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are patient, confident, organized, direct. First, search for Italian restaurants located in Downtown with a moderate price range of $$, as you are planning a dinner delivery for a client meeting. Once you have identified a suitable restaurant, retrieve the menu focusing on the Pasta category to ensure the options meet your client's preferences. After confirming the selection, proceed to create an order for two servings of the chosen pasta dish, with delivery to 123 Main St, Downtown. Use a Credit Card for payment and include the special instruction to leave the order at the door, ensuring a seamless and contactless delivery experience.",
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
                name="create_order",
                kwargs={"user_id": "U087", "restaurant_id": "R001", "items": [{"item_id": "I123", "quantity": 2}], "delivery_address": "123 Main St, Downtown", "payment_method": "Credit Card", "special_instructions": "Leave the order at the door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are logical, optimistic. Search for Italian restaurants in the downtown area within a moderate price range.",
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
        user_id="U098",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are optimistic, patient, organized, cautious. Begin by searching for Italian restaurants in the Chelsea neighborhood with a price range of $$. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R1023 to verify its opening hours and delivery zone to ensure it meets your delivery requirements. Then, proceed to get the restaurant menu for restaurant ID R1023, focusing on the \"Pasta\" category, and add item ID I234 (Spaghetti Carbonara) to cart for user ID U5678 with quantity 1 and extra parmesan, ensuring the order is placed correctly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Chelsea", "price_range": "$$"}
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
                kwargs={"user_id": "U098", "restaurant_id": "R1023", "item_id": "I234", "quantity": 1, "customizations": "extra parmesan"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U020",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown2003@email.com. You are independent, flexible. Search for restaurants with cuisine 'Mexican' in the location 'San Francisco' with price_range 'medium'. Once you identify a potential option, get details for restaurant R567 to check its opening hours and location. This information will help you determine if the restaurant is a viable partner for DoorDash delivery services in the area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "medium"}
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
        user_id="U087",
        instruction="Your name is Patricia Miller and your email is patricia.miller3271@email.com. You are flexible, polite, cautious, confident. First, search for Mexican restaurants in the 90210 area with a price range of $$ to $$$ to find suitable dining options. Once you have identified a restaurant, get the restaurant menu for restaurant ID R5678 to check available items in the taco category. This will help you determine if they offer a variety of taco options that meet your preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "90210", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "taco"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U138",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are independent, cautious, confident, direct. First, search for Italian restaurants near San Francisco, CA with a price range of $10-$30 to find a suitable dining option. Once you have identified a restaurant, get the restaurant menu for restaurant ID R1023 with a focus on the \"Pasta\" category. This will help you decide on the best pasta dish to order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco, CA", "price_range": "$$"}
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
        user_id="U143",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are organized, flexible, optimistic. Get the menu for restaurant ID R567 to find available pasta dishes.",
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
        user_id="U192",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are organized, patient, logical. First, search for restaurants offering Mexican cuisine in Patricia's location with a price range of $10-$20 to find suitable dining options. Once you identify a restaurant, such as R567, get the menu to explore available items in the Tacos category. This will help you understand the variety of tacos offered and make an informed decision. After reviewing the menu, add item I234 (Chicken Taco) to the cart for Patricia with a quantity of 3 and no customizations to complete her order efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Patricia's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U192", "restaurant_id": "R567", "item_id": "I234", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are organized, optimistic. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$20 to find a suitable dining option for a casual evening. Once you have identified a restaurant, get the menu for restaurant ID R245 to view available items in the Tacos category, ensuring there are appealing choices for your taste. After reviewing the menu, add item I876 (Chicken Tacos) to the cart for user ID U001 with quantity 3 and no customizations, preparing for a convenient and delicious meal.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R245", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U143", "restaurant_id": "R245", "item_id": "I876", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are flexible, organized, direct. First, search for Italian restaurants in San Francisco with a price range of $$-$$$, as a client has requested recommendations for a business lunch. After identifying a suitable restaurant, get the restaurant menu for restaurant ID R54321, focusing on pasta dishes, to ensure they have a variety of options available.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R54321", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson8206@email.com. You are direct, optimistic, patient. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to identify potential partners for DoorDash. Once you have a list, focus on restaurant ID R123 to get the menu, specifically the \"Pasta\" category, to evaluate their offerings for potential inclusion in a promotional campaign.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
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
        user_id="U095",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are direct, flexible, confident. First, search for restaurants offering Mexican cuisine in the downtown area within a moderate price range to identify potential dining options. Once you have a list, get details for restaurant R567 to check its operational hours and customer reviews, ensuring it meets your expectations. After confirming the restaurant's suitability, create an order for user U9426 from restaurant R567 with items I789 and I790, specifying the delivery address as \"123 Main St, Apt 4B\" and using \"credit card\" as the payment method.",
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
                kwargs={"user_id": "U095", "restaurant_id": "R567", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are independent, confident, patient, cautious. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$30 to find suitable dining options. Next, get the restaurant details for restaurant R567 to check its operating hours and delivery zone to ensure it meets your logistical needs. Finally, get the restaurant menu for restaurant R567, focusing on the 'Tacos' category, and add item I890 (Chicken Taco) to the cart for user U123 with a quantity of 3 and mild salsa customization.",
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
                kwargs={"user_id": "U048", "restaurant_id": "R567", "item_id": "I890", "quantity": 3, "customizations": "mild salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are logical, independent, confident. Create order for user U2988 at restaurant R00123 with items I789 and I790, using delivery address 123 Main St, San Francisco, CA.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R00123"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R00123"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R00123", "item_id": "I789"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R00123", "item_id": "I790"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U104", "restaurant_id": "R00123", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U002",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are direct, cautious, optimistic. First, search for restaurants in Patricia Brown's location with a cuisine preference for Italian and a price range of medium to find suitable dining options. Next, get restaurant details for restaurant R145 to check its menu and operating hours, ensuring it fits Patricia's preferences. Finally, create an order for user U1418 with restaurant R145, selecting items I234 and I235, and arrange delivery to 123 Main St using a Credit Card for payment.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Patricia Brown's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R145"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U002", "restaurant_id": "R145", "items": [{"item_id": "I234", "quantity": 1}, {"item_id": "I235", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are flexible, confident, independent. First, search for restaurants with cuisine \"Mexican\" in the location \"San Francisco\" with a price range of \"$$\". Once you find a suitable restaurant, get the restaurant details for restaurant ID R456 to verify opening hours and delivery zone, ensuring it aligns with the user's location and schedule. After confirming the restaurant is open and delivers to the desired area, get the restaurant menu for restaurant ID R456 and filter by category \"Tacos\". Finally, add item ID I789 (Chicken Taco) to cart for user ID U123 with quantity 3, specifying no onions, to complete the order preparation process.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
                kwargs={"user_id": "U048", "restaurant_id": "R456", "item_id": "I789", "quantity": 3, "customizations": "no onions"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are flexible, logical, direct, organized. First, search for Mexican restaurants in San Francisco with a price range of $10-$30 to identify potential options for a new promotional campaign. Once you have identified restaurant R5678 as a suitable candidate, get detailed information for this restaurant to check its operational hours and address, ensuring it aligns with our delivery service capabilities. Finally, get the menu for restaurant R5678 focusing on the 'Tacos' category, as we plan to feature this popular item in our upcoming marketing materials.",
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
        user_id="U178",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are independent, polite, flexible. Get the restaurant menu for restaurant ID R5678 to explore available items.",
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
        user_id="U081",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are patient, optimistic, cautious, logical. Search for restaurants offering Mexican cuisine in Jennifer's area with a moderate price range to identify potential dining options. Once you have identified restaurant R567 as a suitable choice, get the menu for restaurant R567 to explore available Mexican dishes that match Jennifer's preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer's area", "price_range": "$$"}
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
        user_id="U151",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are organized, optimistic, logical. First, search for Mexican restaurants in John's area with a price range of $10-$20 to find suitable dining options. Once you have identified a potential restaurant, get restaurant details for restaurant ID R2001 to check their operation hours to ensure they are open during your desired dining time. Finally, get the menu for restaurant ID R2001 focusing on the 'Dinner' category to explore meal options before placing an order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2001"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2001", "category": "Dinner"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are confident, logical. First, search for Mexican restaurants in the Los Angeles area with a price range of $$ to $$$ to identify potential dining options for a client request. Once you have a list, get restaurant details for restaurant ID R5678 to verify it is open and meets delivery zone requirements, ensuring it can serve the client's location. After confirming the restaurant's availability, get the restaurant menu for restaurant ID R5678 to find available items in the \"Tacos\" category, as the client specifically requested tacos.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Los Angeles", "price_range": "$$-$$$"}
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
        user_id="U104",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are independent, patient, direct, flexible. First, search for Italian restaurants in San Francisco with a moderate price range to find a suitable dining option for a client meeting. Once you have identified a restaurant, retrieve the pasta menu from the selected restaurant to review available options.",
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
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are patient, direct, independent. First, search for Mexican restaurants in the Downtown area with a price range of $$ to $$$ to find a suitable dining option. Once you have identified restaurant R321 as a potential choice, get the restaurant details to check its hours and delivery zones to ensure it can deliver to the specified location. After confirming the restaurant's delivery capabilities, create an order for user U123 at restaurant R321 with item I654, ensuring the delivery address is \"123 Main St, Apt 4B\" and the payment method is via credit card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Downtown", "price_range": "$$ to $$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R321"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U151", "restaurant_id": "R321", "items": [{"item_id": "I654", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are independent, logical, polite, flexible. First, search for Mexican restaurants in Midtown with a price range of $10-$20 to find affordable dining options for our customers. Once you identify a potential restaurant, get restaurant details for restaurant R101 (Taco Fiesta) to ensure it meets our quality standards and offers a pleasant dining experience. After confirming the restaurant's suitability, get the restaurant menu for restaurant R101 (Taco Fiesta) and filter by category \"Tacos\" to focus on popular menu items. Finally, add item I201 (Chicken Taco) to cart for user U3233 with quantity 3, as this is a frequently ordered item that aligns with our current promotional offer.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Midtown", "price_range": "$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U042", "restaurant_id": "R101", "item_id": "I201", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U037",
        instruction="Your name is Robert Brown and your email is robert.brown1066@email.com. You are optimistic, logical, independent, flexible. First, search for Italian restaurants located in the downtown area with a moderate price range ($$) to find a suitable dining option. Once you have identified a restaurant that meets your criteria, proceed to create an order from that restaurant. Use the restaurant ID you found, and include two items of your choice. Ensure the delivery address is set to 123 Main St, and select credit card as the payment method. Add a special instruction to leave the delivery at the front door.",
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
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U037", "restaurant_id": "R001", "items": [{"item_id": "I001", "quantity": 1}, {"item_id": "I002", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "Leave the delivery at the front door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U050",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9197@email.com. You are organized, flexible, direct, cautious. First, search for restaurants in the downtown area with cuisine \"Italian\" and price range \"$$\" to find potential options for a client order. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R456 to check business hours and delivery zones to ensure it can accommodate the client's delivery requirements. Finally, get the restaurant menu for restaurant ID R456, focusing on the \"Pizza\" category, and add item I789 (Margherita Pizza) to the cart for user U001 (James Jones) with quantity 2, ensuring the order meets the client's preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "Pizza"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U050", "restaurant_id": "R456", "item_id": "I789", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are organized, flexible, confident. search_restaurants(location=\"downtown\", cuisine=\"Italian\", price_range=\"$$\")",
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
        user_id="U050",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are independent, flexible, logical. First, get the restaurant menu for restaurant ID R234 to explore available items in the Tacos category. Once you have confirmed that the Chicken Taco is available, add item ID I567 (Chicken Taco) to cart for user ID U001 with quantity 3 and extra guacamole customization. This will ensure that the user can enjoy their desired meal with the preferred customization, enhancing their ordering experience on DoorDash.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U050", "restaurant_id": "R234", "item_id": "I567", "quantity": 3, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams7359@email.com. You are flexible, organized. Search for Italian restaurants in Linda Garcia's location with a price range of medium. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R123 to explore available pasta dishes. This will help you recommend the best options for her order on DoorDash.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U106"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda Garcia's location", "price_range": "$$"}
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
        user_id="U134",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are patient, organized, flexible. First, search for Italian restaurants in the downtown area with a price range of $10-$20 to find suitable dining options for our upcoming team lunch. Next, get restaurant details for restaurant ID R789 to check its opening hours and location, ensuring it fits our schedule and is conveniently located. Finally, create an order for user U345 with restaurant ID R789, including items I101 and I102, with the delivery address \"123 Elm Street\", using the payment method \"Credit Card\", and include special instructions to \"Leave at the door\" to accommodate the recipient's preference for contactless delivery.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R789"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U134", "restaurant_id": "R789", "items": [{"item_id": "I101", "quantity": 1}, {"item_id": "I102", "quantity": 1}], "delivery_address": "123 Elm Street", "payment_method": "Credit Card", "special_instructions": "Leave at the door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are patient, cautious. Get the restaurant menu for restaurant ID R456 to view available pasta dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are flexible, optimistic, cautious. Get the menu for restaurant ID R987 to review available items in the Tacos category.",
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
        user_id="U041",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are confident, organized. Add item I789 (Chicken Tacos) to cart for user linda.garcia2772@email.com with quantity 3.",
        actions=[
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U041", "restaurant_id": "R001", "item_id": "I789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are polite, logical, direct. Add item I205 (Chicken Tacos) to cart for user Linda Garcia with quantity 2 and no customizations.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U041"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U041", "restaurant_id": "R123", "item_id": "I205", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are organized, patient, optimistic. First, search for restaurants offering Mexican cuisine in the San Francisco area within a moderate price range to identify potential options for a new DoorDash partnership. Once you have a list, get detailed information for restaurant R5678 to confirm it is open and accepting orders, ensuring it meets the operational requirements for our service.",
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
        user_id="U113",
        instruction="Your name is Linda Miller and your email is linda.miller5151@email.com. You are organized, polite. First, search for restaurants in the downtown area offering Mexican cuisine with a price range of $10-$20 to identify potential options for new users. Next, get detailed information about restaurant R234 to verify its operating hours and delivery zones, ensuring it meets the needs of our delivery service. Finally, get the menu for restaurant R234 to find available items in the \"Tacos\" category, which will help in creating promotional content for our customers interested in Mexican cuisine.",
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
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U055",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are organized, polite, patient, independent. First, search for restaurants offering Mexican cuisine in the user's area to find suitable options for their dinner plans. Once a restaurant is selected, get the menu for restaurant ID R1023 to explore available items. After reviewing the menu, add item I204 (Chicken Tacos) to the cart for user U1558 with quantity 3 to ensure their order is ready for checkout on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "user's area"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U055", "restaurant_id": "R1023", "item_id": "I204", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is Mary Miller and your email is mary.miller1688@email.com. You are cautious, direct, organized, polite. Search for restaurants with Mexican cuisine in the San Francisco area within a moderate price range. Once you have identified potential options, get restaurant details for restaurant ID R1023 to verify operating hours and customer ratings. This information will help ensure that the restaurant meets DoorDash's quality standards and is available during peak delivery times.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U093",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are logical, organized. First, search for Mexican restaurants in the San Francisco area with a price range of $$ to $$$ to find potential dining options. Once you identify a suitable restaurant, get the restaurant details for restaurant R5678 to check their hours and delivery zones, ensuring they can deliver to the desired location. Finally, create an order for user Mary Jones (user_id U4200) at restaurant R5678 with items [I7890, I7891], delivery address 123 Main St, payment method \"credit_card\", and special instructions \"Leave at door,\" ensuring a seamless and efficient delivery experience.",
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
                kwargs={"user_id": "U093", "restaurant_id": "R5678", "items": [{"item_id": "I7890", "quantity": 1}, {"item_id": "I7891", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit_card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is Mary Williams and your email is mary.williams2739@email.com. You are logical, optimistic, organized. Start by searching for Chinese restaurants in San Francisco with a price range of $10-$20 per meal to find suitable dining options. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R5678 to check its operational hours and delivery area, ensuring it fits your schedule and location. Finally, create an order for user ID U1234 at restaurant ID R5678 with items I234 and I235, using delivery address 123 Elm St, San Francisco, and payment method Credit Card, to complete the transaction efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U019", "restaurant_id": "R5678", "items": [{"item_id": "I234", "quantity": 1}, {"item_id": "I235", "quantity": 1}], "delivery_address": "123 Elm St, San Francisco", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is Patricia Jones and your email is patricia.jones4973@email.com. You are direct, polite, cautious. First, search for Mexican restaurants in Linda's area with a price range of $10-$20 to find suitable dining options. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R567 to check their delivery zone and hours, ensuring they can deliver to Linda's location. After confirming delivery availability, get the restaurant menu for restaurant ID R567 and filter by the \"Tacos\" category to explore options. Finally, create an order for user U1610 at restaurant ID R567 with items [(I789, quantity 3)], using the delivery address \"123 Main St.\" and the payment method \"Credit Card.\"",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda's area", "price_range": "$$"}
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
                name="create_order",
                kwargs={"user_id": "U175", "restaurant_id": "R567", "items": [{"item_id": "I789", "quantity": 3}], "delivery_address": "123 Main St.", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are confident, logical, flexible, polite. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to identify potential options for a client meeting. Once you have found a suitable restaurant, get the restaurant menu for restaurant R1023, focusing on the pasta category, to ensure they offer a variety of pasta dishes that can cater to different preferences during the meeting.",
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
        user_id="U167",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are direct, optimistic. First, search for restaurants offering Chinese cuisine in San Francisco with a price range of $10-$30. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R5678, focusing on the 'Main Dishes' category. This will help you make an informed decision for placing an order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U016",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are independent, patient, logical. First, search for restaurants in Jennifer's area with a focus on Italian cuisine and mid-range pricing to find suitable options for a potential DoorDash partnership. Next, get detailed information for restaurant R2345 to evaluate menu options and operational hours, ensuring it aligns with DoorDash's delivery capabilities and customer preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "price_range": "$$"}
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
        user_id="U035",
        instruction="Your name is Michael Smith and your email is michael.smith2502@email.com. You are confident, logical, optimistic. First, search for Italian restaurants in Linda Brown's location with a price range of $10-$30 to find suitable dining options. Once you have identified a restaurant, get the restaurant menu for restaurant ID R101, focusing on the pasta category, to explore potential meal choices. After reviewing the menu, add item I203 (Spaghetti Carbonara) to Linda Brown's cart from restaurant ID R101 with quantity 1, ensuring her selection is ready for checkout.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda Brown's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U035", "restaurant_id": "R101", "item_id": "I203", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are logical, polite, optimistic. First, search for restaurants with Mexican cuisine in the downtown area within a moderate price range to find suitable dining options. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R567 to check its operational hours and delivery zone, ensuring it can deliver to your location. Finally, get the menu for restaurant ID R567 to find available items in the \"Main Course\" category, and if Chicken Tacos are available, add item I890 (Chicken Tacos) to the cart for user U9426 with quantity 3 and extra salsa customization.",
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
                kwargs={"restaurant_id": "R567", "category": "Main Course"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U095", "restaurant_id": "R567", "item_id": "I890", "quantity": 3, "customizations": "extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are cautious, logical, organized. Search for restaurants offering Mexican cuisine in the vicinity of Linda's current location.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda's current location"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U046",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are flexible, polite, cautious, independent. First, search for Mexican restaurants in the San Francisco area with a price range of $$-$$$. Once you identify a few potential options, get the restaurant details for restaurant ID R456 to review ratings and operating hours. This information will help you determine if this restaurant is a suitable addition to the DoorDash platform, ensuring it meets our quality and operational standards.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$-$$$"}
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
        user_id="U163",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are cautious, polite. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$20 to explore options for a casual dinner. Once you have identified restaurant R567 as a potential choice, get the restaurant details to confirm its operating hours and delivery zones, ensuring it fits your schedule and location. Finally, create an order for user U001 with restaurant R567, including items I890 with specified customizations, and use the saved delivery address to complete the process seamlessly.",
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
                kwargs={"user_id": "U163", "restaurant_id": "R567", "items": [{"item_id": "I890", "quantity": 1, "customizations": "extra cheese"}]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U118",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are optimistic, organized. First, search for Thai restaurants in the San Francisco area with a moderate price range to identify potential new partners for DoorDash. Once you have a list, get restaurant details for restaurant ID R789 to confirm it is open for delivery. This will help us ensure that we can provide a diverse selection of Thai cuisine options to our customers.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Thai", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U101",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are logical, patient. Get the restaurant menu for restaurant ID R567 to review available items.",
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
        user_id="U055",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are flexible, independent, optimistic, cautious. Search for restaurants in Robert Miller's area with cuisine 'Italian' and price_range '$$'",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U055"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Robert Miller's area", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U010",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are confident, patient, flexible. First, search for Chinese restaurants in Linda Smith's area with a price range of moderate to identify potential options for a new partnership with DoorDash. Once you have identified a suitable restaurant, get the menu for restaurant R101, focusing on the appetizers category, to evaluate their offerings and see if they align with our delivery service goals.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "Linda Smith's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "appetizers"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U055",
        instruction="Your name is Mary Williams and your email is mary.williams2739@email.com. You are patient, direct. First, search for restaurants in the New York City area offering Mexican cuisine with a price range of $10-$20 to find potential dining options. Next, get detailed information for restaurant R9876 to verify its operational hours and delivery zone, ensuring it fits within the desired area and timing for a potential order. Finally, create an order for user U1558 at restaurant R9876 with items [I2345] and include a special instruction for no onions, making sure the order is tailored to the user's preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R9876"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U055", "restaurant_id": "R9876", "items": [{"item_id": "I2345", "quantity": 1}], "special_instructions": "No onions"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U133",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are logical, independent. First, get restaurant details for restaurant ID R123 to confirm it’s open and accepts orders. Once confirmed, get the restaurant menu for restaurant ID R123 to explore available tacos, ensuring that you can make an informed decision for a customer order on DoorDash.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R123"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams7359@email.com. You are flexible, confident, independent. Search for restaurants offering Mexican cuisine in the downtown area with a price range of $10-$20. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R567 to explore available taco options. This will help you decide if you want to place an order through DoorDash for your upcoming lunch meeting.",
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
        user_id="U076",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are independent, optimistic, confident. First, search for restaurants offering Mexican cuisine in San Francisco within a moderate price range to find suitable dining options. Once you identify a promising restaurant, get the restaurant details for restaurant ID R456 to check their operational hours and delivery zones, ensuring they can deliver to your location. Finally, get the menu for restaurant ID R456 and filter by the 'Tacos' category to explore their offerings, and add item I789 (Chicken Tacos) to your cart for user ID U123 with a quantity of 3 and extra guacamole for a delightful meal experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
                kwargs={"user_id": "U076", "restaurant_id": "R456", "item_id": "I789", "quantity": 3, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U055",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are flexible, logical. First, search for restaurants with Italian cuisine in the downtown area with a price range of $$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R102 to browse available pasta dishes. After reviewing the menu, add item I234 (Spaghetti Carbonara) to cart for user ID U001 with quantity 1.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U055", "restaurant_id": "R102", "item_id": "I234", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are cautious, confident. Search for restaurants with cuisine \"Italian\" in the location \"San Francisco\" and price_range \"$$\". Once you find a suitable option, get the restaurant menu for restaurant_id \"R2345\" to browse available items. This will help you decide on the best dishes to order for delivery to your address at 123 Main St, San Francisco, CA, using your preferred payment method of credit card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U158",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are optimistic, cautious. First, search for Mexican restaurants in San Francisco within the $$ price range to find a suitable option for dinner. Once you have identified a potential restaurant, get the restaurant details for restaurant_id=\"R001\" to ensure it meets your preferences and requirements. After confirming the restaurant is a good choice, proceed to create an order for user_id=\"U12345\" from this restaurant, selecting items with IDs \"I789\" and \"I456\", and arrange for delivery to 123 Elm St, San Francisco, CA. Make sure to use a credit card for payment and include special instructions to leave the order at the door.",
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
                name="create_order",
                kwargs={"user_id": "U158", "restaurant_id": "R001", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I456", "quantity": 1}], "delivery_address": "123 Elm St, San Francisco, CA", "payment_method": "credit_card", "special_instructions": "Leave the order at the door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are flexible, organized, direct, polite. First, search for restaurants in Miami, FL offering Mexican cuisine with a price range of $10-$30. Once you have identified a suitable restaurant, get the restaurant menu for restaurant R2345 to view available items in the Tacos category. This will help you ensure that the menu aligns with customer preferences and price range before proceeding with any orders.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Miami, FL", "price_range": "$$"}
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
        user_id="U176",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are cautious, confident. First, search for restaurants in San Francisco with cuisine type 'Mexican' and price range '$$' to identify potential new additions to the DoorDash platform. Once you have identified a promising restaurant, get the restaurant details for restaurant ID R234 to check their hours and location, ensuring they meet DoorDash's operational requirements.",
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
        user_id="U167",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are direct, flexible. First, get the restaurant menu for restaurant ID R1023, focusing on the pasta category, to ensure the availability of the desired items. Then, create an order for user ID U314 at restaurant ID R1023 with items [I567] and delivery address as 123 Main St, San Francisco. This will ensure that the customer receives their preferred pasta dish efficiently.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U167", "restaurant_id": "R1023", "items": [{"item_id": "I567", "quantity": 1}], "delivery_address": "123 Main St, San Francisco"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are flexible, optimistic. First, search for Italian restaurants in the San Francisco area with a price range of $$. Once you find a suitable restaurant, get the restaurant details for restaurant ID R234 to check business hours and location to ensure it fits your schedule and is conveniently located. After confirming the details, create an order for user ID U101 at restaurant ID R234 with items I123 and I124, ensuring delivery to 123 Main St, and use a credit card for payment.",
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
                kwargs={"user_id": "U006", "restaurant_id": "R234", "items": [{"item_id": "I123", "quantity": 1}, {"item_id": "I124", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit_card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U007",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are organized, cautious, independent, optimistic. Use search_restaurants to find Chinese restaurants in San Francisco within a medium price range. Once you have identified a suitable restaurant, get_restaurant_menu for restaurant ID R5678 to browse available menu items. This will help you decide on a meal option that fits your taste and budget before placing an order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U046",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are organized, independent. Search for restaurants with cuisine \"Mexican\" in the location \"San Francisco, CA\" with price range \"$$\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco, CA", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are independent, logical, optimistic. add_item_to_cart(user_id=\"U001\", restaurant_id=\"R102\", item_id=\"I201\", quantity=1, customizations={\"spicy_level\": \"medium\"})",
        actions=[
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U192", "restaurant_id": "R102", "item_id": "I201", "quantity": 1, "customizations": {"spicy_level": "medium"}}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is Mary Miller and your email is mary.miller1688@email.com. You are confident, patient, independent, cautious. First, get the restaurant menu for restaurant ID R1023 to explore available categories and items. Once you have reviewed the menu, create an order for user U9023 at restaurant ID R1023 with items [I204, I305], delivery address 123 Main St, and payment method credit card.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U104", "restaurant_id": "R1023", "items": [{"item_id": "I204", "quantity": 1}, {"item_id": "I305", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U134",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are independent, direct. Start by searching for restaurants in the 94103 area with cuisine type \"Mexican\" and price range \"$$\" to find suitable dining options. Once you have identified a promising restaurant, get the restaurant details for restaurant ID R1023 to check their operating hours and ensure they are open during your preferred dining time. After confirming the restaurant's availability, get the restaurant menu for restaurant ID R1023 to find available items in the \"Tacos\" category. Finally, create an order for user ID U001 at restaurant ID R1023 with items [I789] and arrange delivery to \"123 Market St, San Francisco, CA 94103\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "94103", "price_range": "$$"}
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
                name="create_order",
                kwargs={"user_id": "U134", "restaurant_id": "R1023", "items": [{"item_id": "I789", "quantity": 1}], "delivery_address": "123 Market St, San Francisco, CA 94103"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U118",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are confident, flexible, polite, patient. Search for Chinese restaurants in the San Francisco area with a price range of $10-$20.",
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
        user_id="U030",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are direct, optimistic, independent. First, search for restaurants in the downtown area with a cuisine preference for Italian and a moderate price range to find potential dining options. Once you have identified restaurant R567, get details to check their operating hours and delivery zones to ensure they can deliver to the desired location. Then, get the menu for restaurant R567 and filter by the 'Pasta' category to select suitable items for an order.",
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
                kwargs={"restaurant_id": "R567", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U101",
        instruction="Your name is Linda Miller and your email is linda.miller5151@email.com. You are polite, patient, optimistic. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$20 to identify potential options for a customer interested in affordable dining. Next, get restaurant details for restaurant R245 to verify its operational hours and customer ratings, ensuring it meets quality and availability standards for a potential order. Finally, get the menu for restaurant R245 to explore available dishes in the \"Tacos\" category, which will allow you to assist a customer in selecting specific items, such as adding item I678 (Chicken Taco) to the cart for user U102 (Michael Davis) with a quantity of 3.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
                kwargs={"user_id": "U101", "restaurant_id": "R245", "item_id": "I678", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U101",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are polite, organized. First, get restaurant details for restaurant ID R512 to verify if it's open and accepting orders, as this will ensure the restaurant can fulfill new orders. Once confirmed, proceed to create an order for user ID U102 at restaurant ID R512 with items [I789, I790], using the delivery address \"123 Elm Street\" and the payment method \"Credit Card.\" This sequence ensures that the order is placed successfully with an operational restaurant, providing a smooth experience for the customer.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R512"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U101", "restaurant_id": "R512", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Elm Street", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is Patricia Jones and your email is patricia.jones4973@email.com. You are flexible, optimistic, polite. First, search for Mexican restaurants in San Francisco within a moderate price range to find a suitable dining option for a client meeting. Once you identify a potential restaurant, get the restaurant menu for restaurant ID R5678 to review available items and ensure they meet the client's dietary preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U175",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are independent, cautious. First, search for restaurants serving Asian cuisine in the downtown area within a medium price range to find potential dining options. Once you identify a suitable restaurant, get restaurant details for restaurant ID R101 to check operating hours and delivery zones, ensuring it fits your schedule and location. Finally, get the restaurant menu for restaurant ID R101 and filter by category \"Main Dishes\" to explore the main course offerings and make an informed decision.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Asian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Main Dishes"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U128",
        instruction="Your name is Robert Brown and your email is robert.brown1066@email.com. You are logical, direct, organized. First, search for restaurants offering Mexican cuisine in the downtown area within a mid-range price category to identify potential dining options. Once you have identified a suitable restaurant, get restaurant details for restaurant ID R200 to verify hours and delivery zone, ensuring it meets the necessary criteria for a convenient order. Finally, create an order for user ID U7359 at restaurant ID R200 with items [I3001, I3005] and delivery address \"123 Main St, Apt 4B\" to complete the transaction efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R200"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U128", "restaurant_id": "R200", "items": [{"item_id": "I3001", "quantity": 1}, {"item_id": "I3005", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U193",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis6303@email.com. You are cautious, polite, organized, independent. First, search for restaurants offering Mexican cuisine within the delivery zone of John Miller's address to ensure that restaurant R1023 is available for delivery. Next, get detailed information for restaurant R1023 to verify its opening hours and delivery options, ensuring it can accommodate an order at the desired time. Finally, get the menu for restaurant R1023, focusing on the \"Tacos\" category, to confirm the availability of Chicken Tacos and Guacamole before proceeding with any order placements.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "John Miller's address"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
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
        user_id="U151",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are confident, logical, patient, direct. search_restaurants(cuisine=\"Italian\", location=\"downtown\", price_range=\"medium\")",
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
        user_id="U178",
        instruction="Your name is Mary Williams and your email is mary.williams2739@email.com. You are logical, direct, confident. Get the menu for restaurant R102, focusing on the Tacos category.",
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
        user_id="U090",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9197@email.com. You are patient, independent, optimistic. Search for Italian restaurants in San Francisco with a price range of $$ to $$$, and then get the restaurant details for restaurant ID R101 to review its ratings and hours of operation. This information will help you identify potential partners for DoorDash to expand its delivery options in the area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is Patricia Jones and your email is patricia.jones4973@email.com. You are patient, logical. First, search for Mexican restaurants in Austin, TX with a medium price range to find a suitable option for dinner. Once you have identified a restaurant, retrieve its details using the restaurant ID to ensure it meets your preferences and has the items you want.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Austin, TX", "price_range": "$$"}
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
        user_id="U081",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are cautious, patient, flexible. Get the restaurant menu for restaurant ID R2345 to browse available items.",
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
        user_id="U113",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are flexible, patient. Get the menu for restaurant R5678, focusing on the 'Dinner Specials' category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Dinner Specials"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are confident, patient. First, search for Italian restaurants located in downtown with a medium price range. Once you find a suitable restaurant, proceed to get the restaurant menu, focusing specifically on the Pasta category.",
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
        user_id="U128",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are optimistic, logical. Start by searching for Italian restaurants in Chicago, IL with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a promising restaurant, get the restaurant details for restaurant ID R1024 to confirm their opening hours and delivery zone to ensure they can deliver to your location. After confirming the restaurant's availability, get the restaurant menu for restaurant ID R1024 to explore available pasta dishes. If Spaghetti Carbonara is available, proceed to add item ID I5678 (Spaghetti Carbonara) to cart for user ID U1001 with quantity 1 and no customizations, completing your order preparation on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Chicago, IL", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1024"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1024"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U128", "restaurant_id": "R1024", "item_id": "I5678", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U086",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are direct, patient, organized. First, search for Italian restaurants in San Francisco with a price range of $$ to identify potential new partners for DoorDash. Once you have a list, get restaurant details for restaurant ID R1024 to confirm it is open and accepting orders, ensuring it meets our operational requirements.",
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
        user_id="U106",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are independent, logical, direct. Create order for user U5307 with restaurant R101, including items I202 and I203, delivery address at 123 Main St, using credit card ending in 1234",
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
                kwargs={"user_id": "U106", "restaurant_id": "R101", "items": [{"item_id": "I202", "quantity": 1}, {"item_id": "I203", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit_card_1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are polite, cautious, confident, flexible. First, search for Italian restaurants in New York City with a price range of $$ to $$$ to find potential dining options. Once you have identified restaurant R101 as a candidate, get detailed information for restaurant R101 to verify it meets the order criteria, ensuring it aligns with the user's preferences and quality expectations. After confirming the restaurant's suitability, create an order for user U9677 at restaurant R101 with items I202 and I203, using delivery address 123 Main St, payment method credit card, and no special instructions, ensuring a seamless and satisfactory delivery experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U143", "restaurant_id": "R101", "items": [{"item_id": "I202", "quantity": 1}, {"item_id": "I203", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are optimistic, confident. First, search for Italian restaurants in San Francisco with a moderate price range to find a suitable dining option. Once you have identified a restaurant that matches your preferences, retrieve the menu of the restaurant with the ID \"R001\" to explore the available dishes. This will help you make an informed decision about your order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U176",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are independent, confident. Get the menu for restaurant ID R5678 to view available items in the Tacos category.",
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
        user_id="U151",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are polite, patient. Create order for user John Garcia from restaurant R123 with items I456 and I789, delivery address \"123 Main St\", and payment method \"Credit Card\".",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R123"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R123", "item_id": "I456"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R123", "item_id": "I789"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U151", "restaurant_id": "R123", "items": [{"item_id": "I456", "quantity": 1}, {"item_id": "I789", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U002",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are patient, independent, direct, logical. Search for Italian restaurants in the downtown area of San Francisco with a price range of $$. Once you find a suitable restaurant, get the menu for restaurant ID R101 to explore available items in the pasta category.",
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
        user_id="U151",
        instruction="Your name is Robert Williams and your email is robert.williams9426@email.com. You are patient, cautious, organized, flexible. First, search for Mexican restaurants in San Francisco with a price range of $$ to $$$ to identify potential options for a team lunch. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R5678 to find available taco options, ensuring you can cater to diverse tastes within the team.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$-$$$"}
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
        user_id="U037",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are polite, cautious. Use search_restaurants to find Mexican restaurants in Linda's area with a price range of $10-$30.",
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
        user_id="U046",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are patient, independent, flexible. First, search for restaurants offering Italian cuisine in Patricia's location with a mid-range price. Once you have identified a suitable restaurant, get the menu for restaurant R101 focusing on the pasta category. This will help you decide on the best pasta options to recommend or order for Patricia.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U046"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Patricia's location", "price_range": "$$"}
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
        user_id="U190",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are flexible, patient, independent. First, search for restaurants offering Asian cuisine in the New York City area with a medium price range to expand our delivery options on DoorDash. Once you have identified potential candidates, get detailed information for restaurant R102 (Sushi Palace) to check their opening hours. This will help us ensure that our service aligns with their operational hours for optimal delivery scheduling.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Asian", "location": "New York City", "price_range": "$$"}
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
        user_id="U095",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are polite, direct, patient. search_restaurants(cuisine=\"Italian\", location=\"Downtown\", price_range=\"$$\")",
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
        user_id="U123",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are flexible, patient. search_restaurants(cuisine=\"Italian\", location=\"New York City\", price_range=\"$$\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U016",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are organized, cautious, polite. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to find suitable dining options. Once you have identified a restaurant, get the restaurant menu for restaurant ID R1023 to explore available Italian dishes. This will help in selecting the best items for creating an order for user ID U8206.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
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
        user_id="U175",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are flexible, logical, independent. First, search for restaurants with cuisine \"Mexican\" in the location \"San Francisco\" with a price range of \"$$\". Once you have identified a suitable restaurant, get the restaurant details for restaurant ID \"R345\" to check its operating hours and delivery zones. This will help ensure that the restaurant can accommodate delivery within the desired timeframe and area for a potential DoorDash partnership.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U002",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are organized, direct, confident. get_restaurant_menu(restaurant_id=\"R123\")",
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
        user_id="U190",
        instruction="Your name is Jennifer Garcia and your email is jennifer.garcia3233@email.com. You are direct, cautious, polite. First, search for restaurants with cuisine \"Italian\" in location \"Downtown\" within price range \"$$\" to find suitable dining options for our customer. Once you have identified a potential restaurant, get restaurant details for restaurant ID R234 to ensure it meets the customer's preferences and quality standards. This will help us provide a seamless and satisfactory experience for our users.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
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
        user_id="U187",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are independent, flexible, confident. Search for restaurants with a cuisine of 'Mexican' in the location 'San Francisco' within a price range of '$$'. Once you have identified a potential restaurant, get restaurant details for restaurant_id 'R456' to check operational hours and delivery zones. This will help ensure that the restaurant can meet delivery requirements and is operational during peak meal times, which is crucial for optimizing delivery efficiency for DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U010",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are patient, direct, cautious, independent. First, search for Italian restaurants located in downtown to find a suitable dining option. Once you have identified a restaurant, specifically look for their pasta menu by retrieving the menu details of the restaurant with ID \"R123\" under the pasta category.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown"}
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
        user_id="U167",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are optimistic, cautious. search_restaurants(location=\"San Francisco\", cuisine=\"Italian\", price_range=\"$$\")",
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
        user_id="U087",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are cautious, independent, patient. First, search for Italian restaurants located in the downtown area that offer a medium price range. Once you have identified a suitable restaurant, retrieve the menu focusing on the pasta category from the restaurant with the ID \"R123\". This will help you decide on the best options available for your order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
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
        user_id="U170",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are optimistic, cautious, confident, independent. First, search for restaurants offering Chinese cuisine in the downtown area with a price range of $$ to $$$ to identify potential partners for DoorDash. Once you have identified a promising restaurant, such as restaurant R567, get detailed information to verify its hours of operation and delivery zones to ensure it aligns with DoorDash's service capabilities.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "downtown", "price_range": "$$-$$$"}
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
        user_id="U187",
        instruction="Your name is Jennifer Garcia and your email is jennifer.garcia3233@email.com. You are logical, optimistic, confident. Search for restaurants in the downtown area with a cuisine preference for Italian.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson5028@email.com. You are cautious, polite, direct. Search for restaurants with cuisine \"Mexican\" in Jennifer's area using her email jennifer.brown7411@email.com for location context.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer's area"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are independent, confident, organized, logical. First, search for restaurants offering Mexican cuisine in the downtown area of San Francisco with a price range of $10-$20 to find a suitable dining option. Next, get detailed information for restaurant R5678 to check their operational hours and location to ensure it fits within your schedule and is conveniently located. Finally, get the menu for restaurant R5678 to explore available dishes in the Tacos category, and add item I7890 (Chicken Tacos) to the cart for user U1234 with quantity 3 and no customizations, preparing for a seamless ordering experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown San Francisco", "price_range": "$$"}
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
                kwargs={"user_id": "U140", "restaurant_id": "R5678", "item_id": "I7890", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are polite, optimistic. First, search for Mexican restaurants in Midtown with a moderate price range to find a good dining option. Once you find a suitable restaurant, retrieve the menu to explore the available dishes. After selecting your favorite dish, add it to your cart to prepare for ordering.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Midtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R001"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U122", "restaurant_id": "R001", "item_id": "I001", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U045",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are logical, independent. Get restaurant menu for restaurant ID R231 to explore available Italian dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R231"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U170",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are confident, direct, organized, optimistic. Create an order for user U123 at restaurant R567 with item I789 and delivery address 123 Main St, Manhattan, with credit card payment.",
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
                kwargs={"restaurant_id": "R567", "item_id": "I789"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U170", "restaurant_id": "R567", "items": [{"item_id": "I789", "quantity": 1}], "delivery_address": "123 Main St, Manhattan", "payment_method": "credit_card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U035",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are flexible, optimistic. First, search for restaurants in the downtown area with cuisine type \"Italian\" and price range \"$$\" to find a suitable dining option. Once you have identified a restaurant, get the restaurant menu for restaurant ID R5678 to explore available Italian dishes. After reviewing the menu, add item I3456 (Spaghetti Carbonara) to the cart for user ID U5883 with quantity 1 and no customizations.",
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
                kwargs={"user_id": "U035", "restaurant_id": "R5678", "item_id": "I3456", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U050",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are patient, direct, logical, optimistic. Search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R567 to review available items in the Tacos category. This will help you decide on the best options to recommend for a group order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U124",
        instruction="Your name is Michael Smith and your email is michael.smith2502@email.com. You are confident, polite, logical. First, search for restaurants in Patricia Jones's location with a cuisine preference of \"Italian\" and a price range of \"$$\". Once you have identified potential options, get the restaurant details for restaurant ID R101 to ensure it meets Patricia's preferences. Finally, create an order for Patricia Jones with restaurant ID R101, including items I234 and I567, using her saved delivery address and default payment card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Patricia Jones's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U124", "restaurant_id": "R101", "items": [{"item_id": "I234", "quantity": 1}, {"item_id": "I567", "quantity": 1}]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is Michael Smith and your email is michael.smith2502@email.com. You are patient, cautious, polite, optimistic. First, search for Mexican restaurants in the San Francisco area with a moderate price range to find a suitable option for a team lunch. Once you have identified a restaurant, get the restaurant menu for restaurant ID R567, focusing on the 'Tacos' category, to review the available options. After reviewing the menu, add item I890 (Chicken Taco) to the cart for user U123 with a quantity of 3 and include extra guacamole, ensuring the order meets the team's preferences for a delightful lunch experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U112", "restaurant_id": "R567", "item_id": "I890", "quantity": 3, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are cautious, confident, logical. First, search for Mexican restaurants in the San Francisco area with a mid-range price level to find potential options for expanding DoorDash's delivery offerings. Once you have identified restaurant R234 as a suitable candidate, get the menu for this restaurant and look for vegetarian options in the \"Entrees\" category to assess the variety and appeal of their offerings.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Entrees"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U142",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are flexible, logical. Search for restaurants offering Mexican cuisine in Patricia's neighborhood with a price range of $10-$20.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Patricia's neighborhood", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are cautious, logical, optimistic. Get the menu for restaurant R1001, focusing on the pasta category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1001", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Mary Miller and your email is mary.miller1688@email.com. You are cautious, flexible. First, search for medium-priced Mexican restaurants in San Francisco to find a suitable option for dinner. Once you have identified a restaurant that meets your criteria, obtain the restaurant details using the restaurant ID to ensure it offers your preferred dishes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are organized, optimistic, patient. First, search for restaurants with Mexican cuisine in Mary's local area with a moderate price range to find potential options for her meal. Once you have identified a suitable restaurant, such as restaurant R234, get detailed information to verify its hours and ratings. This will ensure that the restaurant is open and well-rated before proceeding with the order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Mary's local area", "price_range": "$$"}
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
        user_id="U118",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are cautious, independent, direct. Create order for user linda.smith6714@email.com at restaurant ID R5678 with items [I234, I235].",
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
                name="create_order",
                kwargs={"user_id": "U118", "restaurant_id": "R5678", "items": [{"item_id": "I234", "quantity": 1}, {"item_id": "I235", "quantity": 1}]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are optimistic, flexible. Get the restaurant menu for restaurant ID R5678, focusing on the pasta category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are cautious, independent, logical. First, search for restaurants offering Mexican cuisine in San Francisco with a price range of $10-$20. Once you find a suitable restaurant, get the menu for restaurant R234 to view available items in the \"Tacos\" category. This will help you decide if the restaurant meets your preferences and budget for a potential order on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$"}
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
        user_id="U158",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are logical, organized. First, search for restaurants with Chinese cuisine in the downtown area within a moderate price range to find suitable options for a potential order. Once you have identified a restaurant, get the restaurant details for restaurant ID R567 to confirm the address and hours of operation, ensuring it fits within your schedule. Finally, create an order for user U123 at restaurant ID R567 with items [I890, I891], delivery address 123 Main St, payment method \"credit card\", and special instructions \"Leave at the door\" to complete the transaction seamlessly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U158", "restaurant_id": "R567", "items": [{"item_id": "I890", "quantity": 1}, {"item_id": "I891", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "Leave at the door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U128",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are direct, confident, optimistic, organized. Begin by searching for restaurants in Brooklyn with a focus on vegan cuisine and a price range under $30 to find suitable dining options. Next, get the restaurant details for restaurant ID R5678 to verify their operating hours and delivery zones, ensuring they can deliver to the desired location. Finally, create an order for user U8976 with restaurant ID R5678, including items I234 and I235, using the delivery address 123 Green St and the payment method card ending in 5678, to complete the transaction smoothly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "vegan", "location": "Brooklyn", "price_range": "$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U128", "restaurant_id": "R5678", "items": [{"item_id": "I234", "quantity": 1}, {"item_id": "I235", "quantity": 1}], "delivery_address": "123 Green St", "payment_method": "card ending in 5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U134",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown2003@email.com. You are patient, optimistic. First, search for Italian restaurants in the downtown area with a price range of $10-$30 to find a suitable dining option. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R987 to verify its operating hours and location, ensuring it fits your schedule. After confirming the restaurant's details, proceed to get the menu for restaurant ID R987 to explore available Italian dishes. This will help you decide on the best items to order for delivery through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R987"}
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
        user_id="U163",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are organized, flexible, logical, cautious. Search for restaurants with cuisine 'Mexican' in location 'San Francisco' with price_range 'medium'.",
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
        user_id="U177",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are confident, polite, logical, patient. First, search for restaurants in Patricia Miller's location with cuisine preference set to \"Italian\" and price range set to \"medium\". Once you have identified potential options, get detailed information for restaurant R234 to verify its operating hours and delivery options. This will help ensure that the restaurant can accommodate Patricia's dining preferences and schedule.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U177"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Patricia Miller's location", "price_range": "$$"}
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
        user_id="U132",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are organized, independent, flexible, cautious. First, search for restaurants offering Mexican cuisine in the San Francisco area within a moderate price range to find a suitable option for our customer. Once you have identified a restaurant that meets the criteria, get the menu for restaurant R567 to explore available taco options, ensuring that you can provide the customer with a variety of choices. Finally, create an order for user U1011 at restaurant R567 with items I789 (Chicken Tacos) and I790, ensuring the delivery address is set to 123 Main St and the payment method is processed via credit card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U132", "restaurant_id": "R567", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams7359@email.com. You are independent, optimistic, cautious, confident. First, search for Italian restaurants located in Downtown with a moderate price range of $$. After identifying a suitable restaurant, retrieve the menu focusing on the Pizza category from the restaurant with ID \"R123\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "Pizza"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U193",
        instruction="Your name is Robert Williams and your email is robert.williams9426@email.com. You are cautious, organized, independent, optimistic. Search for restaurants offering Mexican cuisine within John's delivery area, ensuring they meet his dietary preferences. Once you identify a suitable option, get the menu for restaurant ID R234 to find available items for order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican"}
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
        user_id="U122",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are polite, cautious. Get the menu for restaurant ID R123 to explore available pasta dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U007",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are organized, independent, patient. First, search for restaurants offering Mexican cuisine in the Midtown area with a price range of $10-$30 to find suitable dining options. Once you identify a potential restaurant, get the restaurant details for restaurant ID R202 to confirm its address and hours of operation, ensuring it fits your schedule and location preferences. After verifying the restaurant's details, proceed to get the restaurant menu for restaurant ID R202 to review available taco options. This will help you make an informed decision about your order. Once you have reviewed the menu and decided on your order, add item I789 (Chicken Tacos) to the cart for user U6151 with a quantity of 3 and include extra salsa customization to enhance the dining experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Midtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R202"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R202"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U007", "restaurant_id": "R202", "item_id": "I789", "quantity": 3, "customizations": "extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are direct, confident. First, search for restaurants in San Francisco with cuisine type 'Mexican' and price range '$$' to identify potential options for a new promotion. Next, get restaurant details for restaurant ID R1023 to verify opening hours and delivery zone, ensuring it aligns with peak delivery times and areas. Finally, create an order for user robert.garcia9607@email.com from restaurant ID R1023 with items I567 and I568, using the delivery address 123 Market St and payment method 'Credit Card', to test the ordering process and ensure seamless customer experience.",
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
                name="create_order",
                kwargs={"user_id": "U140", "restaurant_id": "R1023", "items": [{"item_id": "I567", "quantity": 1}, {"item_id": "I568", "quantity": 1}], "delivery_address": "123 Market St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U087",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are optimistic, cautious. Search for restaurants in Mary's location with a preference for Italian cuisine and a moderate price range, and then get details for restaurant R567 to check its operating hours and user reviews. This will help you assess the best options available for a potential partnership with DoorDash, ensuring that you recommend a restaurant that not only meets the culinary preferences but also maintains a good reputation and convenient operating hours for customers.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Mary's location", "price_range": "$$"}
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
        user_id="U041",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are flexible, cautious, organized, optimistic. get_restaurant_menu(restaurant_id=\"R123\")",
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
        user_id="U046",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are flexible, confident. First, search for restaurants with Chinese cuisine in the New York City area within a moderate price range to identify potential options for a new delivery partnership. After identifying a suitable restaurant, get the restaurant details for restaurant ID R56789 to verify operating hours and delivery zone, ensuring it aligns with Doordash's logistics and customer demand.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "New York City", "price_range": "$$"}
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
        user_id="U151",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are cautious, optimistic, logical, polite. First, search for Italian restaurants in the San Francisco area with a price range of $$ to $$$ to find suitable dining options for a client meeting. Once you have identified a potential restaurant, get restaurant details for restaurant ID R456 to confirm its hours of operation and delivery options, ensuring it fits within the meeting schedule and offers delivery. After confirming these details, proceed to create an order for user John Garcia with restaurant ID R456, including items [I789, I790], using delivery address 123 Main St, San Francisco, and payment method credit card ending in 1234, to finalize the lunch arrangements for the meeting.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$,$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U151", "restaurant_id": "R456", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card ending in 1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are independent, logical, cautious. Search for restaurants in Linda Garcia's area that offer Mexican cuisine and fall within a mid-range price bracket. Once you find a suitable restaurant, get the menu for restaurant ID R1025, specifically looking for the Tacos category. This will help you decide if the restaurant's offerings meet Linda's preferences and budget for a potential DoorDash order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Garcia's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1025", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are independent, flexible, optimistic. Create order for user ID U001 at restaurant ID R1024 with items [M345, M678], delivery address \"123 Main St, Los Angeles, CA\", and payment method \"credit card\".",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1024"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1024"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R1024", "item_id": "M345"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R1024", "item_id": "M678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U132", "restaurant_id": "R1024", "items": [{"item_id": "M345", "quantity": 1}, {"item_id": "M678", "quantity": 1}], "delivery_address": "123 Main St, Los Angeles, CA", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are patient, direct. First, search for Mexican restaurants in the downtown area with a moderate price range to find a suitable dining option for your upcoming family gathering. Once you have identified a restaurant, get the menu for restaurant ID R1023, focusing on the \"Tacos\" category, to explore their offerings. After reviewing the menu, add item ID I203 (Chicken Tacos) to the cart for user linda.garcia2772@email.com with a quantity of 3 and extra salsa, ensuring a delightful meal experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U041", "restaurant_id": "R1023", "item_id": "I203", "quantity": 3, "customizations": "extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U035",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are optimistic, cautious. First, search for restaurants with Mexican cuisine in Linda's area and within a moderate price range to find suitable options for her. Once you have identified a restaurant, get the menu for restaurant R102 focusing on the \"Tacos\" category to explore specific offerings. This will help you recommend the best taco options to Linda, ensuring a delightful dining experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U187",
        instruction="Your name is Mary Brown and your email is mary.brown1791@email.com. You are logical, independent, polite, confident. First, search for restaurants serving Mexican cuisine in Mary Williams' location with a price range of $10-$20 to find suitable dining options. Once you have identified a potential restaurant, get the menu for restaurant ID R567 to check available items in the \"Tacos\" category, ensuring they meet Mary Williams' preferences. Finally, create an order for user ID mary.williams2739@email.com at restaurant ID R567 with items I789 and I790, using delivery address \"123 Main St\" and payment method \"Credit Card\", to complete the transaction efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Mary Williams", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Tacos"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U187", "restaurant_id": "R567", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U125",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are independent, flexible. First, get details for restaurant R234 to verify if they are open and accepting orders. Then, get the menu for restaurant R234, focusing on the pasta category. This will ensure that you have the most current information about the restaurant's operating status and available pasta dishes before proceeding with any customer orders.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
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
        user_id="U143",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are direct, flexible, organized. First, search for restaurants with cuisine \"Italian\" in the location \"Downtown\" with a price range of \"$$\" to identify potential dining options. Once you have found a suitable restaurant, get restaurant details for restaurant_id \"R123\" to verify operating hours and delivery zones, ensuring it meets your logistical needs. Finally, create an order for user_id \"U567\" with restaurant_id \"R123\" including items \"I456\" and \"I789\" using the delivery address \"123 Main St, Apt 4B\" and payment method \"Credit Card\" to complete the transaction.",
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
                name="create_order",
                kwargs={"user_id": "U143", "restaurant_id": "R123", "items": [{"item_id": "I456", "quantity": 1}, {"item_id": "I789", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U125",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9197@email.com. You are patient, optimistic. Search for Mexican restaurants in the San Francisco area with a price range of $10-$20 to find a suitable option for a lunch meeting. Once you have identified a restaurant, get the menu for restaurant ID R2345 to find available tacos. This will help you decide if the restaurant offers a good variety of taco options for the meeting.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are polite, cautious, patient. First, search for Italian restaurants located in the downtown area with a moderate price range of $$. Once you have identified a suitable restaurant, proceed to get the restaurant menu focusing on the pasta category for restaurant ID \"R456\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are direct, logical. Get the menu for restaurant ID R567 to explore available Italian dishes.",
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
        user_id="U086",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are polite, direct. First, search for Mexican restaurants in Linda's area with a price range of $$. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R234, focusing on the \"Tacos\" category. This will help you decide if the restaurant offers the variety of tacos you are interested in.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda's area", "price_range": "$$"}
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
        user_id="U112",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are patient, independent, cautious. First, search for Mexican restaurants in Midtown with a price range of $$ to identify potential options for expanding our delivery service. Once you have identified a suitable restaurant, get details for restaurant R234 to verify opening hours and delivery zone to ensure it aligns with our service capabilities on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Midtown", "price_range": "$$"}
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
        user_id="U113",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are direct, flexible. First, search for Italian restaurants in the New York City area with a price range of $$ to $$$ to find potential dining options for our users. Once you have identified a suitable restaurant, get details for restaurant R56789 to check its menu and operational hours. This will help ensure we provide accurate information to users looking to place orders through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$-$$$"}
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
        user_id="U030",
        instruction="Your name is John Garcia and your email is john.garcia7961@email.com. You are direct, organized, optimistic, flexible. Get restaurant menu for restaurant ID R567 to find available taco options.",
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
        user_id="U098",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are organized, polite. First, search for restaurants with Mexican cuisine in the area of San Francisco within a moderate price range to find suitable dining options. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R789 to verify its hours and delivery zones, ensuring it can deliver to your location. After confirming the restaurant's availability, obtain the menu for restaurant ID R789 to choose available items. Finally, create an order for user ID U102 at restaurant ID R789 with items [I234, I567], delivery address \"123 Main St, San Francisco\", and payment method \"credit card\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R789"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R789"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U098", "restaurant_id": "R789", "items": [{"item_id": "I234", "quantity": 1}, {"item_id": "I567", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U101",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are confident, optimistic, organized. First, search for restaurants with cuisine \"Mexican\" in location \"San Francisco\" with price range \"$$\" to find a suitable dining option. Once you have identified a promising restaurant, get restaurant details for restaurant ID \"R5678\" to check its operating hours and delivery zones, ensuring it can deliver to your area. After confirming this, get the restaurant menu for restaurant ID \"R5678\" to view available items and select your preferred dishes. Finally, create an order for user ID \"U1234\" with restaurant ID \"R5678\", items [I2345, I2346], delivery address \"123 Main St, San Francisco, CA\", and payment method \"credit_card\" to complete the transaction smoothly.",
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
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U101", "restaurant_id": "R5678", "items": ["I2345", "I2346"], "delivery_address": "123 Main St, San Francisco, CA", "payment_method": "credit_card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are cautious, direct, organized, confident. Get the restaurant menu for restaurant ID R567 to view available items.",
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
        user_id="U176",
        instruction="Your name is Michael Smith and your email is michael.smith2502@email.com. You are cautious, polite, logical. Search for restaurants in the downtown area with a preference for Italian cuisine and moderate price range.",
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
        user_id="U075",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are organized, logical. First, search for restaurants with 'Mexican' cuisine in 'San Francisco' with a price range of '$$' to identify potential new partners for DoorDash. Once you have identified a promising option, get the restaurant details for restaurant ID 'R456' to check its operating hours and ensure it aligns with peak delivery times.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U020",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson8206@email.com. You are optimistic, confident. Add item I678 (Chicken Tacos) to John's cart for restaurant R101 with quantity 2 and extra guacamole customization.",
        actions=[
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U020", "restaurant_id": "R101", "item_id": "I678", "quantity": 2, "customizations": "extra guacamole"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U123",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are polite, cautious, flexible, direct. First, search for restaurants with Italian cuisine in the downtown area with a price range of $$. Once you identify a suitable restaurant, get the restaurant details for restaurant ID R456 to verify its hours and location to ensure it fits your schedule and proximity preferences. After confirming the restaurant's details, create an order for user ID U001 from restaurant ID R456 with items M123 and M234, set the delivery address as 123 Main St, and use a credit card as the payment method.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U123", "restaurant_id": "R456", "items": [{"item_id": "M123", "quantity": 1}, {"item_id": "M234", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U061",
        instruction="Your name is Mary Jones and your email is mary.jones4200@email.com. You are independent, optimistic, organized. First, search for Mexican restaurants in the downtown area with a price range of $$ and above to find suitable options for a special dinner. Once you have identified a restaurant, get the restaurant menu for restaurant ID R567 to view available taco options. This will help you decide on the best items to order for a delightful meal experience.",
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
        user_id="U190",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are logical, independent, patient, cautious. Get the menu for restaurant R567 to explore available items in the \"Main Course\" category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Main Course"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U050",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are polite, logical, direct, flexible. First, search for restaurants offering Thai cuisine in the 94103 zip code area with a price range of $$ to $$$. Once you have identified potential options, get restaurant details for restaurant R5678 to verify its hours and if it meets the delivery zone requirements. This will help us ensure that we can provide timely and accurate delivery services to our customers in this area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Thai", "location": "94103", "price_range": "$$-$$$"}
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
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are independent, direct, polite. Search for restaurants offering Chinese cuisine in New York City within a mid-range price bracket. Once you find a suitable restaurant, such as restaurant R789, get the menu and filter by the 'Dumplings' category. This will allow you to review the options available and ensure they meet your preferences before proceeding with any orders.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R789", "category": "Dumplings"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is Robert Williams and your email is robert.williams9426@email.com. You are cautious, direct. First, search for restaurants offering Mexican cuisine in the San Francisco area within a mid-range price bracket to identify potential options for a client meeting. Once you have identified a suitable restaurant, get the menu for restaurant ID R5678 to identify available items for ordering.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U090",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are logical, confident. Get the menu for restaurant ID R101 to view available items using get_restaurant_menu.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U178",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are confident, cautious. Use `search_restaurants` with `cuisine=\"Mexican\"` and `location=\"San Francisco\"` to find nearby options for Mary Jones.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U178",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are independent, logical, confident. As part of your role at DoorDash, you need to enhance the dining options available for users by first searching for restaurants in the downtown area offering Mexican cuisine within a mid-range price. After identifying a suitable restaurant, proceed to get the menu for restaurant ID R456, focusing on the tacos category. This will help in updating the platform's offerings and ensuring customers have access to diverse meal options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are logical, independent. Search for restaurants in the downtown area offering Mexican cuisine within the price range of $10-$20. Once you find a suitable restaurant, get the menu for restaurant R234, focusing on the 'Tacos' category. This will help you decide on the best options available for a potential order on DoorDash.",
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
        user_id="U046",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are logical, direct, cautious, flexible. First, search for restaurants with cuisine type 'Mexican' in the location 'San Francisco' with a price range '$$' to identify potential dining options. Once you have found a suitable restaurant, get the restaurant menu for restaurant_id 'R102' to explore available dishes. This will allow you to make an informed decision about which items to order for user_id 'U001' with delivery_address '123 Main St, San Francisco'.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U090",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are patient, logical, independent. Get the menu for restaurant R456, focusing on the pasta category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U093",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are logical, confident, patient, flexible. Begin by searching for restaurants in San Francisco with cuisine \"Mexican\" and price range \"$$\" to find potential dining options for a customer. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R5678 to check their hours and delivery zones to ensure they can deliver to the customer's location. After confirming delivery is possible, get the restaurant menu for restaurant ID R5678 with category \"Tacos\" to explore available options. Finally, add item I345 (\"Chicken Taco\") to the cart for user U1234 with a quantity of 2 and no customizations, ensuring the order is ready for checkout.",
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
                kwargs={"user_id": "U093", "restaurant_id": "R5678", "item_id": "I345", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is Patricia Miller and your email is patricia.miller3271@email.com. You are cautious, logical, independent, flexible. Search for restaurants in Linda Brown's area with cuisine preferences for Italian and a moderate price range.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Linda Brown's area", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U142",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are confident, polite. Create order for user Patricia Johnson with restaurant ID R1023 including items I789 and I790, specifying delivery address as 123 Main St, and payment method as credit card.",
        actions=[
            Action(
                name="create_order",
                kwargs={"user_id": "U142", "restaurant_id": "R1023", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U178",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are cautious, independent, polite. First, search for Italian restaurants in San Francisco with a price range of $$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R1023 to find available pasta dishes. After confirming that Spaghetti Bolognese is available, add item I789 (Spaghetti Bolognese) to cart for user ID U001 with quantity 1.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U178", "restaurant_id": "R1023", "item_id": "I789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are patient, organized, logical. Get the menu for restaurant ID R987, focusing on the pasta category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U020",
        instruction="Your name is Robert Brown and your email is robert.brown1066@email.com. You are patient, optimistic, cautious, independent. First, search for restaurants in the San Francisco area with a price range of $$ and offering vegan options to ensure a variety of choices for health-conscious customers. Once you have identified potential options, get restaurant details for restaurant ID R1023 to confirm their operating hours and delivery zones, ensuring they can deliver to your area. Next, obtain the restaurant menu for restaurant ID R1023 to find available vegan items, allowing you to make informed decisions about meal options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
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
        user_id="U143",
        instruction="Your name is Mary Brown and your email is mary.brown1791@email.com. You are flexible, polite, patient, independent. Get the menu for restaurant ID R234 to check available tacos and burritos.",
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
        user_id="U010",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller6443@email.com. You are optimistic, flexible. You are planning a cozy dinner at home and want to enjoy some delicious Italian cuisine. First, search for mid-priced Italian restaurants in San Francisco to find a suitable option. Once you've chosen a restaurant, add a Margherita pizza with extra cheese to your cart.",
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
                kwargs={"user_id": "U010", "restaurant_id": "R001", "item_id": "I123", "quantity": 1, "customizations": "extra cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is John Brown and your email is john.brown5124@email.com. You are confident, cautious. First, get the restaurant menu for restaurant ID R567 to find available taco options. Once you confirm that Chicken Tacos are available, add item I789 (Chicken Taco) to the cart for user Patricia Garcia with quantity 3 and no onions.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U049", "restaurant_id": "R567", "item_id": "I789", "quantity": 3, "customizations": "no onions"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U112",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are organized, polite. Create an order for user U6067 at restaurant R2023 with items I789 and I790, specifying delivery address as \"123 Main St, Apt 4B\" and payment method as credit card.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2023"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2023"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R2023", "item_id": "I789"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R2023", "item_id": "I790"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U112", "restaurant_id": "R2023", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U176",
        instruction="Your name is Mary Miller and your email is mary.miller1688@email.com. You are patient, logical. First, search for restaurants in the downtown area with a cuisine preference for Italian and a price range of $$ to $$$ to find suitable options for a special dinner delivery. Once you have identified a potential choice, get detailed information for restaurant R2345 to verify its opening hours and delivery zones, ensuring it can deliver to your location. After confirming this, get the menu for restaurant R2345, focusing on the pasta category, to select the best dishes for your order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
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
        user_id="U037",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are patient, logical. Get the restaurant menu for restaurant ID R5678 and filter for the category \"Tacos\".",
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
        user_id="U049",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9197@email.com. You are flexible, patient, logical, optimistic. Search for restaurants with Mexican cuisine in the downtown area with a moderate price range. Once you have identified a potential restaurant, get details for restaurant R001 to confirm it is open and check their delivery zones. This information will help ensure that the restaurant can provide delivery services through DoorDash to the desired locations.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
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
        user_id="U048",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are cautious, patient, direct, optimistic. First, search for restaurants with cuisine \"Mexican\" in the location \"San Francisco\" with a price range of \"$$\". Once you find a suitable option, get restaurant details for restaurant ID R101 to ensure it meets your preferences. After confirming the restaurant, create an order for user ID U9904 at restaurant ID R101 with items [I205, I207], delivery address \"123 Main St, San Francisco, CA\", payment method \"Credit Card\", and special instructions \"Leave at door\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U048", "restaurant_id": "R101", "items": [{"item_id": "I205", "quantity": 1}, {"item_id": "I207", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA", "payment_method": "Credit Card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are polite, direct, logical, confident. Get the restaurant menu for restaurant ID R202 to view available sushi options.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R202", "category": "Sushi"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are patient, direct, optimistic, organized. Get the menu for restaurant R6789, focusing on the 'Tacos' category",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R6789", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are confident, cautious. Search for restaurants in Jennifer Garcia's location with a preference for Mexican cuisine and a price range of $10-$30. Once you find a suitable restaurant, get the menu for restaurant R456 to check available items in the \"Tacos\" category.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U042"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer Garcia's location", "price_range": "$$"}
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
        user_id="U106",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson8206@email.com. You are direct, organized, flexible, cautious. First, search for Mexican restaurants in Linda Garcia's area with a price range of $10-$20 to identify potential options for her order. Once you find a suitable restaurant, get restaurant details for restaurant ID R456 to confirm it is open and accepting orders. After confirming the restaurant status, create an order for user Linda Garcia with restaurant ID R456, including items Chicken Tacos and Guacamole, using the delivery address 123 Main St, Apt 4B.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Garcia", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U106", "restaurant_id": "R456", "items": [{"name": "Chicken Tacos", "quantity": 1}, {"name": "Guacamole", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U163",
        instruction="Your name is Mary Miller and your email is mary.miller1688@email.com. You are patient, cautious, independent, organized. First, search for restaurants offering Mexican cuisine in the San Francisco area within a moderate price range to identify potential dining options. Once you have found a suitable restaurant, get the restaurant menu for restaurant ID R345 to find available items in the Tacos category. This will allow you to review the menu offerings and decide on your order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R345", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are optimistic, confident, direct. You are planning a delightful dinner for yourself and want to enjoy some Italian cuisine. First, search_restaurants(cuisine=\"Italian\", location=\"Main Street\", price_range=\"$$\") to find a suitable place nearby. Once you have a list of options, get_restaurant_details(restaurant_id=\"R123\") to ensure the restaurant meets your expectations in terms of ambiance and customer reviews. After confirming it's a great choice, proceed to get_restaurant_menu(restaurant_id=\"R123\", category=\"Pasta\") to explore their pasta offerings. Finally, create_order(user_id=\"U001\", restaurant_id=\"R123\", items=[{\"id\": \"I987\", \"name\": \"Spaghetti Carbonara\", \"quantity\": 1}], delivery_address=\"123 Elm St\", payment_method=\"Credit Card\", special_instructions=\"No cheese\") to enjoy a delicious meal delivered to your doorstep.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Main Street", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R123"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "Pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U104", "restaurant_id": "R123", "items": [{"id": "I987", "name": "Spaghetti Carbonara", "quantity": 1}], "delivery_address": "123 Elm St", "payment_method": "Credit Card", "special_instructions": "No cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Robert Williams and your email is robert.williams9426@email.com. You are direct, patient. search_restaurants(cuisine=\"Italian\", location=\"Downtown\", price_range=\"$$\")",
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
        user_id="U143",
        instruction="Your name is John Brown and your email is john.brown5124@email.com. You are direct, optimistic. Search for restaurants in the San Francisco area offering Mexican cuisine within a mid-range price level. Once you have identified potential options, get detailed information for restaurant R101 to verify its opening hours and location. This will ensure that the restaurant is a viable option for listing on DoorDash and can accommodate delivery times effectively.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams7359@email.com. You are polite, flexible, direct. Create order for user patricia.jones3517@email.com at restaurant R567 with items I789 and I790, using default delivery address and credit card payment method.",
        actions=[
            Action(
                name="create_order",
                kwargs={"user_id": "U124", "restaurant_id": "R567", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are direct, independent, patient. First, search for restaurants offering Mexican cuisine in the San Francisco area within a moderate price range to find potential options for a lunch order. Once you have identified restaurant R5678 as a suitable choice, get details for this restaurant to check its operating hours and delivery zone to ensure it can deliver to 123 Market St. Finally, create an order for user U1234 at restaurant R5678, selecting items from the \"Tacos\" category, specifically a Chicken Taco, and use the saved card as the payment method for delivery to 123 Market St.",
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
                name="create_order",
                kwargs={"user_id": "U098", "restaurant_id": "R5678", "items": [{"item_id": "I001", "quantity": 1}], "delivery_address": "123 Market St", "payment_method": "saved_card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U163",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are flexible, confident, patient, logical. Search for restaurants offering Italian cuisine in downtown with a price range of $$ to $$$.",
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
        user_id="U076",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are organized, independent, direct. Get the menu for restaurant ID R234 to browse available items.",
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
        user_id="U087",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are independent, confident, optimistic, logical. First, search for restaurants offering Mexican cuisine in the ZIP code 94103 with a price range of $10-$20 to find suitable dining options. Then, get restaurant details for restaurant ID R1025 to verify opening hours and delivery zone, ensuring it meets your schedule and location needs. Finally, get the restaurant menu for restaurant ID R1025, focusing on the 'Tacos' category, to review available options before making a decision.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "94103", "price_range": "$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1025"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1025", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U125",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown2003@email.com. You are direct, optimistic. First, search for Italian restaurants in the San Francisco area with a price range of $$ to $$$ to find a suitable dining option. Once you have identified restaurant R245 as a potential choice, get the menu for this restaurant, focusing on the Pasta category, to explore their offerings.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$,$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R245", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U134",
        instruction="Your name is Linda Davis and your email is linda.davis2351@email.com. You are confident, patient, logical, optimistic. Search for restaurants with cuisine \"Mexican\" near \"San Francisco\" with a price range of \"$$\". Once you find a suitable restaurant, get the menu for restaurant ID \"R002\" to explore available Mexican dishes. This will help you decide on the best options for your next DoorDash order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R002"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are patient, organized, confident, independent. First, search for restaurants offering Mexican cuisine in the New York City area within a moderate price range to find suitable options for a potential delivery. Once you have identified a promising restaurant, such as R101, get detailed information to check its hours of operation and delivery zones to ensure it can deliver to your location. After confirming the delivery capability, get the menu for restaurant R101, focusing on the Tacos category, to explore the available options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is Patricia Miller and your email is patricia.miller3271@email.com. You are polite, independent, patient. First, search for Mexican restaurants in Linda Garcia's location with a price range of $10-$20 to find suitable dining options. Once you have identified a potential restaurant, get restaurant details for restaurant ID R789 to check operational hours and ensure it fits within Linda's schedule. After confirming the restaurant's availability, get the menu for restaurant ID R789 and filter for taco items to find specific options that Linda might enjoy. Finally, add item I1234 (Beef Taco) to cart for user Linda Garcia with quantity 3 and no customizations, preparing her order for checkout.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Garcia's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R789"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R789"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U106", "restaurant_id": "R789", "item_id": "I1234", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U193",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are polite, confident, flexible, optimistic. First, search for Italian restaurants in the downtown area with a price range of $$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R234 to find available pasta dishes. This will help us determine if Spaghetti Carbonara is available for ordering.",
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
        user_id="U104",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are organized, polite. \"Create order for user U101 at restaurant R567 with items I789 and I790, and delivery address 123 Market St, San Francisco, using credit card\"",
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
                kwargs={"restaurant_id": "R567", "item_id": "I789"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R567", "item_id": "I790"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U104", "restaurant_id": "R567", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Market St, San Francisco", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U045",
        instruction="Your name is John Garcia and your email is john.garcia7961@email.com. You are polite, confident, optimistic, cautious. First, search for restaurants with Mexican cuisine in the downtown area with a price range of $10-$20 to find a suitable dining option. Once you have identified a potential restaurant, get restaurant details for restaurant ID R1123 to check its hours of operation and delivery zone, ensuring it fits your schedule and location. Finally, get the menu for restaurant ID R1123 to find available items in the \"Tacos\" category, and add item I789 (Chicken Taco) to the cart for user U456 with quantity 3 and no customizations, preparing for a delightful meal delivery experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1123"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1123", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U045", "restaurant_id": "R1123", "item_id": "I789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams7359@email.com. You are organized, direct, patient. First, search for Italian restaurants in the downtown area with a price range of $$. Once you identify a suitable restaurant, get the menu for restaurant ID R1023 to review their offerings. This is part of a project to expand the selection of Italian cuisine available on DoorDash in your area, ensuring a variety of mid-range dining options for customers.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
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
        user_id="U187",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are flexible, independent, polite. Create an order for user Mary Williams with restaurant ID R245, including items I678 and I679, using her saved delivery address and credit card payment method.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U187"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U187", "restaurant_id": "R245", "items": [{"item_id": "I678", "quantity": 1}, {"item_id": "I679", "quantity": 1}], "delivery_address": "Mary Williams' saved address", "payment_method": "Mary Williams' saved payment method"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are cautious, flexible, logical, independent. First, search for Chinese restaurants in the San Francisco area with a price range of $10-$20 to find a suitable dining option. Once you have identified a restaurant that meets these criteria, get the menu for restaurant R456, focusing on the \"Main Dishes\" category. This will allow you to ensure the restaurant offers dishes that align with the budget and preferences before proceeding with any further actions.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "Main Dishes"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are logical, direct, organized, flexible. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to find a suitable dining option for a client meeting. Once you have identified a restaurant, get the restaurant menu for restaurant ID R2345 to explore available dishes and ensure they meet the dietary preferences of your client.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
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
        user_id="U042",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are flexible, polite. Create order for user Jennifer Garcia from restaurant R567 with items Chicken Tacos and Guacamole, delivery address 123 Main St, payment method credit card.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U042", "restaurant_id": "R567", "items": [{"item_id": "I001", "quantity": 1}, {"item_id": "I002", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are cautious, organized, flexible, confident. Create an order for user linda.garcia2772@email.com with restaurant ID R1456, including items [I789, I790 (Guacamole)] with special instructions: \"Extra spicy\".",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1456"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1456"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U041", "restaurant_id": "R1456", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "special_instructions": "Extra spicy"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are polite, optimistic. Get restaurant menu for restaurant ID R5678 to check available items in the 'Tacos' category.",
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
        user_id="U180",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are polite, cautious, confident, logical. search_restaurants(location=\"downtown\", cuisine=\"Italian\", price_range=\"$10-$20\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$10-$20"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U142",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are flexible, cautious, direct. First, search for restaurants in the downtown area offering Mexican cuisine with a medium price range. Once you have identified a suitable option, get the menu for restaurant ID R102, focusing on the \"Tacos\" category. This will help determine if the restaurant offers a variety of taco options that could be appealing to customers on DoorDash looking for a mid-range dining experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are polite, flexible, cautious. First, search for sushi restaurants in San Francisco with a price range of $15-$30 to find potential dining options for a client meeting. Once you have a list, get the restaurant details for restaurant ID R5678 to check its hours and delivery zone, ensuring it fits within the client's requirements for availability and location. Finally, get the menu for restaurant ID R5678, focusing on the 'Sushi Rolls' category, to confirm that the menu offers suitable options for the meeting.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Sushi", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "Sushi Rolls"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are polite, independent, logical, direct. First, search for nearby Asian restaurants in the user's location with a medium price range to identify potential dining options. Once you have a list, get detailed information for restaurant R101 to verify its operating hours, ensuring it fits within the user's schedule. After confirming the restaurant's availability, get the menu for restaurant R101, focusing on the \"Entrees\" category, to help the user make an informed decision. Once the user selects their desired items, create an order for user U9677 from restaurant R101, ensuring the delivery address is set to 123 Main St.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Asian", "location": "user's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Entrees"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U143", "restaurant_id": "R101", "items": [{"item_id": "I001", "quantity": 2}, {"item_id": "I002", "quantity": 1}], "delivery_address": "123 Main St"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U138",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are flexible, confident, logical, optimistic. First, search for Italian restaurants in the downtown area with a moderate price range to find potential dining options. Once you have identified a suitable restaurant, get restaurant details for restaurant ID R567 to check their opening hours and ensure they are open during your desired dining time. Next, get the menu for restaurant ID R567, focusing on the pasta category, to explore their offerings. Finally, add item I234 (Spaghetti Carbonara) from restaurant ID R567 to cart for user ID U345 with quantity 1, as you plan to place an order for delivery through DoorDash.",
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
                kwargs={"restaurant_id": "R567", "category": "pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U138", "restaurant_id": "R567", "item_id": "I234", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U142",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are cautious, independent, confident. First, search for Thai restaurants in the Brooklyn area with a price range of $10-$20 to find potential dining options. Once you have identified a restaurant, get the restaurant details for restaurant R1023 to confirm its opening hours and delivery zone, ensuring it meets your schedule and location needs. Finally, create an order for user U5028 with restaurant R1023, including items I789 and I790, with the delivery address 123 Main St, using the credit card as the payment method, and include the special instructions \"Leave at door\" for a seamless delivery experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Thai", "location": "Brooklyn", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U142", "restaurant_id": "R1023", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are cautious, patient. First, search for Italian restaurants in San Francisco with a price range of $$. Once you find a suitable restaurant, get details for restaurant R234 to check menu and hours. After confirming the restaurant is open and reviewing the menu, focus on the Pasta category and add item I567 (Spaghetti Carbonara) to cart for user michael.williams3137@email.com with quantity 1.",
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
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U167", "restaurant_id": "R234", "item_id": "I567", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Linda Miller and your email is linda.miller5151@email.com. You are independent, logical, patient. First, search for Italian restaurants in San Francisco with a price range of $$-$$$. Once you have identified a suitable restaurant, get restaurant details for restaurant ID R5678 to ensure it meets your preferences. After confirming the restaurant's suitability, get the restaurant menu for restaurant ID R5678, focusing on the pasta category, to decide on the best dishes to order.",
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
                kwargs={"restaurant_id": "R5678", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are confident, patient, optimistic, polite. First, search for Italian restaurants in the downtown area with a price range of $$. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R123 to ensure it meets your preferences. After confirming the restaurant, get the restaurant menu for restaurant ID R123, focusing on the Pizza category, to explore the available options. Finally, add item I456 (Margherita Pizza) to cart for user U001 with quantity 2, ensuring a delightful dining experience through DoorDash.",
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
                kwargs={"restaurant_id": "R123", "category": "Pizza"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U076", "restaurant_id": "R123", "item_id": "I456", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is James Williams and your email is james.williams9904@email.com. You are flexible, optimistic, patient, independent. First, search for Italian restaurants in San Francisco with a price range of $$. Once you have identified a suitable restaurant, specifically restaurant R234, get the restaurant details to check their delivery zone and hours to ensure they can deliver to user U101 (Michael Williams). After confirming the delivery zone and hours, get the menu for restaurant R234 to find available pasta dishes, and then add item I567 (Spaghetti Carbonara) to the cart for user U101 with quantity 1.",
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
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U167", "restaurant_id": "R234", "item_id": "I567", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U002",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are direct, patient. Search for restaurants in Patricia's area with cuisine preference for Italian and a price range of $$ to $$$.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Patricia's area", "price_range": "$$ to $$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are cautious, direct, polite, independent. First, search for Italian restaurants in the San Francisco area with a price range of $$ and above to find a suitable dining option. Once you have identified a restaurant, get the restaurant details for restaurant ID R001 to check their hours and delivery zones to ensure they can deliver to your area. Finally, create an order for user ID U123 at restaurant ID R001 with items I1001 and I1002, using delivery address 123 Main St, payment method credit card, and special instructions \"Leave at door\" to complete your meal request efficiently.",
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
                kwargs={"user_id": "U132", "restaurant_id": "R001", "items": [{"item_id": "I1001", "quantity": 1}, {"item_id": "I1002", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are cautious, patient. Search for restaurants offering Mexican cuisine in the Los Angeles area with a price range of $10-$20.",
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
        user_id="U142",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are direct, organized. Create order for user U5028 from restaurant ID R4523 with items [I893, I894], delivery address 123 Main St, Apt 4, and payment method credit card ending in 1234.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R4523"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R4523"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R4523", "item_id": "I893"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R4523", "item_id": "I894"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U142", "restaurant_id": "R4523", "items": [{"item_id": "I893", "quantity": 1}, {"item_id": "I894", "quantity": 1}], "delivery_address": "123 Main St, Apt 4", "payment_method": "credit card ending in 1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson8206@email.com. You are logical, patient. Get the restaurant menu for restaurant ID R1023, focusing on the Tacos category.",
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
        user_id="U128",
        instruction="Your name is James Williams and your email is james.williams9904@email.com. You are cautious, direct. First, search for restaurants in Midtown offering Chinese cuisine with a price range of $10-$20 to identify potential partners for DoorDash. Once you have a list, get details for restaurant R101 to verify their operating hours and delivery zones, ensuring they align with our service capabilities.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "Midtown", "price_range": "$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are independent, direct, cautious, optimistic. Search for Italian restaurants in the downtown area with a moderate price range and get the menu for restaurant ID R123, focusing on the pasta category. This will help you decide on your meal options before creating a new order for user ID U987. Once you have reviewed the menu and decided on your items, proceed to create a new order from restaurant ID R123 with items: I456 (Spaghetti Carbonara) and I789 (Garlic Bread), specifying the delivery address and payment method to ensure a smooth transaction through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U006", "restaurant_id": "R123", "items": [{"item_id": "I456", "quantity": 1}, {"item_id": "I789", "quantity": 1}], "delivery_address": "123 Main St, Downtown", "payment_method": "credit_card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U077",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are direct, cautious, organized. First, search for Mexican restaurants in the Midtown area with a price range of $10-$30 to identify potential new partners for DoorDash. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R1023 to verify hours of operation and delivery zone, ensuring it aligns with our service area and operational hours.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Midtown", "price_range": "$$"}
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
        user_id="U128",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are direct, patient, flexible, polite. Search for restaurants serving Italian cuisine in Jennifer's location within a moderate price range. Once you have identified a suitable restaurant, get the menu for restaurant ID R234 to explore available pasta dishes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Jennifer's location", "price_range": "$$"}
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
        user_id="U035",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are direct, logical, optimistic. First, search for restaurants offering sushi in the San Francisco area within a mid-range price to identify potential options for a lunch meeting. Once you have a list, get the restaurant details for restaurant ID R1024 to verify their hours and delivery zone to ensure they can accommodate your schedule and location. After confirming this, get the menu for restaurant ID R1024, focusing on the sushi category, to decide on the best items to order for the meeting.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "sushi", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1024"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1024", "category": "sushi"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams7359@email.com. You are logical, direct. First, search for Italian restaurants in San Francisco with a price range of $$. Once you find a suitable restaurant, get restaurant details for restaurant ID R1025 to check business hours and reviews to ensure it meets your dining preferences. After confirming the restaurant is a good choice, get the restaurant menu for restaurant ID R1025 to view available pasta dishes and decide on a meal. Finally, add item I203 (Spaghetti Carbonara) to the cart for user U5428 with quantity 1, ensuring a seamless ordering experience on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1025"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1025"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U113", "restaurant_id": "R1025", "item_id": "I203", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U101",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are logical, independent, organized, patient. Get the menu for restaurant R2345, focusing on the Tacos category.",
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
        user_id="U016",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are polite, cautious, patient, logical. Get details for restaurant R001 to check their current menu and hours of operation.",
        actions=[
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
        user_id="U061",
        instruction="Your name is Robert Williams and your email is robert.williams9426@email.com. You are optimistic, direct, patient, flexible. First, get the menu for restaurant ID R234 to explore available items, ensuring that Spaghetti Bolognese is listed. Then, add item I567 (Spaghetti Bolognese) to the cart for user Patricia Miller with quantity 1, preparing for a potential order.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U061", "restaurant_id": "R234", "item_id": "I567", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are patient, independent. Search for restaurants with Mexican cuisine in San Francisco within a moderate price range and get the menu for restaurant R567, focusing on the \"Tacos\" category. This will help you decide on your meal options for a lunch delivery through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U030",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are optimistic, flexible. First, search for restaurants in the downtown area with cuisine type 'Italian' and a price range of '$$' to identify potential new partners for DoorDash. Once you have identified a promising restaurant, get detailed information for restaurant with ID R101 to verify hours and operational status, ensuring it aligns with DoorDash's delivery schedule.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U090",
        instruction="Your name is John Williams and your email is john.williams6337@email.com. You are patient, logical, direct. You are planning a dinner for your colleagues and want to ensure a delicious and satisfying meal. First, search for Mexican restaurants in San Francisco with a moderate price range to find a suitable place for your order. Once you have identified a promising restaurant, retrieve its details to confirm its suitability, including its ratings and reviews. After confirming the restaurant meets your criteria, proceed to explore the main dishes on their menu to select a delicious option. Finally, add your chosen dish to the cart to prepare for checkout and ensure a smooth ordering process.",
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
                kwargs={"user_id": "U090", "restaurant_id": "R001", "item_id": "I001", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U087",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are patient, optimistic. Get the menu for restaurant ID R123 to identify available items in the pasta category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U133",
        instruction="Your name is James Williams and your email is james.williams9904@email.com. You are optimistic, flexible. Get the menu for restaurant R101, focusing on the pasta category.",
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
        user_id="U030",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are organized, independent, logical. Search for restaurants offering Mexican cuisine in the Seattle area with a price range of $10-$20. Once you have identified potential options, get the menu for restaurant R890 to find available items in the \"Tacos\" category. This will help ensure that the restaurant meets the specific order requirements for our DoorDash customers who are looking for affordable taco options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Seattle", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R890", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U010",
        instruction="Your name is Mary Brown and your email is mary.brown1791@email.com. You are optimistic, polite. Search for restaurants in Linda's location with cuisine type \"Mexican\" and price range \"$$\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda's location", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are organized, confident, direct, flexible. First, search for Mexican restaurants in the San Francisco area with a price range of $$. Once you have identified a potential option, get restaurant details for restaurant R5678 to check operating hours and address to ensure it fits within delivery capabilities. Finally, create an order for user U1012 at restaurant R5678 with items I2345 (Chicken Taco) and delivery address '123 Main St, San Francisco, CA'.",
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
                kwargs={"user_id": "U049", "restaurant_id": "R5678", "items": [{"item_id": "I2345", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U104",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are optimistic, cautious, confident. First, search for Italian restaurants located in the downtown area with a moderate price range of $$. Once you find a suitable restaurant, retrieve the pasta menu from the restaurant with the ID \"R123\" to explore the available options. This will help you make an informed decision on which pasta dish to order for your dinner through DoorDash.",
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
        user_id="U042",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are logical, cautious. Search for Mexican restaurants in the San Francisco area within a $10-$20 price range using search_restaurants. Once you find a suitable restaurant, get the menu for restaurant ID R567 to explore available Mexican dishes using get_restaurant_menu. This will help you decide on the best options to add to your cart for a satisfying meal through DoorDash.",
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
        user_id="U093",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are independent, direct, flexible, polite. Get the restaurant menu for restaurant ID R102 to review available dishes",
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
        user_id="U077",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are organized, polite. Add item I234 (Chicken Tacos) to cart for user linda.garcia4109@email.com with quantity 3.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican"}
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
                kwargs={"user_id": "U077", "restaurant_id": "R001", "item_id": "I234", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are organized, logical, optimistic. First, search for restaurants offering Chinese cuisine in the San Francisco area within a moderate price range to identify potential dining options. Once you have found a suitable restaurant, such as R1024, get the menu for this restaurant, focusing on the 'Entrees' category. This will allow you to review the available dishes and make an informed decision on what to order for delivery through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1024", "category": "Entrees"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams7359@email.com. You are independent, organized. First, search for restaurants offering Mexican cuisine in the New York City area with a mid-range price level to find potential options for a business lunch. Next, get details for restaurant R1023 to verify its operating hours and delivery zones to ensure it can accommodate your location and timing needs. Finally, get the menu for restaurant R1023 focusing on the Tacos category and add item I2501 (Chicken Tacos) to cart for user U5428 with quantity 3, specifying no onions, to prepare for the upcoming lunch order on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "New York City", "price_range": "$$"}
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
                kwargs={"user_id": "U113", "restaurant_id": "R1023", "item_id": "I2501", "quantity": 3, "customizations": "no onions"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U002",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are organized, cautious. First, search for Mexican restaurants located in Midtown with a price range of $10-$20 to identify potential options for partnering with DoorDash. Once you have identified a promising restaurant, obtain detailed information about the restaurant using its ID to assess its suitability for collaboration.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Midtown", "price_range": "$$"}
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
        user_id="U098",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are optimistic, polite. First, search for restaurants in San Francisco offering Asian cuisine with a price range of $$ to $$$ to explore potential dining options. Once you have identified a suitable restaurant, get restaurant details for restaurant R1023 to verify its operating hours and delivery zone, ensuring it can deliver to your area. After confirming the restaurant's delivery capabilities, create an order for user U4736 at restaurant R1023 with items [(I5678, 1), (I5680, 2)] and set the delivery address to 123 Main St, San Francisco, ensuring a smooth and timely delivery experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Asian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1023"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U098", "restaurant_id": "R1023", "items": [["I5678", 1], ["I5680", 2]], "delivery_address": "123 Main St, San Francisco"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U002",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are logical, optimistic, flexible, organized. Search for restaurants with a cuisine of 'Mexican' in the area of 'Los Angeles' with a price range of '$$'.",
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
        user_id="U158",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are polite, flexible. Search for Mexican restaurants in Jennifer Smith's location with a price range of medium.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U158"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer Smith's location", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U061",
        instruction="Your name is John Brown and your email is john.brown5124@email.com. You are confident, independent. Search for restaurants in Patricia Miller's area with a preference for Italian cuisine and a mid-range price. Once you have identified a suitable option, get details for restaurant R1023 to check its ratings and operational hours. This information will help you determine if the restaurant meets the quality and convenience standards necessary for a potential partnership with DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Patricia Miller's area", "price_range": "$$"}
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
        user_id="U110",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are direct, cautious. First, search for Italian restaurants in New York City within a moderate price range to find a suitable dining option for a client meeting. Once you identify a restaurant, specifically look for the restaurant menu for restaurant R567 with a focus on pasta dishes, as your client has expressed a preference for pasta. This will allow you to make an informed decision on where to dine.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U093",
        instruction="Your name is Patricia Miller and your email is patricia.miller3271@email.com. You are polite, independent. First, search for Italian restaurants in Mary Jones' delivery area with a minimum rating of 4.0. Once you have identified a suitable restaurant, proceed to add item I789 (Spaghetti Carbonara) to Mary Jones' cart from restaurant R2345 with quantity 1 and no customizations.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Mary Jones' delivery area"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U093", "restaurant_id": "R2345", "item_id": "I789", "quantity": 1, "customizations": null}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are polite, cautious. First, search for Italian restaurants in the downtown area with a price range of $$ using the search_restaurants tool. Once you have identified a suitable restaurant, get the restaurant details for restaurant_id R001 to check its opening hours using the get_restaurant_details tool to ensure it is open during your preferred dining time. Finally, get the menu for restaurant_id R001 focusing on the pasta category using the get_restaurant_menu tool, and add item I789 (Spaghetti Carbonara) to the cart for user_id U123 from restaurant_id R001 with quantity 1 using the add_item_to_cart tool.",
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
                kwargs={"restaurant_id": "R001", "category": "pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U076", "restaurant_id": "R001", "item_id": "I789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is Mary Williams and your email is mary.williams2739@email.com. You are flexible, direct. First, search_restaurants(cuisine='Italian', location='San Francisco', price_range='$$') to find a suitable dining option for a business lunch. Once you have identified a restaurant, get_restaurant_menu(restaurant_id='R987') to review their menu and ensure they offer a variety of dishes that cater to different dietary preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U106",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are direct, cautious, flexible. First, search for Mexican restaurants in Linda Garcia's area with a mid-range price to identify potential options for our delivery service. Once you have a list, get restaurant details for restaurant R234 to verify their hours and delivery options, ensuring they align with our operational requirements. This information will help us decide whether to include them in our Doordash offerings.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Garcia's area", "price_range": "$$"}
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
        instruction="Your name is John Brown and your email is john.brown5124@email.com. You are direct, optimistic, independent. First, search for Mexican restaurants in the San Francisco area with a price range of $$ to $$$ to find a suitable option for a special dinner. Once you identify a promising restaurant, get the restaurant details for restaurant ID R2345 to check operating hours and delivery zones to ensure they can deliver to your location. After confirming the restaurant's availability, create an order for user ID U1234 at restaurant ID R2345 with items (I6789) and delivery address \"123 Main St, San Francisco, CA\", using the payment method \"Credit Card\", and include special instructions \"Extra napkins, please.\"",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$,$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U151", "restaurant_id": "R2345", "items": [{"item_id": "I6789", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA", "payment_method": "Credit Card", "special_instructions": "Extra napkins, please"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U110",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are polite, flexible, direct, cautious. First, search for restaurants offering Mexican cuisine in the San Francisco area to identify potential partners for DoorDash. Once you have identified a restaurant, get the restaurant details for restaurant ID R234 to check if it's open for delivery. This will help us ensure we are providing accurate delivery options to our customers.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco"}
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
        user_id="U093",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are cautious, direct, confident, flexible. To assist a customer with their dining experience, first search for restaurants with cuisine 'Mexican' in the location 'San Francisco' with a price range of '$$'. Once you have identified a suitable restaurant, get restaurant details for restaurant_id 'R456' to verify operational hours and delivery zones, ensuring it fits the customer's schedule and location. Finally, create an order for user_id 'mary.jones4200' at restaurant_id 'R456' with items ['I789'] and delivery_address '123 Main St, San Francisco, CA', providing a seamless and satisfying meal delivery experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U093", "restaurant_id": "R456", "items": ["I789"], "delivery_address": "123 Main St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U037",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are independent, patient, confident, cautious. Begin by searching for restaurants in your area with a preference for Italian cuisine and a moderate price range. Once you identify restaurant R456 as a potential option, get detailed information to confirm its opening hours and location. After confirming that it meets your requirements, retrieve the menu for restaurant R456, focusing on the pasta category. If Spaghetti Carbonara is available, add item I789 to your cart with a quantity of 1, ensuring that your order is ready for checkout on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "price_range": "$$"}
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
                kwargs={"user_id": "U037", "restaurant_id": "R456", "item_id": "I789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U163",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are independent, optimistic. Get the restaurant menu for restaurant ID R101, focusing on the pasta category.",
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
        user_id="U142",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are direct, cautious, organized, independent. Get the restaurant menu for restaurant ID R1023 to explore available pasta dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U061",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are confident, organized, cautious. Get the menu for restaurant ID R456, focusing on the pasta category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are independent, cautious, patient. First, search for Mexican restaurants in Linda Garcia's area with a price range of $10-$20 to find suitable dining options. Once you have identified a restaurant, get the restaurant menu for restaurant ID R2345 to explore available taco options, ensuring that the menu offers a variety of choices within the desired price range. After reviewing the menu, add item ID I5678 (Chicken Tacos) to the cart for user ID U10293 with a quantity of 3, preparing to create a satisfying meal order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Garcia's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U041", "restaurant_id": "R2345", "item_id": "I5678", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are direct, confident. Get the restaurant menu for restaurant ID R345 to explore available pasta dishes.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R345", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U002",
        instruction="Your name is Robert Brown and your email is robert.brown1066@email.com. You are logical, independent. First, search for restaurants with cuisine \"Italian\" in the location \"San Francisco\" within a moderate price range to identify potential new partners for DoorDash. Once you have identified a suitable restaurant, get restaurant details for restaurant_id \"R12345\" to check operational hours and reviews to ensure they meet DoorDash's quality standards.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U176",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are cautious, confident, logical, independent. Search for restaurants in John's area with cuisine type set to \"Mexican\" and price range set to \"mid-range\"",
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
        user_id="U002",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are patient, logical, organized. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to identify potential options for a new dining experience. Once you have identified restaurant R567 as a suitable choice, get detailed information to verify its operating hours and location to ensure it aligns with your schedule and preferences. Finally, create an order for user U1234 with restaurant R567, including items I890 and I891, and arrange delivery to 123 Main St with payment via credit card, ensuring a seamless and satisfying experience for the customer.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U002", "restaurant_id": "R567", "items": [{"item_id": "I890", "quantity": 1}, {"item_id": "I891", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U170",
        instruction="Your name is Mary Brown and your email is mary.brown1791@email.com. You are optimistic, polite, organized. Create an order for user U102 at restaurant R582 with items I3401 and I3402, delivering to 123 Market Street, San Francisco, payment method: credit card ending in 1234.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R582"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R582"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R582", "item_id": "I3401"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R582", "item_id": "I3402"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U170", "restaurant_id": "R582", "items": [{"item_id": "I3401", "quantity": 1}, {"item_id": "I3402", "quantity": 1}], "delivery_address": "123 Market Street, San Francisco", "payment_method": "credit card ending in 1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U162",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are confident, flexible, logical, independent. First, search for restaurants with Mexican cuisine in San Francisco within a moderate price range to identify potential options for placing an order. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R102 to verify operating hours and ensure it is open for business. After confirming the restaurant is operational, get the menu for restaurant ID R102 focusing on the category \"Tacos\" to decide on the items to order. Finally, create an order for user ID U5118 at restaurant ID R102 with items: 3x Chicken Taco, delivery address: 123 Main St, payment method: credit card, and include special instructions: \"Leave at door.\"",
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
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102", "category": "Tacos"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U162", "restaurant_id": "R102", "items": [{"item_id": "I001", "quantity": 3}], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U019",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are cautious, optimistic, flexible. Search for sushi restaurants in San Francisco within a mid-price range to find a suitable option for your upcoming dinner plans. Once you have identified a restaurant, get the menu for restaurant ID R102 to view available sushi options and decide on your order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Sushi", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U049",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are direct, logical. Search for Mexican restaurants in San Francisco with a price range of $$. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R5678 to view available items. After reviewing the menu, add item ID I9876 (Chicken Tacos) to cart for user ID U1234 with quantity 3.",
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
                kwargs={"user_id": "U049", "restaurant_id": "R5678", "item_id": "I9876", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are direct, independent, confident. Get the restaurant menu for restaurant ID R5678, focusing on the pasta category.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5678", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U110",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are logical, organized. First, search for Italian restaurants in the San Francisco area with a price range of $$ to $$$ to identify potential dining options. Once you have found a restaurant that meets these criteria, get the menu for restaurant ID R1024 to check available pasta dishes. This will help you determine the best options for placing an order for user ID U5441, ensuring that the selected items align with their preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$,$$$"}
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
        user_id="U086",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are confident, flexible, direct. First, search for restaurants with cuisine 'Italian' in location 'Downtown' with price range '$$' to identify potential dining options for a client meeting. Once you have found a suitable restaurant, get the restaurant menu for restaurant ID R567 to find pasta dishes, ensuring there are appealing options for the group.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U007",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are flexible, polite. First, search for restaurants with cuisine 'Mexican' in the area of 'San Francisco' with a price range of '$$'. Once you have identified a suitable option, get restaurant details for restaurant ID 'R1023' to check its operating hours. This will help ensure the restaurant is open during peak delivery times, allowing you to coordinate with DoorDash for optimal delivery scheduling.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U125",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are flexible, cautious, patient. Get the menu for restaurant ID R102 to explore available dishes in the Tacos category.",
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
        user_id="U178",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are optimistic, independent, patient. Get restaurant menu for restaurant ID R101 to browse available dishes",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U098",
        instruction="Your name is Patricia Miller and your email is patricia.miller3271@email.com. You are polite, flexible, optimistic, patient. First, search for restaurants with Mexican cuisine in the downtown area to find a suitable option for our upcoming team lunch. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R456 to check its opening hours and ensure it fits our schedule. After confirming the restaurant is open during our desired time, get the restaurant menu for restaurant ID R456 and filter by the \"Tacos\" category to explore the available taco options. This will help us decide on the items we want to order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R456"}
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
        user_id="U035",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are independent, polite, confident. You are planning a dinner with friends and want to explore Italian cuisine options in Downtown. First, search_restaurants(location=\"Downtown\", cuisine=\"Italian\", price_range=\"$$\") to find a suitable place that fits your budget. Once you find a restaurant you like, such as one with the ID \"R123,\" get_restaurant_menu(restaurant_id=\"R123\", category=\"Pizzas\") to check their pizza offerings. If you find a pizza you like, add_item_to_cart(user_id=\"U5883\", restaurant_id=\"R123\", item_id=\"I456\", quantity=2) to ensure you have enough for everyone to enjoy.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "Pizzas"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U035", "restaurant_id": "R123", "item_id": "I456", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U077",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are flexible, independent. search_restaurants(location=\"downtown\", cuisine=\"Italian\", price_range=\"$$\")",
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
        user_id="U055",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are patient, organized, polite, optimistic. Search for restaurants offering Mexican cuisine in the 94103 area with a price range of $10-$20.",
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
        user_id="U042",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are confident, logical, patient, cautious. Search for restaurants in San Francisco offering Mexican cuisine within a mid-range price. Once you have identified a suitable restaurant, create an order for user U3233 at the selected restaurant with items [I890], using home address \"123 Main St, San Francisco, CA\" and payment method \"Credit Card\".",
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
                name="create_order",
                kwargs={"user_id": "U042", "restaurant_id": "R001", "items": [{"item_id": "I890", "quantity": 1}], "delivery_address": "123 Main St, San Francisco, CA", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U046",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are optimistic, organized, independent. Search for restaurants offering Mexican cuisine in the San Francisco area with a mid-range price, and then get the menu for restaurant R2023 to find available taco options. This will help you identify the best taco offerings to recommend to DoorDash users looking for new dining experiences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U113",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are independent, logical, cautious. First, search for restaurants with Mexican cuisine in the downtown area within a mid-range price to find a suitable option for a dinner order. Once you have identified a potential restaurant, get the restaurant details for restaurant R987 to verify its opening hours and delivery area, ensuring it can accommodate your needs. Finally, create an order for user U123 at restaurant R987 with items (I654), specifying the delivery address as 123 Main St and using a credit card as the payment method.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R987"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U113", "restaurant_id": "R987", "items": [{"item_id": "I654", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are polite, cautious, independent. Search for Italian restaurants in the San Francisco area with a price range of $$. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R456 to explore available pasta dishes. This will help you decide if the restaurant offers a variety of pasta options that meet your taste preferences before placing an order on DoorDash.",
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
        user_id="U045",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are patient, logical, independent, flexible. search_restaurants(location=\"San Francisco\", cuisine=\"Mexican\", price_range=\"mid\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"location": "San Francisco", "cuisine": "Mexican", "price_range": "mid"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U118",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are optimistic, cautious, patient. Get the menu for restaurant ID R1023, focusing on the Tacos category.",
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
        user_id="U090",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are confident, flexible, patient, polite. First, search for restaurants offering Mexican cuisine near Linda's location with a price range of $10-$20 to identify potential dining options. Next, get the menu for restaurant R678 focusing on the \"Tacos\" category to explore specific offerings. Finally, create an order for user U3192 at restaurant R678 with items Chicken Tacos and Guacamole, using delivery address 123 Main St, and select Credit Card as the payment method to ensure a smooth transaction.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R678", "category": "Tacos"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U090", "restaurant_id": "R678", "items": [{"name": "Chicken Tacos", "quantity": 1}, {"name": "Guacamole", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is Mary Williams and your email is mary.williams2739@email.com. You are cautious, optimistic. Create order for user U456 at restaurant R987 with items I123 and I789, deliver to 123 Main St, using credit card payment.",
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
                name="get_item_details",
                kwargs={"restaurant_id": "R987", "item_id": "I789"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U042", "restaurant_id": "R987", "items": [{"item_id": "I123", "quantity": 1}, {"item_id": "I789", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Michael Williams and your email is michael.williams3137@email.com. You are cautious, optimistic, logical, confident. First, search for Mexican restaurants in Linda Garcia's area with a mid-range price to identify potential dining options. Once you have identified restaurant R567 as a suitable choice, get details for restaurant R567 to check its operational status and ratings, ensuring it meets quality standards. Finally, create an order for user Linda Garcia with restaurant R567, including items I890 and I891, using her saved delivery address and credit card ending in 1234, to complete the transaction seamlessly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Garcia's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U041", "restaurant_id": "R567", "items": [{"item_id": "I890", "quantity": 1}, {"item_id": "I891", "quantity": 1}], "payment_method": "credit_card_ending_1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U049",
        instruction="Your name is Patricia Miller and your email is patricia.miller3271@email.com. You are flexible, polite, optimistic, direct. Begin by searching for Mexican restaurants in the San Francisco area with a price range of $$. Once you have identified a suitable restaurant, create an order for user ID U101 with restaurant ID R2345, including items: Chicken Tacos (I5678) with delivery address 123 Main St, San Francisco, and note \"extra salsa.\" This sequence ensures that you select a restaurant that fits the budget and preferences before placing the order, aligning with the business context of providing efficient and tailored food delivery services through DoorDash.",
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
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U049", "restaurant_id": "R2345", "items": [{"item_id": "I5678", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "special_instructions": "extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Robert Williams and your email is robert.williams9426@email.com. You are logical, polite, direct, patient. First, get the menu for restaurant ID R987, focusing on the 'Tacos' category to check available options. Once you have confirmed the availability, proceed to add item I321 (Chicken Taco) to the cart for user U3137 with a quantity of 3 and extra cheese customization.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R987", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U167", "restaurant_id": "R987", "item_id": "I321", "quantity": 3, "customizations": "extra cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U190",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are organized, optimistic. Search for restaurants offering vegan cuisine in Linda Miller's location with a price range of $10-$20.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U190"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "vegan", "location": "Linda Miller's location", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U170",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are independent, logical, cautious, confident. Get restaurant details for restaurant ID 1458 to verify opening hours and location.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "1458"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U007",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are independent, confident, flexible, logical. Get restaurant menu for restaurant ID R567 focusing on the \"Tacos\" category.",
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
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are polite, independent. First, search for Mexican restaurants in Jennifer Miller's local area with a price range of $10-$20 to find suitable dining options. Next, once you have identified a restaurant, get the menu for restaurant ID R6789 to review available items and ensure they meet the preferences and dietary needs. Finally, create an order for user ID U1234 at restaurant ID R6789 with items Chicken Tacos and Guacamole and Chips, ensuring the delivery address is 123 Elm St, Apt 4B, and the payment method is a credit card ending in 5678.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer Miller's local area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R6789"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U123", "restaurant_id": "R6789", "items": [{"name": "Chicken Tacos", "quantity": 1}, {"name": "Guacamole and Chips", "quantity": 1}], "delivery_address": "123 Elm St, Apt 4B", "payment_method": "credit card ending in 5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is Mary Brown and your email is mary.brown1791@email.com. You are organized, patient, independent, flexible. Get the menu for restaurant R202 to check available items.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R202"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are optimistic, flexible, direct, logical. First, search for restaurants offering Mexican cuisine in Jennifer Garcia's area with a moderate price range to identify potential options for a family dinner. Once you have identified a suitable restaurant, get the menu for restaurant ID R567, focusing on the 'Tacos' category, to ensure they have a variety of options that cater to different tastes. This will help streamline the ordering process through DoorDash by confirming the availability of preferred dishes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer Garcia's area", "price_range": "$$"}
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
        user_id="U081",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are logical, direct. First, search for restaurants offering Japanese cuisine in the San Francisco area within a moderate price range to find suitable options for a customer request. Once you have identified a potential restaurant, get restaurant details for restaurant R5678 to verify its operating hours and delivery zones, ensuring it can serve the customer's location. Finally, create an order for user U9197 with restaurant R5678, including items California Roll and Spicy Tuna Roll, specifying delivery address as 123 Main St, San Francisco, and payment method as credit card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Japanese", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U081", "restaurant_id": "R5678", "items": [{"name": "California Roll", "quantity": 1}, {"name": "Spicy Tuna Roll", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Mary Williams and your email is mary.williams2739@email.com. You are confident, flexible, organized. First, get restaurant details for restaurant ID R234 to confirm it is open and meets minimum order requirements. Once confirmed, get the menu for restaurant ID R234 to find available tacos. Then, create an order for user Linda Garcia with restaurant ID R234 including items I678 (Chicken Taco) and I679, delivery address 123 Main St, and payment method credit card ending in 1234.",
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
                kwargs={"user_id": "U041", "restaurant_id": "R234", "items": [{"item_id": "I678", "quantity": 1}, {"item_id": "I679", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card ending in 1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are independent, patient. Create an order for user U001 at restaurant R234 with items [I567, I568], using provided delivery address and payment method.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U180"}
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
                name="get_item_details",
                kwargs={"restaurant_id": "R234", "item_id": "I567"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R234", "item_id": "I568"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U180", "restaurant_id": "R234", "items": [{"item_id": "I567", "quantity": 1}, {"item_id": "I568", "quantity": 1}], "delivery_address": "123 Main St, Anytown, USA", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U093",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are direct, logical, independent. Get the restaurant menu for restaurant ID R456 to view the available items.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U046",
        instruction="Your name is James Williams and your email is james.williams9904@email.com. You are optimistic, patient, cautious. First, search for Italian restaurants in the Downtown area with a moderate price range of $$. Once you find a suitable restaurant, get the menu specifically for Pasta dishes from the restaurant with the ID \"R123\". After reviewing the menu, create an order using your user ID \"U001\" at the same restaurant, selecting two portions of the desired pasta dish. Ensure the delivery is set to \"123 Main St, Apt 4B\" and pay using your Credit Card. Include special instructions to leave the order at the doorstep for a seamless delivery experience.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R123", "category": "Pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U046", "restaurant_id": "R123", "items": [{"item_id": "I001", "quantity": 2}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "Credit Card", "special_instructions": "Leave the order at the doorstep"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is Mary Jones and your email is mary.jones4200@email.com. You are confident, organized, polite, logical. Add item I202 (Spaghetti Carbonara) to cart for user Patricia Miller with quantity 1 and no customizations.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U177"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian"}
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
                kwargs={"user_id": "U177", "restaurant_id": "R001", "item_id": "I202", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Linda Garcia and your email is linda.garcia4109@email.com. You are flexible, logical, organized. First, search for Italian restaurants in the area of Jennifer Brown's current location with a price range of $$ to $$$. Once you have identified a suitable restaurant, confirm that the restaurant with ID R567 matches Jennifer's preferences and get its details. After confirming the match, get the menu for restaurant R567, focusing on the pasta category. Finally, add item I891 (Spaghetti Carbonara) to Jennifer Brown's cart from restaurant R567 with a quantity of 1, ensuring a seamless experience for her on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Jennifer Brown's current location", "price_range": "$$ to $$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U122", "restaurant_id": "R567", "item_id": "I891", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are confident, flexible. Search for restaurants in the San Francisco area offering Asian cuisine within a moderate price range to find potential options for delivery. Once you have identified restaurant R101 as a suitable choice, get details for restaurant R101 to verify if it is currently open and meets minimum order requirements. After confirming these details, create an order for user Linda Williams (user_id U1610) at restaurant R101 with items I202 and I203, specifying delivery address as \"123 Main St, San Francisco\" and payment method as \"Credit Card\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Asian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U175", "restaurant_id": "R101", "items": [{"item_id": "I202", "quantity": 1}, {"item_id": "I203", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are direct, patient, cautious, confident. Create an order for user U3137 from restaurant ID R101 with items I201 and I202, delivering to 123 Main St, using credit card payment.",
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
                kwargs={"restaurant_id": "R101", "item_id": "I201"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R101", "item_id": "I202"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U167", "restaurant_id": "R101", "items": [{"item_id": "I201", "quantity": 1}, {"item_id": "I202", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is Mary Smith and your email is mary.smith5441@email.com. You are cautious, independent. Search for restaurants offering Thai cuisine in John Brown's local area with a mid-range price, and after identifying restaurant R789 as a preferred choice, retrieve the menu focusing on the \"Main Course\" category. This will help you make an informed decision for a potential DoorDash collaboration to expand their offerings in the area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Thai", "location": "John Brown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R789", "category": "Main Course"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U140",
        instruction="Your name is Michael Brown and your email is michael.brown8314@email.com. You are direct, independent, logical, optimistic. Search for restaurants offering Mexican cuisine near Robert Garcia's location with a price range of $10-$20",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U140"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Robert Garcia's location", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U101",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones6091@email.com. You are independent, flexible. Search for Italian restaurants in the San Francisco area with a price range of $$ to $$$ to find suitable options for a dinner event. Once you have identified a restaurant, get the restaurant menu for restaurant ID R2345 to check available pasta dishes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
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
        user_id="U090",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are optimistic, polite. First, search for Italian restaurants in New York City within a medium price range to find a suitable dining option. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R456 to verify its operational hours and current promotions, ensuring it fits your schedule and offers any enticing deals. After confirming the restaurant's details, get the restaurant menu for restaurant ID R456, focusing on the pasta category, to decide on a delicious dish. Finally, add item I789 (Spaghetti Carbonara) to cart for user ID U123 with quantity 1 and gluten-free customization, preparing your order for checkout on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "New York City", "price_range": "$$"}
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
                kwargs={"user_id": "U090", "restaurant_id": "R456", "item_id": "I789", "quantity": 1, "customizations": "gluten-free"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U087",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are direct, cautious, optimistic. First, search for Italian restaurants in Mary's area with a price range of moderate to find suitable options for her dinner plans. Once you have identified a restaurant of interest, get the restaurant menu for restaurant ID R234, focusing on the pasta category, to ensure they offer a variety of pasta dishes that meet her preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "price_range": "$$"}
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
        user_id="U010",
        instruction="Your name is John Brown and your email is john.brown7795@email.com. You are logical, confident. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to identify potential dining options. Next, get restaurant details for restaurant ID R101 to check its operational status and delivery zone, ensuring it can deliver to your area. Finally, create an order for user ID U2478 at restaurant ID R101 with items I250 and I251, using the saved delivery address and credit card payment method, to enjoy a delightful Italian meal delivered to your doorstep.",
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
                name="create_order",
                kwargs={"user_id": "U010", "restaurant_id": "R101", "items": [{"item_id": "I250", "quantity": 1}, {"item_id": "I251", "quantity": 1}]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U010",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are cautious, logical, direct. Create an order for user ID U001 with restaurant ID R345 including item I678 and delivery address at 123 Market St, using credit card payment.",
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
                kwargs={"restaurant_id": "R345", "item_id": "I678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U010", "restaurant_id": "R345", "items": [{"item_id": "I678", "quantity": 1}], "delivery_address": "123 Market St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is Linda Miller and your email is linda.miller5151@email.com. You are optimistic, independent, confident, cautious. First, search for Mexican restaurants in Los Angeles with a price range of $$. Once you have identified the restaurants, get restaurant details for restaurant R102 (El Compadre) to ensure it meets the desired criteria. After confirming the restaurant's suitability, create an order for user U456 (Jennifer Garcia) at restaurant R102 (El Compadre) with items (Chicken Enchiladas, Guacamole and Chips) and delivery address \"123 Main St, Los Angeles, CA\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Los Angeles", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U042", "restaurant_id": "R102", "items": [{"name": "Chicken Enchiladas", "quantity": 1}, {"name": "Guacamole and Chips", "quantity": 1}], "delivery_address": "123 Main St, Los Angeles, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U016",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are independent, direct, cautious. First, get restaurant details for restaurant R001 to check its delivery zone and hours, ensuring it aligns with the peak dinner time and covers the downtown area. Then, get the restaurant menu for restaurant R001 focusing on the Tacos category, as this will help determine the best options for a promotional feature on DoorDash targeting taco enthusiasts.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R001"}
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
        user_id="U104",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are optimistic, organized, patient, independent. Search for restaurants offering vegetarian options within a 5-mile radius of Linda Brown's address, and once you have identified a suitable restaurant, get the menu for restaurant ID R234 to find main course vegetarian dishes. This will help ensure that Linda Brown has a variety of vegetarian options to choose from, enhancing her dining experience with DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Vegetarian", "location": "Linda Brown's address"}
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
        user_id="U019",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown2003@email.com. You are confident, polite, patient, organized. Get the menu for restaurant R1023 to view available sushi options",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1023", "category": "sushi"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U087",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are optimistic, patient. First, search for restaurants offering Mexican cuisine in the 94103 area with a medium price range. Once you have found a suitable option, get the restaurant details using the restaurant ID R567 to ensure it meets your preferences. After confirming the restaurant's suitability, proceed to get the restaurant menu focusing on the Tacos category. Finally, add three of a specific taco item, identified by item ID I789, to your cart for user ID U001, ensuring a satisfying meal choice through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "94103", "price_range": "$$"}
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
                kwargs={"user_id": "U087", "restaurant_id": "R567", "item_id": "I789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U163",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are polite, organized. First, search for restaurants offering Mexican cuisine in the user's area with a moderate price range to identify potential options for inclusion in the DoorDash delivery service. Once you have a list of potential restaurants, get details for restaurant R1024 to verify its operating hours and customer reviews, ensuring it meets DoorDash's quality and availability standards.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
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
        user_id="U020",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are flexible, direct, logical. Search for restaurants with the cuisine \"Mexican\" in the user's location.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "user's location"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are patient, independent, direct. First, search for Italian restaurants located in Downtown with a price range of \"$$\". Once you have identified a suitable restaurant, retrieve the details of the restaurant with the ID \"R12345\" to ensure it meets your dining preferences. After confirming the restaurant's suitability, proceed to get the menu specifically for the \"Pasta\" category from the same restaurant. Finally, add your favorite pasta dish to the cart with the item ID \"I789\", ensuring to customize it with extra cheese, and set the quantity to 1 for your order on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R12345"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R12345", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U048", "restaurant_id": "R12345", "item_id": "I789", "quantity": 1, "customizations": "extra cheese"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U075",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are independent, logical, organized. First, search for restaurants in the San Francisco area with a price range of $$ that offer Mexican cuisine. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R001 to check the availability of delivery. This will help ensure that DoorDash can provide delivery services for the selected restaurant, enhancing customer satisfaction by offering convenient dining options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U076",
        instruction="Your name is Robert Brown and your email is robert.brown1066@email.com. You are confident, optimistic. First, search for restaurants offering Mexican cuisine in Jennifer Davis's current location with a price range of $10-$30 to find suitable dining options. Once you have identified a restaurant, get the menu for restaurant ID R101 to explore available items. This will help you decide on the best dishes to recommend or order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer Davis's current location", "price_range": "$$"}
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
        user_id="U134",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are cautious, logical, independent, polite. You are planning a dinner for two and want to enjoy some Italian cuisine without going overboard on the budget. First, search for Italian restaurants located downtown that offer a mid-range price menu. Once you find a suitable restaurant, get the menu specifically for their Pasta category to explore your options.",
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
        user_id="U192",
        instruction="Your name is Michael Johnson and your email is michael.johnson5428@email.com. You are direct, optimistic, patient, independent. get_restaurant_menu(restaurant_id=\"R123\")",
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
        user_id="U177",
        instruction="Your name is Linda Davis and your email is linda.davis2351@email.com. You are polite, organized. First, search for Italian restaurants in the downtown area with a price range of $$-$$$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R2345. This will allow you to assist Patricia Miller (user ID U3271) in placing an order at this restaurant.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
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
        user_id="U123",
        instruction="Your name is Patricia Miller and your email is patricia.miller3271@email.com. You are organized, logical, direct, optimistic. Begin by searching for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$20 to identify potential options for a customer interested in affordable dining. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R1025 to verify its operating hours and address, ensuring it meets the customer's availability and location preferences. Finally, get the menu for restaurant ID R1025, focusing on the Tacos category to explore available options, as the customer is particularly interested in trying different taco varieties.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R1025"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R1025", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are direct, independent, cautious. Search for Mexican restaurants in Linda's location within a moderate price range.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U175"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda's location", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U041",
        instruction="Your name is Robert Jones and your email is robert.jones3607@email.com. You are independent, patient, cautious. Start by searching for Mexican restaurants in Linda Garcia's location with a price range of $10-$20 to find suitable dining options. Once you identify a potential restaurant, get the restaurant details for restaurant ID R256 to verify it meets Linda Garcia's preferences, ensuring a satisfying dining experience. Finally, create an order for user ID U2772 with restaurant ID R256, selecting items [I102, I103], and arrange delivery to 123 Main St, Apt 4B, using a credit card for payment.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Linda Garcia's location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R256"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U041", "restaurant_id": "R256", "items": [{"item_id": "I102", "quantity": 1}, {"item_id": "I103", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are organized, confident. First, search for Italian restaurants in the San Francisco area with a price range of $$ to $$$ to identify potential dining options for a client meeting. Once you have a list, get restaurant details for restaurant ID R5678 to confirm their operating hours, ensuring they align with the meeting schedule. After confirming the operating hours, get the restaurant menu for restaurant ID R5678, focusing on the pasta category, to recommend a suitable dish for the meeting.",
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
                kwargs={"restaurant_id": "R5678", "category": "pasta"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Robert Brown and your email is robert.brown1066@email.com. You are independent, polite, patient. First, search for Mexican restaurants in Jennifer Brown's area with a price range of $10-$30 to find suitable dining options. Once you identify a restaurant, get the restaurant details for restaurant ID R567 to verify its location and hours, ensuring it fits Jennifer's schedule. After confirming the restaurant's availability, get the menu for restaurant ID R567, focusing on the \"Tacos\" category, to explore meal options. This will help in creating an order for user U7411 with restaurant ID R567, including Chicken Tacos, delivery address at 123 Main St, and credit card payment method, ensuring a seamless and satisfying dining experience for Jennifer.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Jennifer Brown's area", "price_range": "$$"}
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
                name="create_order",
                kwargs={"user_id": "U122", "restaurant_id": "R567", "items": [{"item_id": "Chicken Tacos", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U037",
        instruction="Your name is Linda Miller and your email is linda.miller5151@email.com. You are independent, organized. First, search for Mexican restaurants in the 90210 area with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a potential restaurant, get restaurant details for restaurant ID R2345 to check their operating hours and ensure they are open for your preferred dining time. After confirming the restaurant is open, get the menu for restaurant ID R2345, focusing on the \"Tacos\" category, to explore their offerings. If you find the Chicken Taco appealing, add item ID I5678 (Chicken Taco) to cart for user ID U9876 with quantity 3 to prepare for an order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "90210", "price_range": "$$-$$$"}
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
                kwargs={"user_id": "U037", "restaurant_id": "R2345", "item_id": "I5678", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U061",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are organized, confident. Search for restaurants in Patricia Miller's area with a focus on Mexican cuisine and mid-range prices. Once you have identified potential options, get detailed information for restaurant R456 to verify its operating hours and location. This will ensure that the restaurant is a viable option for a potential partnership with DoorDash, focusing on expanding their delivery offerings in the area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Patricia Miller's area", "price_range": "$$"}
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
        user_id="U110",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are optimistic, direct, organized, confident. First, search for restaurants in the downtown area with a cuisine of \"Italian\" and a price range of \"$$\" to find suitable dining options. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R234 to review their business hours and ratings, ensuring it meets your standards for quality and convenience. Finally, create an order for user U001 at restaurant ID R234 with items I123 and I124, ensuring the delivery address is \"123 Main St\" and the payment method is \"Credit Card\" to complete the transaction smoothly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U110", "restaurant_id": "R234", "items": [{"item_id": "I123", "quantity": 1}, {"item_id": "I124", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U093",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are polite, confident, organized, direct. First, search for Italian restaurants in San Francisco with a price range of $$ to $$$ to identify potential dining options for our upcoming client meeting. Next, get detailed information for restaurant R2345 to check its operating hours and location to ensure it aligns with our meeting schedule. Finally, get the menu for restaurant R2345, focusing on the pasta category, to review their offerings and make a preliminary selection for the meeting.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$,$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R2345"}
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
        user_id="U112",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are patient, flexible, polite. First, search for Italian restaurants in San Francisco within the $$ price range to find suitable dining options for a client meeting. Once you identify a promising restaurant, retrieve detailed information about the restaurant with ID \"R12345\" to ensure it meets the client's preferences and expectations. After confirming the restaurant's suitability, obtain the menu specifically for the Pasta category to explore the available dishes. Finally, add a selected pasta item with ID \"I6789\" to the cart for user Mary Williams at mary.williams6067@email.com, ensuring the order is ready for delivery.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R12345"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R12345", "category": "Pasta"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U112", "restaurant_id": "R12345", "item_id": "I6789", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U055",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are direct, optimistic. Get the restaurant menu for restaurant R5678 to view available items.",
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
        user_id="U162",
        instruction="Your name is Robert Williams and your email is robert.williams9426@email.com. You are patient, optimistic, organized. First, search for Italian restaurants in the downtown area with a moderate price range to find a suitable dining option. Once you have identified a potential restaurant, get the restaurant menu for restaurant ID R12345 to explore available pasta dishes. This will help you decide on the best options for placing an order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
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
        user_id="U123",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are flexible, polite, organized. First, search for restaurants in Jennifer Miller's area (zip code 90210) offering Chinese cuisine to identify potential options for delivery. Next, get restaurant details for restaurant R567 to verify operating hours and delivery zones, ensuring it can serve Jennifer's location. Finally, create an order for user U101 at restaurant R567 with items I789 and I790, using the saved payment method and delivery address, once confirming the restaurant's availability and menu options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "90210"}
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
                kwargs={"user_id": "U123", "restaurant_id": "R567", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U128",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are organized, independent, confident, optimistic. First, search for Mexican restaurants in the downtown area within a moderate price range to find potential options for a business lunch. Once you have identified a suitable restaurant, get the restaurant menu for restaurant R457, focusing on the taco category, to ensure they offer a variety of taco options that would appeal to different tastes.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R457", "category": "taco"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U113",
        instruction="Your name is Linda Brown and your email is linda.brown2988@email.com. You are optimistic, patient, direct, independent. Create an order for user Michael Johnson at restaurant R987 with items I321 and I654, delivering to 123 Main St, apt 45, using credit card payment.",
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
                kwargs={"restaurant_id": "R987", "item_id": "I321"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R987", "item_id": "I654"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U113", "restaurant_id": "R987", "items": [{"item_id": "I321", "quantity": 1}, {"item_id": "I654", "quantity": 1}], "delivery_address": "123 Main St, apt 45", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U045",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are organized, optimistic. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to find a suitable dining option for our upcoming team lunch. Once you identify a restaurant, get the menu for restaurant R123, focusing on the \"Pasta\" category, to ensure they have a good selection of pasta dishes available for our group.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
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
        user_id="U140",
        instruction="Your name is Michael Miller and your email is michael.miller4736@email.com. You are direct, cautious, flexible. First, get restaurant details for restaurant R234 to verify operating hours and delivery zones to ensure they align with the user's location and timing preferences. Once confirmed, get the restaurant menu for restaurant R234 to find available items in the 'Tacos' category, ensuring that the desired items are available for the user.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
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
        user_id="U124",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are flexible, optimistic. Search for restaurants offering Chinese cuisine within the delivery zone of user Patricia Jones at her provided address. Once you identify a suitable restaurant, get the restaurant menu for restaurant ID R2345, focusing on the \"Main Dishes\" category, to ensure they offer Kung Pao Chicken.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U124"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "Patricia Jones' address"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Main Dishes"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U077",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are cautious, organized. First, search for Mexican restaurants in San Francisco with a price range of $$ to $$$ to find a suitable dining option for a client meeting. Once you have identified a potential restaurant, get restaurant details for restaurant ID R5678 to verify their hours of operation, ensuring they are open during the meeting time. After confirming the restaurant's availability, create an order for user U1234 at restaurant ID R5678 with items [(I789, quantity 3, no cheese)] and arrange delivery to \"123 Market St, San Francisco, CA\" to provide a seamless dining experience for the client.",
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
                kwargs={"user_id": "U077", "restaurant_id": "R5678", "items": [{"item_id": "I789", "quantity": 3, "customizations": "no cheese"}], "delivery_address": "123 Market St, San Francisco, CA"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U175",
        instruction="Your name is James Williams and your email is james.williams9904@email.com. You are logical, independent. First, get details for restaurant R456 to check its operational hours and delivery zones to ensure it can deliver to 123 Main St during your desired time. Then, get the menu for restaurant R456 to find available items in the sushi category that can be included in the order for user U1610.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "sushi"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U093",
        instruction="Your name is Mary Jones and your email is mary.jones2326@email.com. You are direct, patient, confident, independent. Get the restaurant menu for restaurant ID R123 to browse available Italian dishes.",
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
        user_id="U110",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are flexible, patient, confident, organized. First, search restaurants with cuisine \"Sushi\" and location \"Midtown\" to find options near Mary, as she is looking for a place to enjoy sushi. Once you identify a suitable restaurant, get restaurant details for restaurant ID R202 to check their operating hours and delivery zone to ensure they can deliver to Mary’s location. After confirming the restaurant can deliver, create an order for user ID U5441 with restaurant ID R202, including items I334 and I335, and set the delivery address to \"123 Main St, Apt 4B\" to complete the transaction smoothly.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Sushi", "location": "Midtown"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R202"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U110", "restaurant_id": "R202", "items": [{"item_id": "I334", "quantity": 1}, {"item_id": "I335", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are polite, optimistic. Please search for restaurants offering Italian cuisine in downtown with a moderate price range, and once you find a suitable option, get detailed information for restaurant R4567 to confirm their operating hours and delivery zone. This will help ensure that we can provide accurate delivery options for our customers on DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U061",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are optimistic, independent, direct, organized. First, search for Mexican restaurants in San Francisco, CA with a price range of $10-$20 to find a suitable dining option for a team lunch. Once you identify a potential restaurant, get restaurant details for restaurant ID R5678 to check its hours of operation and ensure it fits within your team's schedule. After confirming its availability, get the menu for restaurant ID R5678, focusing on the taco category, to explore the options available. Finally, add item ID I234 (Chicken Taco) to cart for user Patricia Miller with quantity 3, as she specifically requested this item for the lunch order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco, CA", "price_range": "$$"}
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
                kwargs={"user_id": "U061", "restaurant_id": "R5678", "item_id": "I234", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U095",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are polite, cautious, independent. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R123, focusing on the pasta category. This will help you decide if they offer a variety of pasta dishes that meet your taste preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
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
        user_id="U045",
        instruction="Your name is John Jones and your email is john.jones9677@email.com. You are polite, logical, optimistic, confident. Create an order for user U6719 with restaurant ID R1023, including items I345 and I567, for delivery to 123 Main St, using credit card payment.",
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
                name="get_item_details",
                kwargs={"restaurant_id": "R1023", "item_id": "I345"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R1023", "item_id": "I567"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U045", "restaurant_id": "R1023", "items": [{"item_id": "I345", "quantity": 1}, {"item_id": "I567", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U035",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are independent, cautious. Search for restaurants offering Mexican cuisine in Linda's current location with a mid-range price. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R101 to browse available items in the \"Tacos\" category.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U046",
        instruction="Your name is Mary Williams and your email is mary.williams2739@email.com. You are polite, logical, organized. First, search for restaurants with Mexican cuisine in the San Francisco area within a moderate price range to find suitable dining options. Once you have identified a restaurant, such as restaurant R1023, proceed to get the restaurant menu to view available items. This will help you make informed decisions when placing an order for a customer.",
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
        user_id="U019",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are logical, organized, flexible. First, search for Mexican restaurants in the downtown area with a price range of $$. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R2345 to check hours and delivery options. After confirming the restaurant meets the criteria and is open for delivery, get the restaurant menu for restaurant ID R2345, focusing on the Tacos category, to ensure they offer a variety of options. Finally, create an order for user Jennifer Davis (user ID U6303) at restaurant ID R2345 with items I6789 and I6790, using delivery address 123 Main St, and ensure the payment method is set to Credit Card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
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
                name="create_order",
                kwargs={"user_id": "U019", "restaurant_id": "R2345", "items": [{"item_id": "I6789", "quantity": 1}, {"item_id": "I6790", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U143",
        instruction="Your name is Linda Smith and your email is linda.smith6714@email.com. You are polite, optimistic, organized. First, search for restaurants in New York City offering Mexican cuisine with a moderate price range. Once you have identified a suitable restaurant, get the restaurant details for restaurant ID R5678 to verify operating hours and minimum order requirements. After confirming the restaurant meets the criteria, create an order for user ID U1234 with restaurant ID R5678, including items I234 and I235, deliver to 123 Main St, using a Credit Card for payment, and include special instructions to \"Leave at the door\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "New York City", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5678"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U143", "restaurant_id": "R5678", "items": [{"item_id": "I234", "quantity": 1}, {"item_id": "I235", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card", "special_instructions": "Leave at the door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are cautious, logical, organized. First, search for restaurants offering vegan cuisine in Jennifer Smith's location to ensure a variety of options are available. Once you have identified a suitable restaurant, get the menu for restaurant R101, focusing on the 'Vegan Specials' category, to review the vegan offerings.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U158"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Vegan", "location": "Jennifer Smith's location"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Vegan Specials"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U002",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith1965@email.com. You are confident, cautious, logical. Search for restaurants with Mexican cuisine in Patricia's area with a moderate price range to find suitable dining options. Once you have identified a restaurant, get the menu for restaurant ID R234 to explore available Mexican dishes. After reviewing the menu, add item I567 (Chicken Tacos) to cart for user Patricia Brown with quantity 3, ensuring she can enjoy her meal choice.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Patricia's area", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U002", "restaurant_id": "R234", "item_id": "I567", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U086",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are confident, cautious, direct, optimistic. First, get restaurant details for restaurant ID R4567 to verify it is open and accepts orders. Then, get the restaurant menu for restaurant ID R4567 to find available pasta dishes. This information will help ensure that we can efficiently list R4567 on DoorDash with accurate menu options for our customers.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R4567"}
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
        user_id="U010",
        instruction="Your name is John Jones and your email is john.jones8935@email.com. You are polite, organized, confident. First, search for Italian restaurants in the downtown area under a $30 price range to identify potential new partners for DoorDash. Once you have identified a promising restaurant, get the menu for that restaurant, focusing on the \"Pasta\" category, to assess the variety and pricing of their offerings.",
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
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are organized, flexible. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to identify potential new partners for DoorDash. Once you have identified a promising restaurant, get detailed information for restaurant R1023 to review their menu and operating hours, ensuring they align with DoorDash's delivery service requirements.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
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
        user_id="U142",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are polite, optimistic, patient, cautious. First, search for restaurants with Mexican cuisine in the downtown area within a moderate price range to find a suitable dining option. Once you have identified a potential restaurant, get the restaurant details for restaurant ID R2345 to check if it's currently open and accepting orders. If the restaurant is open, proceed to get the menu for restaurant ID R2345, focusing on the Tacos category, to explore the available options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
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
        user_id="U112",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are cautious, polite. First, search for restaurants in Mary's area with a preference for Italian cuisine and a moderate price range to find suitable dining options. Once you identify restaurant R234 as a potential choice, retrieve the menu for this restaurant, focusing on the pasta category to explore available options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Mary's area", "price_range": "$$"}
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
        user_id="U122",
        instruction="Your name is James Williams and your email is james.williams3457@email.com. You are cautious, organized. First, search for Japanese restaurants in San Francisco with a price range of $$ to $$$ to identify potential dining options. Once you have a list, get restaurant details for restaurant ID R101 to check if it is open and can accept orders. After confirming the restaurant's operational status, get the menu for restaurant ID R101 to find available sushi options. Finally, create an order for user ID U7411 with restaurant ID R101 and items [I202, I203], using delivery address 123 Main St, San Francisco, and payment method \"Credit Card\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Japanese", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R101"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R101", "category": "Sushi"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U122", "restaurant_id": "R101", "items": [{"item_id": "I202", "quantity": 1}, {"item_id": "I203", "quantity": 1}], "delivery_address": "123 Main St, San Francisco", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U151",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are cautious, confident, polite. First, search for Italian restaurants in San Francisco with a price range of $$. Once you have identified a suitable restaurant, get the menu for restaurant ID R102 to explore available pasta dishes. This will help you make an informed decision when placing an order for a customer.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U085",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are flexible, logical, direct, independent. Search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$20. Once you find a suitable restaurant, get the menu for restaurant ID R456 to explore available items in the 'Tacos' category. Add item ID I789 (Chicken Taco) to cart for user ID U101 with quantity 3 and extra salsa.",
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
                kwargs={"user_id": "U085", "restaurant_id": "R456", "item_id": "I789", "quantity": 3, "customizations": "extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is Robert Garcia and your email is robert.garcia9607@email.com. You are confident, optimistic, patient. Search for restaurants offering Mexican cuisine in San Francisco with a price range of $$ to $$$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R456 to find available items in the 'Tacos' category. After reviewing the menu, add item I789 (Chicken Tacos) to the cart for user Michael Brown with user ID U8314, with a quantity of 3.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "Tacos"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U180", "restaurant_id": "R456", "item_id": "I789", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U087",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are patient, optimistic, flexible. Search for Italian restaurants in San Francisco with a price range of $$ to $$$. After identifying a suitable restaurant, get details for restaurant R345 to check hours and delivery options. Finally, create an order for user U567 at restaurant R345 with items Spaghetti Carbonara and Garlic Bread, delivering to 123 Main St, with the payment method set to credit card.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R345"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U087", "restaurant_id": "R345", "items": [{"name": "Spaghetti Carbonara", "quantity": 1}, {"name": "Garlic Bread", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U085",
        instruction="Your name is Mary Brown and your email is mary.brown6719@email.com. You are direct, patient, organized, confident. First, search for Italian restaurants in the downtown area with a price range of $$-$$$ to find suitable dining options for our customer. Next, get restaurant details for restaurant ID R234 to check their opening hours, ensuring that the restaurant is open during the desired delivery time. Finally, create an order for user ID U001 at restaurant ID R234 with items [I789, I790], delivery address 123 Main St, payment method \"credit card\", and special instructions \"Leave at door\" to complete the customer’s request efficiently.",
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
                kwargs={"user_id": "U085", "restaurant_id": "R234", "items": [{"item_id": "I789", "quantity": 1}, {"item_id": "I790", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "credit card", "special_instructions": "Leave at door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U030",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are organized, independent, flexible. First, search for restaurants in the user's current location with a preferred cuisine type of 'Italian' and a price range of '$$'. Once you find a suitable option, get the restaurant menu for restaurant ID R2023 to explore available items. After reviewing the menu, add item I101 (Spaghetti Carbonara) to the cart for user ID U6337 with quantity 1 and no customizations. This sequence ensures that you select a restaurant that fits the user's preferences and proceed to place an order efficiently.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "current_location", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2023"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U030", "restaurant_id": "R2023", "item_id": "I101", "quantity": 1, "customizations": null}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U132",
        instruction="Your name is Linda Smith and your email is linda.smith2478@email.com. You are confident, flexible. Search for restaurants offering Mexican cuisine in the 94103 area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "94103"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U176",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are independent, confident, patient. First, search for Italian restaurants located in Downtown with a moderate price range. Once you have identified a suitable restaurant, obtain the details of the restaurant with the ID \"R123\" to ensure it meets your preferences. After confirming the restaurant's suitability, proceed to create an order from the restaurant with the ID \"R123\" for a pasta dish, specifying the delivery address as \"123 Main St, Downtown\" and using a credit card for payment. Include special instructions to leave the order at the door.",
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
                kwargs={"restaurant_id": "R123"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U176", "restaurant_id": "R123", "items": [{"item_id": "I001", "quantity": 1}], "delivery_address": "123 Main St, Downtown", "payment_method": "credit_card", "special_instructions": "Leave the order at the door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U006",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis1167@email.com. You are independent, flexible, patient. First, search for restaurants in the San Francisco area, focusing on Italian cuisine and a moderate price range to identify potential new partners for DoorDash. Once you have a list, get details for restaurant R00123 to check its hours and customer reviews, ensuring it aligns with DoorDash's quality standards and operational hours for potential collaboration.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R00123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are cautious, optimistic. First, search for restaurants with Mexican cuisine in the downtown area with a moderate price range to explore potential dining options. Once you have identified a suitable restaurant, get the menu for restaurant ID R234 to find available items in the \"Main Dishes\" category, ensuring they meet your preferences. Finally, create an order for user ID U123 at restaurant ID R234 with items [I789] and specify the delivery address as 123 Main St, ensuring a seamless dining experience through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R234", "category": "Main Dishes"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U122", "restaurant_id": "R234", "items": [{"item_id": "I789", "quantity": 1}], "delivery_address": "123 Main St"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U122",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are polite, organized, optimistic, patient. Get restaurant menu for restaurant R5678 to find available items in the \"Tacos\" category",
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
        user_id="U048",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are logical, independent, polite, cautious. Search for restaurants in San Francisco offering Mexican cuisine within a moderate price range. Once you find a suitable restaurant, get the restaurant menu for restaurant ID R001 to explore available Mexican dishes. This will help you decide on a potential order for a client looking to enjoy a Mexican meal through DoorDash.",
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
        user_id="U016",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams7359@email.com. You are polite, organized, flexible, direct. Search for restaurants offering Mexican cuisine in the San Francisco area with a moderate price range.",
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
        user_id="U006",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are direct, logical, cautious, polite. First, search for restaurants with Italian cuisine in the San Francisco area within a moderate price range to identify potential new partners for DoorDash. Once you have identified these restaurants, get restaurant details for restaurant ID R1023 to verify hours of operation and customer reviews, ensuring the restaurant meets DoorDash's quality standards and operational hours for optimal delivery service.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U123",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are patient, organized, polite, independent. Add item I205 (Spaghetti Carbonara) to cart for user jennifer.miller6443@email.com with quantity 1",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian"}
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
                kwargs={"user_id": "U123", "restaurant_id": "R001", "item_id": "I205", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U177",
        instruction="Your name is Linda Garcia and your email is linda.garcia2772@email.com. You are independent, polite, organized. search_restaurants(cuisine=\"Italian\", location=\"Patricia's area\", price_range=\"medium\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Patricia's area", "price_range": "medium"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U192",
        instruction="Your name is Patricia Jones and your email is patricia.jones4973@email.com. You are patient, cautious. Search for Mexican restaurants in the San Francisco area with a price range of $10-$20 to find potential options for a customer. Once you identify restaurant R345 as a suitable choice, get details for restaurant R345 to verify hours of operation and delivery zone, ensuring it can deliver to the customer's location. After confirming this information, get the menu for restaurant R345 to review available items in the \"Entrees\" category so you can assist in creating an order for user U102 with items [(I678, quantity 3)] and set the delivery address as 123 Main St.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R345"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R345", "category": "Entrees"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U192", "restaurant_id": "R345", "items": [{"item_id": "I678", "quantity": 3}], "delivery_address": "123 Main St"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U178",
        instruction="Your name is Linda Williams and your email is linda.williams1610@email.com. You are flexible, confident. First, search for restaurants offering Chinese cuisine in Mary's location with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a restaurant, proceed to get the restaurant menu for restaurant ID R234 to find available items and categories. This will help you make an informed decision for placing an order through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "Mary's location", "price_range": "$$-$$$"}
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
        user_id="U037",
        instruction="Your name is Michael Smith and your email is michael.smith6151@email.com. You are flexible, patient, logical. Search for restaurants offering Chinese cuisine in Linda Davis's area with a moderate price range",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "Linda Davis's area", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U138",
        instruction="Your name is Mary Williams and your email is mary.williams6067@email.com. You are independent, optimistic. First, search for Italian restaurants in the downtown area with a price range of $$ to $$$ to find a suitable dining option. Once you have identified a potential restaurant, get restaurant details for restaurant ID R789 to check its operating hours and delivery zones, ensuring it can deliver to your location. Finally, create an order for user U3457 at restaurant ID R789 with items [I123, I124] and delivery address \"123 Main St, Apt 4B\" to enjoy a delicious meal at home.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R789"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U138", "restaurant_id": "R789", "items": [{"item_id": "I123", "quantity": 1}, {"item_id": "I124", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is Patricia Garcia and your email is patricia.garcia1231@email.com. You are polite, confident. search_restaurants(location=\"Downtown\", cuisine=\"Italian\", price_range=\"$$\")",
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
        user_id="U123",
        instruction="Your name is Robert Garcia and your email is robert.garcia9808@email.com. You are cautious, logical, direct. First, search for Mexican restaurants in Los Angeles with a price range of $$ to $$$ to find suitable dining options. Once you have identified a restaurant, get the restaurant menu for restaurant ID R456 to explore available items and decide on a meal. After reviewing the menu, add item I789 (Chicken Tacos) to the cart for user U123 with a quantity of 3 and extra salsa customization, ensuring the order is tailored to the user's preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Los Angeles", "price_range": "$$-$$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U123", "restaurant_id": "R456", "item_id": "I789", "quantity": 3, "customizations": "extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are direct, confident. First, search for Italian restaurants in Michael Williams' area with a moderate price range to identify potential dining options. Once you have a list, get the menu for restaurant R234 to explore available pasta dishes. This will help you make an informed decision on which restaurant offers the best selection for Michael to enjoy a satisfying meal through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "Michael Williams' area", "price_range": "$$"}
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
        user_id="U075",
        instruction="Your name is Robert Miller and your email is robert.miller1558@email.com. You are cautious, polite. First, search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $10-$20. Once you have identified a suitable restaurant, get the restaurant menu for restaurant R345 to identify available tacos and burritos. This will help you ensure that the menu items meet the customer's preferences before proceeding with the order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U123",
        instruction="Your name is Patricia Jones and your email is patricia.jones3517@email.com. You are polite, independent, logical, direct. Search for Italian restaurants in the downtown area with a price range of $$ and above, and once you have identified a suitable option, get detailed information for restaurant R567 to verify its operating hours. This will help ensure that the restaurant is open during peak delivery times for DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
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
        user_id="U142",
        instruction="Your name is Patricia Miller and your email is patricia.miller7287@email.com. You are flexible, organized. Start by searching for restaurants in the downtown area offering Mexican cuisine within a moderate price range. Once you have identified a suitable restaurant, get the restaurant details for restaurant R5423 to check its operating hours and delivery zone. After confirming that the restaurant is open and delivers to your area, get the menu for restaurant R5423, focusing on the \"Tacos\" category, to review the available options.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R5423"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R5423", "category": "Tacos"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U180",
        instruction="Your name is John Brown and your email is john.brown5124@email.com. You are logical, optimistic, polite, flexible. Search for restaurants offering Chinese cuisine in the San Francisco area within a moderate price range. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R102 to view available Chinese dishes. This will help ensure that the restaurant meets your culinary preferences and budget before making a decision to place an order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U180",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown7411@email.com. You are independent, cautious, confident, logical. First, search for Mexican restaurants in the Brooklyn area with a price range of $10-$20 to find suitable dining options. Once you have identified a restaurant, get the restaurant menu for restaurant ID R2345, focusing on the Taco category to explore specific offerings. After selecting your preferred item, add item ID I7890 (Chicken Taco) to cart for user ID U8314 with a quantity of 3, ensuring you have enough for your meal.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Brooklyn", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R2345", "category": "Taco"}
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U180", "restaurant_id": "R2345", "item_id": "I7890", "quantity": 3}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U042",
        instruction="Your name is Linda Smith and your email is linda.smith5308@email.com. You are optimistic, direct, polite. First, search for restaurants in the downtown area offering Mexican cuisine with a price range of $10-$20. Once you find a suitable restaurant, get the restaurant menu for restaurant R1023 to find available items in the 'Tacos' category. This will help you identify the best options for a customer looking to enjoy affordable Mexican cuisine through DoorDash.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$$"}
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
        user_id="U112",
        instruction="Your name is Michael Davis and your email is michael.davis4985@email.com. You are cautious, logical. Add item 'Pad Thai' (item_id 'I1122') to cart for user 'mary.williams6067@email.com' with quantity 1.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Thai"}
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
                kwargs={"user_id": "U112", "restaurant_id": "R001", "item_id": "I1122", "quantity": 1}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U035",
        instruction="Your name is Linda Miller and your email is linda.miller5151@email.com. You are organized, logical. Search for restaurants offering Thai cuisine in Linda's vicinity with a medium price range.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Thai", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is Mary Miller and your email is mary.miller1688@email.com. You are confident, independent, patient. Create an order for user U001 with restaurant R102 including items I204 and I207, specifying delivery address as 123 Main St, Apt 4B, payment method as credit card, and special instructions to leave at the door.",
        actions=[
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R102"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R102", "item_id": "I204"}
            ),
            Action(
                name="get_item_details",
                kwargs={"restaurant_id": "R102", "item_id": "I207"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U158", "restaurant_id": "R102", "items": [{"item_id": "I204", "quantity": 1}, {"item_id": "I207", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B", "payment_method": "credit card", "special_instructions": "leave at the door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U128",
        instruction="Your name is Michael Johnson and your email is michael.johnson5118@email.com. You are logical, flexible. Begin by searching for restaurants with Mexican cuisine in the San Francisco area within a medium price range to identify potential new additions to our DoorDash platform. Once you have a list, focus on restaurant R582 by obtaining detailed information to check its operating hours and delivery zone. This will help determine its feasibility for inclusion in our delivery service area.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R582"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U106",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are patient, polite, cautious. First, search for restaurants with Mexican cuisine in the downtown area with a price range under $20 to find suitable dining options. Next, get the restaurant details for restaurant ID R250 to check its operating hours and delivery zones, ensuring it aligns with your delivery needs. Finally, create an order for user ID U5307 at restaurant ID R250 with items [I102] and a delivery address of \"123 Main St, Apt 4B,\" ensuring the order is placed within the restaurant's operating hours and delivery zones.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "downtown", "price_range": "$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R250"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U106", "restaurant_id": "R250", "items": [{"item_id": "I102", "quantity": 1}], "delivery_address": "123 Main St, Apt 4B"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U158",
        instruction="Your name is Linda Brown and your email is linda.brown5883@email.com. You are optimistic, organized, logical. search_restaurants(cuisine=\"Italian\", location=\"downtown\", price_range=\"medium\")",
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
        user_id="U010",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are flexible, cautious. Get the menu for restaurant R567 to find available sushi items.",
        actions=[
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "sushi"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U048",
        instruction="Your name is John Brown and your email is john.brown7947@email.com. You are direct, confident, patient. Search for restaurants in James Williams' location with cuisine preference for Italian.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={"user_id": "U048"}
            ),
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "James Williams"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U124",
        instruction="Your name is Mary Williams and your email is mary.williams2739@email.com. You are direct, patient, independent, cautious. Search for Italian restaurants in the downtown area with a price range of $$ to $$$",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$ $$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U110",
        instruction="Your name is Patricia Brown and your email is patricia.brown1418@email.com. You are flexible, polite. search_restaurants (cuisine=\"Mexican\", location=\"Downtown\", price_range=\"$$\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "Downtown", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is James Jones and your email is james.jones6913@email.com. You are optimistic, independent, direct. Search for restaurants offering Mexican cuisine in the San Francisco area with a price range of $$ to $$$. Once you find a suitable restaurant, specifically look for restaurant R567. Get detailed information about restaurant R567 to verify operating hours and delivery zones to ensure it aligns with DoorDash's delivery capabilities.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Mexican", "location": "San Francisco", "price_range": "$$,$$$"}
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
        user_id="U158",
        instruction="Your name is Linda Jones and your email is linda.jones3192@email.com. You are optimistic, patient, confident, independent. First, search for Italian restaurants in the San Francisco downtown area with a price range of medium to identify potential dining options. Next, get restaurant details for restaurant ID R234 to check operational hours and delivery zone, ensuring it fits within the desired timeframe and location for delivery. Finally, create an order for user U123 with restaurant ID R234, including items I567 and I568, and delivery address 123 Elm St, using a credit card as the payment method, and specify \"Leave at the door\" in the special instructions to accommodate contactless delivery preferences.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R234"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U158", "restaurant_id": "R234", "items": [{"item_id": "I567", "quantity": 1}, {"item_id": "I568", "quantity": 1}], "delivery_address": "123 Elm St", "payment_method": "credit card", "special_instructions": "Leave at the door"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U007",
        instruction="Your name is John Miller and your email is john.miller1015@email.com. You are cautious, flexible, patient. First, search for Italian restaurants in the downtown area with a price range of $$. Once you have identified a suitable restaurant, get the restaurant menu for restaurant ID R456, focusing on the pasta category. This will help you decide on an order for user ID U123. After reviewing the pasta options, create an order with restaurant ID R456, including items [I789] with delivery address \"123 Main St\" and payment method \"Credit Card\".",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R456", "category": "pasta"}
            ),
            Action(
                name="create_order",
                kwargs={"user_id": "U007", "restaurant_id": "R456", "items": [{"item_id": "I789", "quantity": 1}], "delivery_address": "123 Main St", "payment_method": "Credit Card"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U134",
        instruction="Your name is Patricia Jones and your email is patricia.jones4973@email.com. You are organized, optimistic, polite. First, search for restaurants offering Chinese cuisine in the downtown area within a moderate price range to identify potential options for a dinner order. Once you have a list, focus on restaurant R567 and get details to verify its operating hours and delivery zones to ensure it can accommodate your needs. Finally, obtain the menu for restaurant R567, specifically looking at the 'Dinner Specials' category, to decide on suitable items for a future order.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Chinese", "location": "downtown", "price_range": "$$"}
            ),
            Action(
                name="get_restaurant_details",
                kwargs={"restaurant_id": "R567"}
            ),
            Action(
                name="get_restaurant_menu",
                kwargs={"restaurant_id": "R567", "category": "Dinner Specials"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U167",
        instruction="Your name is Linda Garcia and your email is linda.garcia5307@email.com. You are organized, patient, polite. search_restaurants(location=\"Midtown\", cuisine=\"Mexican\", price_range=\"$$\")",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"location": "Midtown", "cuisine": "Mexican", "price_range": "$$"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U076",
        instruction="Your name is Patricia Williams and your email is patricia.williams6296@email.com. You are confident, polite, direct, cautious. First, search for Italian restaurants in the San Francisco area with a price range of $$ to identify potential options for a client meeting. Once you have found a suitable restaurant, get the restaurant menu for restaurant ID R123 to view available pasta dishes, ensuring there is a good selection for the attendees.",
        actions=[
            Action(
                name="search_restaurants",
                kwargs={"cuisine": "Italian", "location": "San Francisco", "price_range": "$$"}
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
        user_id="U037",
        instruction="Your name is James Johnson and your email is james.johnson8780@email.com. You are cautious, optimistic. First, search for restaurants in the downtown area with a price range of $$ and offering Mexican cuisine. Once you find a suitable option, get restaurant details for restaurant ID R567 to check opening hours and delivery zones to ensure they can deliver to your location. After confirming delivery availability, get the menu for restaurant ID R567 focusing on the \"Tacos\" category. If the Chicken Tacos look appealing, add item ID I789 (Chicken Tacos) to the cart for user ID U123 with quantity 3 and extra salsa customization.",
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
                kwargs={"user_id": "U037", "restaurant_id": "R567", "item_id": "I789", "quantity": 3, "customizations": "extra salsa"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="U133",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams7359@email.com. You are direct, logical, independent, flexible. Add item \"I6789\" (Chicken Tacos) to cart for user \"john.brown5124@email.com\" at restaurant ID \"R2345\" with quantity 2.",
        actions=[
            Action(
                name="add_item_to_cart",
                kwargs={"user_id": "U133", "restaurant_id": "R2345", "item_id": "I6789", "quantity": 2}
            ),
        ],
        outputs=[]
    ),
]
