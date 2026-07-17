"""Tests for catalog_01690."""

import pytest

from cartservice.generated.catalog_01690 import (
    Product_01690,
    bucket_by_tag_01690,
    is_valid_sku_01690,
    price_with_tax_01690,
)


def test_price_with_tax_01690():
    assert price_with_tax_01690(1000, 500) == 1050


def test_price_with_tax_negative_01690():
    with pytest.raises(ValueError):
        price_with_tax_01690(1000, -1)


def test_is_valid_sku_01690():
    assert is_valid_sku_01690("abc123")
    assert not is_valid_sku_01690("")


def test_bucket_by_tag_01690():
    p = Product_01690("s1", 100, ["a"])
    assert bucket_by_tag_01690([p]) == {"a": ["s1"]}
