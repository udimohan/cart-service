"""Tests for catalog_01653."""

import pytest

from cartservice.generated.catalog_01653 import (
    Product_01653,
    bucket_by_tag_01653,
    is_valid_sku_01653,
    price_with_tax_01653,
)


def test_price_with_tax_01653():
    assert price_with_tax_01653(1000, 500) == 1050


def test_price_with_tax_negative_01653():
    with pytest.raises(ValueError):
        price_with_tax_01653(1000, -1)


def test_is_valid_sku_01653():
    assert is_valid_sku_01653("abc123")
    assert not is_valid_sku_01653("")


def test_bucket_by_tag_01653():
    p = Product_01653("s1", 100, ["a"])
    assert bucket_by_tag_01653([p]) == {"a": ["s1"]}
