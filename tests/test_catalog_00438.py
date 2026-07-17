"""Tests for catalog_00438."""

import pytest

from cartservice.generated.catalog_00438 import (
    Product_00438,
    bucket_by_tag_00438,
    is_valid_sku_00438,
    price_with_tax_00438,
)


def test_price_with_tax_00438():
    assert price_with_tax_00438(1000, 500) == 1050


def test_price_with_tax_negative_00438():
    with pytest.raises(ValueError):
        price_with_tax_00438(1000, -1)


def test_is_valid_sku_00438():
    assert is_valid_sku_00438("abc123")
    assert not is_valid_sku_00438("")


def test_bucket_by_tag_00438():
    p = Product_00438("s1", 100, ["a"])
    assert bucket_by_tag_00438([p]) == {"a": ["s1"]}
