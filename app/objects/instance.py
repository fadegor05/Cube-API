from typing import List

from pydantic import BaseModel

from app.objects.modrinth_mod import ModrinthMod
from app.objects.curseforge_mod import CurseforgeMod

class Instance(BaseModel):
    id: int
    name: str
    version: str
    changelog: str
    game_version: str
    loader: str
    modrinth: List[ModrinthMod]
    curseforge: List[CurseforgeMod]