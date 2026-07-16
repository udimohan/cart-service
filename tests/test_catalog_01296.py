"""Tests for catalog_01296."""

import pytest

from cartservice.generated.catalog_01296 import (
    Product_01296,
    bucket_by_tag_01296,
    is_valid_sku_01296,
    price_with_tax_01296,
)


def test_price_with_tax_01296():
    assert price_with_tax_01296(1000, 500) == 1050


def test_price_with_tax_negative_01296():
    with pytest.raises(ValueError):
        price_with_tax_01296(1000, -1)


def test_is_valid_sku_01296():
    assert is_valid_sku_01296("abc123")
    assert not is_valid_sku_01296("")


def test_bucket_by_tag_01296():
    p = Product_01296("s1", 100, ["a"])
    assert bucket_by_tag_01296([p]) == {"a": ["s1"]}
