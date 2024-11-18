import aiohttp

from app.core.config import BASE_MODRINTH_URL
from app.integrations.base_integration import BaseIntegration
from app.schemas.mod_schema import ModrinthMod, CompiledInstanceMod


class ModrinthIntegration(BaseIntegration):
    BASE_URL = BASE_MODRINTH_URL

    async def get_mod(self, mod: ModrinthMod) -> CompiledInstanceMod:
        url = self.BASE_URL + f"/project/{mod.mod}/version/{mod.version}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise Exception(f"{self.__repr__()} is not reachable")
                data = await response.json()
                for file in data.get("files", []):
                    if file["primary"]:
                        return CompiledInstanceMod(file=file.get("filename"), url=file.get("url"))
        return None


modrinth_integration = ModrinthIntegration()