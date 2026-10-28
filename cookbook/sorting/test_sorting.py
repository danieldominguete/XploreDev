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
from xploredev.lists.sorting import insertion_sort, merge_sort, quick_sort, knapsack

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

test_array = [5, 2, 9, 1, 5, 6]

log.title("Teste do algoritmo de ordenacao por insercao")
sorted_array = insertion_sort(test_array)
log.info(f"Array original: {test_array}")
log.info(f"Array ordenado: {sorted_array}")

# Teste do algoritmo de ordenacao por merge sort
log.title("Teste do algoritmo de ordenacao por merge sort")
sorted_array_merge = merge_sort(test_array)
log.info(f"Array original: {test_array}")
log.info(f"Array ordenado: {sorted_array_merge}")

# Teste do algoritmo de ordenacao por quick sort
log.title("Teste do algoritmo de ordenacao por quick sort")
sorted_array_quick = quick_sort(test_array)
log.info(f"Array original: {test_array}")
log.info(f"Array ordenado: {sorted_array_quick}")

# Testes de estudo
weights = [2, 1, 3]
values = [4, 2, 3]
capacity = 4

print(knapsack(weights, values, capacity))  # 6


# ==================================================================================
# Encerramento do script
# ==================================================================================
log.close_run()
