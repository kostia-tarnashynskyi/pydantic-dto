init:
	uv sync --frozen --all-groups
	$(shell git config --unset-all core.hooksPath)
	uv run pre-commit install

pre-commit:
	uv run pre-commit run --all-files
