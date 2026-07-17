"""Tests for catalog_01558."""

import pytest

from cartservice.generated.catalog_01558 import (
    Product_01558,
    bucket_by_tag_01558,
    is_valid_sku_01558,
    price_with_tax_01558,
)


def test_price_with_tax_01558():
    assert price_with_tax_01558(1000, 500) == 1050


def test_price_with_tax_negative_01558():
    with pytest.raises(ValueError):
        price_with_tax_01558(1000, -1)


def test_is_valid_sku_01558():
    assert is_valid_sku_01558("abc123")
    assert not is_valid_sku_01558("")


def test_bucket_by_tag_01558():
    p = Product_01558("s1", 100, ["a"])
    assert bucket_by_tag_01558([p]) == {"a": ["s1"]}
