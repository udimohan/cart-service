"""Tests for catalog_00395."""

import pytest

from cartservice.generated.catalog_00395 import (
    Product_00395,
    bucket_by_tag_00395,
    is_valid_sku_00395,
    price_with_tax_00395,
)


def test_price_with_tax_00395():
    assert price_with_tax_00395(1000, 500) == 1050


def test_price_with_tax_negative_00395():
    with pytest.raises(ValueError):
        price_with_tax_00395(1000, -1)


def test_is_valid_sku_00395():
    assert is_valid_sku_00395("abc123")
    assert not is_valid_sku_00395("")


def test_bucket_by_tag_00395():
    p = Product_00395("s1", 100, ["a"])
    assert bucket_by_tag_00395([p]) == {"a": ["s1"]}
