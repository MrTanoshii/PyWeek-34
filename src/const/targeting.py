from typing import List, Tuple, Optional
from functools import partial
from operator import itemgetter, attrgetter
from enemy import Enemy


class TARGETING:
    @staticmethod
    def _hp_getter(arg: Tuple[Enemy, float]) -> float:
        return arg[0].hp_current

    @staticmethod
    def ground_target(enemy: Enemy):
        return not enemy.flying

    air_target = attrgetter("flying")

    closest_target = partial(min, key=itemgetter(1))
    strongest_target = partial(max, key=_hp_getter)
    weakest_target = partial(min, key=_hp_getter)
