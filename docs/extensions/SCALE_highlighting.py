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
        token.Keyword: 'bold #005',
        token.Number: 'bold #ff0000',
        token.Name: 'bold #0000FF',
        token.Name.Function: 'bold #000000',
        token.Name.Class: 'bold #0f0',
        token.Text: 'bold',
        token.String: 'italic #ff0000',
    }
################################################################################
class ScaleLexer(RegexLexer):
    super
    name = 'Scale'
    aliases = ['scale']
    tokens = {
        'root': [
            (r'^=.*\n', token.Name.Function),
            (r'^\'.*\n', token.Comment),
            (r'\bread\b', token.Name,'block'),
            (r'\bend\b', token.Name, 'block'),
            (r'[0-9]',token.Number),
            (r'[\s=]+([+-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+))$',token.Number),
            (r'\"(.+?)\"', token.String),
            (r'\'(.+?)\'', token.String),
            ('\s+', token.Text)
        ],
        'block': [
            (r'[a-zA-Z]', token.Name),
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

