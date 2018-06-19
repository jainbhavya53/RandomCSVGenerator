import sys
import random
import string
import os
import ConfigParser

# TODO add support for boolean values
# TODO add support for default values in case of missing configuration parameters
# TODO validation on number of header equal to number of datatypes if header is specified
# TODO make header specification optional


''' METHODS '''


def rand_string(a, b):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in
                   range(random.randint(a, b)))


def rand_int(a, b):
    return str(random.randint(a, b))


def rand_float(a, b):
    return str(random.uniform(a, b))


def get_absolute_path(path):
    return os.path.abspath(path)


''''''

''' CHECK VARIABLES '''

datatypes = ["STRING", "INTEGER", "FLOAT"]
config_info = {
    'STRING PARAMETERS': ["STRING_LENGTH_MIN", "STRING_LENGTH_MAX"],
    'FLOAT PARAMETERS': ["FLOAT_MIN", "FLOAT_MAX"],
    'INTEGER PARAMETERS': ["INTEGER_MIN", "INTEGER_MAX"],
    'HEADER': ["HEADER", "HEADER_DATATYPES"]
}

''''''

''' config.ini VALIDATION '''
config = ConfigParser.ConfigParser()
config.read(get_absolute_path("config.ini"))

for k, v in config_info.items():
    if k in config.sections():
        for option in v:
            if string.lower(option) not in config.options(k):
                print "Check your config file"
                print "HEADER : %s , OPTION : %s is not a valid entry" % (k, option)
                sys.exit(1)
    else:
        print "Check your config file"
        print "HEADER : %s is not present in the config file" % (k)
''''''

''' RUN-TIME VARIABLES '''

STRING_LENGTH_MAX = int(config.get('STRING PARAMETERS', 'STRING_LENGTH_MAX'))
STRING_LENGTH_MIN = int(config.get('STRING PARAMETERS', 'STRING_LENGTH_MIN'))

FLOAT_MAX = float(config.get('FLOAT PARAMETERS', 'FLOAT_MAX'))
FLOAT_MIN = float(config.get('FLOAT PARAMETERS', 'FLOAT_MIN'))

INTEGER_MAX = long(config.get('INTEGER PARAMETERS', 'INTEGER_MAX'))
INTEGER_MIN = long(config.get('INTEGER PARAMETERS', 'INTEGER_MIN'))

HEADER = config.get('HEADER', 'HEADER')
HEADER_DATATYPES = config.get('HEADER', 'HEADER_DATATYPES')

''''''

''' COMMAND LINE ARGUMENTS VALIDATION '''
if len(sys.argv) != 3:
    print "Invalid Number of Arguments"
    sys.exit(1)

''''''

''' COMMAND LINE ARGUMENTS '''

# Number of records
num_records = long(sys.argv[1])
# separator of records
separator = str(sys.argv[2])

''''''

print "Header :-> "
print HEADER
print "Datatypes :-> "
print HEADER_DATATYPES

''' HEADER DATATYPE VALIDATION '''

header_datatype_split = HEADER_DATATYPES.split(separator)
header_split = HEADER.split(separator)

for head in header_datatype_split:
    line = string.upper(head)
    if line not in datatypes:
        print "Enter Valid Datatypes!!!!"
        sys.exit(1)

''''''

''' HEADER DATATYPE AND HEADER EQUALITY '''

if not (len(header_split) == len(header_datatype_split) and len(header_split) > 0):
    print "Number of Header Columns and Datatypes specified are not equal"

''''''

print "Generated Data :->"
print ""
print HEADER

for i in range(num_records):
    line = ""
    for j in header_datatype_split:
        value = ""
        if string.upper(j) == "STRING":
            value = rand_string(STRING_LENGTH_MIN, STRING_LENGTH_MAX)
        elif string.upper(j) == "INTEGER":
            value = rand_int(INTEGER_MIN, INTEGER_MAX)
        elif string.upper(j) == "FLOAT":
            value = rand_float(FLOAT_MIN, FLOAT_MAX)
        line = line + separator + value
    print line[len(separator):]