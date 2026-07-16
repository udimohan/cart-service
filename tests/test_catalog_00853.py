"""Tests for catalog_00853."""

import pytest

from cartservice.generated.catalog_00853 import (
    Product_00853,
    bucket_by_tag_00853,
    is_valid_sku_00853,
    price_with_tax_00853,
)


def test_price_with_tax_00853():
    assert price_with_tax_00853(1000, 500) == 1050


def test_price_with_tax_negative_00853():
    with pytest.raises(ValueError):
        price_with_tax_00853(1000, -1)


def test_is_valid_sku_00853():
    assert is_valid_sku_00853("abc123")
    assert not is_valid_sku_00853("")


def test_bucket_by_tag_00853():
    p = Product_00853("s1", 100, ["a"])
    assert bucket_by_tag_00853([p]) == {"a": ["s1"]}
