"""Tests for catalog_01609."""

import pytest

from cartservice.generated.catalog_01609 import (
    Product_01609,
    bucket_by_tag_01609,
    is_valid_sku_01609,
    price_with_tax_01609,
)


def test_price_with_tax_01609():
    assert price_with_tax_01609(1000, 500) == 1050


def test_price_with_tax_negative_01609():
    with pytest.raises(ValueError):
        price_with_tax_01609(1000, -1)


def test_is_valid_sku_01609():
    assert is_valid_sku_01609("abc123")
    assert not is_valid_sku_01609("")


def test_bucket_by_tag_01609():
    p = Product_01609("s1", 100, ["a"])
    assert bucket_by_tag_01609([p]) == {"a": ["s1"]}
