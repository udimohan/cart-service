"""Tests for catalog_00597."""

import pytest

from cartservice.generated.catalog_00597 import (
    Product_00597,
    bucket_by_tag_00597,
    is_valid_sku_00597,
    price_with_tax_00597,
)


def test_price_with_tax_00597():
    assert price_with_tax_00597(1000, 500) == 1050


def test_price_with_tax_negative_00597():
    with pytest.raises(ValueError):
        price_with_tax_00597(1000, -1)


def test_is_valid_sku_00597():
    assert is_valid_sku_00597("abc123")
    assert not is_valid_sku_00597("")


def test_bucket_by_tag_00597():
    p = Product_00597("s1", 100, ["a"])
    assert bucket_by_tag_00597([p]) == {"a": ["s1"]}
