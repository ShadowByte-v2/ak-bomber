
import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))