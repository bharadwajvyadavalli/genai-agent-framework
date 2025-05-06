from openai import OpenAI
import os

class PromptStrategy:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def plan(self, user_input, memory) -> tuple:
        # Retrieve top-3 memory
        past = memory.query(user_input, k=3)
        prompt = self._build_prompt(user_input, past)
        resp = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{'role':'system','content':'You are an autonomous agent.'},
                      {'role':'user','content':prompt}]
        )
        text = resp.choices[0].message.content
        # Expect response like: THOUGHTS:...||ACTION: tool,arg1,arg2
        try:
            thoughts, action_line = text.split('||')
            _, thoughts = thoughts.split(':',1)
            _, action = action_line.split(':',1)
            tool_name, *args = [a.strip() for a in action.split(',')]
            return thoughts.strip(), (tool_name, args)
        except:
            # fallback: search
            return text, ('web_search', [user_input])

    def _build_prompt(self, query, memories):
        mem_text = "\n".join(f"- {m}" for m in memories)
        return (
            f"Past relevant memory:\n{mem_text}\n"
            f"\nUser query: {query}\n"
            "Plan your thoughts, then pick an ACTION in format: TOOL,ARG1,ARG2. Separate THOUGHTS and ACTION with '||'."
        )
