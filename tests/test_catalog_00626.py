"""Tests for catalog_00626."""

import pytest

from cartservice.generated.catalog_00626 import (
    Product_00626,
    bucket_by_tag_00626,
    is_valid_sku_00626,
    price_with_tax_00626,
)


def test_price_with_tax_00626():
    assert price_with_tax_00626(1000, 500) == 1050


def test_price_with_tax_negative_00626():
    with pytest.raises(ValueError):
        price_with_tax_00626(1000, -1)


def test_is_valid_sku_00626():
    assert is_valid_sku_00626("abc123")
    assert not is_valid_sku_00626("")


def test_bucket_by_tag_00626():
    p = Product_00626("s1", 100, ["a"])
    assert bucket_by_tag_00626([p]) == {"a": ["s1"]}
