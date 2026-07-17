"""Tests for catalog_01396."""

import pytest

from cartservice.generated.catalog_01396 import (
    Product_01396,
    bucket_by_tag_01396,
    is_valid_sku_01396,
    price_with_tax_01396,
)


def test_price_with_tax_01396():
    assert price_with_tax_01396(1000, 500) == 1050


def test_price_with_tax_negative_01396():
    with pytest.raises(ValueError):
        price_with_tax_01396(1000, -1)


def test_is_valid_sku_01396():
    assert is_valid_sku_01396("abc123")
    assert not is_valid_sku_01396("")


def test_bucket_by_tag_01396():
    p = Product_01396("s1", 100, ["a"])
    assert bucket_by_tag_01396([p]) == {"a": ["s1"]}
