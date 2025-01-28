from smolagents import CodeAgent, ToolCallingAgent, LiteLLMModel

####################### Ollama local #######################
model = LiteLLMModel(
    # model_id="ollama_chat/llama3.3", # too slow, only 70b, too big
    # model_id="ollama_chat/llama3.2", # 3b, perf bad, but ollama only has 1b/3b for this model
    # model_id="ollama_chat/qwen2.5:14b", # search tool cannot fetch webpage somehow ???
    # model_id="ollama_chat/llama3.1:8b", # 8b, perf barely ok
    model_id="ollama_chat/qwen2.5-coder:14b",
    api_base="http://127.0.0.1:11434",
    num_ctx=8192 # ollama default 2048 will fail horribly. 8192 works for easy tasks, more is better
)
agent = CodeAgent(
    tools=[], 
    add_base_tools=True,
    model=model, 
)
agent.run("Read and summarize the latest blog from HuggingFace and focus on the texts not the HTML formats") 