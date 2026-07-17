"""Tests for catalog_00997."""

import pytest

from cartservice.generated.catalog_00997 import (
    Product_00997,
    bucket_by_tag_00997,
    is_valid_sku_00997,
    price_with_tax_00997,
)


def test_price_with_tax_00997():
    assert price_with_tax_00997(1000, 500) == 1050


def test_price_with_tax_negative_00997():
    with pytest.raises(ValueError):
        price_with_tax_00997(1000, -1)


def test_is_valid_sku_00997():
    assert is_valid_sku_00997("abc123")
    assert not is_valid_sku_00997("")


def test_bucket_by_tag_00997():
    p = Product_00997("s1", 100, ["a"])
    assert bucket_by_tag_00997([p]) == {"a": ["s1"]}
