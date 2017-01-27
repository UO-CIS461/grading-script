#
#  Extract variable value from configuration file
#
#  Usage: python3 extract.py config_file variable_name
#  Prints value on standard output
#  
import sys 
import configparser

config = configparser.ConfigParser()
config.read(sys.argv[1])
val = config["DEFAULT"][sys.argv[2]]
print(val)
