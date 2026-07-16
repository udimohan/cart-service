"""Tests for catalog_00226."""

import pytest

from cartservice.generated.catalog_00226 import (
    Product_00226,
    bucket_by_tag_00226,
    is_valid_sku_00226,
    price_with_tax_00226,
)


def test_price_with_tax_00226():
    assert price_with_tax_00226(1000, 500) == 1050


def test_price_with_tax_negative_00226():
    with pytest.raises(ValueError):
        price_with_tax_00226(1000, -1)


def test_is_valid_sku_00226():
    assert is_valid_sku_00226("abc123")
    assert not is_valid_sku_00226("")


def test_bucket_by_tag_00226():
    p = Product_00226("s1", 100, ["a"])
    assert bucket_by_tag_00226([p]) == {"a": ["s1"]}
