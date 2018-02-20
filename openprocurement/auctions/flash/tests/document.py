# -*- coding: utf-8 -*-
import unittest

from openprocurement.auctions.core.tests.base import snitch

from openprocurement.auctions.flash.tests.base import BaseAuctionWebTest
from openprocurement.auctions.core.tests.blanks.document_blanks import (
    # AuctionDocumentResourceTest
    not_found,
    # AuctionDocumentWithDSResourceTest
    create_auction_document_json_invalid,
)
from openprocurement.auctions.flash.tests.blanks.document_blanks import (
    # AuctionDocumentResourceTest
    create_auction_document,
    put_auction_document,
    patch_auction_document,
    # AuctionDocumentWithDSResourceTest
    create_auction_document_json,
    put_auction_document_json
)


class AuctionDocumentResourceTest(BaseAuctionWebTest):
    docservice = False
    test_auction_document_not_found = snitch(not_found)
    test_create_auction_document = snitch(create_auction_document)
    test_put_auction_document = snitch(put_auction_document)
    test_patch_auction_document = snitch(patch_auction_document)


class AuctionDocumentWithDSResourceTest(AuctionDocumentResourceTest):
    docservice = True
    test_create_auction_document_json_invalid = snitch(create_auction_document_json_invalid)
    test_create_auction_document_json = snitch(create_auction_document_json)
    test_put_auction_document_json = snitch(put_auction_document_json)


def suite():
    tests = unittest.TestSuite()
    tests.addTest(unittest.makeSuite(AuctionDocumentResourceTest))
    tests.addTest(unittest.makeSuite(AuctionDocumentWithDSResourceTest))
    return tests


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
