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

### Configuração única (por clone)

Com o ambiente já sincronizado **incluindo dependências de desenvolvimento**:

```bash
git add .
uv run cz commit
```

O hook `commit-msg` valida mensagens quando você usa `git commit -m "..."` diretamente. O fluxo recomendado continua sendo `uv run cz commit`, que já guia o formato correto.

### Passo a passo: do código ao commit

1. **Desenvolver** e revisar o diff (`git status`, `git diff`).
2. **Adicionar** apenas o que entra naquele commit lógico:

   ```bash
   git add caminho/do/arquivo
   ```

3. **Registrar o commit** com o assistente interativo:

   ```bash
   uv run cz commit
   ```

   Escolha o **tipo**, o **escopo** (opcional) e a **descrição** em imperativo (ex.: `feat(io): add parquet export helper`).

4. **Repetir** os passos 1–3 até a branch estar pronta para release ou merge.

| Tipo | Quando usar | Efeito no `cz bump` (versão 0.x) |
|------|-------------|----------------------------------|
| `feat` | Nova funcionalidade na biblioteca | **minor** (ex.: 0.1.0 → 0.2.0) |
| `fix` | Correção de bug | **patch** (ex.: 0.1.0 → 0.1.1) |
| `refactor` | Refatoração sem mudar comportamento externo | **patch** |
| `perf` | Melhoria de desempenho | **patch** |
| `docs` | Só documentação | sem bump automático típico* |
| `test` | Só testes | sem bump automático típico* |
| `chore` | Manutenção (deps, CI, etc.) | sem bump automático típico* |
| `BREAKING CHANGE` no corpo ou `!` após o tipo | Mudança incompatível | **major** quando sair de 0.x ou em 1.x+ |

\*Commits só `docs`/`test`/`chore` não costumam justificar release sozinhos; acumule com `feat`/`fix` ou faça bump manual se necessário.

### Passo a passo: gerar nova versão do pacote

1. **Garantir** que `main` (ou sua branch de release) está limpa, com commits no formato Conventional Commits e CI verde, se houver.
2. **Gerar versão, CHANGELOG e tag**:

   ```bash
   uv run cz bump
   ```

   Na **primeira tag** do repositório (ainda sem tags Git), confirme sem prompt extra:

   ```bash
   uv run cz bump --yes
   ```

3. **Conferir** o que mudou:

   ```bash
   git show HEAD
   cat CHANGELOG.md
   grep '^version' pyproject.toml   # ou a linha version em [project]
   ```

4. **Publicar artefatos** (quando for liberar no PyPI ou registry interno):

   ```bash
   uv build
   uv publish   # credenciais configuradas (token PyPI, etc.)
   ```

5. **Enviar** commit de bump e tag para o remoto:

   ```bash
   git push
   git push --tags
   ```

Resumo do fluxo:

```
alterações → git add → uv run cz commit → (várias vezes) → uv run cz bump → uv build → uv publish → git push --tags
```

Versão atual do pacote: **0.1.0** (`pyproject.toml`).

## Build e publicação (referência rápida)

```bash
uv build
uv publish
```

Use após o `cz bump`, quando a nova versão já estiver taggeada e validada.



### Módulos da biblioteca (`src/xploredev/`)

| Pacote | Arquivo | Responsabilidade |
|--------|---------|------------------|
| `io` | `xdv_file.py` | Pastas, JSON e persistência de `pandas` (Parquet, etc.) |
| `log` | `xdv_log.py` | Logging estruturado e perfil de ambiente em execuções |
| `utils` | `xdv_environment.py` | Localizar a raiz do projeto (`pyproject.toml`) |
| `utils` | `xds_memory.py` | Conversão e utilitários de memória |
| `environment` | `xdv_localhost.py` | Estrutura de pastas para runs locais |
| `lists` | `sorting.py` | Algoritmos de ordenação e knapsack (estudo) |