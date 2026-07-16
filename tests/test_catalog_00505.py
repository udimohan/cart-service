"""Tests for catalog_00505."""

import pytest

from cartservice.generated.catalog_00505 import (
    Product_00505,
    bucket_by_tag_00505,
    is_valid_sku_00505,
    price_with_tax_00505,
)


def test_price_with_tax_00505():
    assert price_with_tax_00505(1000, 500) == 1050


def test_price_with_tax_negative_00505():
    with pytest.raises(ValueError):
        price_with_tax_00505(1000, -1)


def test_is_valid_sku_00505():
    assert is_valid_sku_00505("abc123")
    assert not is_valid_sku_00505("")


def test_bucket_by_tag_00505():
    p = Product_00505("s1", 100, ["a"])
    assert bucket_by_tag_00505([p]) == {"a": ["s1"]}
