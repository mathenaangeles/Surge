import environ

env = environ.Env()
environ.Env.read_env()

# Azure Settings
azure_storage_account = env("AZURE_STORAGE_ACCOUNT")
azure_storage_container = env("AZURE_STORAGE_CONTAINER")
azure_search_service = env("AZURE_SEARCH_SERVICE")
azure_search_index = env("AZURE_SEARCH_INDEX")
azure_openai_service = env("AZURE_OPENAI_SERVICE")
azure_openai_chatgpt_deployment = env("AZURE_OPENAI_CHATGPT_DEPLOYMENT")
azure_openai_chatgpt_model = env("AZURE_OPENAI_CHATGPT_MODEL")
azure_openai_emb_deployment = env("AZURE_OPENAI_EMB_DEPLOYMENT")

# OPEN AI Keys
openai_key = env('API_KEY')
