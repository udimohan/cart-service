"""Tests for catalog_00082."""

import pytest

from cartservice.generated.catalog_00082 import (
    Product_00082,
    bucket_by_tag_00082,
    is_valid_sku_00082,
    price_with_tax_00082,
)


def test_price_with_tax_00082():
    assert price_with_tax_00082(1000, 500) == 1050


def test_price_with_tax_negative_00082():
    with pytest.raises(ValueError):
        price_with_tax_00082(1000, -1)


def test_is_valid_sku_00082():
    assert is_valid_sku_00082("abc123")
    assert not is_valid_sku_00082("")


def test_bucket_by_tag_00082():
    p = Product_00082("s1", 100, ["a"])
    assert bucket_by_tag_00082([p]) == {"a": ["s1"]}
