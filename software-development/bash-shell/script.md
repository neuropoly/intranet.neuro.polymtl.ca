# Script

## Tutorials/Links

[http://linuxconfig.org/bash-scripting-tutorial](http://linuxconfig.org/bash-scripting-tutorial)

[Bash scripting cheatsheet](https://devhints.io/bash)

## Creating a Script

First, create a file with the `*.sh` extension.

Next, open your script and put the following at the top:

```bash
#!/bin/bash
```

## Arrays

Create array from list of files

```bash
FILES=($(ls -r data*.*))
```

Use array \(just an example\)

```bash
${FILES[2]}
```

## Strings

**Get the first 2 characters of a string**

```bash
my_string="hola"
echo ${my_string:0:2}
```

**Get the last 2 characters of a string**

```bash
echo ${my_string: -2}
```

**Remove the first character of a string**

```bash
echo ${my_string:1}
```

**Remove the last 2 characters of a string**

```bash
echo ${my_string%??}
```

**Display the first line where a pattern is found \(here dim3\), and remove the first characters that matches a given string**

```bash
fslhd t1w.nii.gz | grep -m 1 dim3 | sed -e "s/^dim3           //"
```

**Batch actions with grep**

\`grep\` is powerful for creating an action based on a series of input \(e.g. multiple files\). Below is an example to delete several branches in git, based on their prefix name:

```bash
git branch -D `git branch | grep -E 'BRANCH_PREFIX*'`
```

**Check if substring is in string**

```bash
my_string='My long string'
if [[ $my_string == *"My long"* ]]; then
  echo "It's there!"
fi
```

More info here: [http://tldp.org/LDP/abs/html/string-manipulation.html](http://tldp.org/LDP/abs/html/string-manipulation.html)

## Dates

To list the date every week for the next five weeks, starting in 2 days:

```bash
for i in {1..5}; do echo $(date -v +${i}w -v +2d "+%Y-%m-%d"); done
```

## FOR Loop

**Loop across list elements**

```bash
ARRAY=(element1 element2 element3)
for i in ${ARRAY[@]}; do
  echo $i
done
```

**Loop across list elements \(using indices\)**

```bash
ARRAY=(element1 element2 element3)
for i in ${!ARRAY[@]}; do
  echo "Element: $((i+1))/${#ARRAY[@]}"
  echo ${ARRAY[$i]}
done
```

**Loop across a series of files**

```bash
for filename in im1 im2 im3 ; do
  bet $filename ${filename}_brain ;
done
```

**Using ls**

```bash
FILES=`ls folder/*.nii`
for file in $FILES; do
  echo $file
done
```

Do it in a single line:

```bash
FILES=`ls folder/*.nii`; for file in $FILES; do echo $file; done
```

**Using find \(recursive\)**

```bash
FILES=`find . -name *.nii`; for file in $FILES; do echo $file; done
```

**Using a list of string**

```bash
SUBJECT_LIST="subject_a subject_b"

for subject in $SUBJECT_LIST; do
  echo $subject
done
```

## IF Statements

### IF - AND

```bash
if [ ! -z "$var" ] && [ -e "$var" ]; then
  do something ...
else
  do something else...
fi
```

alternative:

```bash
[ ! -z "$var" -a  -e "$var" ]
```

### IF - OR

```bash
if [ ! -z "$var" ] || [ -e "$var" ]; then
  do something ...
fi
```

alternative:

```bash
[ ! -z "$var" -o  -e "$var" ]
```

## CSV Files

### Parse CSV File

```bash
while IFS=, read col1 col2 col3 col4 col5
  do
    echo "$col2"
  done < <FILE>.csv
```

## Command Line Input

```bash
#!/bin/bash
# use predefined variables to access passed arguments
# echo arguments to the shell
echo $1 $2 $3 ' -> echo $1 $2 $3'
# list all arguments:
echo $@
```

```bash
# We can also store arguments from bash command line in special array
args=("$@")
# echo arguments to the shell
echo ${args[0]} ${args[1]} ${args[2]} ' -> args=("$@"); echo ${args[0]} ${args[1]} ${args[2]}'
```

```bash
# use $@ to print out all arguments at once
echo $@ ' -> echo $@'
```

```bash
# use $# variable to print out number of arguments passed to the bash script
echo Number of arguments passed: $# ' -> echo Number of arguments passed: $#'  
```

also see: [Bash: parsing arguments with 'getopts'](https://www.neuro.polymtl.ca/tips_and_tricks/bash_parsing_arguments_with_getopts)

## Log Files

### Generate log file <a id="generate_log_file"></a>

```bash
LOGFILE=<FILE_NAME>.log
{
    # bash commands...
    
} 2>&1 | tee $LOGFILE
```

Generate a log file of a script directly in terminal:

```bash
script.$$ [options] | tee <FILE_NAME>.log
```

Add date to log file: log\_file\_name\_$\(date +%Y%m%d\).logEdit

## Colors

The Mountain Lion Terminal does not support the command `echo -e` therefore the following has to be used:

```bash
printf "\e[0;32mText here\e[0m"
```

### ANSI Escape Codes for Colours

| Colour | ANSI Escape Code |
| :--- | :--- |
| Black | 0;30 |
| Red | 0;31 |
| Green | 0;32 |
| Brown/Orange | 0;33 |
| Blue | 0;34 |
| Purple | 0;35 |
| Cyan | 0;36 |
| Light Grey | 0;37 |
| Yellow | 1;33 |
| White | 1;37 |
| No Colour | 0 |

```bash
BLACK='\033[0;30m'
RED='\033[0;31m'
NC='\033[0m'
```

## Misc

**Pass argument from file**

```bash
mycommand "$(< file.txt)"
```

**Test existence of a file**

```bash
if [ -e "$var" ]; then
```

