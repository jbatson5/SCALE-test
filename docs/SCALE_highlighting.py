from pygments.lexer import RegexLexer, bygroups, include, inherit, words
from pygments.style import Style
from pygments import token
################################################################################
def set_pygments_style(mod_name, cls):
    import sys
    import pygments.styles
    cls_name = cls.__name__
    mod = type(__import__("os"))(mod_name)
    setattr(mod, cls_name, cls)
    setattr(pygments.styles, mod_name, mod)
    sys.modules["pygments.styles." + mod_name] = mod
    from pygments.styles import STYLE_MAP
    STYLE_MAP[mod_name] = mod_name + "::" + cls_name
################################################################################
class ScaleStyle(Style):
    default_style = ""
    styles = {
        token.Comment: 'italic #008000',
        token.Number: 'bold #ff0000',
        token.Name: 'bold #0000FF',
        token.Name.Function: 'bold #000000',
        token.Text: 'bold #000000',
        token.String: 'italic #ff0000',
    }
################################################################################
class ScaleLexer(RegexLexer):
    name = 'Scale'
    aliases = ['scale']
    filenames = ['*.inp']

    tokens = {
        'root': [
            (r'^=.*\n', token.Name.Function),
            (r'^\'.*\n', token.Comment),
            (r'^\‘.*\n', token.Comment),
            (r'[ ]{1,}', token.Text),
            (r'\b(?i)(end([ ]{1,}|\n)end)\s\w+', token.Name,'block'),
            (r'\b(?i)(read|end)\s\w+', token.Name,'block'),
            (r'\b(?i)(end\s*$)', token.Name,'block'),
            (r'\b(?i)(location|cylgeometry|gridgeometry)\s', token.Name, 'block'),
            (r'\b(?i)(energybounds|timebounds)\s', token.Name, 'block'),
            (r'\b(?i)(response|distribution)\s', token.Name, 'block'),
            (r'\b(?i)(pointdetector|regiontally|meshtally)\s', token.Name, 'block'),
            (r'\b(?i)(src|meshsourcesaver)\s', token.Name, 'block'),
            (r'\b(?i)(importancemap|adjointsource|macromaterial)\s', token.Name, 'block'),
            (r'\b(?i)(fill)\s', token.Name, 'block'),
            (r'\b[0-9]+\s',token.Number),
            (r'([-+]?\d*\.?\d+)(?:[eE]([-+]?\d+))?\s',token.Number),
            (r'\"(.+?)\"', token.String),
            (r'\'(.+?)\'', token.String),
            (r'\”(.+?)\”', token.String),
            (r'\‘(.+?)\‘', token.String),
            (r'\“(.+?)\”', token.String),
            (r'\“(.+?)\"', token.String),
            (r'\”(.+?)\"', token.String),
            (r'\!.*\n', token.Comment),
            (r'(\w+|\n| )', token.Text),
            (r'(=|\-|\+|\%|\,|\‘|\$|\{|\}|\(|\)|\[|\]|\–|\_|\.|\…|\*|\,|\;|\:|\<|\>|\?|\/|\\)', token.Text),
            (r'\s+', token.Text),
            (r'.* ', token.Text)
        ],
        'block': [
            (r'(\n|[ ]{0,}\n)', token.Text,'#pop'),
            (r'[a-zA-Z]+\s', token.Name,'#pop'),
            (r'[0-9]+\s', token.Number,'#pop'),
            (r'\!.*\n', token.Comment,'#pop'),
            (r'.*\n', token.Text,'#pop'),
        ],
    }

################################################################################
def test():
    from pygments.styles import get_all_styles, STYLE_MAP
    styles = list(get_all_styles())
    print('style_maps: ', STYLE_MAP.keys())
    print('styles: ',styles)
################################################################################
if __name__ == "__main__":
    test()
################################################################################
