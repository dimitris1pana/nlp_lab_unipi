# https://huggingface.co/Helsinki-NLP/opus-mt-zh-en


# translation_pipeline.py

from transformers import pipeline
import language_tool_python


class NLPTranslationPipeline:
    def __init__(self, source_lang='en', target_lang='fr', model_name=None):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.model_name = model_name or f'Helsinki-NLP/opus-mt-{source_lang}-{target_lang}'
        self.translator = pipeline("translation", model=self.model_name)
        self.tool = language_tool_python.LanguageTool(source_lang)

    def check_grammar(self, text):
        """Checks and returns grammar suggestions."""
        matches = self.tool.check(text)
        corrected_text = language_tool_python.utils.correct(text, matches)
        return corrected_text, matches

    def translate(self, text):
        """Translates the input text."""
        return self.translator(text)[0]['translation_text']

    def process(self, input_text):
        print(f"Original: {input_text}")
        corrected_text, _ = self.check_grammar(input_text)
        print(f"Grammar-corrected: {corrected_text}")
        translation = self.translate(corrected_text)
        print(f"Translation ({self.source_lang} → {self.target_lang}): {translation}")
        return translation



if __name__=="__main__":
    nlp_pipe = NLPTranslationPipeline(source_lang="en", target_lang="fr")
    example_text = "This is a test sentence with a error."
    nlp_pipe.process(example_text)
