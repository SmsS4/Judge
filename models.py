from typing import List, Any, Optional

from dataclasses import dataclass

class Colors:
    HEADER = '\033[95m'
    TASK = '\033[94m'
    INFO = '\033[96m'
    SUCCESSFUL = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


@dataclass
class Test:
    generator: str
    number_of_tests: int
    args: List[Any]
    sub_tasks: List[int]
    validator: Optional[str]


@dataclass
class Config:
    name: str
    resource: str
    solutions: List[str]
    sub_tasks_score: List[int]
    tests: List[Test]
    shutdown_on_failure:bool
