#!/bin/bash
cd /home/kavia/workspace/code-generation/codequest-94803-a470f11f/devarena_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

