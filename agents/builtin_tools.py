from langchain_community.tools import DuckDuckGoSearchResults, ShellTool

search_tool = DuckDuckGoSearchResults()

# results = search_tool.invoke("What is today's date?")

# print(results)

shell_tool = ShellTool()
print(shell_tool.invoke('whoami'))


print(search_tool.name)
print(search_tool.description)
print(search_tool.args)