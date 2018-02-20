# -*- coding: utf-8 -*-
import unittest

from openprocurement.auctions.core.tests.base import snitch
from openprocurement.auctions.core.tests.auctions import (
    AuctionAuctionResourceTestMixin,
    AuctionLotAuctionResourceTestMixin,
    AuctionMultipleLotAuctionResourceTestMixin
)
from openprocurement.auctions.core.tests.blanks.auction_blanks import (
    # AuctionSameValueAuctionResourceTest
    post_auction_auction_not_changed,
    post_auction_auction_reversed,
    # AuctionFeaturesAuctionResourceTest
    get_auction_features_auction
)

from openprocurement.auctions.flash.tests.base import (
    BaseAuctionWebTest, test_features_auction_data,
    test_bids, test_lots, test_organization
)
from openprocurement.auctions.flash.tests.blanks.auction_blanks import (
    # AuctionAuctionResourceTest
    post_auction_auction,
    # AuctionLotAuctionResourceTest
    post_auction_auction_lot,
    # AuctionMultipleLotAuctionResourceTest
    post_auction_auction_2_lot,
)


class AuctionAuctionResourceTest(BaseAuctionWebTest, AuctionAuctionResourceTestMixin):
    initial_status = 'active.tendering'
    initial_bids = test_bids
    test_post_auction_auction = snitch(post_auction_auction)


class AuctionSameValueAuctionResourceTest(BaseAuctionWebTest):
    initial_status = 'active.auction'
    initial_bids = [
        {
            "tenderers": [
                test_organization
            ],
            "value": {
                "amount": 469,
                "currency": "UAH",
                "valueAddedTaxIncluded": True
            }
        }
        for i in range(3)
    ]

    test_post_auction_auction_not_changed = snitch(post_auction_auction_not_changed)
    test_post_auction_auction_reversed = snitch(post_auction_auction_reversed)


class AuctionLotAuctionResourceTest(BaseAuctionWebTest, AuctionLotAuctionResourceTestMixin):
    initial_status = 'active.tendering'
    initial_bids = test_bids
    initial_lots = test_lots

    test_post_auction_auction_lots = snitch(post_auction_auction_lot)


class AuctionMultipleLotAuctionResourceTest(BaseAuctionWebTest,
                                            AuctionMultipleLotAuctionResourceTestMixin):
    initial_status = 'active.tendering'
    initial_bids = test_bids
    initial_lots = 2 * test_lots

    test_post_auction_auction_2_lots = snitch(post_auction_auction_2_lot)


class AuctionFeaturesAuctionResourceTest(BaseAuctionWebTest):
    initial_data = test_features_auction_data
    initial_status = 'active.auction'
    initial_bids = [
        {
            "parameters": [
                {
                    "code": i["code"],
                    "value": 0.1,
                }
                for i in test_features_auction_data['features']
            ],
            "tenderers": [
                test_organization
            ],
            "value": {
                "amount": 469,
                "currency": "UAH",
                "valueAddedTaxIncluded": True
            }
        },
        {
            "parameters": [
                {
                    "code": i["code"],
                    "value": 0.15,
                }
                for i in test_features_auction_data['features']
            ],
            "tenderers": [
                test_organization
            ],
            "value": {
                "amount": 479,
                "currency": "UAH",
                "valueAddedTaxIncluded": True
            }
        }
    ]
    test_get_auction_auction = snitch(get_auction_features_auction)


def suite():
    tests = unittest.TestSuite()
    tests.addTest(unittest.makeSuite(AuctionAuctionResourceTest))
    tests.addTest(unittest.makeSuite(AuctionSameValueAuctionResourceTest))
    tests.addTest(unittest.makeSuite(AuctionLotAuctionResourceTest))
    tests.addTest(unittest.makeSuite(AuctionMultipleLotAuctionResourceTest))
    tests.addTest(unittest.makeSuite(AuctionFeaturesAuctionResourceTest))
    return tests


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
