# Audio

```python
class Audio()
```

---

## Methods

```python
@classmethod
preload()
# Preload all sounds. To be called once.
```

<br/><br/>

```python
@classmethod
play(sound: str) -> pyglet.media.Player
# Play a sound.
```

### Keyword Arguments

-   `sound: str` -- The name of the sound to play.

### Returns: The sound stream player.

<br/><br/>

```python
@classmethod
play_random(sound_list: list) -> pyglet.media.Player
# Play a random sound from a list.
```

### Keyword Arguments

-   `sound_list: list` -- The list of sounds to play from.

### Returns: The sound stream player.

<br/><br/>

```python
@classmethod
stop(sound: Union[str, pyglet.media.Player])
# Stop a currently playing sound or sound stream player.
```

### Keyword Arguments

-   `sound: str` -- The name of the sound to stop.
-   `sound: pyglet.media.Player` -- The sound stream player to stop.
