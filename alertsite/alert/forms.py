# -*- coding: UTF-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Event
CHOICES = (
    ('1', _(u'Январь')),
    ('2', _(u'Февраль')),
    ('3', _(u'Март')),
    ('4', _(u'Апрель')),
    ('5', _(u'Май')),
    ('6', _(u'Июнь')),
    ('7', _(u'Июль')),
    ('8', _(u'Август')),
    ('9', _(u'Сентябрь')),
    ('10', _(u'Октябрь')),
    ('11', _(u'Ноябрь')),
    ('12', _(u'Декабрь')),
)


class CreateEventForm(forms.ModelForm):

    title = forms.CharField(label=_(u'Название'))
    description = forms.CharField(label=_(u'Описание'), widget=forms.Textarea())
    place = forms.CharField(label=_(u'Место'))
    year = forms.IntegerField(label=_(u'Год'), min_value=2016, max_value=2026)
    month = forms.ChoiceField(
        label=_(u'Месяц'),
        widget=forms.Select(),
        choices=CHOICES
    )
    day = forms.IntegerField(label=_(u'День'), min_value=1, max_value=31)
    hour = forms.IntegerField(
        label=_(u'Час (от 0 до 23)'),
        min_value=0,
        max_value=23
    )
    minute = forms.IntegerField(
        label=_(u'Минут (от 0 до 59)'),
        min_value=0,
        max_value=59
    )

    class Meta:
        model = Event
        fields = (
            'title',
            'description',
            'place',
            'invite_list'
        )


class ChangeEventForm(forms.ModelForm):

    description = forms.CharField(label=_(u'Описание'), widget=forms.Textarea())
    place = forms.CharField(label=_(u'Место'))
    year = forms.IntegerField(label=_(u'Год'), min_value=2016, max_value=2026)
    month = forms.ChoiceField(
        label=_(u'Месяц'),
        widget=forms.Select(),
        choices=CHOICES
    )
    day = forms.IntegerField(label=_(u'День'), min_value=1, max_value=31)
    hour = forms.IntegerField(
        label=_(u'Час (от 0 до 23)'),
        min_value=0,
        max_value=23
    )
    minute = forms.IntegerField(
        label=_(u'Минут (от 0 до 59)'),
        min_value=0,
        max_value=59
    )

    class Meta:
        model = Event
        fields = (
            'description',
            'place',
            'invite_list'
        )
