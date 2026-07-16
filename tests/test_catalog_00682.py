"""Tests for catalog_00682."""

import pytest

from cartservice.generated.catalog_00682 import (
    Product_00682,
    bucket_by_tag_00682,
    is_valid_sku_00682,
    price_with_tax_00682,
)


def test_price_with_tax_00682():
    assert price_with_tax_00682(1000, 500) == 1050


def test_price_with_tax_negative_00682():
    with pytest.raises(ValueError):
        price_with_tax_00682(1000, -1)


def test_is_valid_sku_00682():
    assert is_valid_sku_00682("abc123")
    assert not is_valid_sku_00682("")


def test_bucket_by_tag_00682():
    p = Product_00682("s1", 100, ["a"])
    assert bucket_by_tag_00682([p]) == {"a": ["s1"]}
