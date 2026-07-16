"""Tests for catalog_00109."""

import pytest

from cartservice.generated.catalog_00109 import (
    Product_00109,
    bucket_by_tag_00109,
    is_valid_sku_00109,
    price_with_tax_00109,
)


def test_price_with_tax_00109():
    assert price_with_tax_00109(1000, 500) == 1050


def test_price_with_tax_negative_00109():
    with pytest.raises(ValueError):
        price_with_tax_00109(1000, -1)


def test_is_valid_sku_00109():
    assert is_valid_sku_00109("abc123")
    assert not is_valid_sku_00109("")


def test_bucket_by_tag_00109():
    p = Product_00109("s1", 100, ["a"])
    assert bucket_by_tag_00109([p]) == {"a": ["s1"]}
