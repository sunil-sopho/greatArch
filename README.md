# greatArch
The project module involves developing a meta language to parse, execute and automate the running of any software. We use regex to parse the language
and break it into a set of executable instruction that are mostly use to run any software application such as web crawling, opening a browser,
sending request to other apps, opening an application, editing a file, saving a file and many more.
```

More importantly there are few major tasks we have to handle
-- A good regex parser to convert high level instructions to low level sub routines
-- Executing those sub-routines sequentially
-- Developing those sub-routines, few are listed here
----- Finding an Image
----- Clicking at a point
----- Saving/editing a file
----- Editing a text field etc.

```


## Softwares to be used and requirements

```
-- Python>=3.6
-- AutoHotKey
-- AHK module for python
-- Some basic python libraries such as numpy, tesseract
```

## Task Done
- [x] Lexure for regex done
- [x] AHK module for python found
- [ ] Permission issues is a problem
- [ ] FindText has to be made workable for all fonts and screens




# pipeline
```
-- Use lexer or something to
	|- parse the instructions to be executed
	|- validate the sequence of instruction
	|- getting errors / logging
-- Subroutines
	|- can execute different specialized tasks
	|- try different ways to solve those task. For example find image using AHK, then OCR, then something else
  |- generate error file to be able to show traceback
-- Subroutine communication
	|- calling one sub-routine from another
  |- sending data between two sub-routines



```
