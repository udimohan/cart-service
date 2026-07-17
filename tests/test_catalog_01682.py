"""Tests for catalog_01682."""

import pytest

from cartservice.generated.catalog_01682 import (
    Product_01682,
    bucket_by_tag_01682,
    is_valid_sku_01682,
    price_with_tax_01682,
)


def test_price_with_tax_01682():
    assert price_with_tax_01682(1000, 500) == 1050


def test_price_with_tax_negative_01682():
    with pytest.raises(ValueError):
        price_with_tax_01682(1000, -1)


def test_is_valid_sku_01682():
    assert is_valid_sku_01682("abc123")
    assert not is_valid_sku_01682("")


def test_bucket_by_tag_01682():
    p = Product_01682("s1", 100, ["a"])
    assert bucket_by_tag_01682([p]) == {"a": ["s1"]}
