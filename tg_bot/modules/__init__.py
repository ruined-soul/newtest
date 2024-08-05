import os
import importlib

def register_modules(dispatcher):
    module_files = [f[:-3] for f in os.listdir(os.path.dirname(__file__)) if f.endswith('.py') and f != '__init__.py']
    for module_name in module_files:
        module = importlib.import_module(f'tg_bot.modules.{module_name}')
        if hasattr(module, 'register'):
            module.register(dispatcher)
