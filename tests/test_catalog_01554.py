"""Tests for catalog_01554."""

import pytest

from cartservice.generated.catalog_01554 import (
    Product_01554,
    bucket_by_tag_01554,
    is_valid_sku_01554,
    price_with_tax_01554,
)


def test_price_with_tax_01554():
    assert price_with_tax_01554(1000, 500) == 1050


def test_price_with_tax_negative_01554():
    with pytest.raises(ValueError):
        price_with_tax_01554(1000, -1)


def test_is_valid_sku_01554():
    assert is_valid_sku_01554("abc123")
    assert not is_valid_sku_01554("")


def test_bucket_by_tag_01554():
    p = Product_01554("s1", 100, ["a"])
    assert bucket_by_tag_01554([p]) == {"a": ["s1"]}
