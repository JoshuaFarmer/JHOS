# extensions: #
.jhos (jhos file)
.jhosh (jhos header file)
# other #
very simple programming language

# 0.8 #
VERSION // version of JHOS
PI // π
RUN // only in the shell
FUNCTION [name]
MAIN // reserved name
{}
()
FILE [nameOfFile/Var] [->/<-/<+/<v-/-v>] [var] // open file
-> // read from file
<- // write to file
<+ // append to file
<v- // write to file (the name of the file is in a variable)
-v> // read from file (the name of the file is in a variable)
USING [fileName] // import external file
UNDEFINE [var] // remove variable
if // if ([var/num] [EQUAL_TO/LESS_THAN/GREATER_THAN] [var/value]) (STR/VAR)
(STR)
(VAR)
(NUM)
(NULL)
EQUAL_TO
NOT_EQUAL_TO
LESS_THAN
GREATER_THAN
SKIP // skip next line (yes, you need this to end an if statement. no work otherwise :skull:)
LOOP // buggy as fuck
DEFINE [name] as"[value/var]"(STR/NUM/NULL/VAR) // create variable
REDEFINE [name] as"[value/var]"(STR/NUM/NULL/VAR) // redefine a variable
SYS"[value/var]"(VAR/*) // execute a system command
// comment
// math
ADD [var/value] [var/value] OUTPUT_TO:[var]
SUBTRACT [var/value] [var/value] OUTPUT_TO:[var]
MULTIPLY [var/value] [var/value] OUTPUT_TO:[var]
DIVIDE [var/value] [var/value] OUTPUT_TO:[var]
MODULO [var/value] [var/value] OUTPUT_TO:[var]
COMPARE [var/value] [var/value] OUTPUT_TO:[var]
INT [var/value] OUTPUT_TO:[var]
IS [var/value] [EQUAL_TO/LESS_THAN/GREATER_THAN] [var/value] OUTPUT_TO:[var]
GET_ITEM [x] OF [var] SPLIT_BY:[const string]
CONCAT [var] AND [var]
RANDOM [var/value] [var/value] OUTPUT_TO:[var]
INPUT"[value/var]"[var]:(STR/NUM/VAR)
PRINT "[value/var]" (STR/VAR)
END_PROGRAM
FUNCTION_CALL:[name of function]
FC:[name of function]
FUNCTION_CALL_IF:TRUE,T/FALSE,F:[name of function]
FCIF:TRUE,T/FALSE,F:[name of function]
PYTHON@[python code]@
RETURN