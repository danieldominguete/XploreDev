# XploreDev

Biblioteca Python e cookbook para experimentos em engenharia de software

## Estrutura do repositório

```
src/xploredev/     → biblioteca (publicável no PyPI)
cookbook/          → scripts e notebooks de receitas locais
references/        → material de estudo
```

## Configuração do ambiente

Este projeto usa **[uv](https://docs.astral.sh/uv/)** para ambientes e dependencias.
Nao use `requirements.txt` nem `pip install` — tudo fica em `pyproject.toml` + `uv.lock`.

### 1. Instalar uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Inicializar ambiente do projeto

Na raiz do repositio (onde está o `pyproject.toml`):

```bash
uv sync --all-groups
```

O `uv sync` cria `.venv/`, instala dependências fixadas em `uv.lock` e registra **`xploredev`** em modo editável a partir de `src/xploredev/`.

Para **criar um projeto Python novo** com uv (fora deste repo):

```bash
uv init --python 3.12
uv add pandas          # exemplo: adiciona dependencia e atualiza pyproject.toml + uv.lock
uv sync
```

### 3. Notebooks sem output no Git (nbstripout)

Este repo **nao usa** o pacote [`pre-commit`](https://pre-commit.com/) para notebooks. A limpeza e feita pelo **filtro Git** do [`nbstripout`](https://github.com/kynan/nbstripout) (ja dependencia em `pyproject.toml`).

**Uma vez por clone** (depois de `uv sync`), na raiz do repo:

```bash
uv run nbstripout --install --attributes .gitattributes
```

Isso registra o filtro em `.git/config` e versiona regras em `.gitattributes` (`*.ipynb filter=nbstripout`). No `git add`, outputs sao removidos do que entra no indice; no working tree voce pode continuar executando o notebook normalmente.

Conferir se esta ativo:

```bash
uv run nbstripout --is-installed
uv run nbstripout --status
```

Se recriar o `.venv` ou mudar o caminho do Python, reinstale o filtro:

```bash
uv run nbstripout --install --attributes .gitattributes --force
```

Limpar notebooks ja versionados (one-shot), se necessario:

```bash
uv run nbstripout $(git ls-files '*.ipynb')
```

Validar CI/local sem alterar arquivos:

```bash
uv run nbstripout --verify $(git ls-files '*.ipynb')
```

### 4. Execução

Validação do setup:

```bash
uv run xploredev
```

Testes:

```bash
uv run pytest
```

Exemplo de cookbook:

```bash
uv run python cookbook/sorting/test_sorting.py
```

## Versionamento semântico (Commitizen)

Commits seguem **[Conventional Commits](https://www.conventionalcommits.org/)** via [Commitizen](https://commitizen-tools.github.io/commitizen/). A versão do pacote vive em `pyproject.toml` (`[project].version`); o `cz bump` atualiza essa versão, o `CHANGELOG.md` e cria a tag Git `vX.Y.Z`.

### Commits & Push

```bash
git add .
uv run cz commit
git push
```

| Tipo | Quando usar | Bump |
|------|-------------|------|
| `feat` | Nova funcionalidade | minor |
| `fix` | Correcao de bug | patch |
| `docs` | Documentacao | — |
| `refactor` | Refatoracao | patch |
| `test` | Testes | — |
| `chore` | Manutencao | — |

### Release e publicacao

```bash
uv run cz bump          # bump de versao + CHANGELOG + tag
uv build                # gera dist/*.whl
uv publish              # publica no PyPI (quando configurado)
```

Na primeira release (sem tags Git), use `--yes`:

```bash
uv run cz bump --yes
```



### Módulos da biblioteca (`src/xploredev/`)

| Pacote | Arquivo | Responsabilidade |
|--------|---------|------------------|
| `io` | `xdv_file.py` | Pastas, JSON e persistência de `pandas` (Parquet, etc.) |
| `log` | `xdv_log.py` | Logging estruturado e perfil de ambiente em execuções |
| `utils` | `xdv_environment.py` | Localizar a raiz do projeto (`pyproject.toml`) |
| `utils` | `xds_memory.py` | Conversão e utilitários de memória |
| `environment` | `xdv_localhost.py` | Estrutura de pastas para runs locais |
| `lists` | `sorting.py` | Algoritmos de ordenação e knapsack (estudo) |