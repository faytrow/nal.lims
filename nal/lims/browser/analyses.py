from senaite.core.listing import utils
from senaite.core.listing.interfaces import IListingView
from senaite.core.listing.interfaces import IListingViewAdapter
from zope.component import adapts
from zope.interface import implements

class AnalysesListingViewAdapter(object):
    adapts(IListingView)
    implements(IListingViewAdapter)

    def __init__(self, listing, context):
        self.listing = listing
        self.context = context

    def before_render(self):
	self.columns["CaptureDate"].append('"ajax": True')
	self.columns["CaptureDate"].append('"type": "datetime"')
        return

    def folder_item(self, obj, item, index):
        item["allow_edit"].append("CaptureDate")
        return item
