# -*- coding: utf-8 -*-
import unittest
from openprocurement.auctions.core.tests.base import snitch
from openprocurement.auctions.core.tests.tender import AuctionResourceTestMixin
from openprocurement.auctions.core.tests.blanks.tender_blanks import (
    # AuctionTest
    simple_add_auction,
    # AuctionResourceTest
    patch_tender_jsonpatch,
    auction_features,
    auction_features_invalid,
    # AuctionProcessTest
    invalid_auction_conditions,
)

from openprocurement.auctions.flash.models import FlashAuction
from openprocurement.auctions.flash.tests.base import (
    BaseWebTest, BaseAuctionWebTest, test_auction_data, test_organization
)
from openprocurement.auctions.flash.tests.blanks.tender_blanks import (
    # AuctionTest
    create_role,
    edit_role,
    # AuctionResourceTest
    guarantee,
    dateModified_auction,
    patch_auction,
    create_auction,
    create_auction_generated,
    create_auction_invalid,
    # AuctionProcessTest
    one_valid_bid_auction,
    one_invalid_bid_auction,
    first_bid_auction
)


class AuctionTest(BaseWebTest):
    auction = FlashAuction
    initial_data = test_auction_data

    test_simple_add_auction = snitch(simple_add_auction)
    test_create_role = snitch(create_role)
    test_edit_role = snitch(edit_role)


class AuctionResourceTest(BaseWebTest, AuctionResourceTestMixin):
    initial_status = 'active.enquiries'
    initial_data = test_auction_data
    initial_organization = test_organization

    test_create_auction_invalid = snitch(create_auction_invalid)
    test_create_auction_generated = snitch(create_auction_generated)
    test_create_auction = snitch(create_auction)
    test_auction_features_invalid = snitch(auction_features_invalid)
    test_auction_features = snitch(auction_features)
    test_patch_tender_jsonpatch = snitch(patch_tender_jsonpatch)
    test_patch_auction = snitch(patch_auction)
    test_dateModified_auction = snitch(dateModified_auction)
    test_guarantee = snitch(guarantee)


class AuctionProcessTest(BaseAuctionWebTest):
    setUp = BaseWebTest.setUp
    initial_organization = test_organization

    test_invalid_auction_conditions = snitch(invalid_auction_conditions)
    test_one_valid_bid_auction = snitch(one_valid_bid_auction)
    test_one_invalid_bid_auction = snitch(one_invalid_bid_auction)
    test_first_bid_auction = snitch(first_bid_auction)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AuctionTest))
    suite.addTest(unittest.makeSuite(AuctionResourceTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
