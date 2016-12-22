# -*- coding: UTF-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Comment


class CommentsForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'cols': '55',
        'rows': '10',
        'placeholder': _(u'Присоединяйтесь к обсуждению...'),
        'spellcheck': 'true',
        'maxlength': '2000'
    }))

    class Meta:
        model = Comment
        fields = ('body',)
