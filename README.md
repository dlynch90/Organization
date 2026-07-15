# Organization Project

## Repository Structure
This monorepo follows the [Next.js](https://nextjs.org/docs/basic-features/monorepo) monorepo architecture:
- `apps/`: Contains end-user applications and services
- `packages/`: Contains reusable libraries, modules, and components
- `.devcontainer/`: Dev container configuration

## Development
1. Install Docker Desktop
2. Build dev container:
   ```bash
   code --user-data-dir ~/.codecontainers .
   ```
3. Activate environment:
   ```bash
   source .venv/bin/activate
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r dev-requirements.txt

## Contributing
1. File issues in the `issues` branch
2. Create feature branches using:
   ```bash
   git checkout -b feature/<name>
3. Pull requests must be reviewed by at least 2 engineers

## Testing
1. Run unit tests:
   ```bash
   pytest tests/ -v
2. Run integration tests:
   ```bash
   playbook running/integration-tests

## Documentation
All documentation should reside in:
- `docs/`: Technical and API documentation
- `internal-docs/`: Internal team documentation

## Security
- Secrets managed via 1Password via MCP
- No direct hardcoding of secrets
- All access requires RBAC approval

## Compliance
[ ] All changes meet governance gates
[ ] All changes pass pre-commit hooks
[ ] All changes undergo peer review