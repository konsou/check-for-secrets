import logging

import llm_api

llm_logger = logging.getLogger("llm_api")
llm_logger.setLevel(logging.ERROR)

LLM_API = llm_api.OllamaApi(model="llama3.1:8b", base_url="http://localhost:11434/v1")
