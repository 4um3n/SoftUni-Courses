class DisableFormFieldsMixin:
    def _disable_form_fields(self):
        for field in self.fields.values():
            field.disabled = True


class SetFormFieldsPlaceholders:
    def _set_placeholders(self, **placeholders):
        for field, placeholder in placeholders.items():
            if field in self.fields:
                self.fields[field].widget.attrs["placeholder"] = placeholder
