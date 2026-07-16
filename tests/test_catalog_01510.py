"""Tests for catalog_01510."""

import pytest

from cartservice.generated.catalog_01510 import (
    Product_01510,
    bucket_by_tag_01510,
    is_valid_sku_01510,
    price_with_tax_01510,
)


def test_price_with_tax_01510():
    assert price_with_tax_01510(1000, 500) == 1050


def test_price_with_tax_negative_01510():
    with pytest.raises(ValueError):
        price_with_tax_01510(1000, -1)


def test_is_valid_sku_01510():
    assert is_valid_sku_01510("abc123")
    assert not is_valid_sku_01510("")


def test_bucket_by_tag_01510():
    p = Product_01510("s1", 100, ["a"])
    assert bucket_by_tag_01510([p]) == {"a": ["s1"]}
