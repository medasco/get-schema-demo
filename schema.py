import json 
from pprint import pprint

def get_schema(model_name):
    ddict = None

    with open(model_name, 'r') as file:
        ddict = json.load(file)
    
    ddict = ddict['components']['schemas']
    for akey, aval in ddict.items():
        # check schema has attribute: 'properties'
        if 'properties' in aval:
            # if properties check ref link
            for bkey, bval in aval['properties'].items():
                if '$ref' in bval:
                    # if ref links matched schema, get shema
                    link_keys = bval['$ref'].rsplit('/', 1)[1]
                    # schema sub to ref link
                    ddict[akey]['properties'][bkey] = ddict[link_keys]
            
                if 'items' in bval:
                    # if ref links matched schema, get shema
                    link_keys = bval['items']['$ref'].rsplit('/', 1)[1]
                    # schema sub to ref link
                    ddict[akey]['properties'][bkey]['items'] = ddict[link_keys]
            

    with open('schema.json', 'w') as f:
        json.dump(ddict, f, indent=2)


if __name__ == "__main__":
    jfile = 'Challenge2 Open API(1).json'
    get_schema(jfile)
    