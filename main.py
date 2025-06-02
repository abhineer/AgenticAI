from agent_router import run_agent

if __name__ == "__main__":
    query = input("Enter your query: ")
    result = run_agent(query)
    print("\n💡 Result:\n")
    print(result)
