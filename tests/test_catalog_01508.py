"""Tests for catalog_01508."""

import pytest

from cartservice.generated.catalog_01508 import (
    Product_01508,
    bucket_by_tag_01508,
    is_valid_sku_01508,
    price_with_tax_01508,
)


def test_price_with_tax_01508():
    assert price_with_tax_01508(1000, 500) == 1050


def test_price_with_tax_negative_01508():
    with pytest.raises(ValueError):
        price_with_tax_01508(1000, -1)


def test_is_valid_sku_01508():
    assert is_valid_sku_01508("abc123")
    assert not is_valid_sku_01508("")


def test_bucket_by_tag_01508():
    p = Product_01508("s1", 100, ["a"])
    assert bucket_by_tag_01508([p]) == {"a": ["s1"]}
