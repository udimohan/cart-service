"""Tests for catalog_00653."""

import pytest

from cartservice.generated.catalog_00653 import (
    Product_00653,
    bucket_by_tag_00653,
    is_valid_sku_00653,
    price_with_tax_00653,
)


def test_price_with_tax_00653():
    assert price_with_tax_00653(1000, 500) == 1050


def test_price_with_tax_negative_00653():
    with pytest.raises(ValueError):
        price_with_tax_00653(1000, -1)


def test_is_valid_sku_00653():
    assert is_valid_sku_00653("abc123")
    assert not is_valid_sku_00653("")


def test_bucket_by_tag_00653():
    p = Product_00653("s1", 100, ["a"])
    assert bucket_by_tag_00653([p]) == {"a": ["s1"]}
