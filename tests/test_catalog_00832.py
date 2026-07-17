"""Tests for catalog_00832."""

import pytest

from cartservice.generated.catalog_00832 import (
    Product_00832,
    bucket_by_tag_00832,
    is_valid_sku_00832,
    price_with_tax_00832,
)


def test_price_with_tax_00832():
    assert price_with_tax_00832(1000, 500) == 1050


def test_price_with_tax_negative_00832():
    with pytest.raises(ValueError):
        price_with_tax_00832(1000, -1)


def test_is_valid_sku_00832():
    assert is_valid_sku_00832("abc123")
    assert not is_valid_sku_00832("")


def test_bucket_by_tag_00832():
    p = Product_00832("s1", 100, ["a"])
    assert bucket_by_tag_00832([p]) == {"a": ["s1"]}
