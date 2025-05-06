from fastapi import FastAPI, HTTPException
from agent.core import Agent

app = FastAPI(title="GenAI Agent API")
agent = Agent()

@app.get('/agent')
def query_agent(q: str):
    if not q:
        raise HTTPException(status_code=400, detail="Query parameter 'q' required")
    thoughts, action = agent.strategy.plan(q, agent.memory)
    tool, args = action
    result = agent.tools.get(tool, lambda *a: "Unknown tool").run(*args)
    agent.memory.add(q, result)
    return { 'thoughts': thoughts, 'action': action, 'result': result }
