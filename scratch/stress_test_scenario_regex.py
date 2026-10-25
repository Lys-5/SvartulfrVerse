import re
import unittest

class TestRegexStress(unittest.TestCase):
    def test_plain_prefix_detection(self):
        text = '''=>Erik:
"Hello"
Erik: "Plain prefix"
=>Narrator:
Some narration
Edric Douglas: "Another plain"
Logan: In fondo
'''
        plain = re.findall(r'^(?!=>)([A-Z][a-zA-Z0-9_\' \-]+):\s*(?:\"|[A-Z])', text, flags=re.MULTILINE)
        plain = [p for p in plain if not p.startswith('=>')]
        self.assertEqual(plain, ['Erik', 'Edric Douglas', 'Logan'])

    def test_arrow_prefix_detection(self):
        text = '''=>Narrator:
Narration text
=>Erik:
"Dialogue"
=>Logan Járn Douglas:
"Dialogue 2"
=>Wulfnic:
"Dialogue 3"
'''
        tags = re.findall(r'^=>([A-Za-z0-9_]+):', text, flags=re.MULTILINE)
        self.assertEqual(tags, ['Narrator', 'Erik', 'Wulfnic'])
        # Logan Járn Douglas is NOT matched by [A-Za-z0-9_]+ because of spaces/accents!
        # Which is why short canonical tags without spaces are required!

if __name__ == '__main__':
    unittest.main()
