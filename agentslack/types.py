from dataclasses import dataclass, field
from typing import Set, Dict
from collections import defaultdict
from agentslack.Slack import Slack

@dataclass 
class Message:
    message: str
    channel_id: str
    user_id: str
    timestamp: str

    def __eq__(self, other):
        return self.message == other.message and self.channel_id == other.channel_id and self.user_id == other.user_id and self.timestamp == other.timestamp
    
    def is_in(self, messages: list) -> bool:
        """Check if the message exists in the provided list."""
        return self in messages

@dataclass
class SlackApp:
    slack_id: str
    slack_token: str 

@dataclass 
class Channel:
    slack_id: str
    name: str 


@dataclass
class Agent:
    world_name: str
    agent_name: str 
    slack_app: SlackApp
    channels: list[Channel] = field(default_factory=list)
    read_messages: defaultdict[str, list[Message]] = field(default_factory=lambda: defaultdict(list))
    slack_client: Slack = None 
    tools: Set[str] = field(default_factory=set)
    included_humans: Set[str] = field(default_factory=set) # humans this agent can't interact with

@dataclass
class World:
    agents: Set[str] = field(default_factory=set)
    humans: Set[str] = field(default_factory=set)
    start_datetime: str = field(default_factory=str)
    slack_client: Slack = None 
    channels: list[Channel] = field(default_factory=list)
    human_mappings: Dict[str, str] = field(default_factory=dict) # human_id -> slack_app_id
