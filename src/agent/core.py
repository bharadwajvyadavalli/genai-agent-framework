import logging
import sys
from agent.memory.faiss_memory import FaissMemory
from agent.prompt_strategy import PromptStrategy
from agent.tools.web_search import WebSearchTool
from agent.tools.calculator import CalculatorTool
from agent.tools.file_tool import FileTool
from dotenv import load_dotenv

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(name)s: %(message)s')
    return logging.getLogger(__name__)

class Agent:
    def __init__(self):
        load_dotenv()
        self.logger = setup_logging()
        # Initialize memory and tools
        self.memory = FaissMemory()
        self.tools = {
            'web_search': WebSearchTool(),
            'calc': CalculatorTool(),
            'file': FileTool()
        }
        self.strategy = PromptStrategy()

    def repl(self):
        self.logger.info("Starting agent REPL. Type 'exit' or Ctrl+C to quit.")
        try:
            while True:
                user_input = input("\n> ").strip()
                if not user_input or user_input.lower() == 'exit':
                    break

                # Reasoning
                thoughts, action = self.strategy.plan(user_input, self.memory)
                print(f"\n[Thoughts]\n{thoughts}\n")
                tool_name, args = action
                if tool_name not in self.tools:
                    print(f"Unknown tool: {tool_name}")
                    continue
                # Execute
                result = self.tools[tool_name].run(*args)
                print(f"[Result]\n{result}\n")
                # Memory
                self.memory.add(user_input, result)
        except KeyboardInterrupt:
            self.logger.info("Exiting REPL.")
            sys.exit(0)

if __name__ == '__main__':
    Agent().repl()
