import re

# VALUE TO PARSE
#123 @ 3,2: 5x4
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