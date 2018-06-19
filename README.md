# RandomCSVGenerator
This will allow you
to generate Random CSV Records with custom separator and header datatypes. You can also configure parameters for each datatype.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites
```
1. Python 2.7 or higher
2. RandomCSVGenerator Project
```
### Installations
#### 1. Installing Python 2.7
You can use this website to download and install python depending on the type of OS you are using :->
```
https://www.python.org/downloads/
```
#### 2. Cloning RandomCSVGenerator Project
Run the following command to clone this repository :->
```
git clone https://github.com/jainbhavya53/RandomCSVGenerator.git
```
## Configuring parameters for Data Generation
Editing the ```config.ini``` file will allow us to configure the parameters for data generation.
Curently supported datatypes are :

* String
* Float
* Integer

Contents of config.ini file :->
```
[STRING PARAMETERS]
STRING_LENGTH_MIN = 0
STRING_LENGTH_MAX = 10

[FLOAT PARAMETERS]
FLOAT_MIN = -1000
FLOAT_MAX = 1000

[INTEGER PARAMETERS]
INTEGER_MIN = -10
INTEGER_MAX = 10

[HEADER]
#Column Header and Datatypes should be delimited by the same "separator" as expected in generated data 
HEADER = column_1,column_2,column_3,column_4
#Supported Datatypes are:->
#1.String
#2.Float
#3.Integer
HEADER_DATATYPES = INTEGER,STRING,FLOAT,STring
```
You can configure these parameters according to your requirement.
## Generating Data
Command for generating data
```
python data_generation_csv_generic.py <N> <SEPARATOR>
```
where ```N``` is the number of records and ```SEPARATOR``` is the delimiter

## Example 
```
python data_generation_csv_generic.py 10 ,
```
The above command with datatypes parameters specified in sample config.ini file generates the following output:->
```
Header :->
column_1,column_2,column_3,column_4
Datatypes :->
INTEGER,STRING,FLOAT,STring
Generated Data :->

column_1,column_2,column_3,column_4
9,3k,-540.450594417,S
10,xT1FWfdmYk,-916.543448779,GGk
-6,EW,980.341087103,6F2HNP
8,Kv1Cy,-845.540112675,9U3lVN9PRe
10,aiJrRv05K,850.752687729,helLsESDua
-7,nzStZPk,266.884379839,hGiqb3rpw
-10,D81c,-5.3958294684,A58n
0,S,805.145195425,HrOD
-4,6v3rB0zUc,-748.117901443,8aQU8lu1
6,nj,-184.882332682,1sRgiMimlo
```
#### Note
Header and Header_Datatypes specified in config.ini should contain the same delimiter as that of ```SEPARATOR```.
