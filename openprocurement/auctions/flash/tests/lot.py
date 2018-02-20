# -*- coding: utf-8 -*-
import unittest

from openprocurement.auctions.core.tests.base import snitch
from openprocurement.auctions.core.tests.lot import AuctionLotResourceTestMixin, AuctionLotProcessTestMixin
from openprocurement.auctions.core.tests.blanks.lot_blanks import (
    # AuctionLotFeatureResourceTest
    auction_value,
    auction_features_invalid,
    # AuctionLotBidderResourceTest
    create_auction_bidder_invalid,
    patch_auction_bidder,
    # AuctionLotFeatureBidderResourceTest
    create_auction_bidder_invalid_feature,
    create_auction_bidder_feature
)

from openprocurement.auctions.flash.tests.base import (
    BaseWebTest, BaseAuctionWebTest, test_lots, test_auction_data, test_organization
)
from openprocurement.auctions.flash.tests.blanks.lot_blanks import (
    # AuctionLotResourceTest
    patch_auction_currency
)


class AuctionLotResourceTest(BaseAuctionWebTest, AuctionLotResourceTestMixin):
    test_lots = test_lots
    test_auction_data = test_auction_data

    test_patch_auction_currency = snitch(patch_auction_currency)


class AuctionLotFeatureResourceTest(BaseAuctionWebTest):
    initial_lots = 2 * test_lots
    test_auction_data = test_auction_data

    test_auction_value = snitch(auction_value)
    test_auction_features_invalid = snitch(auction_features_invalid)


class AuctionLotBidderResourceTest(BaseAuctionWebTest):
    initial_status = 'active.tendering'
    initial_lots = test_lots
    initial_organization = test_organization

    test_create_auction_bidder_invalid = snitch(create_auction_bidder_invalid)
    test_patch_auction_bidder = snitch(patch_auction_bidder)


class AuctionLotFeatureBidderResourceTest(BaseAuctionWebTest):
    initial_lots = test_lots
    initial_organization = test_organization

    def setUp(self):
        super(AuctionLotFeatureBidderResourceTest, self).setUp()
        self.lot_id = self.initial_lots[0]['id']
        response = self.app.patch_json('/auctions/{}'.format(self.auction_id), {"data": {
            "items": [
                {
                    'relatedLot': self.lot_id,
                    'id': '1'
                }
            ],
            "features": [
                {
                    "code": "code_item",
                    "featureOf": "item",
                    "relatedItem": "1",
                    "title": u"item feature",
                    "enum": [
                        {
                            "value": 0.01,
                            "title": u"good"
                        },
                        {
                            "value": 0.02,
                            "title": u"best"
                        }
                    ]
                },
                {
                    "code": "code_lot",
                    "featureOf": "lot",
                    "relatedItem": self.lot_id,
                    "title": u"lot feature",
                    "enum": [
                        {
                            "value": 0.01,
                            "title": u"good"
                        },
                        {
                            "value": 0.02,
                            "title": u"best"
                        }
                    ]
                },
                {
                    "code": "code_tenderer",
                    "featureOf": "tenderer",
                    "title": u"tenderer feature",
                    "enum": [
                        {
                            "value": 0.01,
                            "title": u"good"
                        },
                        {
                            "value": 0.02,
                            "title": u"best"
                        }
                    ]
                }
            ]
        }})
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json['data']['items'][0]['relatedLot'], self.lot_id)
        self.set_status('active.tendering')

    test_create_auction_bidder_invalid_feature = snitch(create_auction_bidder_invalid_feature)
    test_create_auction_bidder_feature = snitch(create_auction_bidder_feature)


class AuctionLotProcessTest(BaseAuctionWebTest, AuctionLotProcessTestMixin):
    setUp = BaseWebTest.setUp
    initial_organization = test_organization
    test_lots = test_lots
    test_auction_data = test_auction_data


def suite():
    tests = unittest.TestSuite()
    tests.addTest(unittest.makeSuite(AuctionLotResourceTest))
    tests.addTest(unittest.makeSuite(AuctionLotFeatureResourceTest))
    tests.addTest(unittest.makeSuite(AuctionLotBidderResourceTest))
    tests.addTest(unittest.makeSuite(AuctionLotFeatureBidderResourceTest))
    tests.addTest(unittest.makeSuite(AuctionLotProcessTest))
    return tests


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
