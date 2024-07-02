import json
import logging
import os
from typing import Any, List, Optional
from sys import argv

class Translator:
    """Localize your apps easily and quickly."""
    def __init__(self, filename: Optional[str] = None, suffix: Optional[str] = "_lang") -> None:
        """
        Creates a new Translator object.
        
        -------
        ### Parameters:
            filename: `Optional[str]`
                The name of the file to load the translations from. The file must be in the same folder as this file.
                
                For example, if you want to load the translations from `main_lang.json`, you have to pass `main` as the filename.

                If not provided, it will use the name of the file that called this class.
            
            suffix: `Optional[str]` = "_lang"
                The suffix of the translation file. The default is "_lang", which means the translation file must be named `filename` + "_lang.json".
        
        -------
        ### Returns:
            `Translator`
                The newly created Translator object.
        """
        self.filename = filename or argv[0][:-3]
        try:
            with open(self.filename + suffix + ".json", "r", encoding="utf-8") as f:
                self.file = json.load(f)
        except:
            raise ValueError("No translation file found for {}".format(os.path.basename(self.filename)))
    
    def t(self, text: str, lang: str, **kwargs: Any) -> str | List[str]:
        """
        Gets the translation of a string like it's done in i18n.
        
        If `text` is not found in the translation file, or if there isn't a translation file, it returns `text` itself.
        
        -------
        ### Parameters:
            text: `str`
                The key to find in the translation file.
            lang: `str`
                The 2-letter language code of the language you want to translate to.
            **kwargs: `Any`
                The arguments to pass to the string formatter.
        
        -------
        ### Returns:
            `str`
                The translated string.
            `List[str]`
                If the translation is a list, it returns the list of translated strings.
        """
        translations = self.file.get(lang)
        if not translations:
            logging.error("No translations for language {}".format(lang))
            return text
        trans_text = translations.get(text)
        if trans_text:
            if isinstance(trans_text, list):
                return [i.format(**kwargs) for i in translations[text]]
            return translations[text].format(**kwargs)
        else:
            logging.error("Translation for \"{}\" not found for language {}".format(text, lang))
            return text
    
    translate = t
    
    def o(self, text: str, num: int | float, lang: str, **kwargs: Any) -> str:
        """
        Gets the singular and plural form of a string like it's done in i18n.
        
        For this, you need to have the key in the JSON be a list of two strings, the first being the singular form, the second being the plural form.
        
        -------
        ### Parameters:
            text: `str`
                The key to find in the translation file.
            lang: `str`
                The 2-letter language code of the language you want to translate to.
            num: `int` or `float`
                The number to decide which form to use.
            **kwargs: `Any`
                The arguments to pass to the string formatter.
                
        -------
        ### Returns:
            `str`
                If `num` is 1, returns the first item of the list.
                Otherwise, it returns the last item of the list.
                If the list only has 1 item, it returns that item.
        """
        trans = self.t(text, lang, **kwargs)
        if type(trans) == str:
            raise TypeError("Translation for \"{}\" is not a list".format(text))
        if num == 1:
            return trans[0] if trans else None
        else:
            return trans[-1] if trans else None
        
    one = o
    
    def __call__(self, text: str, lang: str, **kwargs) -> str:
        """
        Gets the translation of a string like it's done in i18n.
        
        If `text` is not found in the translation file, or if there isn't a translation file, it returns `text` itself.
        
        -------
        ### Parameters:
            text: `str`
                The key to find in the translation file.
            lang: `str`
                The 2-letter language code of the language you want to translate to.
            **kwargs: `Any`
                The arguments to pass to the string formatter.
        
        -------
        ### Returns:
            `str`
                The translated string.
        """
        return self.t(text, lang, **kwargs)