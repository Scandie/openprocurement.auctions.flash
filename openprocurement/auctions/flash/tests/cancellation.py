# -*- coding: utf-8 -*-
import unittest

from openprocurement.auctions.core.tests.cancellation import (
    AuctionCancellationResourceTestMixin,
    AuctionCancellationDocumentResourceTestMixin,
    AuctionLotCancellationResourceTestMixin,
    AuctionLotsCancellationResourceTestMixin
)
from openprocurement.auctions.flash.tests.base import (
    BaseAuctionWebTest, test_lots, test_bids
)


class AuctionCancellationResourceTest(BaseAuctionWebTest,
                                      AuctionCancellationResourceTestMixin):
    initial_status = 'active.tendering'
    initial_bids = test_bids


class AuctionLotCancellationResourceTest(BaseAuctionWebTest,
                                         AuctionLotCancellationResourceTestMixin):
    initial_status = 'active.tendering'
    initial_lots = test_lots
    initial_bids = test_bids


class AuctionLotsCancellationResourceTest(BaseAuctionWebTest,
                                          AuctionLotsCancellationResourceTestMixin):
    initial_status = 'active.tendering'
    initial_lots = 2 * test_lots
    initial_bids = test_bids


class AuctionCancellationDocumentResourceTest(BaseAuctionWebTest,
                                              AuctionCancellationDocumentResourceTestMixin):

    def setUp(self):
        super(AuctionCancellationDocumentResourceTest, self).setUp()
        # Create cancellation
        response = self.app.post_json('/auctions/{}/cancellations'.format(
            self.auction_id), {'data': {'reason': 'cancellation reason'}})
        cancellation = response.json['data']
        self.cancellation_id = cancellation['id']


def suite():
    tests = unittest.TestSuite()
    tests.addTest(unittest.makeSuite(AuctionCancellationResourceTest))
    tests.addTest(unittest.makeSuite(AuctionLotCancellationResourceTest))
    tests.addTest(unittest.makeSuite(AuctionLotsCancellationResourceTest))
    tests.addTest(unittest.makeSuite(AuctionCancellationDocumentResourceTest))
    return tests


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
