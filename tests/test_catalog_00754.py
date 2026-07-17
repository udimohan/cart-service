"""Tests for catalog_00754."""

import pytest

from cartservice.generated.catalog_00754 import (
    Product_00754,
    bucket_by_tag_00754,
    is_valid_sku_00754,
    price_with_tax_00754,
)


def test_price_with_tax_00754():
    assert price_with_tax_00754(1000, 500) == 1050


def test_price_with_tax_negative_00754():
    with pytest.raises(ValueError):
        price_with_tax_00754(1000, -1)


def test_is_valid_sku_00754():
    assert is_valid_sku_00754("abc123")
    assert not is_valid_sku_00754("")


def test_bucket_by_tag_00754():
    p = Product_00754("s1", 100, ["a"])
    assert bucket_by_tag_00754([p]) == {"a": ["s1"]}
