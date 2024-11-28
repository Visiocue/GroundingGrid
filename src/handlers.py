from dataclasses import dataclass

from abc import ABC, abstractmethod
from typing import List, Dict

import PIL.Image


@dataclass
class Bbox:
    x1: float
    y1: float
    x2: float
    y2: float

class Annotator(ABC):
    @abstractmethod
    def annotate(self, image: List, ontology: List[str]) -> Dict[str, List[Bbox]]:
        pass

    @abstractmethod
    def query(self, image: PIL.Image.Image):
        pass

class ChatGpt(Annotator):
    def annotate(self, image: List, ontology: List[str]) -> Dict[str, List[Bbox]]:
        pass
    pass


class Gemini(Annotator):
    pass