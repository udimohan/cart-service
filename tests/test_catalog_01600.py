"""Tests for catalog_01600."""

import pytest

from cartservice.generated.catalog_01600 import (
    Product_01600,
    bucket_by_tag_01600,
    is_valid_sku_01600,
    price_with_tax_01600,
)


def test_price_with_tax_01600():
    assert price_with_tax_01600(1000, 500) == 1050


def test_price_with_tax_negative_01600():
    with pytest.raises(ValueError):
        price_with_tax_01600(1000, -1)


def test_is_valid_sku_01600():
    assert is_valid_sku_01600("abc123")
    assert not is_valid_sku_01600("")


def test_bucket_by_tag_01600():
    p = Product_01600("s1", 100, ["a"])
    assert bucket_by_tag_01600([p]) == {"a": ["s1"]}
