from .index import bp as index
from .auth import bp as auth
from .categories import bp as categories
from .threads import bp as threads

BLUEPRINTS = [index, auth, categories, threads]
