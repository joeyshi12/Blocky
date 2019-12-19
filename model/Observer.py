from abc import abstractmethod

from pygame.surface import Surface


class Observer:
    @abstractmethod
    def update(self, display: Surface):
        pass
