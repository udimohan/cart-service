"""Tests for catalog_00325."""

import pytest

from cartservice.generated.catalog_00325 import (
    Product_00325,
    bucket_by_tag_00325,
    is_valid_sku_00325,
    price_with_tax_00325,
)


def test_price_with_tax_00325():
    assert price_with_tax_00325(1000, 500) == 1050


def test_price_with_tax_negative_00325():
    with pytest.raises(ValueError):
        price_with_tax_00325(1000, -1)


def test_is_valid_sku_00325():
    assert is_valid_sku_00325("abc123")
    assert not is_valid_sku_00325("")


def test_bucket_by_tag_00325():
    p = Product_00325("s1", 100, ["a"])
    assert bucket_by_tag_00325([p]) == {"a": ["s1"]}
