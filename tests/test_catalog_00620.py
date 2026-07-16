"""Tests for catalog_00620."""

import pytest

from cartservice.generated.catalog_00620 import (
    Product_00620,
    bucket_by_tag_00620,
    is_valid_sku_00620,
    price_with_tax_00620,
)


def test_price_with_tax_00620():
    assert price_with_tax_00620(1000, 500) == 1050


def test_price_with_tax_negative_00620():
    with pytest.raises(ValueError):
        price_with_tax_00620(1000, -1)


def test_is_valid_sku_00620():
    assert is_valid_sku_00620("abc123")
    assert not is_valid_sku_00620("")


def test_bucket_by_tag_00620():
    p = Product_00620("s1", 100, ["a"])
    assert bucket_by_tag_00620([p]) == {"a": ["s1"]}
