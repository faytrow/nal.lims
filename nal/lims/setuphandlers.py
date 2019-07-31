# -*- coding: utf-8 -*-
#
# Copyright 2018 Botswana Harvard Partnership (BHP)

from nal.lims import logger
from nal.lims import bhpMessageFactory as _
from BTrees.OOBTree import OOBTree
from zope.annotation.interfaces import IAnnotations


def setupHandler(context):
    """NAL setup handler
    """

    if context.readDataFile('nal.lims.txt') is None:
        return

    logger.info("NAL setup handler [BEGIN]")

    portal = context.getSite()

    # Run installers
    setup_laboratory(portal)

    # Apply ID format to content types
    setup_id_formatting(portal)

    # Hide unused AR Fields
    hide_unused_ar_fields(portal)


    logger.info("NAL setup handler [DONE]")


def setup_laboratory(portal):
    """Setup Laboratory
    """
    logger.info("*** Setup Laboratory ***")
    lab = portal.bika_setup.laboratory
    lab.edit(title=_('NAL'))
    lab.reindexObject()

def hide_unused_ar_fields(portal):
    """Hides unused fields from AR Add Form
    """
    logger.info("*** Hiding default fields from AR Add ***")
    field_names_to_hide = ["AdHoc", "Batch", "CCContact", "CCEmails",
                           "ClientOrderNumber", "ClientReference",
                           "ClientSampleID", "Composite", "Contact",
                           "DateSampled", "DefaultContainerType",
                           "EnvironmentalConditions", "InvoiceExclude",
                           "PreparationWorkflow", "Priority", "Sample",
                           "SampleCondition", "Sampler",
                           "SamplingDate", "SamplingDeviation", "SamplingRound",
                           "Specification", "StorageLocation", "SubGroup",
                           "Template", "Custom Field",]

    bika_setup = portal.bika_setup
    annotation = IAnnotations(bika_setup)
    AR_CONFIGURATION_STORAGE = "bika.lims.browser.analysisrequest.manage.add"
    storage = annotation.get(AR_CONFIGURATION_STORAGE, OOBTree())

    visibility = storage.get('visibility', {}).copy()
    for field_name in field_names_to_hide:
        visibility[field_name] = False
    storage.update({"visibility": visibility})
    annotation[AR_CONFIGURATION_STORAGE] = storage
