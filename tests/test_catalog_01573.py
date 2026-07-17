"""Tests for catalog_01573."""

import pytest

from cartservice.generated.catalog_01573 import (
    Product_01573,
    bucket_by_tag_01573,
    is_valid_sku_01573,
    price_with_tax_01573,
)


def test_price_with_tax_01573():
    assert price_with_tax_01573(1000, 500) == 1050


def test_price_with_tax_negative_01573():
    with pytest.raises(ValueError):
        price_with_tax_01573(1000, -1)


def test_is_valid_sku_01573():
    assert is_valid_sku_01573("abc123")
    assert not is_valid_sku_01573("")


def test_bucket_by_tag_01573():
    p = Product_01573("s1", 100, ["a"])
    assert bucket_by_tag_01573([p]) == {"a": ["s1"]}
