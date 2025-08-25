init:
	uv sync --frozen --all-groups
	uv run pre-commit install

pre-commit:
	uv run pre-commit run --all-files
