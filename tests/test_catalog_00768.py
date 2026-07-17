"""Tests for catalog_00768."""

import pytest

from cartservice.generated.catalog_00768 import (
    Product_00768,
    bucket_by_tag_00768,
    is_valid_sku_00768,
    price_with_tax_00768,
)


def test_price_with_tax_00768():
    assert price_with_tax_00768(1000, 500) == 1050


def test_price_with_tax_negative_00768():
    with pytest.raises(ValueError):
        price_with_tax_00768(1000, -1)


def test_is_valid_sku_00768():
    assert is_valid_sku_00768("abc123")
    assert not is_valid_sku_00768("")


def test_bucket_by_tag_00768():
    p = Product_00768("s1", 100, ["a"])
    assert bucket_by_tag_00768([p]) == {"a": ["s1"]}
