"""
Xplore DS :: Localhost Tools Package
"""

# importando as bibliotecas padrao
from pathlib import Path
import sys, os

# Configurando path para raiz do projeto e setup de reconhecimento da pasta da lib
project_folder = Path(__file__).resolve().parents[2]
sys.path.append(str(project_folder))

from xploredev.io.file import create_folder


class XploreDevLocalhost:
    def __init__(self, run_folder: str) -> None:

        # criando a pasta de runs caso não exista
        create_folder(str(run_folder) + "/runs")
