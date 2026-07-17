"""Tests for catalog_01281."""

import pytest

from cartservice.generated.catalog_01281 import (
    Product_01281,
    bucket_by_tag_01281,
    is_valid_sku_01281,
    price_with_tax_01281,
)


def test_price_with_tax_01281():
    assert price_with_tax_01281(1000, 500) == 1050


def test_price_with_tax_negative_01281():
    with pytest.raises(ValueError):
        price_with_tax_01281(1000, -1)


def test_is_valid_sku_01281():
    assert is_valid_sku_01281("abc123")
    assert not is_valid_sku_01281("")


def test_bucket_by_tag_01281():
    p = Product_01281("s1", 100, ["a"])
    assert bucket_by_tag_01281([p]) == {"a": ["s1"]}
