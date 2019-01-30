import re

fabric_area = {}

claims = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2'
]


# VALUE TO PARSE
# #123 @ 3,2: 5x4
parse_regex = '^\#(?P<elf_id>\d{1,10})\s\@\s(?P<x>\d{1,4})\,(?P<y>\d{1,4})\:\s(?P<dx>\d{1,4})x(?P<dy>\d{1,4})*$'
regex = re.compile(parse_regex)

def parse_claim(claim_request):
    regex_match = regex.match(claim_request)
    claim_raw = regex_match.groupdict()
    return {
        'elf_id': int(claim_raw['elf_id']),
        'x': int(claim_raw['x']),
        'y': int(claim_raw['y']),
        'dx': int(claim_raw['dx']),
        'dy': int(claim_raw['dy']),
    }


for claim_raw in claims:
    claim = parse_claim(claim_raw)
    for x in range(claim['x'], (claim['x'] + claim['dx'])):
        for y in range(claim['y'], (claim['y'] + claim['dy'])):
            fabric_area[ f'{x},{y}'] = ( 'X' if fabric_area.get( f'{x},{y}') else claim['elf_id'] )

print('have {} spaces with more than one request'.format(len(list(filter(lambda elf_id: elf_id == 'X', fabric_area.values())))))