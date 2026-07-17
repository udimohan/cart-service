"""Tests for catalog_00221."""

import pytest

from cartservice.generated.catalog_00221 import (
    Product_00221,
    bucket_by_tag_00221,
    is_valid_sku_00221,
    price_with_tax_00221,
)


def test_price_with_tax_00221():
    assert price_with_tax_00221(1000, 500) == 1050


def test_price_with_tax_negative_00221():
    with pytest.raises(ValueError):
        price_with_tax_00221(1000, -1)


def test_is_valid_sku_00221():
    assert is_valid_sku_00221("abc123")
    assert not is_valid_sku_00221("")


def test_bucket_by_tag_00221():
    p = Product_00221("s1", 100, ["a"])
    assert bucket_by_tag_00221([p]) == {"a": ["s1"]}
