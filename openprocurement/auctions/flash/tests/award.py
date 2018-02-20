# -*- coding: utf-8 -*-
import unittest

from openprocurement.auctions.core.tests.award import (
    AuctionLotAwardResourceTestMixin,
    Auction2LotAwardResourceTestMixin,
    AuctionAwardDocumentResourceTestMixin,
    AuctionLotAwardComplaintResourceTestMixin,
    Auction2LotAwardComplaintResourceTestMixin,
    AuctionAwardComplaintDocumentResourceTestMixin,
    Auction2LotAwardComplaintDocumentResourceTestMixin,
    Auction2LotAwardDocumentResourceTestMixin
)
from openprocurement.auctions.core.tests.base import snitch
from openprocurement.auctions.flash.tests.base import (
    BaseAuctionWebTest,
    test_bids,
    test_lots,
    test_organization
)

from openprocurement.auctions.core.plugins.awarding.v1.tests.blanks.award_blanks import (
    # AuctionAwardResourceTest
    create_auction_award_invalid,
    create_auction_award,
    patch_auction_award,
    patch_auction_award_unsuccessful,
    get_auction_award,
    patch_auction_award_Administrator_change,
    # AuctionAwardComplaintResourceTest
    create_auction_award_complaint_invalid,
    create_auction_award_complaint,
    patch_auction_award_complaint,
    review_auction_award_complaint,
    get_auction_award_complaint,
    get_auction_award_complaints
)


class AuctionAwardResourceTest(BaseAuctionWebTest):
    initial_status = 'active.qualification'
    initial_bids = test_bids
    test_create_auction_award_invalid = snitch(create_auction_award_invalid)
    test_create_auction_award = snitch(create_auction_award)
    test_patch_auction_award = snitch(patch_auction_award)
    test_patch_auction_award_unsuccessful = snitch(patch_auction_award_unsuccessful)
    test_get_auction_award = snitch(get_auction_award)
    test_patch_auction_award_Administrator_change = snitch(patch_auction_award_Administrator_change)


class AuctionLotAwardResourceTest(BaseAuctionWebTest, AuctionLotAwardResourceTestMixin):
    initial_status = 'active.qualification'
    initial_lots = test_lots
    initial_bids = test_bids
    initial_organization = test_organization


class Auction2LotAwardResourceTest(BaseAuctionWebTest, Auction2LotAwardResourceTestMixin):
    initial_status = 'active.qualification'
    initial_lots = 2 * test_lots
    initial_bids = test_bids
    initial_organization = test_organization


class AuctionAwardComplaintResourceTest(BaseAuctionWebTest):
    initial_status = 'active.qualification'
    initial_bids = test_bids

    def setUp(self):
        super(AuctionAwardComplaintResourceTest, self).setUp()
        # Create award
        response = self.app.post_json('/auctions/{}/awards'.format(
            self.auction_id),
            {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': self.initial_bids[0]['id']}})
        award = response.json['data']
        self.award_id = award['id']

    test_create_auction_award_complaint_invalid = snitch(create_auction_award_complaint_invalid)
    test_create_auction_award_complaint = snitch(create_auction_award_complaint)
    test_patch_auction_award_complaint = snitch(patch_auction_award_complaint)
    test_review_auction_award_complaint = snitch(review_auction_award_complaint)
    test_get_auction_award_complaint = snitch(get_auction_award_complaint)
    test_get_auction_award_complaints = snitch(get_auction_award_complaints)


class AuctionLotAwardComplaintResourceTest(BaseAuctionWebTest,
                                           AuctionLotAwardComplaintResourceTestMixin):
    initial_status = 'active.qualification'
    initial_lots = test_lots
    initial_bids = test_bids
    initial_organization = test_organization

    def setUp(self):
        super(AuctionLotAwardComplaintResourceTest, self).setUp()
        # Create award
        bid = self.initial_bids[0]
        response = self.app.post_json('/auctions/{}/awards'.format(
            self.auction_id), {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': bid['id'], 'lotID': bid['lotValues'][0]['relatedLot']}})
        award = response.json['data']
        self.award_id = award['id']


class Auction2LotAwardComplaintResourceTest(BaseAuctionWebTest,
                                            Auction2LotAwardComplaintResourceTestMixin):
    initial_status = 'active.qualification'
    initial_lots = 2 * test_lots
    initial_bids = test_bids
    initial_organization = test_organization

    def setUp(self):
        super(Auction2LotAwardComplaintResourceTest, self).setUp()
        # Create award
        bid = self.initial_bids[0]
        response = self.app.post_json('/auctions/{}/awards'.format(
            self.auction_id), {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': bid['id'], 'lotID': bid['lotValues'][0]['relatedLot']}})
        award = response.json['data']
        self.award_id = award['id']

    test_get_auction_lot_award_complaint = snitch(get_auction_award_complaint)
    test_get_auction_lot_award_complaints = snitch(get_auction_award_complaints)


class AuctionAwardComplaintDocumentResourceTest(BaseAuctionWebTest,
                                                AuctionAwardComplaintDocumentResourceTestMixin):
    initial_status = 'active.qualification'
    initial_bids = test_bids

    def setUp(self):
        super(AuctionAwardComplaintDocumentResourceTest, self).setUp()
        # Create award
        response = self.app.post_json('/auctions/{}/awards'.format(
            self.auction_id), {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': self.initial_bids[0]['id']}})
        award = response.json['data']
        self.award_id = award['id']
        # Create complaint for award
        response = self.app.post_json('/auctions/{}/awards/{}/complaints'.format(
            self.auction_id, self.award_id), {'data': {'title': 'complaint title', 'description': 'complaint description', 'author': test_organization}})
        complaint = response.json['data']
        self.complaint_id = complaint['id']
        self.complaint_owner_token = response.json['access']['token']


class Auction2LotAwardComplaintDocumentResourceTest(BaseAuctionWebTest,
                                                    Auction2LotAwardComplaintDocumentResourceTestMixin):
    initial_status = 'active.qualification'
    initial_bids = test_bids
    initial_lots = 2 * test_lots

    def setUp(self):
        super(Auction2LotAwardComplaintDocumentResourceTest, self).setUp()
        # Create award
        bid = self.initial_bids[0]
        response = self.app.post_json('/auctions/{}/awards'.format(
            self.auction_id), {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': bid['id'], 'lotID': bid['lotValues'][0]['relatedLot']}})
        award = response.json['data']
        self.award_id = award['id']
        # Create complaint for award
        response = self.app.post_json('/auctions/{}/awards/{}/complaints'.format(
            self.auction_id, self.award_id), {'data': {'title': 'complaint title', 'description': 'complaint description', 'author': test_organization}})
        complaint = response.json['data']
        self.complaint_id = complaint['id']
        self.complaint_owner_token = response.json['access']['token']


class AuctionAwardDocumentResourceTest(BaseAuctionWebTest,
                                       AuctionAwardDocumentResourceTestMixin):
    initial_status = 'active.qualification'
    initial_bids = test_bids

    def setUp(self):
        super(AuctionAwardDocumentResourceTest, self).setUp()
        # Create award
        response = self.app.post_json('/auctions/{}/awards'.format(
            self.auction_id), {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': self.initial_bids[0]['id']}})
        award = response.json['data']
        self.first_award_id = award['id']


class Auction2LotAwardDocumentResourceTest(BaseAuctionWebTest,
                                           Auction2LotAwardDocumentResourceTestMixin):
    initial_status = 'active.qualification'
    initial_bids = test_bids
    initial_lots = 2 * test_lots

    def setUp(self):
        super(Auction2LotAwardDocumentResourceTest, self).setUp()
        # Create award
        bid = self.initial_bids[0]
        response = self.app.post_json('/auctions/{}/awards'.format(
            self.auction_id), {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': bid['id'], 'lotID': bid['lotValues'][0]['relatedLot']}})
        award = response.json['data']
        self.award_id = award['id']


def suite():
    tests = unittest.TestSuite()
    tests.addTest(unittest.makeSuite(AuctionAwardResourceTest))
    tests.addTest(unittest.makeSuite(AuctionLotAwardResourceTest))
    tests.addTest(unittest.makeSuite(Auction2LotAwardResourceTest))
    tests.addTest(unittest.makeSuite(AuctionAwardComplaintResourceTest))
    tests.addTest(unittest.makeSuite(AuctionLotAwardComplaintResourceTest))
    tests.addTest(unittest.makeSuite(Auction2LotAwardComplaintResourceTest))
    tests.addTest(unittest.makeSuite(AuctionAwardComplaintDocumentResourceTest))
    tests.addTest(unittest.makeSuite(Auction2LotAwardComplaintDocumentResourceTest))
    tests.addTest(unittest.makeSuite(AuctionAwardDocumentResourceTest))
    tests.addTest(unittest.makeSuite(Auction2LotAwardDocumentResourceTest))
    return tests


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
