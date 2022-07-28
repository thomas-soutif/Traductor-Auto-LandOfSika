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
You will need an api key to run the project, go to the https://www.deepl.com/en/pro-api website, and create your account for free

Then, store your API KEY to the .env file as the variable `KEY_DEEPL_API`

## Script I've made to translate all xml file of the mod (powershell version)

- Creation of the file `example_script_to_translate_all_xml_file.ps1`

``` powershell
$source_lang = $args[0]
$destination_lang = $args[1]
$path = $args[2]


Get-ChildItem -Path $path -Filter *.xml -Recurse -File| Sort-Object Length -Descending | ForEach-Object {
    $full_path_file = $_.FullName
    $full_path_file_new_xml_file = $full_path_file.replace($source_lang,$destination_lang)
    #write($full_path_file_new_xml_file)
    try{
        $sent ='Translate the file ' + $full_path_file + " ? [y or n]"
        $response = Read-Host $sent
        if( $response -eq "y"){
            New-Item -ItemType File -Path $full_path_file_new_xml_file -Force
            python translate_xml_file.py --file_path=$full_path_file --target_language="FRENCH" --module_api="DEEPL" --file_name_destination=$full_path_file_new_xml_file
        }else{
            $b = Test-Path $full_path_file_new_xml_file
            if($b){

            }else{
                New-Item -ItemType File -Path $full_path_file_new_xml_file -Force
                Copy-Item $full_path_file -Destination $full_path_file_new_xml_file
            }
        }
    }
    catch{

    }
}
```
- Execute the powershell file `example_script_to_translate_all_xml_file.ps1`

``` powershell
.\example_script_to_translate_all_xml_file.ps1 "EN" "FR" .\LanguagesXmlFiles\ 
```

Explanations : This script will list all of the xml files and ask you if you want to translate it. It will create a new direcory with the new files translated
Here, the xml files sources we try to translate are in the subfolder EN/ , and the new folder that will be create is the subfolder FR/

- This is a screen shot of what you got **before** executing this script :
- 
![image](https://user-images.githubusercontent.com/23268707/181644506-7a4f586e-63fa-4170-b54a-9834eadd4add.png)

- **After** executing this script

![image](https://user-images.githubusercontent.com/23268707/181644610-b27bd795-4a3e-439f-832a-b8f6c4e76625.png)


