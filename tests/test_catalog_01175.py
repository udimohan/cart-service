"""Tests for catalog_01175."""

import pytest

from cartservice.generated.catalog_01175 import (
    Product_01175,
    bucket_by_tag_01175,
    is_valid_sku_01175,
    price_with_tax_01175,
)


def test_price_with_tax_01175():
    assert price_with_tax_01175(1000, 500) == 1050


def test_price_with_tax_negative_01175():
    with pytest.raises(ValueError):
        price_with_tax_01175(1000, -1)


def test_is_valid_sku_01175():
    assert is_valid_sku_01175("abc123")
    assert not is_valid_sku_01175("")


def test_bucket_by_tag_01175():
    p = Product_01175("s1", 100, ["a"])
    assert bucket_by_tag_01175([p]) == {"a": ["s1"]}
