# -*- coding: utf-8 -*-
#
# New Age Laboratories (NAL)

from bika.lims.interfaces import IBikaLIMS


class INalLIMS(IBikaLIMS):
    """nal/inferfaces.py Marker interface that defines a Zope 3 browser layer.
    A layer specific for this add-on product.
    This interface is referred in browserlayer.xml.
    All views and viewlets register against this layer will appear on
    your Plone site only when the add-on installer has been run.
    """
