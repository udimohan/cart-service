"""Tests for catalog_01168."""

import pytest

from cartservice.generated.catalog_01168 import (
    Product_01168,
    bucket_by_tag_01168,
    is_valid_sku_01168,
    price_with_tax_01168,
)


def test_price_with_tax_01168():
    assert price_with_tax_01168(1000, 500) == 1050


def test_price_with_tax_negative_01168():
    with pytest.raises(ValueError):
        price_with_tax_01168(1000, -1)


def test_is_valid_sku_01168():
    assert is_valid_sku_01168("abc123")
    assert not is_valid_sku_01168("")


def test_bucket_by_tag_01168():
    p = Product_01168("s1", 100, ["a"])
    assert bucket_by_tag_01168([p]) == {"a": ["s1"]}
