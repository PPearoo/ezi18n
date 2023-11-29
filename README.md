[Github](https://github.com/PearooXD/ezi18n) | [PyPI](https://pypi.org/project/ezi18n/)

--------
## Setting up
 Start by downloading the package via pip.
 ```
 python3 -m pip install ezi18n
 ```

 After that, you can just import it into your file.

--------
## Examples
 ```py
 import ezi18n
 import random
 
 _ = ezi18n.Translator() # if you don't provide anything in the brackets, it will look for the file's name's language JSON file. If the main file is  main.py, it will look for main_lang.json - unless you provide a base filename (in this case: main) and/or a suffix (by default: _lang)
 dice = random.randint(1, 6)
 language = input("What's your native language? / Was ist Deine Muttersprache? (en/de) >>> ")
 
 print(_("dice_result", language, dice=dice))
 ```
 ```json
 {
    "en": {
        "dice_result": "Your dice rolled {dice}!"
    },
    "de": {
        "dice_result": "Dein Würfel hat eine {dice} gewürfelt!"
    }
 }
 ```

 

-------
## Working with plurals
 ```py
 import ezi18n
 import locale

 _ = ezi18n.Translator("main", "_plurals") # this will look for main_plurals.json as the language JSON file
 apples = int(input("How many apples do you have? >>> "))
 language = locale.getdefaultlocale()[:2] # this will return the default OS language, such as en, hu, de, fr, es etc.

 print(_.one("apples", language, apples=apples))
 ```
 ```json
 {
    "en": {
        "apples": ["You only have one apple! What a loser...", "You have {apples} apples!"]
    },
    "hu": {
        "apples": ["{apple} almád van!"]
    }
 }
 ```

 This example does a great job at presenting how the `.one()` function works. Here's the explanation for the code:

 The code will look for the default OS language, and will tell you how many apples you have with plurals in mind. I always get angry when I see "you have 1 apples"-ish text on a website, and it's an easy fix, but for some reason, many developers don't pay attention to it.

 Hungarian doesn't make a difference between plurals, so the list for "hu"/"apples" only has 1 item. This won't be a problem though - the library isn't hardcoded to only look for the first and second elements in the returned list, it will look for the **first** and the **last**. Which means that if a list only has 1 item, it will only return that item.