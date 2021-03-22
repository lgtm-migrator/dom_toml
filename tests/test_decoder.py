# stdlib
from textwrap import dedent

# 3rd party
from toml.decoder import InlineTableDict

# this package
from dom_toml import loads
from dom_toml.decoder import TomlPureDecoder


def test_decoder():

	config = dedent("""\
	[project]
	license = {file = "LICENSE"}
	""")

	data = loads(config)["project"]
	assert isinstance(data, dict)
	assert isinstance(data["license"], dict)
	assert isinstance(data["license"], InlineTableDict)

	data = loads(config, decoder=TomlPureDecoder)["project"]
	assert isinstance(data, dict)
	assert isinstance(data["license"], dict)
	assert not isinstance(data["license"], InlineTableDict)
