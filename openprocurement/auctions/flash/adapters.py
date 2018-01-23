# -*- coding: utf-8 -*-
from openprocurement.auctions.core.adapters import AuctionConfigurator
from openprocurement.auctions.core.plugins.awarding.v1.adapters import (
    AwardingV1ConfiguratorMixin
)
from openprocurement.auctions.flash.models import Auction


class AuctionFlashConfigurator(AuctionConfigurator,
                               AwardingV1ConfiguratorMixin):
    name = 'Auction Flash Configurator'
    model = Auction
