"""Tests for catalog_01688."""

import pytest

from cartservice.generated.catalog_01688 import (
    Product_01688,
    bucket_by_tag_01688,
    is_valid_sku_01688,
    price_with_tax_01688,
)


def test_price_with_tax_01688():
    assert price_with_tax_01688(1000, 500) == 1050


def test_price_with_tax_negative_01688():
    with pytest.raises(ValueError):
        price_with_tax_01688(1000, -1)


def test_is_valid_sku_01688():
    assert is_valid_sku_01688("abc123")
    assert not is_valid_sku_01688("")


def test_bucket_by_tag_01688():
    p = Product_01688("s1", 100, ["a"])
    assert bucket_by_tag_01688([p]) == {"a": ["s1"]}
