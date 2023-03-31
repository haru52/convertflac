.PHONY: dev-install lint lint-npm lint-text lint-yml lint-sh lint-action lint-py update-gi

dev-install:
	npm ci
	vale sync
	pipenv sync --dev

lint: lint-npm lint-text lint-yml lint-sh lint-action

lint-npm:
	npm run lint

lint-text:
	vale README.md docs/CONTRIBUTING.md docs/SECURITY.md .github/*.md .github/ISSUE_TEMPLATE

lint-yml:
	yamllint --strict .

lint-sh:
	shellcheck .husky/commit-msg .husky/pre-commit bin/*.sh

lint-action:
	actionlint

lint-py:
	pipenv run lint

update-gi:
	gibo update
	cat .gitignore_custom >| .gitignore
	gibo dump macOS Linux Windows VisualStudioCode JetBrains Vim Node Python >> .gitignore
