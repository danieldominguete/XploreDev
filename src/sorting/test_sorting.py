"""
Xplore DEV :: Sorting Algorithm Tests
"""

# Importando bibliotecas padrao
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Configurando path para raiz do projeto e setup de reconhecimento da pasta da lib
project_folder = Path(__file__).resolve().parents[2]
sys.path.append(str(project_folder))

# Importando biblioteca XploreDEV
from xploredev.environment.localhost import XploreDevLocalhost
from xploredev.environment.logging import XploreDevLogging
from xploredev.lists.sorting import insertion_sort

# ==================================================================================
# Setup do script

script_name = os.path.basename(__file__)

# Variaveis de ambiente
load_dotenv()

# Criando estrutura de execucao local
env = XploreDevLocalhost(run_folder=project_folder)

# Criando estrutura de logs
log = XploreDevLogging(project_root=project_folder, script_name=script_name)
log.init_run()
log.log_environment_setup()

# ==================================================================================
# Parametrizacao do script
# ==================================================================================
log.title("Script setup")

# Configuracao de dados de saida
output_folder = "output"


# ==================================================================================
# Execucao das regras de negocio
# ==================================================================================

# Teste do algoritmo de ordenacao por insercao
log.title("Teste do algoritmo de ordenacao por insercao")

test_array = [5, 2, 9, 1, 5, 6]
sorted_array = insertion_sort(test_array)

log.info(f"Array original: {test_array}")
log.info(f"Array ordenado: {sorted_array}")

# ==================================================================================
# Encerramento do script
# ==================================================================================
log.close_run()
