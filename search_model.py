import asyncio, platform, aiohttp, requests
if platform.system() == 'Windows':
    from asyncio import WindowsSelectorEventLoopPolicy
    asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
from duckduckgo_search import AsyncDDGS
from PyQt6 import QtCore

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

class DDGImageSearch(QtCore.QThread):
    fetched = QtCore.pyqtSignal(str, str, QtCore.QByteArray)

    def __init__(self, query : str, max_results=10, separate_query_with_comma : bool = False):
        super().__init__()
        if not separate_query_with_comma:
            self.query = [query]
        else:
            self.query = query.split(',')
        self.query = [q.strip() for q in self.query]
        self.max_results = max_results

    def run(self):
        asyncio.run(self.aget_tasks())
        self.quit()

    async def aget_tasks(self):
        words = self.query
        tasks = [self.aget_results(w) for w in words]
        await asyncio.gather(*tasks)
        
    async def aget_results(self, word):
        results = await AsyncDDGS().images(word, region='wt-wt', safesearch='off', max_results=self.max_results)
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(len(results)):
                tasks.append(self.download_image(session, results[i]))
            await asyncio.gather(*tasks)
    
    async def download_image(self, session : aiohttp.ClientSession, ddg_result):
        title = ddg_result["title"]
        image_url = ddg_result["image"]
        thumbnail_url = ddg_result["thumbnail"]
        try:
            async with session.get(thumbnail_url) as response:
                if response.status != 200:
                    print(f'Failed to get {thumbnail_url} from {title}')
                    return
                thumbnail = await response.read()
                self.fetched.emit(title, image_url, QtCore.QByteArray(thumbnail))
        except:
            print(f'Failed to get {thumbnail_url} from {title}')
            
            
class ImageDownload(QtCore.QThread):
    fetched = QtCore.pyqtSignal(QtCore.QByteArray)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        r = requests.get(self.url, headers=headers)
        if r.status_code != 200:
            print(f'Failed to get {self.url}')
        self.fetched.emit(QtCore.QByteArray(r.content))
        self.quit()
        
            
        

