"""
Xplore DEV :: Function Overview

Author: daniel.dominguet@gmail.com
"""

# %%
from pathlib import Path
from dotenv import load_dotenv

from xploredev.log.xdv_log import create_logger
from xploredev.utils.xdv_environment import resolve_project_root

# -----------------------------------------------------------------------------
# PARAMETERS CONFIGURATION
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# SCRIPT EXECUTION
# -----------------------------------------------------------------------------
# Environment setup
# -----------------------------------------------------------------------------
# Getting project root and script path
script_path = Path(__file__).resolve()
project_root = resolve_project_root(script_path.parent)

# Loading environment variables
load_dotenv(project_root / ".env")

# Creating logger
log = create_logger(project_root, script_path)

# Initializing run
log.init_run()
log.log_environment_setup()
# %%
# -----------------------------------------------------------------------------
# Pipeline execution
# -----------------------------------------------------------------------------
try:
    log.title("Lambda functions")
    even = lambda x: x + 1
    log.info(f"Even function: {even(1)}")
except Exception as exc:
    log.error("Pipeline execution failed: %s", exc, exc_info=True)
    raise
finally:
    log.close_run()

# %%
