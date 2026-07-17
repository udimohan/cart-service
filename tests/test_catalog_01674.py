"""Tests for catalog_01674."""

import pytest

from cartservice.generated.catalog_01674 import (
    Product_01674,
    bucket_by_tag_01674,
    is_valid_sku_01674,
    price_with_tax_01674,
)


def test_price_with_tax_01674():
    assert price_with_tax_01674(1000, 500) == 1050


def test_price_with_tax_negative_01674():
    with pytest.raises(ValueError):
        price_with_tax_01674(1000, -1)


def test_is_valid_sku_01674():
    assert is_valid_sku_01674("abc123")
    assert not is_valid_sku_01674("")


def test_bucket_by_tag_01674():
    p = Product_01674("s1", 100, ["a"])
    assert bucket_by_tag_01674([p]) == {"a": ["s1"]}
