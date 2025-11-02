# API Configuration - Use environment variables in production
API_KEYS = {
    'openai': 'your_openai_key_here',
    'gemini': 'your_gemini_key_here', 
    'claude': 'your_claude_key_here'
}

# Experimental Parameters
EXPERIMENT_CONFIG = {
    'temperature': 0.7,
    'max_tokens': 1000,
    'repetitions': 5,
    'models': ['chatgpt-4', 'gemini-pro', 'claude-3-sonnet'],
    'delay_between_requests': 2
}
