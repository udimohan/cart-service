"""Tests for catalog_01726."""

import pytest

from cartservice.generated.catalog_01726 import (
    Product_01726,
    bucket_by_tag_01726,
    is_valid_sku_01726,
    price_with_tax_01726,
)


def test_price_with_tax_01726():
    assert price_with_tax_01726(1000, 500) == 1050


def test_price_with_tax_negative_01726():
    with pytest.raises(ValueError):
        price_with_tax_01726(1000, -1)


def test_is_valid_sku_01726():
    assert is_valid_sku_01726("abc123")
    assert not is_valid_sku_01726("")


def test_bucket_by_tag_01726():
    p = Product_01726("s1", 100, ["a"])
    assert bucket_by_tag_01726([p]) == {"a": ["s1"]}
