'''
@overdive the JSON object
add parameter "ensure_ascii=False" 
'''

from sqlalchemy.dialects.postgresql import JSON

class JSONUnicode(JSON):
	def __init__(self, none_as_null = False):
		JSON.__init__(self, none_as_null = none_as_null)

	def bind_process(self, dialect):
		json_serializer = json.dumps
		if util.py2k:
			encoding = dialect.encoding

			def process(value):
				if isinstance(value, elements.Null) or (
					value is None and self.none_as_null
				):
					return None
				return json_serializer(value, ensure_ascii=False).encode(encoding)
		else:
			def process(value):
				if isinstance(value, elements.Null) or (
					value is None and self.none_as_null
				):
					return None
				return json_serializer(value, ensure_ascii=False)
		return process