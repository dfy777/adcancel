from os import name
from typing import List
from configparser import ConfigParser

cf = ConfigParser()
cf.read("config.ini", "utf-8")
cf_map = dict(cf.items("base"))

TEMP_NAME = "nameTemplate"
TEMP_ERROR = "errorTemplate"
DEBUG = False


classNameList = list(cf_map["classnamelist"].replace(' ','').split(','))
idNameList = list(cf_map["idnamelist"].replace(' ','').split(','))

def generateJS(nameList : List[str], fileName : str) -> str:
    template = open(fileName,"r")
    r = template.read()
    result = ""

    for cnt in range(len(nameList)):
        content = r.replace(TEMP_NAME, nameList[cnt])
        if (DEBUG):
            content = content.replace(TEMP_ERROR, "alert(e);")
        else:
            content = content.replace(TEMP_ERROR, "")
        result += content + "\n\n"

    template.close()
    return result
    #print(start)
    


if __name__ == "__main__":

    start = "$(document).ready(function(){\n"
    end = "});"
    
    f = open("./js/adcancel.js", "w")
    classContent = generateJS(classNameList, "class.txt")
    idContent = generateJS(idNameList, "id.txt")
    start += classContent + "//    ========================\n" +idContent + end
    f.write(start)
    f.close()
    #print(start)