import logging

import llm_api

llm_logger = logging.getLogger("llm_api")
llm_logger.setLevel(logging.ERROR)

# Not smart enough
# LLM_API = llm_api.OllamaApi(model="llama3.1:8b", base_url="http://localhost:11434/v1")

# Too big / slow
# LLM_API = llm_api.OllamaApi(model="gemma2:27b", base_url="http://localhost:11434/v1")

# Hmm, potentially good
# LLM_API = llm_api.OllamaApi(model="solar-pro", base_url="http://localhost:11434/v1")

# Not smart enough
# LLM_API = llm_api.OllamaApi(model="phi3:14b", base_url="http://localhost:11434/v1")

# Potentially good
# LLM_API = llm_api.OllamaApi(model="gemma2:9b", base_url="http://localhost:11434/v1")

# Potentially good - blazingly fast!
LLM_API = llm_api.OllamaApi(model="qwen2.5:14b", base_url="http://localhost:11434/v1")

# Ollama doesn't use the full context - hack https://github.com/TheAiSingularity/graphrag-local-ollama/issues/24
# LLM_API = llm_api.OllamaApi(
#     model="qwen2.5-ctx-16k:14b", base_url="http://localhost:11434/v1"
# )

# Bad - did not notice the API key in .env
# LLM_API = llm_api.OllamaApi(model="llama3.2", base_url="http://localhost:11434/v1")


# LLM_API = llm_api.GroqApi(model="llama-3.1-70b-versatile")
