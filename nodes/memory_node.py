from logger_config import logger

def update_memory(memory, entry):
    memory.append(entry)
    logger.info(f"Memory updated: {entry}")
    return memory
