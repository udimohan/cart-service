"""Tests for catalog_01034."""

import pytest

from cartservice.generated.catalog_01034 import (
    Product_01034,
    bucket_by_tag_01034,
    is_valid_sku_01034,
    price_with_tax_01034,
)


def test_price_with_tax_01034():
    assert price_with_tax_01034(1000, 500) == 1050


def test_price_with_tax_negative_01034():
    with pytest.raises(ValueError):
        price_with_tax_01034(1000, -1)


def test_is_valid_sku_01034():
    assert is_valid_sku_01034("abc123")
    assert not is_valid_sku_01034("")


def test_bucket_by_tag_01034():
    p = Product_01034("s1", 100, ["a"])
    assert bucket_by_tag_01034([p]) == {"a": ["s1"]}
