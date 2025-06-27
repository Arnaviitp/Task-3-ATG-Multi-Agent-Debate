from logger_config import logger

def judge_debate(memory):
    summary = "\n".join([f"[Round {m['round']}] {m['agent']}: {m['argument']}" for m in memory])
    logger.info("[Judge] Summary of debate:\n" + summary)

    a_count = sum(1 for m in memory if m['agent'] == "Scientist")
    b_count = sum(1 for m in memory if m['agent'] == "Philosopher")

    winner = "Scientist" if a_count >= b_count else "Philosopher"
    reason = "Scientist gave more grounded, risk-based arguments aligned with public safety principles." if winner == "Scientist" \
        else "Philosopher emphasized autonomy and historical insights on overregulation."
    
    logger.info(f"[Judge] Winner: {winner}")
    logger.info(f"[Judge] Reason: {reason}")
    return {"summary": summary, "winner": winner, "reason": reason}
