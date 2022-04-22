class DisableFormFieldsMixin:
    def _disable_form_fields(self):
        for field in self.fields.values():
            field.disabled = True
