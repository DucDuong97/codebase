
import os
from pathlib import Path
import shutil

class AppAnalyser(object):

    TEMP_DIR = os.path.join(Path(__file__).parent,'temp')
    DEV_DIR  = os.path.join(Path(__file__).parent,'temp','dev')
    APPS_DIR = os.path.join(Path(__file__).parent,'temp','apps')
    CSS_DIR  = os.path.join(Path(__file__).parent,'temp','css')
    JS_DIR   = os.path.join(Path(__file__).parent,'temp','jss')
    
    def __init__(self, dir):
        try:
            shutil.copytree(os.path.join(dir,'dev') , os.path.join(AppAnalyser.TEMP_DIR,'dev'))
            shutil.copytree(os.path.join(dir,'apps'), os.path.join(AppAnalyser.TEMP_DIR,'apps'))
            # shutil.copytree(os.path.join(dir,'apt','static','js'), os.path.join(self.TEMP_DIR,'js'))
            # shutil.copytree(os.path.join(dir,'apt','static','css'), os.path.join(self.TEMP_DIR,'css'))
        except Exception as e:
            print('Error: your app folder is not well constructed.')
        self.dev_dirs = list(Path(AppAnalyser.DEV_DIR).rglob("*.php"))
        self.apps_dirs = list(Path(AppAnalyser.APPS_DIR).rglob("*.php"))
        # self.css_dirs = list(Path(self.CSS_DIR).rglob("*.css"))
        # self.js_dirs = list(Path(self.JS_DIR).rglob("*.js"))
        
        pass

    def __del__(self):
        shutil.rmtree(self.TEMP_DIR)
        pass
    
    def getContexts(self):
        contexts = []
        for path in self.dev_dirs:
            contexts.append({
                'file': path,
                'actual_file': str(path).replace(AppAnalyser.TEMP_DIR, ''),
                'lang':'php',
                'type': 'dev',
            })
        for path in self.apps_dirs:
            contexts.append({
                'file': path,
                'actual_file': str(path).replace(AppAnalyser.TEMP_DIR, ''),
                'lang':'php',
                'type': 'apps',
            })
        return contexts