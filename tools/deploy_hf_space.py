"""Deploys Toumi to a Hugging Face Space (bonus).

Usage (from business_bot/):
    hf auth login                                    # once, with a token that has write access
    python tools/deploy_hf_space.py <hf-username>/garliclo-toumi

Uploads only app.py, requirements.txt, me/ and assets/ (never .env), stores OPENAI_API_KEY from .env as an
encrypted Space secret, and keeps the team inbox hidden on the public app.
"""
import sys
from pathlib import Path

import gradio
from dotenv import dotenv_values
from huggingface_hub import HfApi

ROOT = Path(__file__).resolve().parent.parent

SPACE_README = f"""---
title: Garliclo Toumi
emoji: 🧄
colorFrom: yellow
colorTo: gray
sdk: gradio
sdk_version: {gradio.__version__}
app_file: app.py
pinned: false
short_description: Toumi, the AI assistant of Garliclo (air-peeled garlic)
---

# Toumi: Garliclo's assistant
Ask about Garliclo's air-peeled garlic, prices, delivery across Lebanon, or leave your details for a quote.
"""


def main() -> None:
    if len(sys.argv) != 2 or "/" not in sys.argv[1]:
        sys.exit("Usage: python tools/deploy_hf_space.py <hf-username>/<space-name>")
    repo_id = sys.argv[1]
    env = dotenv_values(ROOT / ".env")
    if not env.get("OPENAI_API_KEY"):
        sys.exit("OPENAI_API_KEY is missing from .env")

    api = HfApi()
    api.create_repo(repo_id, repo_type="space", space_sdk="gradio", exist_ok=True)
    api.upload_folder(folder_path=str(ROOT), repo_id=repo_id, repo_type="space",
                      allow_patterns=["app.py", "requirements.txt", "me/*", "assets/*"],
                      commit_message="Deploy Toumi")
    api.upload_file(path_or_fileobj=SPACE_README.encode("utf-8"), path_in_repo="README.md",
                    repo_id=repo_id, repo_type="space", commit_message="Space config")
    api.add_space_secret(repo_id, "OPENAI_API_KEY", env["OPENAI_API_KEY"])
    for key, value in {"LLM_PROVIDER": "openai", "SHOW_ADMIN_PANEL": "false",
                       "MAX_MESSAGES_PER_SESSION": "30", "MAX_TURNS_PER_DAY": "300"}.items():
        api.add_space_variable(repo_id, key, value)
    print(f"Deployed: https://huggingface.co/spaces/{repo_id}  (first build takes a few minutes)")


if __name__ == "__main__":
    main()
