# -*- coding: utf-8 -*-
#
# Copyright 2018 Botswana Harvard Partnership (BHP)
 from Products.Archetypes.public import StringWidget
from Products.Archetypes.public import TextAreaWidget
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from bhp.lims.config import GENDERS
from bika.lims import bikaMessageFactory as _
from bika.lims.browser.fields import DateTimeField
from bika.lims.browser.widgets import DateTimeWidget
from bika.lims.browser.widgets import SelectionWidget
from bika.lims.fields import ExtBooleanField
from bika.lims.fields import ExtStringField
from bika.lims.fields import ExtTextField
from bika.lims.interfaces import IAnalysisRequest
from zope.component import adapts
from zope.interface import implements
 class AnalysisRequestSchemaExtender(object):
    adapts(IAnalysisRequest)
    implements(IOrderableSchemaExtender)
     def __init__(self, context):
        self.context = context
     fields = [
        ExtStringField(
            "ParticipantID",
            required=1,
            widget=StringWidget(
                label=_("Participant ID"),
                maxlength=8,
                size=8,
                render_own_label=True,
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible'},
            )
        ),
         ExtStringField(
            "OtherParticipantReference",
            required=1,
            widget=StringWidget(
                label=_("Other Participant Ref"),
                maxlength=12,
                size=12,
                render_own_label=True,
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible'},
            )
        ),
         ExtStringField(
            "ParticipantInitials",
            required=1,
            widget=StringWidget(
                label=_("Participant Initials"),
                maxlength=2,
                size=2,
                render_own_label=True,
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible'},
            )
        ),
         ExtStringField(
            "Visit",
            required=1,
            widget=StringWidget(
                label=_("Visit Number"),
                maxlength=4,
                size=4,
                render_own_label=True,
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible'},
            )
        ),
         ExtBooleanField(
            "Fasting",
            required=1,
            default=False,
            widget=SelectionWidget(
                format="radio",
                label=_("Fasting"),
                render_own_label=True,
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible'},
            ),
        ),
         DateTimeField(
            'DateOfBirth',
            required=1,
            widget=DateTimeWidget(
                label=_('Date of Birth'),
                datepicker_nofuture=1,
                show_time=False,
                render_own_label=True,
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible'},
            ),
        ),
         ExtStringField(
            "Volume",
            required=1,
            widget=StringWidget(
                label=_("Volume"),
                maxlength=8,
                size=8,
                render_own_label=True,
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible'},
            )
        ),
         ExtTextField(
            "OtherInformation",
            default_content_type="text/plain",
            allowable_content_types=("text/plain",),
            default_output_type="text/plain",
            widget=TextAreaWidget(
                label=_("Other relevant clinical information"),
                render_own_label=True,
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible'},
            ),
        ),
    ]
     def getOrder(self, schematas):
        return schematas
     def getFields(self):
        return self.fields
 class AnalysisRequestSchemaModifier(object):
    adapts(IAnalysisRequest)
    implements(ISchemaModifier)
     def __init__(self, context):
        self.context = context
     def fiddle(self, schema):
        schema['Sample'].widget.label = _("Specimen")
        return schema