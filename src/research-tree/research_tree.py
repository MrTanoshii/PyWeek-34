import src.const as C
from src.classes import *


class ResearchTree:
    """ResearchTree is the base class for the research tree."""

    research_tree = C.RESEARCHTREE.DEFAULT_STATE

    @classmethod
    def get_research_tree(cls) -> dict:
        """Get the full research tree state.

        Returns:
        dict -- the research tree state"""

        return cls.research_tree

    @classmethod
    def get_research_state(cls, research: str) -> bool:
        """Get an individual research state.

        Keyword arguments:
        research -- the research to get the state of

        Returns:
        bool -- the state of the research"""

        return cls.research_tree[research]

    @classmethod
    def unlock_research(cls, research: str):
        """Unlock a research.

        Keyword arguments:
        research -- the research to unlock"""

        if cls.satisfy_research_cost(research):
            Gold.increment(-cls.research_tree[research]["GOLD_COST"])
            Research.increment(-cls.research_tree[research]["RESEARCH_COST"])
            cls.research_tree[research]["UNLOCKED"] = True

    @classmethod
    def satisfy_research_cost(cls, research: str) -> bool:
        """Check if the player can afford the research.

        Keyword arguments:
        research -- the research to check the cost of

        Returns:
        bool -- whether the player can afford the research"""

        return (
            Gold.get() >= cls.research_tree[research]["GOLD_COST"]
            and Research.get() >= cls.research_tree[research]["RESEARCH_COST"]
        )

    @classmethod
    def reset(cls):
        """Reset the research tree to the default state."""

        cls.research_tree = C.RESEARCHTREE.DEFAULT_STATE
