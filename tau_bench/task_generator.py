# Copyright Sierra

import json
import random
import uuid
from typing import List, Dict, Any, Optional, Set
from dataclasses import dataclass
from tau_bench.types import Task, Action


@dataclass
class TaskTemplate:
    """Template for generating new tasks"""
    domain: str
    task_type: str  # e.g., "exchange", "return", "booking", "modification"
    instruction_template: str
    required_actions: List[str]
    optional_actions: List[str]
    personality_traits: List[str]
    complexity_level: int  # 1-5, where 5 is most complex


class TaskGenerator:
    """Generate diverse synthetic tasks based on existing patterns"""
    
    def __init__(self, domain: str):
        self.domain = domain
        self.templates = self._load_templates()
        self.entities = self._load_entities()
        
    def _load_templates(self) -> List[TaskTemplate]:
        """Load task templates for the domain"""
        if self.domain == "retail":
            return self._get_retail_templates()
        elif self.domain == "airline":
            return self._get_airline_templates()
        else:
            raise ValueError(f"Unsupported domain: {self.domain}")
    
    def _get_retail_templates(self) -> List[TaskTemplate]:
        """Define retail task templates"""
        return [
            TaskTemplate(
                domain="retail",
                task_type="exchange",
                instruction_template="You are {user_name} in {zip_code}. You received your order #{order_id} and wish to exchange the {item1} for {item1_replacement} and the {item2} for {item2_replacement}. {preference_condition}. You are {personality}.",
                required_actions=["find_user_id_by_name_zip", "get_order_details", "exchange_delivered_order_items"],
                optional_actions=["get_product_details", "get_user_details"],
                personality_traits=["detail-oriented", "impatient", "methodical", "reactive", "private"],
                complexity_level=3
            ),
            TaskTemplate(
                domain="retail",
                task_type="return",
                instruction_template="You are {user_name} in {zip_code}. You want to return the {items} from your recent order. {return_reason}. You are {personality} and {behavior_note}.",
                required_actions=["find_user_id_by_name_zip", "get_order_details", "return_delivered_order_items"],
                optional_actions=["get_product_details", "get_user_details"],
                personality_traits=["emotional", "polite", "frustrated", "cooperative", "demanding"],
                complexity_level=2
            ),
            TaskTemplate(
                domain="retail",
                task_type="inquiry_and_modification",
                instruction_template="You are {user_name} in {zip_code}. You want to know {inquiry_question}. You also want to {modification_action} your pending {item_type}. {specific_requirements}. You are {personality}.",
                required_actions=["find_user_id_by_name_zip", "list_all_product_types", "modify_pending_order_items"],
                optional_actions=["get_product_details", "get_user_details", "get_order_details"],
                personality_traits=["curious", "specific", "private", "detail-oriented", "efficient"],
                complexity_level=4
            ),
            TaskTemplate(
                domain="retail",
                task_type="complex_multi_action",
                instruction_template="You are {user_name} in {zip_code}. You have multiple orders and need to {action1} some items, {action2} others, and {inquiry} about {topic}. {conditional_behavior}. You are {personality}.",
                required_actions=["find_user_id_by_name_zip", "get_user_details"],
                optional_actions=["get_order_details", "exchange_delivered_order_items", "return_delivered_order_items", "modify_pending_order_items", "list_all_product_types"],
                personality_traits=["organized", "overwhelmed", "decisive", "cautious", "thorough"],
                complexity_level=5
            )
        ]
    
    def _get_airline_templates(self) -> List[TaskTemplate]:
        """Define airline task templates"""
        return [
            TaskTemplate(
                domain="airline",
                task_type="booking",
                instruction_template="Your user id is {user_id}. You want to fly from {origin} to {destination} on {date} ({flight_type}). {time_preferences}. You want to fly in {cabin_class}. {flight_preferences}. {payment_preferences}. You have {baggage_count} baggage(s). {insurance_preference}. You are {personality}.",
                required_actions=["book_reservation"],
                optional_actions=[],
                personality_traits=["reactive", "specific", "flexible", "price-conscious", "time-sensitive"],
                complexity_level=3
            ),
            TaskTemplate(
                domain="airline",
                task_type="modification",
                instruction_template="Your user id is {user_id}. You have a reservation {reservation_context} and want to {modification_type}. {specific_requirements}. {payment_preferences}. You are {personality}.",
                required_actions=["update_reservation_flights"],
                optional_actions=["update_reservation_passengers", "update_reservation_baggages"],
                personality_traits=["urgent", "emotional", "cooperative", "demanding", "flexible"],
                complexity_level=4
            ),
            TaskTemplate(
                domain="airline",
                task_type="cancellation",
                instruction_template="Your user id is {user_id}. You need to cancel your {trip_description} due to {cancellation_reason}. {insurance_context}. You are {personality}.",
                required_actions=["cancel_reservation"],
                optional_actions=[],
                personality_traits=["urgent", "unwell", "disappointed", "understanding", "frustrated"],
                complexity_level=2
            ),
            TaskTemplate(
                domain="airline",
                task_type="bulk_modification",
                instruction_template="Your user id is {user_id}. You have {issue_context} and need to {bulk_action} for all your reservations. {specific_requirements}. You want to know {calculation_request}. You are {personality}.",
                required_actions=["update_reservation_flights"],
                optional_actions=["update_reservation_passengers", "update_reservation_baggages"],
                personality_traits=["emotional", "overwhelmed", "cooperative", "analytical", "urgent"],
                complexity_level=5
            )
        ]
    
    def _load_entities(self) -> Dict[str, List[str]]:
        """Load entity pools for task generation"""
        if self.domain == "retail":
            return {
                "user_names": ["Alex Johnson", "Maria Garcia", "David Chen", "Sarah Williams", "James Brown", "Lisa Anderson", "Michael Davis", "Jennifer Wilson"],
                "zip_codes": ["10001", "90210", "60601", "30301", "19101", "02101", "33101", "94101"],
                "items": ["mechanical keyboard", "smart thermostat", "wireless headphones", "laptop", "tablet", "smartwatch", "cleaner", "desk lamp", "water bottle", "t-shirt", "jacket", "shoes"],
                "item_replacements": {
                    "mechanical keyboard": ["keyboard with clicky switches", "RGB backlit keyboard", "wireless keyboard"],
                    "smart thermostat": ["Google Home compatible thermostat", "Apple HomeKit thermostat", "WiFi thermostat"],
                    "wireless headphones": ["noise-canceling headphones", "gaming headset", "bluetooth earbuds"],
                    "desk lamp": ["LED desk lamp", "adjustable lamp", "battery-powered lamp"],
                    "water bottle": ["larger water bottle", "insulated bottle", "glass water bottle"],
                    "t-shirt": ["v-neck t-shirt", "long-sleeve shirt", "polo shirt"]
                },
                "colors": ["purple", "blue", "red", "black", "white", "green", "gray"],
                "sizes": ["XS", "S", "M", "L", "XL", "XXL"],
                "materials": ["cotton", "polyester", "wool", "silk", "linen"],
                "return_reasons": ["doesn't fit properly", "wrong color", "damaged during shipping", "not as described", "changed mind"],
                "order_ids": [f"#W{random.randint(1000000, 9999999)}" for _ in range(100)]
            }
        elif self.domain == "airline":
            return {
                "user_ids": [f"{name.lower().replace(' ', '_')}_{random.randint(1000, 9999)}" for name in ["Alex Johnson", "Maria Garcia", "David Chen", "Sarah Williams", "James Brown", "Lisa Anderson"]],
                "cities": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"],
                "airports": {"New York": ["JFK", "LGA", "EWR"], "Los Angeles": ["LAX"], "Chicago": ["ORD", "MDW"], "Houston": ["IAH", "HOU"], "Seattle": ["SEA"], "Denver": ["DEN"]},
                "dates": ["2024-05-20", "2024-05-21", "2024-05-22", "2024-05-23", "2024-05-24", "2024-05-25", "2024-05-26", "2024-05-27"],
                "cabin_classes": ["economy", "business", "first"],
                "flight_types": ["one_way", "round_trip"],
                "reservation_ids": [f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(100, 999)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}" for _ in range(50)]
            }
        else:
            return {}
    
    def generate_task(self, template: Optional[TaskTemplate] = None, complexity_range: Optional[tuple] = None) -> Task:
        """Generate a single synthetic task"""
        if template is None:
            available_templates = self.templates
            if complexity_range:
                min_complexity, max_complexity = complexity_range
                available_templates = [t for t in self.templates if min_complexity <= t.complexity_level <= max_complexity]
            template = random.choice(available_templates)
        
        # Generate task content based on template
        if self.domain == "retail":
            return self._generate_retail_task(template)
        elif self.domain == "airline":
            return self._generate_airline_task(template)
        else:
            raise ValueError(f"Unsupported domain: {self.domain}")
    
    def _generate_retail_task(self, template: TaskTemplate) -> Task:
        """Generate a retail task from template"""
        entities = self.entities
        
        # Select random entities
        user_name = random.choice(entities["user_names"])
        zip_code = random.choice(entities["zip_codes"])
        order_id = random.choice(entities["order_ids"])
        personality = random.choice(template.personality_traits)
        
        # Generate template-specific content
        template_vars = {
            "user_name": user_name,
            "zip_code": zip_code,
            "order_id": order_id,
            "personality": personality
        }
        
        if template.task_type == "exchange":
            item1 = random.choice(entities["items"])
            item2 = random.choice([item for item in entities["items"] if item != item1])
            template_vars.update({
                "item1": item1,
                "item2": item2,
                "item1_replacement": random.choice(entities["item_replacements"].get(item1, [item1])),
                "item2_replacement": random.choice(entities["item_replacements"].get(item2, [item2])),
                "preference_condition": random.choice([
                    "If there is no exact match, you'd prefer the closest alternative",
                    "If unavailable, you'd go for a different color but same features",
                    "If not available, you'd rather return the items instead"
                ])
            })
        elif template.task_type == "return":
            items = random.sample(entities["items"], random.randint(1, 3))
            template_vars.update({
                "items": ", ".join(items),
                "return_reason": random.choice(entities["return_reasons"]),
                "behavior_note": random.choice([
                    "want to resolve this quickly",
                    "don't want to provide unnecessary details",
                    "expect a full refund",
                    "need this resolved today"
                ])
            })
        elif template.task_type == "inquiry_and_modification":
            item_type = random.choice(["t-shirts", "jackets", "shoes", "accessories"])
            template_vars.update({
                "inquiry_question": f"how many {random.choice(entities['items'])} options are available",
                "modification_action": random.choice(["modify", "change", "update"]),
                "item_type": item_type,
                "specific_requirements": f"change to {random.choice(entities['colors'])} color, {random.choice(entities['sizes'])} size, prefer {random.choice(entities['materials'])}"
            })
        elif template.task_type == "complex_multi_action":
            template_vars.update({
                "action1": random.choice(["exchange", "return", "modify"]),
                "action2": random.choice(["upgrade", "cancel", "reorder"]),
                "inquiry": random.choice(["ask", "inquire", "find out"]),
                "topic": random.choice(["shipping options", "product availability", "return policies", "warranty information"]),
                "conditional_behavior": random.choice([
                    "If options are limited, you'll accept alternatives",
                    "You want to complete everything in one session",
                    "You're flexible but prefer the most convenient options",
                    "You want detailed explanations for each step"
                ])
            })
        
        # Generate instruction
        instruction = template.instruction_template.format(**template_vars)
        
        # Generate simplified actions (for SFT we don't need exact action sequences)
        actions = self._generate_simplified_actions(template.required_actions, template.optional_actions)
        
        return Task(
            user_id=f"{user_name.lower().replace(' ', '_')}_{random.randint(1000, 9999)}",
            instruction=instruction,
            actions=actions,
            outputs=[]  # Simplified for SFT generation
        )
    
    def _generate_airline_task(self, template: TaskTemplate) -> Task:
        """Generate an airline task from template"""
        entities = self.entities
        
        # Select random entities
        user_id = random.choice(entities["user_ids"])
        personality = random.choice(template.personality_traits)
        
        template_vars = {
            "user_id": user_id,
            "personality": personality
        }
        
        if template.task_type == "booking":
            origin_city = random.choice(entities["cities"])
            dest_city = random.choice([city for city in entities["cities"] if city != origin_city])
            template_vars.update({
                "origin": origin_city,
                "destination": dest_city,
                "date": random.choice(entities["dates"]),
                "flight_type": random.choice(entities["flight_types"]),
                "cabin_class": random.choice(entities["cabin_classes"]),
                "time_preferences": random.choice([
                    "You do not want to fly before 11am",
                    "You prefer afternoon flights",
                    "You need an early morning departure",
                    "You want the last flight of the day"
                ]),
                "flight_preferences": random.choice([
                    "You prefer direct flights but one stopover is fine",
                    "You only want direct flights",
                    "You don't mind stopovers if the price is better",
                    "You prefer the fastest route"
                ]),
                "payment_preferences": random.choice([
                    "You want to use your certificates to pay",
                    "You prefer to pay with credit card",
                    "You want to use gift cards if possible",
                    "You have a specific payment method preference"
                ]),
                "baggage_count": random.randint(0, 3),
                "insurance_preference": random.choice(["You do not want insurance", "You want travel insurance", "You'll decide about insurance later"])
            })
        elif template.task_type == "modification":
            template_vars.update({
                "reservation_context": random.choice([
                    "that you don't remember the ID for",
                    f"(ID: {random.choice(entities['reservation_ids'])})",
                    "from your recent booking"
                ]),
                "modification_type": random.choice([
                    "change to a later flight",
                    "upgrade your cabin class",
                    "add checked baggage",
                    "change the passenger details",
                    "modify the return flight"
                ]),
                "specific_requirements": random.choice([
                    "You want the fastest option available",
                    "You don't care about cost but want convenience",
                    "You prefer to stay in the same cabin class",
                    "You want to minimize connection time"
                ]),
                "payment_preferences": random.choice([
                    "You prefer gift card payment",
                    "You want to use your smallest balance gift card",
                    "You'll pay with the original payment method",
                    "You want to use certificates if possible"
                ])
            })
        elif template.task_type == "cancellation":
            template_vars.update({
                "trip_description": random.choice([
                    "upcoming business trip",
                    "vacation to Texas",
                    "weekend getaway",
                    "family visit"
                ]),
                "cancellation_reason": random.choice([
                    "a family emergency",
                    "feeling unwell",
                    "work conflicts",
                    "weather concerns",
                    "changed plans"
                ]),
                "insurance_context": random.choice([
                    "You have travel insurance and want to use it",
                    "You're willing to use insurance if needed",
                    "You don't have insurance but hope for understanding",
                    "You want to know about refund options"
                ])
            })
        elif template.task_type == "bulk_modification":
            template_vars.update({
                "issue_context": random.choice([
                    "schedule conflicts with all your upcoming trips",
                    "a family emergency affecting multiple reservations",
                    "work policy changes that affect your travel",
                    "health concerns requiring trip adjustments"
                ]),
                "bulk_action": random.choice([
                    "reschedule",
                    "modify the cabin class",
                    "add insurance",
                    "change destinations",
                    "update passenger details"
                ]),
                "specific_requirements": random.choice([
                    "You want all changes to be consistent across reservations",
                    "You prefer to minimize total cost increases",
                    "You want the fastest processing possible",
                    "You need flexibility for future changes"
                ]),
                "calculation_request": random.choice([
                    "the total cost difference",
                    "the cancellation fees if any",
                    "the best available options",
                    "the timeline for processing"
                ])
            })
        
        # Generate instruction
        instruction = template.instruction_template.format(**template_vars)
        
        # Generate simplified actions
        actions = self._generate_simplified_actions(template.required_actions, template.optional_actions)
        
        return Task(
            user_id=user_id,
            instruction=instruction,
            actions=actions,
            outputs=[]  # Simplified for SFT generation
        )
    
    def _generate_simplified_actions(self, required_actions: List[str], optional_actions: List[str]) -> List[Action]:
        """Generate simplified action sequence for SFT purposes"""
        actions = []
        
        # Add required actions
        for action_name in required_actions:
            actions.append(Action(name=action_name, kwargs={}))
        
        # Add some optional actions randomly
        num_optional = random.randint(0, min(2, len(optional_actions)))
        for action_name in random.sample(optional_actions, num_optional):
            actions.append(Action(name=action_name, kwargs={}))
        
        return actions
    
    def generate_task_batch(self, count: int, complexity_range: Optional[tuple] = None) -> List[Task]:
        """Generate a batch of diverse tasks"""
        tasks = []
        
        # Ensure diversity by using different templates
        for i in range(count):
            template = None
            if len(self.templates) > 1:
                # Cycle through templates for diversity
                template = self.templates[i % len(self.templates)]
            
            task = self.generate_task(template=template, complexity_range=complexity_range)
            tasks.append(task)
        
        return tasks
    
    def get_template_statistics(self) -> Dict[str, Any]:
        """Get statistics about available templates"""
        stats = {
            "total_templates": len(self.templates),
            "by_complexity": {},
            "by_type": {},
            "domain": self.domain
        }
        
        for template in self.templates:
            # Complexity distribution
            if template.complexity_level not in stats["by_complexity"]:
                stats["by_complexity"][template.complexity_level] = 0
            stats["by_complexity"][template.complexity_level] += 1
            
            # Type distribution
            if template.task_type not in stats["by_type"]:
                stats["by_type"][template.task_type] = 0
            stats["by_type"][template.task_type] += 1
        
        return stats


def create_synthetic_task_pool(domain: str, count: int = 1000, complexity_range: Optional[tuple] = None) -> List[Task]:
    """Create a large pool of synthetic tasks for SFT generation"""
    generator = TaskGenerator(domain)
    return generator.generate_task_batch(count, complexity_range)


def enhance_existing_tasks_with_synthetic(original_tasks: List[Task], domain: str, enhancement_ratio: float = 2.0) -> List[Task]:
    """Enhance existing tasks with synthetic variations"""
    synthetic_count = int(len(original_tasks) * enhancement_ratio)
    generator = TaskGenerator(domain)
    synthetic_tasks = generator.generate_task_batch(synthetic_count)
    
    # Combine and shuffle
    combined_tasks = original_tasks + synthetic_tasks
    random.shuffle(combined_tasks)
    
    return combined_tasks 