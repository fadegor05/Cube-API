from app.configuration.config import BASE_MODRINTH_URL

from typing import Dict

from requests import request

def get_mod_files_from_modrinth(mod: str, version: str) -> Dict | None:
    url = BASE_MODRINTH_URL + f'/project/{mod}/version/{version}'
    response = request(method='GET', url=url)
    data = response.json()
    files = data['files']
    print(files)
    mods_url = {}
    for file in files:
        if file['primary'] == True:
            mods_url[file['filename']] = file['url']
    
    return mods_url