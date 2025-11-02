"""
Lucky Seed Node - Manual n input for 7-resonance
Formula: output = int((n * 7) * resonance_factor)
Author: eddy
"""

class EddyLuckySeedNode:
    """
    Strict 7-resonance transformer with formula constraint
    Formula: output = int((n * 7) * resonance_factor)
    Constraint: output <= 100000
    """
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        # Max n depends on resonance_factor
        # For 1.15: max n = 12173 (output ~98089)
        # For 2.0: max n = 7142 (output ~99988)
        return {
            "required": {
                "n": ("INT", {
                    "default": 957,
                    "min": 1,
                    "max": 12173,
                    "step": 1,
                    "tooltip": "n value, output = int((n*7)*resonance)"
                }),
                "resonance_factor": ("FLOAT", {
                    "default": 1.15,
                    "min": 1.0,
                    "max": 2.0,
                    "step": 0.01,
                    "tooltip": "Resonance multiplier (default 1.15)"
                }),
            }
        }
    
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("seed",)
    FUNCTION = "generate_lucky_seed"
    CATEGORY = "eddy/seeds"
    
    def generate_lucky_seed(self, n, resonance_factor=1.15):
        """
        Apply strict formula: output = int((n * 7) * resonance_factor)
        Constraint: output <= 100000
        """
        seven_base = n * 7
        lucky_seed = int(seven_base * resonance_factor)
        
        # Enforce 100000 limit
        if lucky_seed > 100000:
            lucky_seed = 100000
            print(f"[WARNING] Lucky seed capped at 100000 (n={n}, resonance={resonance_factor})")
        
        return (lucky_seed,)

# ComfyUI node registration - only keep main node
NODE_CLASS_MAPPINGS = {
    "EddyLuckySeedNode": EddyLuckySeedNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EddyLuckySeedNode": "Lucky Seed (7-Resonant)",
}
