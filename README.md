# 🧄 Garliclo Business Assistant — "Toumi"

**EECE 503P/798S: Agentic Systems — C3: Introduction to Agents**

▶️ **[Demo video](https://youtu.be/kFykLcy0tM4)**

Toumi is the AI assistant of **Garliclo | Nader Garlic**, a Lebanese air-peeled garlic supplier founded in 1980 by
Joseph Nader. It answers questions from the business profile, routes every message, collects leads, and logs feedback
and unanswered questions through tool calls, in a branded Gradio app.

## Submission checklist

| Requirement | Where |
|---|---|
| `business_summary.txt`, `about_business.pdf` | [`me/`](me/) |
| `business_agent.ipynb` | [`business_agent.ipynb`](business_agent.ipynb) (executed, with outputs) |
| Persona and instructions | Notebook §2: `PERSONA` and `INSTRUCTIONS` blocks |
| Router | Notebook §3: LLM classifier (general question / lead / feedback) + keyword fallback |
| Two tools | Notebook §4: `record_customer_interest(email, name, message)`, `record_feedback(question)`, MCP-style schemas |
| System prompt + agent loop | Notebook §5–6: summary + PDF in the prompt, chat history, tool calls |
| Gradio `ChatInterface` | Notebook §7, [`app.py`](app.py) |
| API key in `.env` (not uploaded) | [`.gitignore`](.gitignore), template in [`.env.example`](.env.example) |
| ⭐ Bonus: reflection | Notebook §8: draft and revised replies logged to the console, `logs/` and the UI |
| Evaluation | Notebook §9: 15-message test set, **15/15 passed** |

## How it works

```
message → Router (gpt-4.1-nano) → Agent (gpt-4.1-mini + route's tools) → Reflection → reply
                                    ⇄ record_customer_interest / record_feedback → console + logs/*.jsonl
```

* **Router:** classifies each message; messages with an email go straight to lead collection.
* **Agent:** persona, instructions, business summary and PDF in the system prompt, the last 10 exchanges as
  short-term memory, and only the tools of the chosen route.
* **Reflection:** checks the draft for invented facts, missing contact requests, and wrong language before sending.
  It also logs any unanswered question the agent forgot to log.
* Runs on OpenAI by default, or on Gemini with `LLM_PROVIDER=gemini`.

## Run it

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env      # add your OPENAI_API_KEY
python app.py               # or open business_agent.ipynb and Run All
```

Set `SHOW_ADMIN_PANEL=true` in `.env` to see the **Team inbox** tab with logged leads and feedback.

## Business information

Sources: [@garliclo.lb](https://www.instagram.com/garliclo.lb/),
[Factories in Lebanon](https://factoriesinlebanon.com/acadp_listings/garliclo-nader-garlic/), Garliclo's logo and
price list, and the business owner. Assumed: the delivery fee table, pack sizes, shelf life, payment method names, and
the mission/vision wording.
