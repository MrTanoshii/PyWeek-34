
> Values still needs adjustment; not final values
## Infantry
```python
health_max: float = 30
health_current: float = health_max
speed_original: float = 10
speed_current: float = speed_original
flying: bool = false
boss: bool = false
frozen: bool = false
poisoned: bool = false
armor: int = 0
gold_drop: int = 10
```

## Heavy Infantry
```python
health_max: float = 75
health_current: float = health_max
speed_original: float = 6
speed_current: float = speed_original
flying: bool = false
boss: bool = false
frozen: bool = false
poisoned: bool = false
armor: int = 0
gold_drop: int = 20
```

## Scout
```python
health_max: float = 20
health_current: float = health_max
speed_original: float = 20
speed_current: float = speed_original
flying: bool = false
boss: bool = false
frozen: bool = false
poisoned: bool = false
armor: int = 0
gold_drop: int = 15
```

## Tank/Humvee/Stryker(?)
Possibly spawns 3 basic infantry and 1 Heavy Infantry on death?
```python
health_max: float = 400
health_current: float = health_max
speed_original: float = 5
speed_current: float = speed_original
flying: bool = false
boss: bool = false
frozen: bool = false
poisoned: bool = false
armor: int = 10
gold_drop: int = 50
```

## Plane(?)
```python
health_max: float = 200
health_current: float = health_max
speed_original: float = 10
speed_current: float = speed_original
flying: bool = true
boss: bool = false
frozen: bool = false
poisoned: bool = false
armor: int = 10
gold_drop: int = 30
```