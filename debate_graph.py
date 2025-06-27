from langgraph.graph import StateGraph, END
from nodes.user_input_node import get_debate_topic
from nodes.agent_node import generate_argument, agent_a_persona, agent_b_persona
from nodes.memory_node import update_memory
from nodes.judge_node import judge_debate

def debate_flow():
    state = get_debate_topic()
    
    while state["round"] < 8:
        agent = agent_a_persona if state["agent_a_turn"] else agent_b_persona
        arg = generate_argument(agent, state["memory"], state["round"])
        state["memory"] = update_memory(state["memory"], arg)
        state["round"] += 1
        state["agent_a_turn"] = not state["agent_a_turn"]

    judgment = judge_debate(state["memory"])
    return judgment
