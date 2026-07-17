"""Tests for catalog_00174."""

import pytest

from cartservice.generated.catalog_00174 import (
    Product_00174,
    bucket_by_tag_00174,
    is_valid_sku_00174,
    price_with_tax_00174,
)


def test_price_with_tax_00174():
    assert price_with_tax_00174(1000, 500) == 1050


def test_price_with_tax_negative_00174():
    with pytest.raises(ValueError):
        price_with_tax_00174(1000, -1)


def test_is_valid_sku_00174():
    assert is_valid_sku_00174("abc123")
    assert not is_valid_sku_00174("")


def test_bucket_by_tag_00174():
    p = Product_00174("s1", 100, ["a"])
    assert bucket_by_tag_00174([p]) == {"a": ["s1"]}
