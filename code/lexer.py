import sys
import re
import lexer
from exit import fault
"""
    Author :: Sunil Kumar
    File :: lexer.py
    Description ::
        Lexer Parsing using Tokens
        Object - (Token,Name,Meaning and special usage values)
"""

Next    = 'NEXTLINE'

tokenExprs = [
    (r'[ \t]+',              None,None,"","" ),
    (r'[\n]',              Next,Next ,"",""),
    (r'<mode>',             "MODE","mode setter","",""),
    (r'<{gui}>',             "GUI","GUI","",""), 
    (r'<{web}>',             "WEB","WEB","",""), 
    (r'<{ip}{[-a-zA-Z0-9%_.:\s]+}>', "IP","","",""), 
    (r'<findText>',             "findText","","",""), 
    (r'[-a-zA-Z0-9%_:,.!<>{}()*][^\n<{}]+', "WORDS","WORDS","",""),

]

def lex(characters, token_exprs):

    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for tokenExpr in tokenExprs:
            pattern, tag, meaning,sp1,sp2 = tokenExpr 
            try:
                regex = re.compile(pattern)
            except:
                fault("error with compile",-1)

            match = regex.match(characters,pos)
            if match:
                text = match.group(0)
                if tag:
                    special = ""
                    if tag == "MODE":
                        meaning = "setter"
                    elif tag == "IP":
                        meaning = text[5:-2]
                    elif tag == "WEB":
                        meaning = "WEB"
                    elif tag == "GUI":
                        meaning = "GUI"
                    elif tag == "NEXTLINE":
                        meaning = "NEXTLINE"
                    elif tag == "WORDS":
                        meaning = text
                    token = (text,tag,meaning,special)
                    tokens.append(token)
                    # print(tokenExpr," : ",pos," : ",match)
                break
        if not match:
            fault("Illegal pattern found near: "+characters[pos:]+" : "+str(pos),-1)
        else:
            pos = match.end(0)
    return tokens           

def lexerGrt(characters):
    return lexer.lex(characters, tokenExprs)
