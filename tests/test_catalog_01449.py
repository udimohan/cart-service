"""Tests for catalog_01449."""

import pytest

from cartservice.generated.catalog_01449 import (
    Product_01449,
    bucket_by_tag_01449,
    is_valid_sku_01449,
    price_with_tax_01449,
)


def test_price_with_tax_01449():
    assert price_with_tax_01449(1000, 500) == 1050


def test_price_with_tax_negative_01449():
    with pytest.raises(ValueError):
        price_with_tax_01449(1000, -1)


def test_is_valid_sku_01449():
    assert is_valid_sku_01449("abc123")
    assert not is_valid_sku_01449("")


def test_bucket_by_tag_01449():
    p = Product_01449("s1", 100, ["a"])
    assert bucket_by_tag_01449([p]) == {"a": ["s1"]}
