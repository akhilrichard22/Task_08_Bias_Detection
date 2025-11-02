import json
import time
import random
from openai import OpenAI
import google.generativeai as genai
from anthropic import Anthropic
from config import API_KEYS

class ExperimentRunner:
    def __init__(self):
        self.setup_apis()
        self.responses = []
        
    def setup_apis(self):
        # OpenAI ChatGPT
        self.openai_client = OpenAI(api_key=API_KEYS['openai'])
        
        # Google Gemini
        genai.configure(api_key=API_KEYS['gemini'])
        self.gemini_model = genai.GenerativeModel('gemini-pro')
        
        # Anthropic Claude
        self.claude_client = Anthropic(api_key=API_KEYS['claude'])
    
    def query_openai(self, prompt, repetition):
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            return {
                "model": "chatgpt-4",
                "prompt": prompt,
                "response": response.choices[0].message.content,
                "repetition": repetition,
                "timestamp": time.time()
            }
        except Exception as e:
            return {"error": str(e)}
    
    def query_gemini(self, prompt, repetition):
        try:
            response = self.gemini_model.generate_content(prompt)
            return {
                "model": "gemini-pro",
                "prompt": prompt,
                "response": response.text,
                "repetition": repetition,
                "timestamp": time.time()
            }
        except Exception as e:
            return {"error": str(e)}
    
    def query_claude(self, prompt, repetition):
        try:
            response = self.claude_client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1000,
                temperature=0.7,
                messages=[{"role": "user", "content": prompt}]
            )
            return {
                "model": "claude-3-sonnet",
                "prompt": prompt,
                "response": response.content[0].text,
                "repetition": repetition,
                "timestamp": time.time()
            }
        except Exception as e:
            return {"error": str(e)}
    
    def run_experiment(self):
        with open('prompts/prompt_templates.json', 'r') as f:
            prompts = json.load(f)
        
        models = [self.query_openai, self.query_gemini, self.query_claude]
        
        for prompt_id, prompt_text in prompts.items():
            for model_func in models:
                for repetition in range(5):
                    print(f"Running {prompt_id} with {model_func.__name__} rep {repetition}")
                    
                    result = model_func(prompt_text, repetition)
                    result['prompt_id'] = prompt_id
                    self.responses.append(result)
                    
                    # Rate limiting
                    time.sleep(2)
        
        # Save results
        with open('data/raw_responses.json', 'w') as f:
            json.dump(self.responses, f, indent=2)

if __name__ == "__main__":
    runner = ExperimentRunner()
    runner.run_experiment()
