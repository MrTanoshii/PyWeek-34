# Research Tree

```python
class ResearchTree()
```

---

## Methods

```python
@classmethod
get_research_tree(cls) -> dict
#Gets the full state of the research tree
```

<br/><br/>

```python
@classmethod
get_research_state(cls, research: str) -> bool
#Get an individual research state.
```

### Keyword arguments

-   `research: str` -- the research to get the state of

### Returns: The state of the research

<br/><br/>

```python
@classmethod
unlock_research(cls, research: str)
#Unlock a research
```

### Keyword arguments

-   `research: str` -- the research to unlock

<br/><br/>

```python
@classmethod
satisfy_research_cost(cls, research: str) -> bool
#Check if the player can afford the research
```

### Keyword arguments

-   `research: str` -- the research to check the cost of

### Returns: whether the player can afford the research

<br/><br/>

```python
@classmethod
reset(cls)
#Reset the research tree to the default state
```
