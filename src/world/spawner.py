from pytiled_parser.tiled_object import Rectangle
from typing import List, Tuple
from .world import World


class Spawner:
    def __init__(self, world: World, spawner: Rectangle):
        self.world = world
        self.spawner = spawner
        self.path = self.calculate_path_to_finish()

    def get_path(self, obj: Rectangle) -> List[Rectangle]:
        """
        Recursively get list of objects on the path
        :param obj: start point
        :return: a list of all objects on the path
        """
        next_id = obj.properties.get("path")
        if next_id:
            next_objects = list(filter(lambda x: x.id == next_id, self.world.objects))
            if next_objects:
                return [obj] + self.get_path(next_objects[0])
        return [obj]

    def calculate_path_to_finish(self) -> List[List[float]]:
        return list(
            map(
                lambda x: self.world.tiled_to_screen(x.coordinates.x, x.coordinates.y),
                self.get_path(self.spawner),
            )
        )
