"""
Eddy Int Seven Random - Pure random 7-resonant seed generator
Author: eddy
"""

import random

class EddyIntSevenRandomV2:
    """
    Random seed generator with strict 7-resonance formula constraint
    Formula: output = int((n*7)*1.15*10), max output ~1,000,000
    """
    
    MAX_N = 12173  # Max n to keep output <= 100000
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 0xffffffffffffffff,
                }),
            },
            "hidden": {
                "extra_pnginfo": "EXTRA_PNGINFO",
                "prompt": "PROMPT"
            },
        }
    
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("seed",)
    FUNCTION = "generate_seed"
    CATEGORY = "eddy"
    
    OUTPUT_NODE = True
    
    def generate_seed(self, seed, extra_pnginfo=None, prompt=None):
        """
        Random seed generator
        Formula: seed = int((n * 7) * 1.15 * 10)
        Constraint: n <= 12173, output <= ~1,000,000
        ComfyUI auto-adds control_after_generate for dynamic behavior
        """
        
        # Generate random n from seed
        random.seed(seed)
        n = random.randint(1, self.MAX_N)
        
        # Apply strict formula: (n * 7) * 1.15 * 10 (scaled by 10)
        seven_base = n * 7
        output_seed = int(seven_base * 1.15 * 10)
        
        # Safety check (should never trigger with MAX_N constraint)
        if output_seed > 1_000_000:
            output_seed = 1_000_000
            print(f"[WARNING] Output capped at 1000000 (n={n})")
        
        # Debug output
        print(f"[7-Resonant] Input seed: {seed} -> n={n} -> Output: {output_seed}")
        
        # CRITICAL: Verify what we're actually returning
        actual_return = (output_seed,)
        print(f"[7-Resonant] ACTUAL RETURN VALUE: {actual_return[0]} (type: {type(actual_return[0])})")
        
        return actual_return
    
    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("nan")  # Always regenerate when control_after_generate=randomize

# Node registration - only keep V2
NODE_CLASS_MAPPINGS = {
    "EddyIntSevenRandomV2": EddyIntSevenRandomV2,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EddyIntSevenRandomV2": "Int (7×1.15 Random)",
}
