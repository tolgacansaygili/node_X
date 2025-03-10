import random
from ..comfy.model import ComfyNode

class RandomPromptNode(ComfyNode):
    CATEGORY = "Custom"
    FUNCTION_NAME = "random_prompt"
    INPUTS = []
    OUTPUTS = ["STRING"]

    def execute(self, inputs):
        prompts = [
            "A stunning young woman with long, wavy golden hair, standing in a sunlit meadow...",
            "A breathtaking woman with voluminous, curly hair flowing in the wind...",
            "A mystical young woman with deep green eyes and long, wavy chestnut hair, standing in an enchanted forest...",
            "A mesmerizing young woman with platinum blonde hair, standing beneath the Northern Lights...",
            "A melancholic young woman with wet, tousled hair, standing under soft rain in an urban setting..."
        ]
        return [random.choice(prompts)]
