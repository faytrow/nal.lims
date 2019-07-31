from Products.Archetypes.public import StringWidget
from Products.Archetypes.public import TextAreaWidget
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from bika.lims import bikaMessageFactory as _
from bika.lims.browser.fields import DateTimeField
from Products.Archetypes.public import (DateTimeField, DisplayList, LinesField,
                                        MultiSelectionWidget, ReferenceField,
                                        Schema, StringField, StringWidget,
                                        TextAreaWidget, TextField,
                                        registerType)
from bika.lims.browser.widgets import DateTimeWidget
from bika.lims.browser.widgets import SelectionWidget
from bika.lims.fields import ExtBooleanField
from bika.lims.fields import ExtStringField
from bika.lims.fields import ExtTextField
from bika.lims.fields import ExtDateTimeField
from bika.lims.interfaces import IBatch
from zope.component import adapts
from zope.interface import implements

#Additional Batch fields
class BatchSchemaExtender(object):
    adapts(IBatch)
    implements(ISchemaExtender)
    def __init__(self, context):
        self.context = context
    fields = [
        ExtDateTimeField(
            'DateTimeIn',
            required=False,
            widget=DateTimeWidget(
                label=_("Date/Time In (Incubation)"),
                show_time = True,
                size=20,
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible'},
            )
        ),
    ]
    def getFields(self):
        return self.fields
class BatchSchemaModifier(object):
    adapts(IBatch)
    implements(ISchemaModifier)
    def __init__(self, context):
        self.context = context
    def fiddle(self, schema):
        schema['BatchDate'].widget.show_time = True
        schema['BatchDate'].widget.label = _("SDG Received Date")
        schema['InheritedObjectsUI'].widget.visible = False
        schema['Remarks'].widget.visible = False
        schema['BatchLabels'].widget.visible = False
        return schema
