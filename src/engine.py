import json
import os
from security import ThreatAnalyzer

class ThreatEngine:
    def __init__(self, scenario_file="data/scenarios.json"):
        with open(scenario_file, "r") as f:
            self.data = json.load(f)
        self.current_node = self.data["start_node"]
        self.score = 0
        self.analyzer = ThreatAnalyzer()

    def run(self):
        print("\n" + "=" * 55)
        print("   THE SPRAWL: INTERACTIVE THREAT MODELING ENGINE")
        print("=" * 55)

        while True:
            scene = self.data["scenes"].get(self.current_node)
            if not scene:
                print("\n[END OF SIMULATION]")
                break

            print(f"\n--- {scene['title']} ---")
            print(scene["dialogue"])

            choices = scene.get("choices", [])
            if not choices:
                print("\n[SIMULATION CONCLUDED]")
                break

            print("\nSelect your response:")
            for idx, choice in enumerate(choices, 1):
                print(f" [{idx}] {choice['text']}")

            user_choice = input("\nChoice > ").strip()
            
            if not user_choice.isdigit() or int(user_choice) < 1 or int(user_choice) > len(choices):
                print("Invalid input! Cyber-deck glitched. Choose a valid option number.")
                continue

            selected = choices[int(user_choice) - 1]
            if selected.get("is_correct"):
                print("\n[SUCCESS] Threat accurately identified!")
                self.score += 100
            else:
                print("\n[WARNING] Threat miscalculated!")

            self.current_node = selected["next_node"]

        print(f"\nFinal Security Score: {self.score} PTS\n")
