# use v1 to instead of pydantic
import pydantic as origin_pydantic
main_pydantic_version, *_ = origin_pydantic.__version__
import sys
if main_pydantic_version == "2":
    from pydantic import v1
    sys.modules['pydantic'] = v1

from .session import Session
from .application import Rocketry, Grouper
from .core import Scheduler

try:
    from ._version import *
except ImportError:
    # Package was not built the standard way
    __version__ = version = '0.0.0.UNKNOWN'
    __version_tuple__ = version_tuple = (0, 0, 0, 'UNKNOWN', '')

from ._setup import _setup_defaults
from . import (
    conditions,
    log,

    args,
    time,
    tasks,
)
from .tasks import FuncTask
_setup_defaults()
session = Session(config={"execution": "process"})
session.set_as_default()

# Reset pydantic version to avoid conflicts with calling system
sys.modules['pydantic'] = origin_pydantic