# -*- coding: utf-8 -*-
#
# Copyright 2018 New Age Laboratories (NAL)
from archetypes.schemaextender.interfaces import ISchemaModifier
from bika.lims import bikaMessageFactory as _
from bika.lims.interfaces import IClient
from zope.component import adapts
from zope.interface import implements
class ClientSchemaModifier(object):
    adapts(IClient)
    implements(ISchemaModifier)
    def __init__(self, context):
       self.context = context
    def fiddle(self, schema):
       schema['TaxNumber'].widget.label = _("Grower #")
       return schema
