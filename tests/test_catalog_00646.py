"""Tests for catalog_00646."""

import pytest

from cartservice.generated.catalog_00646 import (
    Product_00646,
    bucket_by_tag_00646,
    is_valid_sku_00646,
    price_with_tax_00646,
)


def test_price_with_tax_00646():
    assert price_with_tax_00646(1000, 500) == 1050


def test_price_with_tax_negative_00646():
    with pytest.raises(ValueError):
        price_with_tax_00646(1000, -1)


def test_is_valid_sku_00646():
    assert is_valid_sku_00646("abc123")
    assert not is_valid_sku_00646("")


def test_bucket_by_tag_00646():
    p = Product_00646("s1", 100, ["a"])
    assert bucket_by_tag_00646([p]) == {"a": ["s1"]}
