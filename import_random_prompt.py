import random
class RandomPrompt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompts": ("STRING", {"default": "Bir kış manzarasında kadın, karlı bir ormanda adam, sıcak bir yaz günü sahilde kişi"})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "select_random_prompt"

    def select_random_prompt(self, prompts):
        prompt_list = prompts.split(";")  # ";" ile ayırarak prompt'ları liste yap
        selected_prompt = random.choice(prompt_list)
        return (selected_prompt,)

NODE_CLASS_MAPPINGS = {
    "RandomPrompt": RandomPrompt
}
