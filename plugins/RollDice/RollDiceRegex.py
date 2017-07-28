import re

class RollRegex(object):
    """This is the interface for the Roll Plugins Regex"""
    def __init__(self):
        super(RollRegex, self).__init__()
        self.regex = re.compile(ur'^roll\s\d+[d]\d+\s[+]\s\d+|^roll\d+[d]\d+\s[+]\s\d+|^roll\s\d+[d]\d+[+]\s\d+|^roll\s\d+[d]\d+\s[+]\d+|^roll\d+[d]\d+[+]\s\d+|^roll\d+[d]\d+\s[+]\d+|^roll\s\d+[d]\d+[+]\d+|^roll\d+[d]\d+[+]\d+', re.MULTILINE | re.IGNORECASE)

    def get(self):
        return self.regex

    def test(self, testString):
        matches = re.findall(self.regex, testString)
        return ((len(matches) > 0), matches)
