import os
import time
import yaml
import asyncio
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from notebooklm import NotebookLMClient

class SyncHandler(FileSystemEventHandler):
    def __init__(self, sync_manager, loop):
        self.sync_manager = sync_manager
        self.loop = loop

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(('.pdf', '.docx', '.txt', '.xlsx')):
            print(f"Detectat canvi a: {event.src_path}")
            asyncio.run_coroutine_threadsafe(self.sync_manager.upload_file(event.src_path), self.loop)

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(('.pdf', '.docx', '.txt', '.xlsx')):
            print(f"Nou fitxer detectat: {event.src_path}")
            asyncio.run_coroutine_threadsafe(self.sync_manager.upload_file(event.src_path), self.loop)

class SyncManager:
    def __init__(self, config_path="config/sync_config.yaml"):
        self.config_path = config_path
        self.config = self.load_config()
        self.client = None
        
    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return yaml.safe_load(f)
        return {"notebook_id": None, "session_cookie": None, "watch_dir": "docs/PB/V1"}

    async def setup(self):
        if self.config.get('session_cookie'):
            # El client de notebooklm-py requereix un format d'AuthTokens o similar
            # Per simplicitat en aquest wrapper, demanem a l'usuari que faci login un cop
            # o que ens passi la cookie. La llibreria suporta 'from_storage()'.
            pass

    async def upload_file(self, file_path):
        # Recarreguem la config per si s'ha editat el fitxer mentre el script corre
        self.config = self.load_config()
        notebook_id = self.config.get('notebook_id')
        if not notebook_id or notebook_id == "INSEREIX_EL_TEU_NOTEBOOK_ID_AQUÍ":
            print("Notebook ID no configurat.")
            return

        try:
            # Nota: notebooklm-py usa emmagatzematge de Playwright per defecte
            # Si no hi ha storage, fallarà. Instruirem l'usuari sobre 'notebooklm login'
            async with await NotebookLMClient.from_storage() as client:
                print(f"Pujant {file_path} a NotebookLM...")
                await client.sources.add_file(notebook_id, file_path)
                print("Pujada completada.")
        except Exception as e:
            print(f"Error pujant fitxer: {e}")

    async def sync_once(self):
        watch_dir = self.config.get('watch_dir', 'docs/PB/V1')
        if not os.path.exists(watch_dir):
            print(f"Carpeta {watch_dir} no existeix. Saltant sincronització.")
            return
            
        print(f"Iniciant sincronització puntual de: {watch_dir}")
        for root, dirs, files in os.walk(watch_dir):
            for file in files:
                if file.endswith(('.pdf', '.docx', '.txt', '.xlsx')):
                    await self.upload_file(os.path.join(root, file))
        print("Sincronització puntual finalitzada.")

    def start_watching(self, loop):
        watch_dir = self.config.get('watch_dir', 'docs/PB/V1')
        if not os.path.exists(watch_dir):
            os.makedirs(watch_dir)
            
        observer = Observer()
        handler = SyncHandler(self, loop)
        observer.schedule(handler, watch_dir, recursive=True)
        observer.start()
        print(f"Monitoritzant carpetes: {watch_dir}")
        return observer

async def main():
    manager = SyncManager()
    # Executem sincronització inicial
    await manager.sync_once()
    
    # Iniciem monitorització
    loop = asyncio.get_running_loop()
    observer = manager.start_watching(loop)
    
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    asyncio.run(main())
