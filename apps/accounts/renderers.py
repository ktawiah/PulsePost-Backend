import json

from rest_framework.renderers import JSONRenderer


class AccountsRenderer(JSONRenderer):
    charset = "utf-8"
    SHORT_SEPARATORS = (",", ":")
    LONG_SEPARATORS = (", ", ": ")
    INDENT_SEPARATORS = (",", ": ")

    def render(
        self,
        data,
        accepted_media_type=None,
        renderer_context=None,
    ):
        """Render `data` into JSON, returning a bytestring."""
        if data is None:
            return b""

        renderer_context = renderer_context or {}
        indent = self.get_indent(accepted_media_type, renderer_context)

        if indent is None:
            separators = self.SHORT_SEPARATORS if self.compact else self.LONG_SEPARATORS
        else:
            separators = self.INDENT_SEPARATORS

        if "ErrorDetail" in str(data):
            ret = json.dumps(
                obj={"error": data},
                cls=self.encoder_class,
                indent=indent,
                ensure_ascii=self.ensure_ascii,
                allow_nan=not self.strict,
                separators=separators,
            )
        else:
            ret = json.dumps(
                obj={"data": data},
                cls=self.encoder_class,
                indent=indent,
                ensure_ascii=self.ensure_ascii,
                allow_nan=not self.strict,
                separators=separators,
            )

        ret = ret.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
        return ret.encode()
