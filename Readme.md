# extensions: #
.jhos (jhos file)
.jhosh (jhos header file)
<br>
# other #
very simple programming language
<br>
# 0.8 #
VERSION // version of JHOS
<br>
PI // π
<br>
RUN // only in the shell<br>
FUNCTION [name]<br>
MAIN // reserved name<br>
{}<br>
()<br>
FILE [nameOfFile/Var] [->/<-/<+/<v-/-v>] [var] // open file<br>
-> // read from file<br>
<- // write to file<br>
<+ // append to file<br>
<v- // write to file (the name of the file is in a variable)<br>
-v> // read from file (the name of the file is in a variable)<br>
USING [fileName] // import external file<br>
UNDEFINE [var] // remove variable<br>
if // if ([var/num] [EQUAL_TO/LESS_THAN/GREATER_THAN] [var/value]) (STR/VAR)<br>
(STR)<br>
(VAR)<br>
(NUM)<br>
(NULL)<br>
EQUAL_TO<br>
NOT_EQUAL_TO<br>
LESS_THAN<br>
GREATER_THAN<br>
SKIP // skip next line (yes, you need this to end an if statement. no work otherwise :skull:)<br>
LOOP // buggy as fuck<br>
DEFINE [name] as"[value/var]"(STR/NUM/NULL/VAR) // create variable<br>
REDEFINE [name] as"[value/var]"(STR/NUM/NULL/VAR) // redefine a variable<br>
SYS"[value/var]"(VAR/*) // execute a system command<br>
// comment<br>
// math<br>
ADD [var/value] [var/value] OUTPUT_TO:[var]<br>
SUBTRACT [var/value] [var/value] OUTPUT_TO:[var]<br>
MULTIPLY [var/value] [var/value] OUTPUT_TO:[var]<br>
DIVIDE [var/value] [var/value] OUTPUT_TO:[var]<br>
MODULO [var/value] [var/value] OUTPUT_TO:[var]<br>
COMPARE [var/value] [var/value] OUTPUT_TO:[var]<br>
INT [var/value] OUTPUT_TO:[var]<br>
IS [var/value] [EQUAL_TO/LESS_THAN/GREATER_THAN] [var/value] OUTPUT_TO:[var]<br>
GET_ITEM [x] OF [var] SPLIT_BY:[const string]<br>
CONCAT [var] AND [var]<br>
RANDOM [var/value] [var/value] OUTPUT_TO:[var]<br>
INPUT"[value/var]"[var]:(STR/NUM/VAR)<br>
PRINT "[value/var]" (STR/VAR)<br>
END_PROGRAM<br>
FUNCTION_CALL:[name of function]<br>
FC:[name of function]<br>
FUNCTION_CALL_IF:TRUE,T/FALSE,F:[name of function]<br>
FCIF:TRUE,T/FALSE,F:[name of function]<br>
PYTHON@[python code]@<br>
RETURN<br>

equal_to, less_than, greater_than and not_equal_to can be replaced by:
=, <, >, !=
