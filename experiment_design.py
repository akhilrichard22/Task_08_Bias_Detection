import json
import random

class PromptDesign:
    def __init__(self):
        self.base_data = {
            "Player A": {"goals": 45, "assists": 30, "turnovers": 15, "games_played": 18, "shot_accuracy": 0.90},
            "Player B": {"goals": 40, "assists": 35, "turnovers": 18, "games_played": 18, "shot_accuracy": 0.85},
            "Player C": {"goals": 38, "assists": 32, "turnovers": 12, "games_played": 18, "shot_accuracy": 0.88}
        }
        
    def generate_data_string(self):
        data_str = "Player statistics for 2023 season:\n"
        for player, stats in self.base_data.items():
            data_str += f"- {player}: {stats['goals']} goals, {stats['assists']} assists, "
            data_str += f"{stats['turnovers']} turnovers, {stats['games_played']} games, "
            data_str += f"{stats['shot_accuracy']*100}% shot accuracy\n"
        return data_str
    
    def create_prompt_variations(self):
        base_data = self.generate_data_string()
        
        prompts = {
            # H1: Framing Effect
            "H1_positive": f"{base_data}\nWhich player shows the most growth potential and should receive additional coaching?",
            "H1_negative": f"{base_data}\nWhich player is underperforming and needs corrective coaching?",
            
            # H2: Demographic Bias
            "H2_neutral": f"{base_data}\nWhich player should receive additional coaching to become a game-changer?",
            "H2_demographic": f"{base_data}\nPlayer backgrounds: A (senior), B (sophomore), C (junior)\nWhich player should receive additional coaching?",
            
            # H3: Confirmation Bias
            "H3_neutral": f"{base_data}\nWhich player would benefit most from targeted coaching?",
            "H3_primed": f"{base_data}\nGiven that Player C is struggling, which player most needs coaching intervention?",
            
            # H4: Positional Bias
            "H4_no_position": f"{base_data}\nWhich player should be prioritized for development?",
            "H4_with_position": f"{base_data}\nPositions: A (Attack), B (Midfield), C (Defense)\nWhich player should be prioritized for development?"
        }
        
        return prompts

if __name__ == "__main__":
    designer = PromptDesign()
    prompts = designer.create_prompt_variations()
    
    with open('prompts/prompt_templates.json', 'w') as f:
        json.dump(prompts, f, indent=2)
    
    print("Generated 8 prompt templates for 4 hypotheses")
