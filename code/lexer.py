
import sys
import re
import lexer
"""
        Author :: Sunil Kumar
        File :: lexer.py
Description ::
Lexer Parsing using Tokens
Object - (Token,Name,Meaning and special usage values)

"""

RESERVED = 'RESERVED'
INT      = 'INT'
ID       = 'ID'
Next    = 'NEXTLINE'
PARAM = "PARAM"
PARAMS = "PARAMS"

token_exprs = [
    (r'[ \t]+',              None,None,"","" ),
    (r'[\n]',              Next,Next ,"",""),
    (r'<{Start}>',             "START","START","",""), #start handler for start match
    (r'<{Ignore}>',            "IGNORE","IGNORE","",""),
    (r'<{ignore}>',            "IGNORE","IGNORE","",""),
    (r'<{///[0-9]+}>',         "IGLINE","","",""),
    (r'<{End}>',                   "END","END","",""),
    (r'<{DTTM}>',                   "DTTM","DTTM","",""),
    (r'<{///rep[0-9]+}>',          "REP","","",""),
    (r'<{///repEnd}>',          "REPEND","","",""),
    (r'<{Table}>',             "TABLE","","N",""),
    (r'<{TableA}>',             "TABLE","","A",""),
    (r'<{[0-9]+}{Table}>',             "TABLEFin","","",""),
    (r'<{Table<[-a-zA-Z0-9%_:,\s]+><[-a-zA-Z0-9%_\s]+>}>',             "TABLEDel","","",""),
    (r'<{<[-a-zA-Z0-9%_\s]+>}>',          PARAM,"","",""),
    (r'<{{[-a-zA-Z0-9%_:\s]+}<[-a-zA-Z0-9%_\s]+>}>',          "PARAM1","","",""),
    (r'<{<[-a-zA-Z0-9%_\s]+>{[-a-zA-Z0-9%_:\s]+}}>',          "PARAM2","","",""),
    (r'<{{[-a-zA-Z0-9%_:\s]+}<[-a-zA-Z0-9%_\s]+>{[-a-zA-Z0-9%_:\s]+}}>',          "PARAM3","","",""),
    (r'<{<[-a-zA-Z0-9%_\s]+><[-a-zA-Z0-9%_\s]+>}>',          PARAMS,"","",""),
    (r'<{{[-a-zA-Z0-9%_:\s]+}<[-a-zA-Z0-9%_\s]+><[-a-zA-Z0-9%_\s]+>}>',          "PARAMS1","","",""),
    (r'<{<[-a-zA-Z0-9%_\s]+><[-a-zA-Z0-9%_\s]+>{[-a-zA-Z0-9%_:\s]+}}>',          "PARAMS2","","",""),
    (r'<{{[-a-zA-Z0-9%_:\s]+}<[-a-zA-Z0-9%_\s]+><[-a-zA-Z0-9%_\s]+>{[-a-zA-Z0-9%_:\s]+}}>',          "PARAMS3","","",""),
    (r'<{TableFin}>',             "TABLEFIN","","",""),
    (r'<{TableEnd}>',           "TABLEEND","F","N",""),
    (r'<{TableEnd<T>}>',           "TABLEEND","T","N",""),
    (r'<{TableEnd<F>}>',           "TABLEEND","F","N",""),
    (r'<{TableEnd<T>}>',           "TABLEEND","T","N",""),
    (r'<{TableEnd<AT>}>',           "TABLEEND","T","A",""), #may need automatic from table tag not end tag
    (r'<{TableEnd<TA>}>',           "TABLEEND","T","A",""),
    (r'<{///n}>',           "IGLINES","IGLINES","",""),
    (r'<{CASE}>',           "CASESTART","CASESTART","",""),
    (r'<{CASEEND}>',        "CASEEND","CASEEND","",""),
    (r'<{HANDLE[0-9]+}>',   "HANDLER","","",""),
    (r'<{Save}>',           "SAVE","SAVE","",""),
    (r'<{Optional}>',         "Optional","Optional","",""),
    (r'<{OptionalEnd}>',         "OptionalEnd","OptionalEnd","",""),
    (r'<{DelStart<[-a-zA-Z0-9%_:,\s]+><[-a-zA-Z0-9%_\s]+>}>',             "DelStart","","",""), 
    (r'<{DelEnd}>', "DelEnd","","",""),
    # (r'\(',                    RESERVED),
    # (r'\)',                    RESERVED),
    # (r';',                     RESERVED),
    # (r'\+',                    RESERVED),
    # (r'-',                     RESERVED),
    # (r'\*',                    RESERVED),
    # (r'/',                     RESERVED),
    # (r'<=',                    RESERVED),
    # (r'<',                     RESERVED),
    # (r'>=',                    RESERVED),
    # (r'>',                     RESERVED),
    # (r'=',                     RESERVED),
    # (r'!=',                    RESERVED),
    # (r'and',                   RESERVED),
    # (r'or',                    RESERVED),
    # (r'not',                   RESERVED),
    # (r'if',                    RESERVED),
    # (r'then',                  RESERVED),
    # (r'else',                  RESERVED),
    # (r'while',                 RESERVED),
    # (r'do',                    RESERVED),
    # (r'[^\w\s*]+',                   RESERVED,"SPECIAL"),
    # (r'[0-9]+',                INT,"INT"),
    # (r'(<([^{]+))*[^\n<]+', "WORDS","WORDS","",""), 
    (r'[-a-zA-Z0-9%_:.!<>{}()*][^\n<{}]+', "WORDS","WORDS","",""), 

]

# [^(?!{).$]*

def lex(characters, token_exprs):
    """
        Lexing is done on rule files which is char array
        |
        |- PARAM - meaning - name
        |- PARAMS - meaning - (name,location) [-array]
        |- IGLINE - meaning - Number of lines
        |- REP - meaning - Number of repition
        |- TABLE - meaning - 10000000
        |- Hand;er - meaning - Case number

    """
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            # print(token_expr)

            pattern, tag,meaning,appendStart,appendEnd = token_expr
            try:
                regex = re.compile(pattern)
            except:
                sys.stderr.write("error occured in compile")
                sys.exit(-1)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                # print(text)
                if tag:
                    special = appendStart
                    if(tag == "PARAM"):
                        meaning = text[3:-3]
                        token = (text,tag,meaning,appendStart,appendEnd)
                        tokens.append(token)
                        # continue
                        break
                    elif tag == "PARAM1":
                        tag = "PARAM"
                        meaning = text[3:-3].split("}<")
                        appendStart = meaning[0]
                        meaning = meaning[1]
                        token = (text,tag,meaning,appendStart,appendEnd)
                        tokens.append(token)
                        break
                    elif tag == "PARAM2":
                        tag = "PARAM"
                        meaning = text[3:-3].split(">{")
                        appendEnd = meaning[1]
                        meaning = meaning[0]
                        token = (text,tag,meaning,appendStart,appendEnd)
                        tokens.append(token)
                        break

                    elif tag == "PARAM3":
                        tag = "PARAM"
                        meaning = text[3:-3].split("}<")
                        appendStart = meaning[0]
                        appendEnd = meaning[1].split(">{")[1]
                        meaning = meaning[1].split(">{")[0]
                        token = (text,tag,meaning,appendStart,appendEnd)
                        tokens.append(token)
                        break
                        # print(meaning)
                    if(tag == "PARAMS"):
                        meaning = text[3:-3].split("><")
                        token = (text,tag,meaning,appendStart,appendEnd)
                        tokens.append(token)
                        break
                    elif tag == "PARAMS1":
                        tag = "PARAMS"
                        meaning = text[3:-3].split("}<")
                        appendStart = meaning[0]
                        meaning = meaning[1].split("><")
                        token = (text,tag,meaning,appendStart,appendEnd)
                        tokens.append(token)
                        break
                    elif tag == "PARAMS2":
                        tag = "PARAMS"
                        meaning = text[3:-3].split(">{")
                        appendEnd = meaning[1]
                        meaning = meaning[0].split("><")
                        token = (text,tag,meaning,appendStart,appendEnd)
                        tokens.append(token)
                        break
                    elif tag == "PARAMS3":
                        tag = "PARAMS"
                        meaning = text[3:-3].split("}<")
                        appendStart = meaning[0]
                        appendEnd = meaning[1].split(">{")[1]
                        meaning = meaning[1].split(">{")[0].split("><")
                        token = (text,tag,meaning,appendStart,appendEnd)
                        tokens.append(token)
                        break
                        # print(text[3:-3],meaning)
                    elif tag == "IGLINE":
                        meaning = text[5:-2]
                    elif tag == "REP":
                        meaning = text[8:-2]
                    elif tag == "TABLE":
                        # ifinite rows as of now
                        tag = "REP"
                        meaning = "10000000"
                    elif tag == "TABLEFin":
                        tag = "REP"
                        meaning = text[2:-2].split("}{")[0]
                    elif tag == "TABLEDel":
                        tag = "DelStart"
                        meaning = text[8:-3].split("><")
                    elif tag == "HANDLER":
                        # print(text[8:-2])
                        meaning = text[8:-2]
                    elif tag == "DelStart":
                        meaning = text[11:-3].split("><")
                    # elif tag == "Table":
                    token = (text, tag,meaning,special)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character found near: %s\\' % characters[pos:])
            sys.exit(-1)
        else:
            pos = match.end(0)
    return tokens

def nokia_lex(characters):
    return lexer.lex(characters, token_exprs)
