# Traductor-Auto-LandOfSika

A tool to translate all the XML files language of the mod project **The Land Of Sika** by translating with an API Translator
Translate also the sentence with dynamic variables as {PLAYER.NAME} without changing the meaning of the sentence.

**The tool is now released !**

## How it works ?

This tool make possible to translate a all XML file from a language to another. I create an XML Manager LandOfSika, that is able to do some operations on the XML files precisely for the XML Languages file of the projet TheLandOfSika. But you could do your own XML Manager to treat any other custom XML File, by making an Inheritance
from the XML Manager class. (All of that will be explain in details later in a documentation for developers who want to extend the project for their own xml file)

Thus, it use by default the module DeepL to make the request for the translation. I will implement later a module for GoogleTranslate if needed, and as the same thing from the XML Manager, you could do your own module translation.

### Dynamic variable as overview

The tool is not just translating the XML File , I integrated a recognization of dynamic variable for the XmlManager Land of Sika. It will ask you to give a value for each one when you use the program, to be able to keep a meaning of the translation. For example, the line

```xml
<string id="TWOCstrAnm001" text="{PLAYER.NAME},you try to escape the darkness" />
 ```

will be translated as 

```xml
<string id="TWOCstrAnm001" text="{PLAYER.NAME}, vous essayez d'échapper à l'obscurité" />
```

All of this is possible because you have fill a meaning for the {PLAYER.NAME} during the execution of the program (don't worry you will be guide during the use of this last one)
Thus, all the meaning you give for dynamic variables are store in a file , and the program detect them and propose you to automoatically use them to continue the translation

### Multithreading

I implemented threads and multithreading to improve the execution time of the translations. For DeepL, I made a pool of 10 threads, and was able to improve the execution time from 3-4 minutes to 20 seconds. It will depend on the module you use, and I will integrated this notion in the module class later, but for now feel free to change the variable `CONCURRENCY = 10` (by default). But be careful, for DeepL the limit is 10 traductions in the same time.



## Install the project

You should have at least `**poetry**` and `**git**` install, the project is install to a virtual env automatically.

First, clone the project to the directory you want.

```bash
git clone https://github.com/thomas-soutif/Traductor-Auto-LandOfSika.git
```

Then, install the project dependancies and the virtual env with poetry

```
poetry install
```

Verify your virtual environnement

```
poetry env info
```
If you need to activate it, if you are on Windows:

```cmd
C:\Users\tombo\AppData\Local\pypoetry\Cache\virtualenvs\[your virtualenv created]\activate
```
On Linux :
```bash
source [Path of the bin virtual env]
```
## Translate your first xml file with DeepL (example for French language)

Go to the project directory, and run :
```python
python translate_xml_file.py --file_path={Your XML File Path} --target_language="FRENCH" --module_api="DEEPL" --file_name_destination="{Your file name destination path}"
```
- **file_path** : Should be the xml file path (with the .xml) include
- **target_language** : One of the following list ` ['FRENCH', 'ENGLISH', 'SPANISH', 'RUSSIAN', 'GERMAN', 'FINNISH', 'ITALIAN', 'DUTCH', 'POLISH', 'TURKISH', 'SWEDISH', 'BULGARIAN', 'GREEK', 'CZECH']`. If nothing specify the default value use will be English
- **module_api** : For now, only DEEPL supported
- **file_name_destination** : The path (with the .xml) where you want to store the new xml file. By default, it will use the file_path and add "-COPY-{target_language}"

Warning : Not all language available give a good result, especially for the languages that are not roman (like GREEK), I didn't test all of them yet

### Get your DeepL API Key
You will need an api key to run the project, go to the https://www.deepl.com/en/pro-api website, and create your account for free (You will have a limit of 500 000 characters per month, not enough tro translate all the mod, but a part of it)

Then, store your API KEY to the .env file as the variable `KEY_DEEPL_API`
