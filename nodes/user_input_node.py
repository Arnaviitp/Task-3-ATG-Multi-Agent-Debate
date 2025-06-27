def get_debate_topic():
    topic = input("Enter topic for debate: ")
    return {"topic": topic, "round": 0, "memory": [], "agent_a_turn": True}
