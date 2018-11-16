# -*- coding: utf-8 -*-
#
# Copyright 2018 Botswana Harvard Partnership (BHP)

from nal.lims import logger
from nal.lims import bhpMessageFactory as _
from BTrees.OOBTree import OOBTree
from zope.annotation.interfaces import IAnnotations


def setupHandler(context):
    """BHP setup handler
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


def setup_id_formatting(portal):
    """Setup default ID formatting
    """
    logger.info("*** Setup ID Formatting ***")
    bs = portal.bika_setup

    def set_format(format):
        if 'portal_type' not in format:
            return
        logger.info("Applying format {} for {}".format(format.get('form',''),
                                                       format.get('portal_type')))
        portal_type = format['portal_type']
        ids = list()
        id_map = bs.getIDFormatting()
        for record in id_map:
            if record.get('portal_type', '') == portal_type:
                continue
            ids.append(record)
        ids.append(format)
        bs.setIDFormatting(ids)

    # Sample ID format
    set_format(dict(form='{seq:06d}',
                    portal_type='Sample',
                    prefix='sample',
                    sequence_type='generated',
                    split_length=1,
                    value=''))

    # Analysis Request ID format
    set_format(dict(form='{sampleId}R{seq:d}',
                    portal_type='AnalysisRequest',
                    counter_reference='AnalysisRequestSample',
                    counter_type='backreference',
                    sequence_type='counter',
                    value=''))


def hide_unused_ar_fields(portal):
    """HIdes unused fields from AR Add Form
    """
    logger.info("*** Hiding default fields from AR Add ***")
    field_names_to_hide = ["AdHoc", "Batch", "CCContact", "CCEmails",
                           "ClientOrderNumber", "ClientReference",
                           "ClientSampleID", "Composite", "Contact",
                           "DateSampled", "DefaultContainerType",
                           "EnvironmentalConditions", "InvoiceExclude",
                           "PreparationWorkflow", "Priority", "Sample",
                           "SampleCondition", "SamplePoint", "Sampler",
                           "SamplingDate", "SamplingDeviation", "SamplingRound",
                           "Specification", "StorageLocation", "SubGroup",
                           "Template",]

    bika_setup = portal.bika_setup
    annotation = IAnnotations(bika_setup)
    AR_CONFIGURATION_STORAGE = "bika.lims.browser.analysisrequest.manage.add"
    storage = annotation.get(AR_CONFIGURATION_STORAGE, OOBTree())

    visibility = storage.get('visibility', {})
    for field_name in field_names_to_hide:
        visibility[field_name] = False
    storage.update({"visibility": visibility})
    annotation[AR_CONFIGURATION_STORAGE] = storage
