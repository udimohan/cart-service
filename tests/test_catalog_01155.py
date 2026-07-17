"""Tests for catalog_01155."""

import pytest

from cartservice.generated.catalog_01155 import (
    Product_01155,
    bucket_by_tag_01155,
    is_valid_sku_01155,
    price_with_tax_01155,
)


def test_price_with_tax_01155():
    assert price_with_tax_01155(1000, 500) == 1050


def test_price_with_tax_negative_01155():
    with pytest.raises(ValueError):
        price_with_tax_01155(1000, -1)


def test_is_valid_sku_01155():
    assert is_valid_sku_01155("abc123")
    assert not is_valid_sku_01155("")


def test_bucket_by_tag_01155():
    p = Product_01155("s1", 100, ["a"])
    assert bucket_by_tag_01155([p]) == {"a": ["s1"]}
