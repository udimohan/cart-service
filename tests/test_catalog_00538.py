"""Tests for catalog_00538."""

import pytest

from cartservice.generated.catalog_00538 import (
    Product_00538,
    bucket_by_tag_00538,
    is_valid_sku_00538,
    price_with_tax_00538,
)


def test_price_with_tax_00538():
    assert price_with_tax_00538(1000, 500) == 1050


def test_price_with_tax_negative_00538():
    with pytest.raises(ValueError):
        price_with_tax_00538(1000, -1)


def test_is_valid_sku_00538():
    assert is_valid_sku_00538("abc123")
    assert not is_valid_sku_00538("")


def test_bucket_by_tag_00538():
    p = Product_00538("s1", 100, ["a"])
    assert bucket_by_tag_00538([p]) == {"a": ["s1"]}
