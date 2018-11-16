# -*- coding: utf-8 -*-
#
# New Age Laboratories (NAL)

import logging
from zope.i18nmessageid import MessageFactory

# Defining a Message Factory for when this product is internationalized.
bhpMessageFactory = MessageFactory('nal')

logger = logging.getLogger('nal')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    logger.info("*** Initializing NAL LIMS Customization Package ***")
