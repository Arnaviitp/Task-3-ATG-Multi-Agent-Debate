from logger_config import logger
import random

agent_a_persona = "Scientist"
agent_b_persona = "Philosopher"

agent_a_args = [
    "AI must be regulated due to high-risk applications.",
    "Like medicine, AI can have life-altering consequences.",
    "Unregulated AI may lead to unethical experimentation.",
    "Public trust is gained via strict regulations."
]

agent_b_args = [
    "Regulation could stifle philosophical progress and autonomy.",
    "Overregulation limits freedom of thought.",
    "Innovation in AI stems from fewer constraints.",
    "History shows overregulation delays societal evolution."
]

def generate_argument(agent_name, memory, round_num):
    used = [m['argument'] for m in memory if m['agent'] == agent_name]
    pool = agent_a_args if agent_name == agent_a_persona else agent_b_args
    available = list(set(pool) - set(used))
    argument = random.choice(available) if available else "[Repeated argument error]"
    logger.info(f"[Round {round_num+1}] {agent_name}: {argument}")
    return {"agent": agent_name, "round": round_num+1, "argument": argument}
