__version__ = "0.0.1"

from ._core import add, subtract

from dataclasses import dataclass

from abc import ABC, abstractmethod
from typing import List, Dict

import PIL.Image
import openai

# Async function for text generation
async def generate_text(prompt):
    response = await openai.ChatCompletion.acreate(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message['content']

async def generate_image(prompt):
    response = await openai.Image.acreate(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']

@dataclass
class Bbox:
    x1: float
    y1: float
    x2: float
    y2: float

class Annotator(ABC):
    # @abstractmethod
    def annotate(self, image: List, ontology: List[str]) -> Dict[str, List[Bbox]]:
        pass

    @abstractmethod
    def query(self, image: PIL.Image.Image):
        pass

class ChatGpt(Annotator):
    def __init__(self, apikey=""):
        openai.api_key = apikey

    async def query(self, image: PIL.Image.Image):
        return await generate_text("a cat")


class Gemini(Annotator):
    pass

__all__ = ["__version__", "add", "subtract", "Annotator", "ChatGpt"]
