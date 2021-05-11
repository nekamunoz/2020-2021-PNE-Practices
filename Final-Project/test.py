import http.client
import json
import socketserver
import termcolor
import http.server
import jinja2
from urllib.parse import urlparse, parse_qs
import serverutils as su
import pathlib
dict_species = su.obtain_data("/info/assembly/cat")
print(dict_species)

print(dict_species["karyotype"])