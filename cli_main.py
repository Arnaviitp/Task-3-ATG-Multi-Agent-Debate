from debate_graph import debate_flow

if __name__ == "__main__":
    print("Multi-Agent Debate Simulator (LangGraph)")
    result = debate_flow()
    print("\n=== Final Summary ===")
    print(result["summary"])
    print(f"\n🏆 Winner: {result['winner']}")
    print(f"🔍 Reason: {result['reason']}")
