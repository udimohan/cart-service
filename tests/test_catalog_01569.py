"""Tests for catalog_01569."""

import pytest

from cartservice.generated.catalog_01569 import (
    Product_01569,
    bucket_by_tag_01569,
    is_valid_sku_01569,
    price_with_tax_01569,
)


def test_price_with_tax_01569():
    assert price_with_tax_01569(1000, 500) == 1050


def test_price_with_tax_negative_01569():
    with pytest.raises(ValueError):
        price_with_tax_01569(1000, -1)


def test_is_valid_sku_01569():
    assert is_valid_sku_01569("abc123")
    assert not is_valid_sku_01569("")


def test_bucket_by_tag_01569():
    p = Product_01569("s1", 100, ["a"])
    assert bucket_by_tag_01569([p]) == {"a": ["s1"]}
