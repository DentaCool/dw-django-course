from __future__ import absolute_import

from django import forms

from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingFormField


class CkEditorForm(forms.Form):
    ckeditor_standard_example = RichTextFormField()
    ckeditor_upload_example = RichTextUploadingFormField(
        config_name="my-custom-toolbar"
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author_comment', 'created', 'body')