"""Tests for catalog_01071."""

import pytest

from cartservice.generated.catalog_01071 import (
    Product_01071,
    bucket_by_tag_01071,
    is_valid_sku_01071,
    price_with_tax_01071,
)


def test_price_with_tax_01071():
    assert price_with_tax_01071(1000, 500) == 1050


def test_price_with_tax_negative_01071():
    with pytest.raises(ValueError):
        price_with_tax_01071(1000, -1)


def test_is_valid_sku_01071():
    assert is_valid_sku_01071("abc123")
    assert not is_valid_sku_01071("")


def test_bucket_by_tag_01071():
    p = Product_01071("s1", 100, ["a"])
    assert bucket_by_tag_01071([p]) == {"a": ["s1"]}
