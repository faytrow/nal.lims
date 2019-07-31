from Products.Archetypes.public import (DateTimeField, DisplayList, LinesField,
                                        MultiSelectionWidget, ReferenceField,
                                        Schema, StringField, StringWidget,
                                        TextAreaWidget, TextField,
                                        registerType)
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from bika.lims import bikaMessageFactory as _
from bika.lims.browser.fields import DateTimeField
from bika.lims.browser.widgets import DateTimeWidget
from bika.lims.browser.widgets import SelectionWidget
from bika.lims.browser.widgets import ReferenceWidget
from bika.lims.fields import ExtBooleanField
from bika.lims.fields import ExtStringField
from bika.lims.fields import ExtTextField
from bika.lims.fields import ExtReferenceField
from bika.lims.browser.fields import UIDReferenceField
from bika.lims.interfaces import IAnalysisRequest
from Products.CMFCore.permissions import ModifyPortalContent
from Products.CMFCore.permissions import View
from zope.component import adapts
from zope.interface import implements

#Additional AR fields
class AnalysisRequestSchemaExtender(object):
    adapts(IAnalysisRequest)
    implements(IOrderableSchemaExtender)
    def __init__(self, context):
        self.context = context

    fields = [
	ExtStringField(
            'ReportContact',
            required=1,
            widget=StringWidget(
                label=_("Report To Contact"),
                maxlength=30,
                size=20,
                render_own_label=True,
                description=_("The person the results will be primarily reported for."),
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible'},
            )
        ),

	ExtStringField(
            'CollectedBy',
            required=1,
            widget=StringWidget(
                label=_("Collected By"),
                maxlength=30,
                size=20,
                render_own_label=True,
                description=_("The person who collected the sample."),
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible'},
            )
        ),
    ]
   
    def getOrder(self, schematas):
        return schematas
    def getFields(self):
        return self.fields
