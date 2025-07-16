# Copyright Sierra

from pydantic import BaseModel
from typing import List, Dict, Any, Optional, Union

RESPOND_ACTION_NAME = "respond"
RESPOND_ACTION_FIELD_NAME = "content"

class SFTConfig(BaseModel):
    agent_strategies: List[str] = ["tool-calling", "react", "act"]
    user_strategies: List[str] = ["llm", "react", "verify", "reflection"]
    num_conversations_per_strategy: int = 100
    domains: List[str] = ["airline", "retail", "telecom", "doordash", "healthcare"]  # Updated to include all 5 domains
    filter_successful_only: bool = True
    output_format: str = "openai"  # "openai", "alpaca", "sharegpt"
    temperature_range: List[float] = [0.0, 0.3, 0.7]
    diversification_strategies: List[str] = []

class Action(BaseModel):
    name: str
    kwargs: Dict[str, Any]


class Task(BaseModel):
    user_id: str
    actions: List[Action]
    instruction: str
    outputs: List[str] = []
    domain: Optional[str] = None  # Added domain field
    annotator: Optional[str] = None  # Added annotator field
    complexity: Optional[int] = None  # Added complexity field
    generated_at: Optional[str] = None  # Added generated_at field


class RewardOutputInfo(BaseModel):
    r_outputs: float
    outputs: Dict[str, bool]


class RewardActionInfo(BaseModel):
    r_actions: float
    gt_data_hash: str


class RewardResult(BaseModel):
    reward: float
    info: Union[RewardOutputInfo, RewardActionInfo]
    actions: List[Action]


class SolveResult(BaseModel):
    reward: float
    messages: List[Dict[str, Any]]
    info: Dict[str, Any]
    total_cost: Optional[float] = None


class EnvInfo(BaseModel):
    task: Task
    source: Optional[str] = None
    user_cost: Optional[float] = None
    reward_info: Optional[RewardResult] = None


class EnvResponse(BaseModel):
    observation: str
    reward: float
    done: bool
    info: EnvInfo


class EnvResetResponse(BaseModel):
    observation: str
    info: EnvInfo


class EnvRunResult(BaseModel):
    task_id: int
    reward: float
    info: Dict[str, Any]
    traj: List[Dict[str, Any]]
    trial: int


class RunConfig(BaseModel):
    model_provider: str
    user_model_provider: str
    model: str
    user_model: str = "gpt-4o"
    num_trials: int = 1
    env: str = "retail"
    agent_strategy: str = "tool-calling"
    temperature: float = 0.0
    task_split: str = "test"
    start_index: int = 0
    end_index: int = -1
    task_ids: Optional[List[int]] = None
    dataset_start: Optional[int] = None
    dataset_end: Optional[int] = None
    log_dir: str = "results"
    max_concurrency: int = 1
    seed: int = 10
    shuffle: int = 0
    user_strategy: str = "llm"
    few_shot_displays_path: Optional[str] = None
    custom_dataset_path: Optional[str] = None  # Added for custom dataset support
