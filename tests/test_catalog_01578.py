"""Tests for catalog_01578."""

import pytest

from cartservice.generated.catalog_01578 import (
    Product_01578,
    bucket_by_tag_01578,
    is_valid_sku_01578,
    price_with_tax_01578,
)


def test_price_with_tax_01578():
    assert price_with_tax_01578(1000, 500) == 1050


def test_price_with_tax_negative_01578():
    with pytest.raises(ValueError):
        price_with_tax_01578(1000, -1)


def test_is_valid_sku_01578():
    assert is_valid_sku_01578("abc123")
    assert not is_valid_sku_01578("")


def test_bucket_by_tag_01578():
    p = Product_01578("s1", 100, ["a"])
    assert bucket_by_tag_01578([p]) == {"a": ["s1"]}
