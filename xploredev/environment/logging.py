"""
Xplore DS :: Logging Tools Package
"""

import logging
import warnings
from datetime import datetime
import time
from pathlib import Path
from xploredev.io.file import create_folder
from xploredev.utils.general import convert_bytes
import sys
import os
import platform
import psutil


class XploreDevLogging:

    def __init__(self, project_root: str, script_name: str) -> None:

        # capturando referencias de caminhos
        self.project_root = project_root
        self.script_name = script_name

        # capturando referencias de tempos de inicialização
        self.dt_init = datetime.now()
        self.dt_init_str = self.dt_init.strftime("%y%m%d%H%M%S")
        self.ts_init = time.time()

        # configurando o nome do arquivo de log
        self.log_name = Path(str(script_name)).stem + "_" + self.dt_init_str + ".log"
        self.log_run = Path(str(script_name)).stem + "_" + self.dt_init_str

        # configurando locais de registros de logs
        self.log_path = str(project_root) + "/runs/" + str(self.log_run) + "/"

        # configurando o path completo de log
        self.log_file = self.log_path + self.log_name

        # criando a pasta caso não exista
        create_folder(self.log_path)

        # configurando o logger
        self.logger = self._setup_logger()

        # Configuracao de warnings
        # warnings.filterwarnings(os.getenv("PYTHON_WARNINGS"))

    def _setup_logger(self) -> None:

        # configurando o logger
        log_config = {
            "level": logging.INFO,
            "format": "%(asctime)s - %(levelname)s - %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S",
            "handlers": [logging.FileHandler(self.log_file), logging.StreamHandler()],
        }

        logging.basicConfig(**log_config)

        return logging.basicConfig(**log_config)

    def info(self, message: str) -> None:

        logging.info(message)

    def warning(self, message: str) -> None:

        logging.warning(message)

    def error(self, message: str) -> None:

        logging.error(message)

    def title(self, message: str) -> None:

        logging.info(
            "**********************************************************************************"
        )
        logging.info(message)
        logging.info(
            "**********************************************************************************"
        )

    def subtitle(self, message: str) -> None:

        logging.info(
            "=================================================================================="
        )
        logging.info(message)
        logging.info(
            "=================================================================================="
        )

    def section(self, message: str) -> None:

        logging.info(
            "----------------------------------------------------------------------------------"
        )
        logging.info(message)
        logging.info(
            "----------------------------------------------------------------------------------"
        )

    def init_run(self) -> None:

        # configurando abertura de run
        logging.info(
            "**********************************************************************************"
        )
        logging.info("Starting script: " + self.log_run)
        logging.info(
            "**********************************************************************************"
        )

    def close_run(self) -> None:

        time_ref_end = datetime.now()
        time_end = time.time()
        exec_time = ((time_end - self.ts_init) / 60) / 60

        logging.info(
            "**********************************************************************************"
        )
        logging.info("Execution finished script: " + self.log_run)
        logging.info("Conclusion at " + str(time_ref_end.strftime("%Y-%m-%d %H:%M")))
        logging.info("Execution time: %.2f hours" % exec_time)
        logging.info(
            "**********************************************************************************"
        )
        logging.info(
            "                                                                          XploreDEV"
        )
        logging.info(
            "**********************************************************************************"
        )

    def log_environment_setup(self) -> None:

        logging.info(
            "**********************************************************************************"
        )
        logging.info("Environment Setup")
        logging.info(
            "----------------------------------------------------------------------------------"
        )
        logging.info("Machine Setup")
        logging.info(
            "----------------------------------------------------------------------------------"
        )
        logging.info("Machine: " + str(platform.machine()))
        logging.info("Processor: " + str(platform.processor()))
        logging.info("Physical cores: " + str(psutil.cpu_count(logical=False)))
        logging.info("Total cores: " + str(psutil.cpu_count(logical=True)))
        logging.info(
            "Physical memory: {gb:.2f}GB".format(
                gb=convert_bytes(psutil.virtual_memory().total, "GB"),
            )
        )
        logging.info(
            "----------------------------------------------------------------------------------"
        )
        logging.info("OS Setup")
        logging.info(
            "----------------------------------------------------------------------------------"
        )
        logging.info("OS id: " + str(platform.platform()))
        logging.info("OS System: " + str(platform.system()))
        logging.info("OS Node Name: " + str(platform.node()))
        logging.info("OS Release:" + str(platform.release()))

        logging.info(
            "----------------------------------------------------------------------------------"
        )
        logging.info("Python Setup")
        logging.info(
            "----------------------------------------------------------------------------------"
        )
        logging.info("Python version: " + sys.version)
        logging.info("Python path: " + sys.executable)
        logging.info("Python warnings: " + str(os.getenv("PYTHON_WARNINGS")))
        logging.info(
            "----------------------------------------------------------------------------------"
        )
        logging.info("Run Setup")
        logging.info(
            "----------------------------------------------------------------------------------"
        )
        logging.info("Root folder:" + str(self.project_root))
        logging.info("Run name: " + str(self.log_run))
        logging.info("Artifacts folder:" + str(self.log_path))

        logging.info(
            "**********************************************************************************"
        )
