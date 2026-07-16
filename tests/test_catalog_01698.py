"""Tests for catalog_01698."""

import pytest

from cartservice.generated.catalog_01698 import (
    Product_01698,
    bucket_by_tag_01698,
    is_valid_sku_01698,
    price_with_tax_01698,
)


def test_price_with_tax_01698():
    assert price_with_tax_01698(1000, 500) == 1050


def test_price_with_tax_negative_01698():
    with pytest.raises(ValueError):
        price_with_tax_01698(1000, -1)


def test_is_valid_sku_01698():
    assert is_valid_sku_01698("abc123")
    assert not is_valid_sku_01698("")


def test_bucket_by_tag_01698():
    p = Product_01698("s1", 100, ["a"])
    assert bucket_by_tag_01698([p]) == {"a": ["s1"]}
