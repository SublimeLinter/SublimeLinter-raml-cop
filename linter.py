from SublimeLinter.lint import Linter


class RamlCop(Linter):

    defaults = {
        "selector": "source.raml"
    }

    cmd = 'raml-cop --no-color --no-includes'

    regex = (
        r'^\[.+:(?P<line>\d+):(?P<col>\d+)\] '
        r'(?:(?P<error>ERROR)|(?P<warning>WARNING)) '
        r'(?P<message>.+)'
    )

    line_col_base = (0, 0)

    tempfile_suffix = '-'
