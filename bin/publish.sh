#!/bin/sh

python -m pip install --upgrade twine
python -m twine upload --username __token__ dist/*
